"""Functions that generate Dash plots."""
import datetime as dt
import logging
from typing import Dict, List, Tuple

import plotly.graph_objects as go

from constants import MARKER_SYMBOLS, COMUNA_TO_REGION, REGION_TO_COMUNAS, REGIONS_SORTED
from constants import REGIONS_TO_ABBR, POR_MIL_HAB
from data_client import DataCache


class FigCache():
    def __init__(self, df_cache: DataCache):
        self.cache: Dict[Tuple[str, tuple, tuple], go.Figure] = {}
        self.df_cache = df_cache

    def get_fig(self, dataset_name: str, **kwargs) -> go.Figure:
        arg_names = tuple(kwargs.keys())
        arg_values = tuple(tuple(val) if isinstance(val, list) else val for val in kwargs.values())
        key = (dataset_name, arg_names, arg_values)
        return self.get(key)

    def get(self, key: Tuple[str, tuple, tuple]) -> go.Figure:
        fig = self.cache.get(key, None)
        dataset_name = key[0]

        if fig is None or self.df_cache.will_download(dataset_name):
            logging.warning(f'Cache miss for figure: {key}')
            fig = self._make_fig(key)
            self.cache[key] = fig

        return self.cache[key]

    def __getitem__(self, key: Tuple[str, tuple, tuple]) -> go.Figure:
        return self.get(key)

    def _make_fig(self, key: Tuple[str, tuple, tuple]):
        dataset_name, arg_names, arg_values = key
        kwargs = dict(zip(arg_names, arg_values))

        name_to_func = {
            'p1_casos_acumulados_comuna': make_fig_p1_casos_acumulados_comuna,
            'fallecidos_cumulativo_t': make_fig_fallecidos_cumulativo_t,
            'fallecidos_etario_t': make_fig_fallecidos_etario_t,
            'casos_totales_cumulativo_t': make_fig_casos_totales_cumulativo_t,
            'casos_nuevos_cumulativo_t': make_fig_casos_nuevos_cumulativo_t,
            'uci_t': make_fig_uci_t,
            'pcr_t': make_fig_pcr_t,
            'numero_ventiladores_t': make_fig_numero_ventiladores_t,
            'casos_nuevos_per_test': make_fig_casos_nuevos_per_test,
        }

        func = name_to_func[dataset_name]
        return func(dfs=self.df_cache, **kwargs)  # type: ignore


def make_fig_p1_casos_acumulados_comuna(
        dfs: DataCache, *, regions: List[str], comunas: List[str], **kwargs):
    data = dfs['p1_casos_acumulados_comuna']

    yaxis_title = 'Casos acumulados'
    yaxis_type = 'linear'

    fig = go.Figure()
    for region in REGIONS_SORTED:
        if region in regions:
            for comuna in REGION_TO_COMUNAS[region]:
                casos = data[comuna][-1]
                if casos >= 10:
                    scatter = go.Scatter(
                        x=data.index, y=data[comuna], mode='lines+markers',
                        name=f'{comuna} ({REGIONS_TO_ABBR[region]})',
                        marker_symbol=MARKER_SYMBOLS[region], marker_size=8,
                        showlegend=True
                    )
                    fig.add_trace(scatter)
        else:
            for comuna in comunas:
                if region == COMUNA_TO_REGION[comuna] and data[comuna][-1] >= 10:
                    scatter = go.Scatter(
                        x=data.index, y=data[comuna], mode='lines+markers',
                        name=f'{comuna} ({REGIONS_TO_ABBR[region]})', marker_symbol=MARKER_SYMBOLS[region], marker_size=8,
                        showlegend=True
                    )
                    fig.add_trace(scatter)

    fig.layout = {
        'title': 'Casos acumulados por comuna',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type,
        },
        'height': 520
    }

    return fig


def make_fig_fallecidos_cumulativo_t(
        dfs: DataCache, *, yaxis_type: str, value_type: str, **kwargs):
    data = dfs['fallecidos_cumulativo_t_per_k'] if value_type == POR_MIL_HAB else dfs['fallecidos_cumulativo_t']

    lo_yaxis_title = 'Muertes acumuladas' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    lo_yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(
            x=data.index, y=data[col], mode='lines+markers', name=col,
            marker_symbol=MARKER_SYMBOLS[col], marker_size=10
        )
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': 'Muertes acumulados por región',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': lo_yaxis_title,
            'type': lo_yaxis_type
        },
        'height': 520
    }

    return fig


