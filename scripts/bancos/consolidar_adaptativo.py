#!/usr/bin/env python3
"""
Consolidador adaptativo de extractos bancarios CSV.

Detecta automaticamente el formato del CSV (Bancolombia antiguo, nuevo mayo,
nuevo jun-jul) y consolida multiples archivos en uno solo.

Uso:
    python3 consolidar_adaptativo.py archivo1.csv archivo2.csv -o consolidado.csv
    python3 consolidar_adaptativo.py *.csv -o consolidado.csv

Autor: Muno Labs
"""

import csv
import sys
import argparse
from datetime import datetime


def detectar_formato(fila):
    """Detecta el formato basado en la estructura y contenido de la fila."""
    if len(fila) >= 15:
        return "antiguo"
    elif len(fila) >= 9 and len(fila) < 15:
        try:
            fecha_str = fila[3].strip()
            if len(fecha_str) == 8:
                datetime.strptime(fecha_str, '%d%m%Y')
                return "nuevo_mayo"
        except ValueError:
            pass
        try:
            fecha_str = fila[3].strip()
            if len(fecha_str) == 8:
                datetime.strptime(fecha_str, '%Y%m%d')
                return "nuevo_jun_jul"
        except ValueError:
            pass
    elif len(fila) >= 8:
        return "nuevo_jun_jul"
    return "desconocido"


def procesar_formato_antiguo(fila):
    """Procesa filas del formato antiguo (ene-abr Bancolombia)."""
    try:
        fecha = datetime.strptime(fila[0].strip(), '%Y%m%d').strftime('%Y-%m-%d')
        descripcion = fila[6].strip() if len(fila) > 6 else ""
        monto = float(fila[8].strip()) if len(fila) > 8 else 0.0
        tipo = fila[10].strip() if len(fila) > 10 else ""
        codigo = fila[7].strip() if len(fila) > 7 else ""
        return {'fecha': fecha, 'descripcion': descripcion, 'monto': monto, 'tipo': tipo, 'codigo': codigo}
    except Exception as e:
        print(f"Error procesando formato antiguo: {e}", file=sys.stderr)
        return None


def procesar_formato_mayo(fila):
    """Procesa filas del formato nuevo (mayo, fecha DDMMYYYY)."""
    try:
        fecha = datetime.strptime(fila[3].strip(), '%d%m%Y').strftime('%Y-%m-%d')
        descripcion = fila[7].strip() if len(fila) > 7 else ""
        monto = float(fila[5].strip()) if len(fila) > 5 else 0.0
        tipo = "C" if monto >= 0 else "D"
        codigo = fila[6].strip() if len(fila) > 6 else ""
        return {'fecha': fecha, 'descripcion': descripcion, 'monto': monto, 'tipo': tipo, 'codigo': codigo}
    except Exception as e:
        print(f"Error procesando formato mayo: {e}", file=sys.stderr)
        return None


def procesar_formato_jun_jul(fila):
    """Procesa filas del formato jun-jul (fecha YYYYMMDD)."""
    try:
        fecha = datetime.strptime(fila[3].strip(), '%Y%m%d').strftime('%Y-%m-%d')
        descripcion = fila[7].strip() if len(fila) > 7 else ""
        monto = float(fila[5].strip()) if len(fila) > 5 else 0.0
        tipo = "C" if monto >= 0 else "D"
        codigo = fila[6].strip() if len(fila) > 6 else ""
        return {'fecha': fecha, 'descripcion': descripcion, 'monto': monto, 'tipo': tipo, 'codigo': codigo}
    except Exception as e:
        print(f"Error procesando formato jun-jul: {e}", file=sys.stderr)
        return None


PROCESADORES = {
    "antiguo": procesar_formato_antiguo,
    "nuevo_mayo": procesar_formato_mayo,
    "nuevo_jun_jul": procesar_formato_jun_jul,
}


def consolidar(archivos, archivo_salida, encoding='latin-1'):
    """Consolida multiples archivos CSV en uno solo."""
    transacciones = []

    for archivo in archivos:
        try:
            print(f"Procesando: {archivo}")
            with open(archivo, 'r', encoding=encoding) as f:
                reader = csv.reader(f)
                for fila in reader:
                    if not fila:
                        continue
                    formato = detectar_formato(fila)
                    procesador = PROCESADORES.get(formato)
                    if not procesador:
                        continue
                    resultado = procesador(fila)
                    if resultado and resultado['fecha'] and resultado['descripcion'] and resultado['monto'] != 0.0:
                        transacciones.append([
                            resultado['fecha'], resultado['descripcion'],
                            resultado['monto'], resultado['tipo'], resultado['codigo']
                        ])
        except Exception as e:
            print(f"Error procesando {archivo}: {e}", file=sys.stderr)

    transacciones.sort(key=lambda x: x[0])

    with open(archivo_salida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['fecha', 'descripcion', 'monto', 'tipo', 'codigo_transaccion'])
        writer.writerows(transacciones)

    # Estadisticas
    creditos = [t for t in transacciones if t[3] == 'C']
    debitos = [t for t in transacciones if t[3] == 'D']
    print(f"\nArchivo consolidado: {archivo_salida}")
    print(f"Total transacciones: {len(transacciones)}")
    print(f"Creditos: {len(creditos)} - Total: ${sum(t[2] for t in creditos):,.2f}")
    print(f"Debitos: {len(debitos)} - Total: ${sum(t[2] for t in debitos):,.2f}")
    if transacciones:
        print(f"Periodo: {transacciones[0][0]} a {transacciones[-1][0]}")

    return archivo_salida


def main():
    parser = argparse.ArgumentParser(description='Consolida extractos bancarios CSV (Bancolombia)')
    parser.add_argument('archivos', nargs='+', help='Archivos CSV a procesar')
    parser.add_argument('-o', '--output', default='consolidado.csv', help='Archivo de salida (default: consolidado.csv)')
    parser.add_argument('-e', '--encoding', default='latin-1', help='Encoding de los CSV (default: latin-1)')
    args = parser.parse_args()
    consolidar(args.archivos, args.output, args.encoding)


if __name__ == "__main__":
    main()
