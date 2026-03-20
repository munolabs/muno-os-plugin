#!/usr/bin/env python3
"""
Consolidador simple de extractos bancarios CSV (Bancolombia formato antiguo).

Uso:
    python3 consolidar_simple.py archivo1.csv archivo2.csv -o consolidado.csv

Autor: Muno Labs
"""

import csv
import sys
import argparse
from datetime import datetime


def formatear_fecha(fecha_str):
    """Convierte fecha de YYYYMMDD a YYYY-MM-DD."""
    try:
        return datetime.strptime(fecha_str.strip(), '%Y%m%d').strftime('%Y-%m-%d')
    except ValueError:
        return fecha_str.strip()


def consolidar(archivos, archivo_salida, encoding='latin-1'):
    """Consolida archivos CSV de extractos bancarios."""
    transacciones = []

    for archivo in archivos:
        try:
            print(f"Procesando: {archivo}")
            with open(archivo, 'r', encoding=encoding) as f:
                reader = csv.reader(f)
                for fila in reader:
                    if len(fila) >= 11:
                        fecha = formatear_fecha(fila[0])
                        descripcion = fila[6].strip() if len(fila) > 6 else ""
                        monto = float(fila[8].strip()) if len(fila) > 8 else 0.0
                        tipo = fila[10].strip() if len(fila) > 10 else ""
                        codigo = fila[7].strip() if len(fila) > 7 else ""

                        if fecha and descripcion and monto != 0.0:
                            transacciones.append([fecha, descripcion, monto, tipo, codigo])
        except Exception as e:
            print(f"Error procesando {archivo}: {e}", file=sys.stderr)

    transacciones.sort(key=lambda x: x[0])

    with open(archivo_salida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['fecha', 'descripcion', 'monto', 'tipo', 'codigo_transaccion'])
        writer.writerows(transacciones)

    creditos = [t for t in transacciones if t[3] == 'C']
    debitos = [t for t in transacciones if t[3] == 'D']

    print(f"\nArchivo consolidado: {archivo_salida}")
    print(f"Total transacciones: {len(transacciones)}")
    print(f"Creditos: {len(creditos)} - Total: ${sum(t[2] for t in creditos):,.2f}")
    print(f"Debitos: {len(debitos)} - Total: ${sum(t[2] for t in debitos):,.2f}")


def main():
    parser = argparse.ArgumentParser(description='Consolidador simple de extractos bancarios')
    parser.add_argument('archivos', nargs='+', help='Archivos CSV a procesar')
    parser.add_argument('-o', '--output', default='consolidado.csv', help='Archivo de salida')
    parser.add_argument('-e', '--encoding', default='latin-1', help='Encoding (default: latin-1)')
    args = parser.parse_args()
    consolidar(args.archivos, args.output, args.encoding)


if __name__ == "__main__":
    main()