def make_fig_fallecidos_etario_t(dfs: DataCache, **kwargs):
    data = dfs['fallecidos_etario_t']

    fig = go.Figure()
    bar_trace = go.Bar(x=data.columns.values, y=data.iloc[-1, :].values, name='Muertes totales')
    fig.add_trace(bar_trace)

    fig.layout = {
        'title': 'Muertes totales por rango etario',
        'xaxis': {'title': 'Rango etario'},
        'yaxis': {
            'title': 'Muertes confirmadas',
            'type': 'linear'
        },
        'height': 400
    }

    return fig


def make_fig_casos_totales_cumulativo_t(
        dfs: DataCache, *, yaxis_type: str, value_type: str, **kwargs):
    data = dfs['casos_totales_cumulativo_t_per_k'] if value_type == POR_MIL_HAB else dfs['casos_totales_cumulativo_t']

    yaxis_title = 'Casos confirmados' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(
            x=data.index, y=data[col], mode='lines+markers', name=col,
            marker_symbol=MARKER_SYMBOLS[col], marker_size=10
        )
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': 'Casos confirmados acumulados por región',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type
        },
        'height': 520
    }

    return fig


def make_fig_casos_totales_evolucion(dfs: DataCache, **kwargs):
    data = dfs['casos_totales_evolucion']
    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(
            x=data.index, y=data[col], mode='lines+markers', name=col,
            marker_symbol=MARKER_SYMBOLS[col], marker_size=10
        )
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': 'Evolución de casos confirmados por región',
        'xaxis': {'title': 'Días desde el décimo caso confirmado en la región'},
        'yaxis': {'title': 'Número de casos confirmados', 'type': 'log'},
        'height': 520
    }

    return fig


def make_fig_casos_nuevos_cumulativo_t(
        dfs: DataCache, *, yaxis_type: str, value_type: str, **kwargs):
    data = dfs['casos_nuevos_cumulativo_t_per_k'] if value_type == POR_MIL_HAB else dfs['casos_nuevos_cumulativo_t']

    yaxis_title = 'Casos confirmados nuevos' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    last_date = dt.datetime.strptime(data.index[-1], '%Y-%m-%d')
    start_date = last_date - dt.timedelta(days=60)
    end_date = last_date + dt.timedelta(days=2)

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(
            x=data.index, y=data[col], mode='lines+markers', name=col,
            marker_symbol=MARKER_SYMBOLS[col], marker_size=10
        )
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': 'Casos nuevos confirmados por región',
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

    return fig


def make_fig_uci_t(
        dfs: DataCache, *, yaxis_type: str, value_type: str, **kwargs):
    data = dfs['uci_t_per_k'] if value_type == POR_MIL_HAB else dfs['uci_t']

    yaxis_title = 'Pacientes en UCI' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(
            x=data.index, y=data[col], mode='lines+markers', name=col,
            marker_symbol=MARKER_SYMBOLS[col], marker_size=10
        )
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': 'Pacientes en UCI por región',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type
        },
        'height': 520
    }

    return fig


def make_fig_pcr_t(
        dfs: DataCache, *, yaxis_type: str, value_type: str, **kwargs):
    data = dfs['pcr_t_per_k'] if value_type == POR_MIL_HAB else dfs['pcr_t']

    yaxis_title = 'Tests PCR aplicados' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(
            x=data.index, y=data[col], mode='lines+markers', name=col,
            marker_symbol=MARKER_SYMBOLS[col], marker_size=10
        )
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': 'Tests PCR aplicados por región',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type
        },
        'height': 520
    }

    return fig


def make_fig_numero_ventiladores_t(dfs: DataCache, **kwargs):
    data = dfs['numero_ventiladores_t']

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data.index, y=data['ocupados'], mode='lines+markers', name='Ocupados', fill='tozeroy'
        )
    )
    fig.add_trace(go.Scatter(x=data.index, y=data['total'], mode='lines+markers', name='Total'))
    fig.layout = {
        'title': 'Uso de ventiladores',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': 'Número de ventiladores',
        },
        'height': 520
    }

    return fig


def make_fig_casos_nuevos_per_test(dfs: DataCache, *, yaxis_type: str, **kwargs):
    data = dfs['casos_nuevos_per_test']

    yaxis_title = 'Tasa de tests positivos [%]'
    yaxis_type = 'linear'

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(
            x=data.index, y=data[col], mode='lines+markers', name=col,
            marker_symbol=MARKER_SYMBOLS[col], marker_size=10, visible='legendonly'
        )
        if col == 'Total':
            scatter.marker.color = 'black'
            scatter.visible = True

        fig.add_trace(scatter)

    fig.layout = {
        'title': 'Tasa de tests positivos',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type,
            'range': [0.0, 0.5],
        },
        'height': 520,
        'yaxis_tickformat': '%',
    }

    return fig
