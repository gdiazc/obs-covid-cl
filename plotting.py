"""Functions that generate Dash plots."""
from flask_caching import Cache
import plotly.graph_objects as go

from constants import MARKER_SYMBOLS, COMUNA_TO_REGION, REGION_TO_COMUNAS, REGIONS_SORTED
from constants import REGIONS_TO_ABBR


def make_fig_p1_casos_acumulados_comuna(dfs, figs, date_day, date_month,
                                        regions=[], comunas=[]):
    key = ('p1_casos_acumulados_comuna', tuple(regions), tuple(comunas))

    if key not in figs:
        data = dfs['p1_casos_acumulados_comuna']

        yaxis_title = 'Casos acumulados'
        yaxis_type = 'linear'

        fig = go.Figure()
        for region in REGIONS_SORTED:
            if region in regions:
                for comuna in REGION_TO_COMUNAS[region]:
                    casos = data[comuna][-1]
                    if casos >= 10:
                        scatter = go.Scatter(x=data.index, y=data[comuna], mode='lines+markers',
                                        name=f'{comuna} ({REGIONS_TO_ABBR[region]})', marker_symbol=MARKER_SYMBOLS[region], marker_size=8,
                                        showlegend=True)
                        fig.add_trace(scatter)
            else:
                for comuna in comunas:
                    if region == COMUNA_TO_REGION[comuna] and data[comuna][-1] >= 10:
                        scatter = go.Scatter(x=data.index, y=data[comuna], mode='lines+markers',
                                        name=f'{comuna} ({REGIONS_TO_ABBR[region]})', marker_symbol=MARKER_SYMBOLS[region], marker_size=8,
                                        showlegend=True)
                        fig.add_trace(scatter)

        # for col in data.columns:
        #     region = COMUNA_TO_REGION[col]
        #     casos = data[col][-1]
        #     if region in regions and casos >= 10:
        #         scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers',
        #                             name=col, marker_symbol=MARKER_SYMBOLS[region], marker_size=8,
        #                             showlegend=True)
        #         fig.add_trace(scatter)

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

        figs[key] = fig
    return figs[key]
