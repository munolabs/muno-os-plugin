#!/usr/bin/env python3
"""
Script para obtener la TRM (Tasa Representativa del Mercado) desde el API SDMX
del Banco de la República de Colombia.

Fuente: https://totoro.banrep.gov.co/nsi-jax-ws/rest/data
Documentación: WEB_SERVICES_DOCUMENTO_TECNICO_CONSUMO_SDMX.pdf

Autor: Muno Labs
"""

import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import sys

# Configuración del API
BASE_URL = "https://totoro.banrep.gov.co/nsi-jax-ws/rest/data"
AGENCY_ID = "ESTAT"
FLOW_ID_LATEST = "DF_TRM_DAILY_LATEST"
FLOW_ID_HIST = "DF_TRM_DAILY_HIST"
VERSION = "1.0"

# Namespaces SDMX
NAMESPACES = {
    'message': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message',
    'generic': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic',
    'common': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common'
}


def get_trm_latest():
    """
    Obtiene la TRM más reciente desde el API SDMX del Banco de la República.

    Returns:
        dict: Diccionario con 'valor', 'fecha', 'fecha_iso'
        None: Si hay error
    """
    url = f"{BASE_URL}/{AGENCY_ID},{FLOW_ID_LATEST},{VERSION}/all/ALL/"
    params = {
        'dimensionAtObservation': 'TIME_PERIOD',
        'detail': 'full'
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()

        # Parsear XML
        root = ET.fromstring(response.content)

        # Buscar la observación
        obs = root.find('.//generic:Obs', NAMESPACES)
        if obs is None:
            print("Error: No se encontró observación en la respuesta")
            return None

        # Extraer fecha
        obs_dimension = obs.find('generic:ObsDimension', NAMESPACES)
        fecha_raw = obs_dimension.get('value') if obs_dimension is not None else None

        # Extraer valor
        obs_value = obs.find('generic:ObsValue', NAMESPACES)
        valor = obs_value.get('value') if obs_value is not None else None

        if fecha_raw and valor:
            # Formatear fecha de YYYYMMDD a DD/MM/YYYY
            fecha_obj = datetime.strptime(fecha_raw, '%Y%m%d')
            fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
            fecha_iso = fecha_obj.strftime('%Y-%m-%d')

            # Formatear valor
            valor_float = float(valor)
            valor_formateado = f"{valor_float:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

            return {
                'valor': valor_float,
                'valor_formateado': valor_formateado,
                'fecha': fecha_formateada,
                'fecha_iso': fecha_iso
            }

        return None

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
    except ET.ParseError as e:
        print(f"Error parseando XML: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None


def get_trm_historico(start_year=None, end_year=None):
    """
    Obtiene la TRM histórica para un rango de fechas.

    Args:
        start_year: Año de inicio (YYYY)
        end_year: Año de fin (YYYY) - Nota: el API usa "menor que", así que para incluir 2024, usar 2025

    Returns:
        list: Lista de diccionarios con 'valor', 'fecha', 'fecha_iso'
    """
    url = f"{BASE_URL}/{AGENCY_ID},{FLOW_ID_HIST},{VERSION}/all/ALL/"
    params = {
        'dimensionAtObservation': 'TIME_PERIOD',
        'detail': 'full'
    }

    if start_year:
        params['startPeriod'] = str(start_year)
    if end_year:
        params['endPeriod'] = str(end_year)

    try:
        response = requests.get(url, params=params, timeout=60)
        response.raise_for_status()

        root = ET.fromstring(response.content)

        resultados = []
        for obs in root.findall('.//generic:Obs', NAMESPACES):
            obs_dimension = obs.find('generic:ObsDimension', NAMESPACES)
            obs_value = obs.find('generic:ObsValue', NAMESPACES)

            if obs_dimension is not None and obs_value is not None:
                fecha_raw = obs_dimension.get('value')
                valor = obs_value.get('value')

                if fecha_raw and valor:
                    fecha_obj = datetime.strptime(fecha_raw, '%Y%m%d')
                    resultados.append({
                        'valor': float(valor),
                        'fecha': fecha_obj.strftime('%d/%m/%Y'),
                        'fecha_iso': fecha_obj.strftime('%Y-%m-%d')
                    })

        # Ordenar por fecha
        resultados.sort(key=lambda x: x['fecha_iso'])
        return resultados

    except Exception as e:
        print(f"Error obteniendo histórico: {e}")
        return []


def main():
    """Función principal para ejecutar desde línea de comandos."""
    print("\n" + "=" * 55)
    print(" TRM OFICIAL - Banco de la República de Colombia")
    print(" (API SDMX - REST)")
    print("=" * 55 + "\n")

    resultado = get_trm_latest()

    if resultado:
        print(f"   Valor:  ${resultado['valor_formateado']} COP/USD")
        print(f"   Fecha:  {resultado['fecha']}")
        print(f"\n   (Valor numérico: {resultado['valor']:,.2f})")
        print("\n" + "=" * 55)
        print("\n Fuente: Banco de la República")
        print("   https://www.banrep.gov.co")
        print("\n API: SDMX REST")
        print("   https://totoro.banrep.gov.co/nsi-jax-ws/rest/data")
        print("\n" + "=" * 55 + "\n")
        return 0
    else:
        print(" Error: No se pudo obtener la TRM")
        print("\n" + "=" * 55 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
