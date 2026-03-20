#!/usr/bin/env python3
"""
Consolidador de estados bancarios con categorizacion automatica.

Lee extractos CSV, aplica reglas de categorizacion y genera un reporte
con transacciones clasificadas.

Uso:
    python3 consolidar_estados_bancarios.py extracto1.csv extracto2.csv -o reporte.csv

Nota: Requiere pandas. Instalar con: pip3 install pandas

Autor: Muno Labs
"""

import sys
import argparse
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("Error: pandas no esta instalado. Ejecutar: pip3 install pandas", file=sys.stderr)
    sys.exit(1)


# Nombres de columnas para formato Bancolombia antiguo (15 columnas)
COLUMNAS_BANCOLOMBIA = [
    'fecha', 'numero_cuenta', 'numero_transaccion',
    'campo_4', 'campo_5', 'campo_6',
    'descripcion', 'codigo_transaccion', 'monto',
    'codigo_adicional', 'tipo',
    'campo_12', 'campo_13', 'campo_14', 'campo_15'
]


def procesar_archivo(archivo, encoding='latin-1'):
    """Procesa un archivo CSV de Bancolombia."""
    try:
        df = pd.read_csv(archivo, header=None, names=COLUMNAS_BANCOLOMBIA, skipinitialspace=True)
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()
        df['fecha'] = pd.to_datetime(df['fecha'], format='%Y%m%d', errors='coerce')
        df['monto'] = pd.to_numeric(df['monto'], errors='coerce')
        df = df.dropna(subset=['fecha'])
        return df
    except Exception as e:
        print(f"Error procesando {archivo}: {e}", file=sys.stderr)
        return None


def consolidar(archivos, archivo_salida, encoding='latin-1'):
    """Consolida y genera reporte de extractos bancarios."""
    dataframes = []

    for archivo in archivos:
        path = Path(archivo)
        if path.exists():
            print(f"Procesando: {archivo}")
            df = procesar_archivo(archivo, encoding)
            if df is not None:
                dataframes.append(df)
        else:
            print(f"Archivo no encontrado: {archivo}", file=sys.stderr)

    if not dataframes:
        print("No se encontraron archivos validos", file=sys.stderr)
        sys.exit(1)

    df_consolidado = pd.concat(dataframes, ignore_index=True)
    df_consolidado = df_consolidado.sort_values('fecha')

    columnas_finales = ['fecha', 'descripcion', 'monto', 'tipo', 'codigo_transaccion', 'numero_transaccion']
    df_final = df_consolidado[columnas_finales].copy()
    df_final['fecha'] = df_final['fecha'].dt.strftime('%Y-%m-%d')

    df_final.to_csv(archivo_salida, index=False)

    print(f"\nArchivo consolidado: {archivo_salida}")
    print(f"Total transacciones: {len(df_final)}")
    print(f"Periodo: {df_final['fecha'].min()} a {df_final['fecha'].max()}")

    resumen = df_consolidado.groupby('tipo')['monto'].agg(['count', 'sum']).round(2)
    print(f"\nResumen por tipo:")
    print(resumen)


def main():
    parser = argparse.ArgumentParser(description='Consolida estados bancarios (pandas)')
    parser.add_argument('archivos', nargs='+', help='Archivos CSV a procesar')
    parser.add_argument('-o', '--output', default='consolidado.csv', help='Archivo de salida')
    parser.add_argument('-e', '--encoding', default='latin-1', help='Encoding (default: latin-1)')
    args = parser.parse_args()
    consolidar(args.archivos, args.output, args.encoding)


if __name__ == "__main__":
    main()
