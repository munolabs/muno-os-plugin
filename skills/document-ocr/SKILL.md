---
name: document-ocr
description: Extrae texto de PDFs e imágenes usando AWS Textract. Especialmente útil para PDFs de diseño (Illustrator) sin texto extraíble. Trigger en "extraer texto", "OCR", "leer PDF escaneado", "documento sin texto", "Textract".
---

# Document OCR

Extrae texto de PDFs e imágenes usando AWS Textract. Útil para documentos escaneados o PDFs de diseño que no tienen texto extraíble.

## Archivos en este Skill

```
document-ocr/
├── SKILL.md
```

Scripts de referencia (en /scripts/ocr/):
- `textract_pdf_analyzer.py` - Procesar PDFs
- `textract_images_analyzer.py` - Procesar imagenes

## Prerequisitos

- AWS CLI configurado con credenciales
- Permisos para AWS Textract
- Región: `us-east-1` (default)
- Python 3.x con boto3

## Flujo de Trabajo

### Para PDFs

```bash
python3 scripts/ocr/textract_pdf_analyzer.py "documento.pdf" "resultado"
```

**Output:** Archivos .txt con texto extraido por pagina.

### Para Imagenes

```bash
python3 scripts/ocr/textract_images_analyzer.py "carpeta_imagenes/" "resultado"
```

### Para PDFs de Illustrator/Diseño

Los PDFs creados en Illustrator o herramientas de diseño frecuentemente no tienen texto extraíble (el texto está como curvas/paths).

**Solución: Convertir a imágenes primero**

```bash
# 1. Convertir PDF a imágenes con ImageMagick
magick -density 300 "archivo.pdf" -quality 100 "output/page.png"

# 2. Procesar imágenes con Textract
python3 scripts/ocr/textract_images_analyzer.py "output/" "resultado"
```

## Gotchas

1. **PDFs de diseño**: El Read tool de Claude no extrae texto de PDFs de Illustrator. Usar flujo de conversión a imagen + Textract.

2. **Límites de Textract**:
   - Máximo 5MB por documento síncrono
   - Para documentos grandes, usar async con S3

3. **Calidad de imagen importa**: Para mejor OCR, usar density 300 o más al convertir PDF.

4. **Tablas**: Textract puede detectar tablas, pero el output puede necesitar post-procesamiento.

5. **Idioma**: Textract funciona mejor con inglés, pero soporta español y otros idiomas.

6. **Costos**: Textract tiene costo por página. Verificar pricing antes de procesar documentos grandes.

## AWS Configuration

```
Región: us-east-1
Cuenta: [configurar en AWS CLI]
```

## Scripts

### textract_pdf_analyzer.py
```bash
python3 scripts/ocr/textract_pdf_analyzer.py input.pdf output_prefix
# Envia PDF a Textract, guarda resultado en .txt y .json
# Para PDFs >5MB usa analisis asincrono con S3
```

### textract_images_analyzer.py
```bash
python3 scripts/ocr/textract_images_analyzer.py input_folder/ output_prefix
# Procesa todas las imagenes PNG en la carpeta
```

## Output

Archivos de texto plano con el contenido extraído:
- `resultado_page_1.txt`
- `resultado_page_2.txt`
- etc.

O archivo consolidado:
- `resultado_full.txt`

## Alternativas

Si Textract no está disponible:
- **Google Cloud Vision API** - Similar funcionalidad
- **Tesseract** - Open source, local, menos preciso
- **Adobe Acrobat** - Para PDFs con texto oculto
