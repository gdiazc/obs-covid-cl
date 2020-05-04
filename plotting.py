"""Functions that generate Dash plots."""
from flask_caching import Cache
import plotly.graph_objects as go

from constants import MARKER_SYMBOLS, COMUNA_TO_REGION


def make_fig_p1_casos_acumulados_comuna(dfs, date_day, date_month,
                                        regions=['Metropolitana', 'Valparaíso']):
    data = dfs['p1_casos_acumulados_comuna']

    yaxis_title = 'Casos acumulados'
    yaxis_type = 'linear'

    fig = go.Figure()
    for col in data.columns:
        region = COMUNA_TO_REGION[col]
        casos = data[col][-1]
        if region in regions and casos > 0:
            scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers',
                                 name=col, marker_symbol=MARKER_SYMBOLS[region], marker_size=8)
            fig.add_trace(scatter)

    fig.layout = {
        'title': f'Casos acumulados por comuna ({date_day} {date_month})',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type,
            # 'range': [0.0, 50.0],
        },
        'height': 520
    }

    return fig
