#!/usr/bin/env python3
import boto3
import json
import sys
from pathlib import Path

def analyze_pdf_with_textract(pdf_path, output_path=None, region='us-east-1'):
    """
    Analiza un PDF usando AWS Textract y extrae todo el texto.
    
    Args:
        pdf_path: Ruta al archivo PDF
        output_path: Ruta para guardar el resultado (opcional)
        region: Región de AWS (default: us-east-1)
    
    Returns:
        dict con el texto extraído y metadata
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF no encontrado: {pdf_path}")
    
    print(f"📄 Procesando: {pdf_path.name}")
    print(f"📏 Tamaño: {pdf_path.stat().st_size / 1024 / 1024:.2f} MB")
    
    with open(pdf_path, 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()
    
    textract = boto3.client('textract', region_name=region)
    
    print("🔄 Enviando a AWS Textract...")
    
    if len(pdf_bytes) > 5 * 1024 * 1024:
        print("⚠️  PDF muy grande (>5MB), usando análisis asíncrono...")
        s3 = boto3.client('s3', region_name=region)
        bucket_name = f"textract-temp-{boto3.client('sts').get_caller_identity()['Account']}"
        
        try:
            s3.head_bucket(Bucket=bucket_name)
        except:
            print(f"📦 Creando bucket temporal: {bucket_name}")
            s3.create_bucket(Bucket=bucket_name)
        
        key = f"temp/{pdf_path.name}"
        s3.put_object(Bucket=bucket_name, Key=key, Body=pdf_bytes)
        
        response = textract.start_document_text_detection(
            DocumentLocation={'S3Object': {'Bucket': bucket_name, 'Name': key}}
        )
        
        job_id = response['JobId']
        print(f"🆔 Job ID: {job_id}")
        print("⏳ Esperando resultados...")
        
        import time
        while True:
            result = textract.get_document_text_detection(JobId=job_id)
            status = result['JobStatus']
            
            if status == 'SUCCEEDED':
                print("✅ Análisis completado")
                break
            elif status == 'FAILED':
                raise Exception("Textract falló")
            
            time.sleep(2)
        
        blocks = result['Blocks']
        
        while 'NextToken' in result:
            result = textract.get_document_text_detection(
                JobId=job_id,
                NextToken=result['NextToken']
            )
            blocks.extend(result['Blocks'])
        
        s3.delete_object(Bucket=bucket_name, Key=key)
        
    else:
        response = textract.detect_document_text(
            Document={'Bytes': pdf_bytes}
        )
        blocks = response['Blocks']
    
    pages = {}
    current_page = 1
    page_text = []
    
    for block in blocks:
        if block['BlockType'] == 'PAGE':
            if page_text:
                pages[current_page] = '\n'.join(page_text)
                page_text = []
            current_page = block.get('Page', current_page)
        elif block['BlockType'] == 'LINE':
            text = block.get('Text', '')
            page_text.append(text)
    
    if page_text:
        pages[current_page] = '\n'.join(page_text)
    
    full_text = '\n\n'.join([f"=== PÁGINA {p} ===\n{text}" for p, text in sorted(pages.items())])
    
    result = {
        'file': str(pdf_path),
        'total_pages': len(pages),
        'total_blocks': len(blocks),
        'pages': pages,
        'full_text': full_text
    }
    
    print(f"\n📊 Resultados:")
    print(f"   • Páginas procesadas: {len(pages)}")
    print(f"   • Bloques detectados: {len(blocks)}")
    print(f"   • Caracteres extraídos: {len(full_text)}")
    
    if output_path:
        output_path = Path(output_path)
        
        with open(output_path.with_suffix('.txt'), 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"\n💾 Texto guardado en: {output_path.with_suffix('.txt')}")
        
        with open(output_path.with_suffix('.json'), 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"💾 JSON guardado en: {output_path.with_suffix('.json')}")
    
    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 textract_pdf_analyzer.py <pdf_path> [output_path]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        result = analyze_pdf_with_textract(pdf_path, output_path)
        print("\n✅ Proceso completado exitosamente")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
