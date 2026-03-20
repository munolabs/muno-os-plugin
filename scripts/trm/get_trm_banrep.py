#!/usr/bin/env python3
"""
Script para obtener la Tasa Representativa del Mercado (TRM) oficial
del Banco de la República de Colombia.

Este script usa Playwright para cargar dinámicamente la página web y
obtener el valor EXACTO y actualizado de la TRM oficial.

IMPORTANTE: Este valor es crítico para decisiones financieras.
El script valida el formato y rango del valor obtenido.

Uso:
    python3 get_trm_banrep.py

Requisitos:
    pip3 install playwright --break-system-packages
    playwright install chromium

Salida:
    Imprime el valor de la TRM y la fecha en formato legible.
    Retorna código 0 si exitoso, 1 si hay error.

Autor: Muno Labs
"""

import sys
import re
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

def get_trm_banrep():
    """
    Obtiene el valor oficial de la TRM desde el sitio del Banco de la República
    usando Playwright para ejecutar JavaScript y obtener el valor dinámico.

    Returns:
        tuple: (valor_trm_str, fecha_str, valor_trm_float)
               ejemplo: ("3.806,16", "26/11/2025", 3806.16)
               o (None, None, None) si hay error
    """
    url = "https://suameca.banrep.gov.co/estadisticas-economicas/informacionSerie/1/tasa_cambio_peso_colombiano_trm_dolar_usd"

    try:
        with sync_playwright() as p:
            # Lanzar navegador
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Navegar a la página
            page.goto(url, wait_until='networkidle', timeout=30000)

            # Esperar a que los elementos se carguen (el sitio usa Angular)
            page.wait_for_selector('.tileValor', timeout=10000)

            # Extraer valor y fecha usando JavaScript
            result = page.evaluate("""
                () => {
                    const valorElem = document.querySelector('.tileValor');
                    const fechaElem = document.querySelector('.tilefecha');

                    return {
                        valor: valorElem ? valorElem.textContent.trim() : null,
                        fecha: fechaElem ? fechaElem.textContent.trim() : null
                    };
                }
            """)

            browser.close()

            valor_str = result.get('valor')
            fecha_str = result.get('fecha')

            if not valor_str or not fecha_str:
                print("❌ Error: No se encontraron los valores en la página.", file=sys.stderr)
                return None, None, None

            # Validar formato del valor (ej: "3.806,16")
            if not re.match(r'^\d{1,3}(\.\d{3})?,\d{2}$', valor_str):
                print(f"❌ Error: Formato de TRM inesperado: '{valor_str}'", file=sys.stderr)
                return None, None, None

            # Validar formato de fecha (DD/MM/YYYY)
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', fecha_str):
                print(f"❌ Error: Formato de fecha inesperado: '{fecha_str}'", file=sys.stderr)
                return None, None, None

            # Convertir valor a float para validación
            # Formato colombiano: 3.806,16 -> 3806.16
            valor_float = float(valor_str.replace('.', '').replace(',', '.'))

            # Validación de rango razonable (la TRM debería estar entre 1000 y 10000)
            if not (1000 <= valor_float <= 10000):
                print(f"⚠️  Advertencia: Valor de TRM fuera de rango esperado: ${valor_float}", file=sys.stderr)
                print(f"   Verifica manualmente en: {url}", file=sys.stderr)

            return valor_str, fecha_str, valor_float

    except PlaywrightTimeout:
        print("❌ Error: Timeout al cargar la página del Banco de la República.", file=sys.stderr)
        print("   La página tardó más de lo esperado en cargar.", file=sys.stderr)
        return None, None, None
    except Exception as e:
        print(f"❌ Error inesperado: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return None, None, None

def main():
    """Función principal que obtiene e imprime la TRM oficial."""

    print("🏦 Consultando TRM oficial del Banco de la República...\n")

    valor_str, fecha_str, valor_float = get_trm_banrep()

    if valor_str and fecha_str:
        print("=" * 55)
        print("💵 TRM OFICIAL - Banco de la República de Colombia")
        print("=" * 55)
        print(f"\n   Valor:  ${valor_str} COP/USD")
        print(f"   Fecha:  {fecha_str}")
        print(f"\n   (Valor numérico: {valor_float:,.2f})")
        print("\n" + "=" * 55)
        print(f"\n✅ TRM obtenida exitosamente")
        print(f"\n📍 Fuente oficial: Banco de la República")
        print(f"   https://www.banrep.gov.co")
        print("\n⚠️  IMPORTANTE: Valor certificado para operaciones financieras")
        return 0
    else:
        print("\n" + "=" * 55)
        print("❌ No se pudo obtener la TRM")
        print("=" * 55)
        print("\n🔍 Verifica manualmente en:")
        print("   https://www.banrep.gov.co")
        print("\n💡 Posibles causas:")
        print("   - Problemas de conexión a internet")
        print("   - Sitio del Banco de la República no disponible")
        print("   - Playwright no está instalado correctamente")
        return 1

if __name__ == "__main__":
    sys.exit(main())
