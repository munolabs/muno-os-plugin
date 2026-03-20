#!/bin/bash
# generate.sh — Genera el daily brief HTML a partir del template y un JSON de datos
# Uso: bash generate.sh <data.json> [output-dir]
#
# El JSON lo genera Claude con los datos del dia, este script lo inyecta en el template.
# El output-dir es opcional (default: daily-reports/)

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE="$SKILL_DIR/template.html"
DATA_FILE="${1:?Uso: generate.sh <data.json> [output-dir]}"
CONFIG_FILE="$SKILL_DIR/config.json"
OUTPUT_DIR="${2:-}"

# Use python3 for all JSON reading and HTML generation
python3 - "$TEMPLATE" "$DATA_FILE" "$CONFIG_FILE" "$OUTPUT_DIR" << 'PYEOF'
import json
import sys
import os
from datetime import datetime

template_path = sys.argv[1]
data_path = sys.argv[2]
config_path = sys.argv[3]
output_dir_arg = sys.argv[4] if len(sys.argv) > 4 else ""

# Load data JSON
with open(data_path, 'r') as f:
    data = json.load(f)

# Load config if exists
config = {}
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)

# Determine output directory
if output_dir_arg:
    output_dir = output_dir_arg
else:
    output_dir = config.get('output', {}).get('dir', 'daily-reports')

# Determine timezone
tz = config.get('timezone', 'UTC')

# Determine date for filename
date_str = data.get('date_short', datetime.now().strftime('%Y-%m-%d'))
output_path = os.path.join(output_dir, f"{date_str}.html")
os.makedirs(output_dir, exist_ok=True)

# Brand colors
brand = config.get('brand', {})
color_primary = brand.get('primary', '#8DEDCF')
color_secondary = brand.get('secondary', '#4D9EFF')

# Locale
locale = data.get('locale', config.get('locale', 'es'))

# Localized labels
if locale == 'en':
    sources_label = 'Sources'
    generated_label = 'Generated'
else:
    sources_label = 'Fuentes consultadas'
    generated_label = 'Generado'

# Default greeting
name = data.get('name', config.get('name', ''))
greeting = data.get('greeting', '')
if not greeting:
    if locale == 'en':
        greeting = f"Good morning, {name}." if name else "Good morning."
    else:
        greeting = f"Buenos dias, {name}." if name else "Buenos dias."

# Load template
with open(template_path, 'r') as f:
    html = f.read()

# Build replacements
replacements = {
    '{{LOCALE}}': locale,
    '{{DATE_SHORT}}': date_str,
    '{{COLOR_PRIMARY}}': color_primary,
    '{{COLOR_SECONDARY}}': color_secondary,
    '{{GREETING}}': greeting,
    '{{DIA_SEMANA}}': data.get('dia_semana', ''),
    '{{FECHA_LARGA}}': data.get('fecha_larga', ''),
    '{{HORA}}': data.get('hora', ''),
    '{{TZ_LABEL}}': data.get('timezone_label', ''),
    '{{QUOTE_HTML}}': data.get('quote_html', ''),
    '{{STATS_HTML}}': data.get('stats_html', ''),
    '{{ALERTS_HTML}}': data.get('alerts_html', ''),
    '{{SECTIONS_HTML}}': data.get('sections_html', ''),
    '{{SOURCES_LABEL}}': sources_label,
    '{{SOURCES_HTML}}': data.get('sources_html', ''),
    '{{GENERATED_LABEL}}': generated_label,
}

for placeholder, value in replacements.items():
    html = html.replace(placeholder, str(value))

with open(output_path, 'w') as f:
    f.write(html)

print(output_path)
PYEOF
