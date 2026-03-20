#!/usr/bin/env python3
import boto3
import json
import sys
from pathlib import Path
import glob

def analyze_images_with_textract(images_dir, output_path=None, region='us-east-1'):
    """
    Analiza múltiples imágenes usando AWS Textract y extrae todo el texto.
    
    Args:
        images_dir: Directorio con las imágenes
        output_path: Ruta para guardar el resultado (opcional)
        region: Región de AWS (default: us-east-1)
    
    Returns:
        dict con el texto extraído y metadata
    """
    images_dir = Path(images_dir)
    
    if not images_dir.exists():
        raise FileNotFoundError(f"Directorio no encontrado: {images_dir}")
    
    image_files = sorted(glob.glob(str(images_dir / "*.png")))
    
    if not image_files:
        raise FileNotFoundError(f"No se encontraron imágenes PNG en: {images_dir}")
    
    print(f"📁 Directorio: {images_dir}")
    print(f"📄 Imágenes encontradas: {len(image_files)}")
    
    textract = boto3.client('textract', region_name=region)
    
    all_pages = {}
    total_blocks = 0
    
    for i, image_file in enumerate(image_files):
        print(f"\n🔄 Procesando imagen {i+1}/{len(image_files)}: {Path(image_file).name}")
        
        with open(image_file, 'rb') as img:
            image_bytes = img.read()
        
        try:
            response = textract.detect_document_text(
                Document={'Bytes': image_bytes}
            )
            
            blocks = response['Blocks']
            page_text = []
            
            for block in blocks:
                if block['BlockType'] == 'LINE':
                    text = block.get('Text', '')
                    page_text.append(text)
            
            page_num = i + 1
            all_pages[page_num] = '\n'.join(page_text)
            total_blocks += len(blocks)
            
            print(f"   ✅ Líneas extraídas: {len(page_text)}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            all_pages[page_num] = f"[Error procesando página {page_num}]"
    
    full_text = '\n\n'.join([f"=== PÁGINA {p} ===\n{text}" for p, text in sorted(all_pages.items())])
    
    result = {
        'source_dir': str(images_dir),
        'total_pages': len(all_pages),
        'total_images': len(image_files),
        'total_blocks': total_blocks,
        'pages': all_pages,
        'full_text': full_text
    }
    
    print(f"\n📊 Resultados:")
    print(f"   • Páginas procesadas: {len(all_pages)}")
    print(f"   • Bloques detectados: {total_blocks}")
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
        print("Uso: python3 textract_images_analyzer.py <images_dir> [output_path]")
        sys.exit(1)
    
    images_dir = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        result = analyze_images_with_textract(images_dir, output_path)
        print("\n✅ Proceso completado exitosamente")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
