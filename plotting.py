"""Functions that generate Dash plots."""
import datetime as dt
from typing_extensions import Literal

from flask_caching import Cache
import pandas as pd
import plotly.graph_objects as go

from constants import MARKER_SYMBOLS, COMUNA_TO_REGION, REGION_TO_COMUNAS, REGIONS_SORTED
from constants import REGIONS_TO_ABBR, POR_MIL_HAB


def make_fig_p1_casos_acumulados_comuna(
    dfs, figs, date_day, date_month, regions=[], comunas=[]):
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


def make_fig_fallecidos_cumulativo_t(
    dfs: pd.DataFrame, figs_cache: dict, date_day: int, date_month: str, *,
    yaxis_type: str, value_type: str):
    key = ('fallecidos_cumulativo_t', yaxis_type, value_type)

    if key not in figs_cache:
        data = dfs['fallecidos_cumulativo_t_per_k'] if value_type == POR_MIL_HAB else dfs['fallecidos_cumulativo_t']

        lo_yaxis_title = 'Muertes acumuladas' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
        lo_yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

        fig = go.Figure()
        for col in data.columns:
            scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                                 marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
            if col == 'Total':
                scatter.marker.color = 'black'

            fig.add_trace(scatter)

        fig.layout = {
            'title': f'Muertes acumulados por región ({date_day} {date_month})',
            'xaxis': {'title': 'Fecha'},
            'yaxis': {
                'title': lo_yaxis_title,
                'type': lo_yaxis_type
            },
            'height': 520
        }

        figs_cache[key] = fig
    return figs_cache[key]


def make_fig_fallecidos_etario_t(dfs: pd.DataFrame, figs_cache: dict,
    date_day: int, date_month: str):
    key = ('fallecidos_etario_t', '', '')

    if key not in figs_cache:
        data = dfs['fallecidos_etario_t']

        fig = go.Figure()
        bar = go.Bar(x=data.columns.values, y=data.iloc[-1, :].values, name='Muertes totales')
        fig.add_trace(bar)

        fig.layout = {
            'title': f'Muertes totales por rango etario (hasta {date_day} {date_month})',
            'xaxis': {'title': 'Rango etario'},
            'yaxis': {
                'title': 'Muertes confirmadas',
                'type': 'linear'
            },
            'height': 400
        }

        figs_cache[key] = fig
    return figs_cache[key]


def make_fig_casos_totales_cumulativo_t(
    dfs: pd.DataFrame, figs_cache: dict, date_day: int, date_month: str, *,
    yaxis_type: str, value_type: str):
    key = ('casos_totales_cumulativo_t', yaxis_type, value_type)

    if key not in figs_cache:
        data = dfs['casos_totales_cumulativo_t_per_k'] if value_type == POR_MIL_HAB else dfs['casos_totales_cumulativo_t']

        yaxis_title = 'Casos confirmados' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
        yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

        fig = go.Figure()
        for col in data.columns:
            scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                                 marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
            if col == 'Total':
                scatter.marker.color = 'black'

            fig.add_trace(scatter)

        fig.layout = {
            'title': f'Casos confirmados acumulados por región ({date_day} {date_month})',
            'xaxis': {'title': 'Fecha'},
            'yaxis': {
                'title': yaxis_title,
                'type': yaxis_type
            },
            'height': 520
        }

        figs_cache[key] = fig
    return figs_cache[key]


def make_fig_casos_totales_evolucion(
    dfs: pd.DataFrame, figs_cache: dict, date_day: int, date_month: str):
    key = ('casos_totales_evolucion', '', '')

    if key not in figs_cache:
        data = dfs['casos_totales_evolucion']
        fig = go.Figure()
        for col in data.columns:
            scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                                 marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
            if col == 'Total':
                scatter.marker.color = 'black'

            fig.add_trace(scatter)

        fig.layout = {
            'title': f'Evolución de casos confirmados por región ({date_day} {date_month})',
            'xaxis': {'title': 'Días desde el décimo caso confirmado en la región'},
            'yaxis': {'title': 'Número de casos confirmados', 'type': 'log'},
            'height': 520
        }

        figs_cache[key] = fig
    return figs_cache[key]


