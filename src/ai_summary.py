# -*- coding: utf-8 -*-
'''
from src.utils import currency, percent

def generate_summary(metrics):

    return f"""
### 📊 Resumen Ejecutivo

• Apartamentos vendidos: {metrics['vendidos']}

• Apartamentos disponibles: {metrics['disponibles']}

• Avance comercial: {metrics['avance']:.1f} %

• Valor vendido:
${metrics['valor_vendido']:,.0f}

• Valor inventario:
${metrics['inventario']:,.0f}

• Precio promedio:
${metrics['precio_promedio']:,.0f}

• Variación semanal:
{metrics['delta_vendidos']}
"""
'''

from src.utils import currency, percent


def generate_summary(metrics):

    return f"""
### 📊 Resumen Ejecutivo

• Apartamentos vendidos: {metrics['vendidos']}

• Apartamentos disponibles: {metrics['disponibles']}

• Avance comercial: {percent(metrics['avance'])}

• Valor vendido: {currency(metrics['valor_vendido'])}

• Valor inventario: {currency(metrics['inventario'])}

• Precio promedio: {currency(metrics['precio_promedio'])}
"""