def make_fig_casos_nuevos_cumulativo_t(
    dfs: pd.DataFrame, figs_cache: dict, date_day: int, date_month: str, *,
    yaxis_type: str, value_type: str):
    key = ('casos_nuevos_cumulativo_t', yaxis_type, value_type)

    if key not in figs_cache:
        data = dfs['casos_nuevos_cumulativo_t_per_k'] if value_type == POR_MIL_HAB else dfs['casos_nuevos_cumulativo_t']

        yaxis_title = 'Casos confirmados nuevos' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
        yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

        last_date = dt.datetime.strptime(data.index[-1], '%Y-%m-%d')
        start_date = last_date - dt.timedelta(days=60)
        end_date = last_date + dt.timedelta(days=2)

        fig = go.Figure()
        for col in data.columns:
            scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                                 marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
            if col == 'Total':
                scatter.marker.color = 'black'

            fig.add_trace(scatter)

        fig.layout = {
            'title': f'Casos nuevos confirmados por región ({date_day} {date_month})',
            'xaxis': {
                'title': 'Fecha',
                'range': (start_date, end_date),
            },
            'yaxis': {
                'title': yaxis_title,
                'type': yaxis_type,
            },
            'height': 520
        }

        figs_cache[key] = fig
    return figs_cache[key]


def make_fig_uci_t(
    dfs: pd.DataFrame, figs_cache: dict, date_day: int, date_month: str, *,
    yaxis_type: str, value_type: str):
    key = ('uci_t', yaxis_type, value_type)

    if key not in figs_cache:
        data = dfs['uci_t_per_k'] if value_type == POR_MIL_HAB else dfs['uci_t']

        yaxis_title = 'Pacientes en UCI' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
        yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

        fig = go.Figure()
        for col in data.columns:
            scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                                 marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
            if col == 'Total':
                scatter.marker.color = 'black'

            fig.add_trace(scatter)

        fig.layout = {
            'title': f'Pacientes en UCI por región ({date_day} {date_month})',
            'xaxis': {'title': 'Fecha'},
            'yaxis': {
                'title': yaxis_title,
                'type': yaxis_type
            },
            'height': 520
        }

        figs_cache[key] = fig
    return figs_cache[key]


def make_fig_pcr_t(
    dfs: pd.DataFrame, figs_cache: dict, date_day: int, date_month: str, *,
    yaxis_type: str, value_type: str):
    key = ('pcr_t', yaxis_type, value_type)

    if key not in figs_cache:
        data = dfs['pcr_t_per_k'] if value_type == POR_MIL_HAB else dfs['pcr_t']

        yaxis_title = 'Tests PCR aplicados' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
        yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

        fig = go.Figure()
        for col in data.columns:
            scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                                 marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
            if col == 'Total':
                scatter.marker.color = 'black'

            fig.add_trace(scatter)

        fig.layout = {
            'title': f'Tests PCR aplicados por región ({date_day} {date_month})',
            'xaxis': {'title': 'Fecha'},
            'yaxis': {
                'title': yaxis_title,
                'type': yaxis_type
            },
            'height': 520
        }

        figs_cache[key] = fig
    return figs_cache[key]


def make_fig_numero_ventiladores_t(
    dfs: pd.DataFrame, figs_cache: dict, date_day: int, date_month: str):
    key = ('numero_ventiladores_t', '', '')

    if key not in figs_cache:
        data = dfs['numero_ventiladores_t']

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['ocupados'], mode='lines+markers', name='Ocupados', fill='tozeroy'))
        fig.add_trace(go.Scatter(x=data.index, y=data['total'], mode='lines+markers', name='Total'))
        fig.layout = {
            'title': f'Uso de ventiladores',
            'xaxis': {'title': 'Fecha'},
            'yaxis': {
                'title': 'Número de ventiladores',
                'range': [0, 2500]
            },
            'height': 520
        }

        figs_cache[key] = fig
    return figs_cache[key]


def make_fig_casos_nuevos_per_test(
    dfs: pd.DataFrame, figs_cache: dict, date_day: int, date_month: str, *,
    yaxis_type: str):
    key = ('casos_nuevos_per_test', yaxis_type, '')

    if key not in figs_cache:
        data = dfs['casos_nuevos_per_test']

        yaxis_title = 'Tasa de tests positivos [%]'
        yaxis_type = 'linear'

        fig = go.Figure()
        for col in data.columns:
            scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                                 marker_symbol=MARKER_SYMBOLS[col], marker_size=10, visible='legendonly')
            if col == 'Total':
                scatter.marker.color = 'black'
                scatter.visible = True

            fig.add_trace(scatter)

        fig.layout = {
            'title': f'Tasa de tests positivos ({date_day} {date_month})',
            'xaxis': {'title': 'Fecha'},
            'yaxis': {
                'title': yaxis_title,
                'type': yaxis_type,
                'range': [0.0, 0.5],
            },
            'height': 520,
            'yaxis_tickformat': '%',
        }

        figs_cache[key] = fig
    return figs_cache[key]
