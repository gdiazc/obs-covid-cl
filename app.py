# -*- coding: utf-8 -*-
import datetime as dt
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sqlalchemy

from dash.dependencies import Input, Output


external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']

dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dash_app.title = 'obs-covid chile'

app = dash_app.server

DB = None

DASH_ENV = os.environ.get('DASH_ENV', None)
IS_DEV = DASH_ENV is None
if IS_DEV is None:
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_NAME = os.environ['DB_NAME']
    CLOUD_SQL_CONNECTION_NAME = os.environ['CLOUD_SQL_CONNECTION_NAME']


def get_db():
    global DB
    if DB is None:
        # postgres://<db_user>:<db_pass>@/<db_name>?unix_sock=/cloudsql/<cloud_sql_instance_name>/.s.PGSQL.5432
        sql_url = sqlalchemy.engine.url.URL(
            drivername='postgres+pg8000',
            username=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
            query={
                'unix_sock': '/cloudsql/{}/.s.PGSQL.5432'.format(CLOUD_SQL_CONNECTION_NAME)}
        )
        DB = sqlalchemy.create_engine(sql_url)
    return DB


if not IS_DEV:
    DB = get_db()
    # df = pd.read_sql('casos_totales_cumulativo_t', con=DB, parse_dates=['Region']).set_index('Region')
    df = pd.read_sql('casos_totales_cumulativo_t', con=DB, index_col=['Region'])
else:
    url = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/CasosTotalesCumulativo_T.csv'
    df = pd.read_csv(url, index_col='Region')

POPULATION = {
    'Arica y Parinacota': 226068,
    'Tarapacá': 581802,
    'Antofagasta': 607534,
    'Atacama': 286168,
    'Coquimbo': 757586,
    'Valparaíso': 1815902,
    'Metropolitana': 7112808,
    'O’Higgins': 914555,
    'Maule': 1044950,
    'Ñuble': 480609,
    'Biobío': 1556805,
    'Araucanía': 957224,
    'Los Ríos': 384837,
    'Los Lagos': 828708,
    'Aysén': 103158,
    'Magallanes': 166533,
}
POPULATION['Total'] = sum(POPULATION.values())

MARKER_SYMBOLS = {
    'Arica y Parinacota': 'triangle-up',
    'Tarapacá': 'triangle-left',
    'Antofagasta': 'triangle-down',
    'Atacama': 'triangle-right',
    'Coquimbo': 'triangle-ne',
    'Valparaíso': 'triangle-sw',
    'Metropolitana': 'star',
    'O’Higgins': 'hexagram',
    'Maule': 'star-diamond',
    'Ñuble': 'diamond-tall',
    'Biobío': 'diamond-wide',
    'Araucanía': 'star-triangle-up',
    'Los Ríos': 'star-triangle-down',
    'Los Lagos': 'star-square',
    'Aysén': 'bowtie',
    'Magallanes': 'hourglass',
    'Total': 'x'
}

URLS = {
    'casos_nuevos_cumulativo_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto13/CasosNuevosCumulativo_T.csv',
    'uci_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto8/UCI_T.csv',
    'numero_ventiladores_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto20/NumeroVentiladores_T.csv',
    'pcr_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR_T.csv',
    'fallecidos_cumulativo_t': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto14/FallecidosCumulativo_T.csv'
}

DFS = {}

# fallecidos_cumulativo_t
DFS['fallecidos_cumulativo_t'] = pd.read_csv(URLS['fallecidos_cumulativo_t'], index_col='Region')
DFS['fallecidos_cumulativo_t_per_k'] = DFS['fallecidos_cumulativo_t'].apply(lambda col: col * 1_000.0 / POPULATION[col.name])

# uci_t
DFS['uci_t'] = pd.read_csv(URLS['uci_t'], index_col='Region')
DFS['uci_t'] = DFS['uci_t'].loc['2020-04-01':, :]  # type: ignore
DFS['uci_t']['Total'] = DFS['uci_t'].sum(axis=1)
DFS['uci_t_per_k'] = DFS['uci_t'].apply(lambda col: col * 1_000.0 / POPULATION[col.name])

# casos_nuevos_cumulativo_t
DFS['casos_nuevos_cumulativo_t'] = pd.read_csv(URLS['casos_nuevos_cumulativo_t'], index_col='Region')
DFS['casos_nuevos_cumulativo_t_per_k'] = DFS['casos_nuevos_cumulativo_t'].apply(lambda col: col * 1_000.0 / POPULATION[col.name])

# NumeroVentiladores_T
DFS['numero_ventiladores_t'] = pd.read_csv(URLS['numero_ventiladores_t'], index_col='Ventiladores')
DFS['numero_ventiladores_t'] = DFS['numero_ventiladores_t'].drop(columns=['disponibles'])

# PCR_T
DFS['pcr_t'] = pd.read_csv(URLS['pcr_t'], index_col='Region', na_values='-')
DFS['pcr_t'] = DFS['pcr_t'].loc['2020-04-09':, :]  # type: ignore
DFS['pcr_t']['Total'] = DFS['pcr_t'].sum(axis=1)
DFS['pcr_t_per_k'] = DFS['pcr_t'].apply(lambda col: col * 1_000.0 / POPULATION[col.name])

# casos_nuevos_per_test
DFS['casos_nuevos_per_test'] = (DFS['casos_nuevos_cumulativo_t'] / DFS['pcr_t']).loc['2020-04-09':, :] * 100.0   # type: ignore

POR_MIL_HAB = 'Por Mil Hab.'


def prepare_report():
    # Regiones with top new deaths:
    top_3_deaths = sorted(DFS['fallecidos_cumulativo_t'].iloc[-1].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]
    top_3_deaths_last_day = sorted(DFS['fallecidos_cumulativo_t'].diff().iloc[-1].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]
    top_3_uci = sorted(DFS['uci_t'].iloc[-1].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]
    top_3_new_cases = sorted(DFS['casos_nuevos_cumulativo_t'].iloc[-1].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]
    top_3_new_cases_per_k = sorted(DFS['casos_nuevos_cumulativo_t_per_k'].iloc[-1].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]
    tests_today = DFS['pcr_t'].iloc[-1]['Total']
    tests_yesterday = DFS['pcr_t'].iloc[-2]['Total']
    tests_diff = tests_today - tests_yesterday
    report = {
        'top_3_deaths': top_3_deaths,
        'top_3_deaths_last_day': top_3_deaths_last_day,
        'top_3_uci': top_3_uci,
        'top_3_new_cases': top_3_new_cases,
        'top_3_new_cases_per_k': top_3_new_cases_per_k,
        'tests_today': tests_today,
        'tests_yesterday': tests_yesterday,
        'tests_diff': tests_diff
    }
    return report


REPORT = prepare_report()


def get_start_days(df):
    """Build a series with regions as an index, values being date at which 10 cases was reached."""
    df_is_day_0 = ((df >= 10).astype(int).cumsum() == 1).astype(int)
    start_days = df_is_day_0.apply(lambda col: df.index.values * col).sum(axis=0)
    return start_days


def days_to_shift(col):
    earliest_date = dt.datetime.strptime('2020-03-03', '%Y-%m-%d')
    return (earliest_date - dt.datetime.strptime(dias_iniciales[col.name], '%Y-%m-%d')).days


# Transform:
dias_iniciales = get_start_days(df)
plot_df = df.drop(columns=['Aysén'])\
            .apply(lambda col: col.shift(days_to_shift(col)))\
            .reset_index()\
            .drop(columns=['Region'])

df_per_k = df.apply(lambda col: col * 1_000.0 / POPULATION[col.name])

# fig = px.line(plot_df,
#               #   x='Días desde el décimo caso confirmado en la región',
#               x=plot_df.index,
#               #   y='Número de casos confirmados (escala logarítmica)')
#               y=plot_df['Total'])

date_day = 19


def make_fig_fallecidos_cumulativo_t(yaxis_type='Lineal', value_type=POR_MIL_HAB):
    data = DFS['fallecidos_cumulativo_t_per_k'] if value_type == POR_MIL_HAB else DFS['fallecidos_cumulativo_t']

    yaxis_title = 'Muertes acumuladas' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                             marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': f'Muertes acumulados por región ({date_day} abril)',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type
        },
        'height': 520
    }
    return fig


def make_fig1(yaxis_type='Lineal', value_type=POR_MIL_HAB):
    data = df_per_k if value_type == POR_MIL_HAB else df

    yaxis_title = 'Casos confirmados' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                             marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

        # fig.add_trace(go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
        #                          marker_symbol=MARKER_SYMBOLS[col], marker_size=10,))

    fig.layout = {
        'title': f'Casos confirmados acumulados por región ({date_day} abril)',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type
        },
        'height': 520
    }
    return fig


def make_fig2():
    data = plot_df
    fig = go.Figure()
    for col in plot_df.columns:
        scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                             marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': f'Evolución de casos confirmados por región ({date_day} abril)',
        'xaxis': {'title': 'Días desde el décimo caso confirmado en la región'},
        'yaxis': {'title': 'Número de casos confirmados', 'type': 'log'},
        'height': 520
    }
    return fig


def make_fig_casos_nuevos_cumulativo_t(yaxis_type='Lineal', value_type=POR_MIL_HAB):
    data = DFS['casos_nuevos_cumulativo_t_per_k'] if value_type == POR_MIL_HAB else DFS['casos_nuevos_cumulativo_t']

    yaxis_title = 'Casos confirmados nuevos' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    fig = go.Figure()
    for col in data.columns:
        scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                             marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': f'Casos nuevos confirmados por región ({date_day} abril)',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type
        },
        'height': 520
    }
    return fig


def make_fig_uci_t(yaxis_type='Lineal', value_type=POR_MIL_HAB):
    data = DFS['uci_t_per_k'] if value_type == POR_MIL_HAB else DFS['uci_t']

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
        'title': f'Pacientes en UCI por región ({date_day} abril)',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type
        },
        'height': 520
    }
    return fig


def make_fig_pcr_t(yaxis_type='Lineal', value_type=POR_MIL_HAB):
    data = DFS['pcr_t_per_k'] if value_type == POR_MIL_HAB else DFS['pcr_t']

    yaxis_title = 'Tests PCR aplicados' + (' por mil hab.' if value_type == POR_MIL_HAB else '')
    yaxis_type = 'linear' if yaxis_type == 'Lineal' else 'log'

    fig = go.Figure()
    for col in data.columns:
        # fig.add_trace(go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
        #                          marker_symbol=MARKER_SYMBOLS[col], marker_size=10))
        scatter = go.Scatter(x=data.index, y=data[col], mode='lines+markers', name=col,
                             marker_symbol=MARKER_SYMBOLS[col], marker_size=10)
        if col == 'Total':
            scatter.marker.color = 'black'

        fig.add_trace(scatter)

    fig.layout = {
        'title': f'Tests PCR aplicados por región ({date_day} abril)',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type
        },
        'height': 520
    }
    return fig


def make_fig4():
    data = DFS['numero_ventiladores_t']

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['ocupados'], mode='lines+markers', name='Ocupados', fill='tozeroy'))
    fig.add_trace(go.Scatter(x=data.index, y=data['total'], mode='lines+markers', name='Total'))
    fig.layout = {
        'title': f'Uso de ventiladores',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': 'Número de ventiladores',
            'range': [0, 2000]
        },
        'height': 520
    }
    return fig


def make_fig_casos_nuevos_per_test(yaxis_type='Lineal'):
    data = DFS['casos_nuevos_per_test']

    yaxis_title = 'Casos nuevos por cada test'
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
        'title': f'Casos nuevos por cada test ({date_day} abril)',
        'xaxis': {'title': 'Fecha'},
        'yaxis': {
            'title': yaxis_title,
            'type': yaxis_type,
            'range': [0.0, 50.0],
        },
        'height': 520
    }
    return fig


dash_app.layout = html.Div(className='container', children=[
    html.H1(children='obs-covid chile'),

    dcc.Markdown(children='''
    Gráficos actualizados **automáticamente** en base a datos del
    [Ministerio de Ciencias](http://www.minciencia.gob.cl/covid19).

    Todos los gráficos son interactivos:
    - Click y doble click en nombres de series (por ejemplo, nombres de regiones) para seleccionarlas.
    - Ver botones para opciones incluyendo zoomear y guardar imágenes.

    Creado por [@gdiazc](https://twitter.com/gdiazc).
    '''),

    html.H2(id='reporte', className='mt-4', children=f'Reporte ejecutivo {date_day} abril'),

    dcc.Markdown('''
    Cifras importantes del día, actualizadas **automáticamente**.

    1. Muertes ([ir al gráfico](#h2_fallecidos_cumulativo_t))
        - **Regiones con más muertes hoy:**
            - {top_3_deaths_last_day_string}
        - **Regiones con más muertes hasta la fecha:**
            - {top_3_deaths_string}
    1. Casos críticos ([ir al gráfico](#h2_uci_t))
        - **Regiones con más pacientes UCI hoy:**
            - {top_3_uci_string}
    1. Casos confirmados ([ir al gráfico](#h2_casos_nuevos_cumulativo_t))
        - **Regiones con más casos nuevos hoy:**
            - {top_3_new_cases_string}
    1. Testeo ([ir al gráfico](#h2_pcr_t))
        - **Tests PCR realizados hoy:**
            - {tests_today_string} tests ({tests_diff_string})
    '''.format(
        top_3_deaths_last_day_string=', '.join([f'{reg} (`{int(n)}` muertes)' for reg, n in REPORT['top_3_deaths_last_day']]),
        top_3_deaths_string=', '.join([f'{reg} (`{int(n)}` muertes)' for reg, n in REPORT['top_3_deaths']]),
        top_3_uci_string=', '.join([f'{reg} (`{n}` pacientes UCI)' for reg, n in REPORT['top_3_uci']]),
        top_3_new_cases_string=', '.join([f'{reg} (`{n}` casos)' for reg, n in REPORT['top_3_new_cases']]),
        # top_3_new_cases_per_k_string=', '.join([f'{reg} ({n:.2} casos)' for reg, n in REPORT['top_3_new_cases_per_k']]),
        tests_today_string=f'`{int(REPORT["tests_today"])}`',
        tests_diff_string='`' + str(abs(int(REPORT['tests_diff']))) + ('` más' if REPORT['tests_diff'] > 0 else '` menos') + ' que ayer',
    )),

    html.H2(id='h2_fallecidos_cumulativo_t', className='mt-4',
            children='Gráfico 1. Muertes acumuladas por región'),

    dcc.Markdown('''
        Opciones:
    '''),

    dbc.Form(inline=True, children=[
        # dbc.FormGroup(className="mr-3", children=[
        #     dcc.RadioItems(
        #         id='graph_fallecidos_cumulativo_t-yaxis-type',
        #         className='form-check form-check-inline',
        #         options=[{'label': i, 'value': i} for i in ['Lineal', 'Logarítmico']],
        #         value='Lineal',
        #         labelStyle={'display': 'inline-block'},
        #         labelClassName='form-check-label mr-2'
        #     )
        # ]),
        dbc.FormGroup(className="mr-3", children=[
            dcc.RadioItems(
                id='graph_fallecidos_cumulativo_t-value-type',
                className='form-check form-check-inline',
                options=[{'label': i, 'value': i} for i in ['Total', POR_MIL_HAB]],
                value=POR_MIL_HAB,
                labelStyle={'display': 'inline-block'},
                labelClassName='form-check-label mr-2'
            )
        ])
    ]),

    dcc.Graph(
        id='graph_fallecidos_cumulativo_t',
        figure=make_fig_fallecidos_cumulativo_t()
    ),

    html.H2(className='mt-4', children='Gráfico 2. Casos confirmados acumulados por región'),

    dcc.Markdown('''
        **Nota:** La cifra de número de casos confirmados está altamente correlacionada
        con el número de test aplicados, por lo que no se recomienda usarla para estimar
        el tamaño de la población infectada.

        Opciones:
    '''),

    dbc.Form(inline=True, children=[
        dbc.FormGroup(className="mr-3", children=[
            dcc.RadioItems(
                id='graph1-yaxis-type',
                className='form-check form-check-inline',
                options=[{'label': i, 'value': i} for i in ['Lineal', 'Logarítmico']],
                value='Lineal',
                labelStyle={'display': 'inline-block'},
                labelClassName='form-check-label mr-2'
            )
        ]),
        dbc.FormGroup(className="mr-3", children=[
            dcc.RadioItems(
                id='graph1-value-type',
                className='form-check form-check-inline',
                options=[{'label': i, 'value': i} for i in ['Total', POR_MIL_HAB]],
                value=POR_MIL_HAB,
                labelStyle={'display': 'inline-block'},
                labelClassName='form-check-label mr-2'
            )
        ])
    ]),

    dcc.Graph(
        id='graph1',
        figure=make_fig1()
    ),

    html.H2(className='mt-4', children='Gráfico 3. Evolución de casos totales por región'),

    dcc.Markdown('''
        Esta variante cambia el eje horizontal: en vez de reportar cifras según fecha, se reportan según "días desde alcanzar 10 casos confirmado".
    '''),

    dcc.Graph(
        id='graph2',
        figure=make_fig2()
    ),

    # ===========
    # Gráfico 4. Casos nuevos confirmados por región
    # ===========

    html.H2(id='h2_casos_nuevos_cumulativo_t', className='mt-4', children='Gráfico 4. Casos nuevos confirmados por región'),

    dcc.Markdown('''
    Opciones:
    '''),

    dbc.Form(inline=True, children=[
        dbc.FormGroup(className="mr-3", children=[
            dcc.RadioItems(
                id='graph_casos_nuevos_cumulativo_t-value-type',
                className='form-check form-check-inline',
                options=[{'label': i, 'value': i} for i in ['Total', POR_MIL_HAB]],
                value=POR_MIL_HAB,
                labelStyle={'display': 'inline-block'},
                labelClassName='form-check-label mr-2'
            )
        ])
    ]),

    dcc.Graph(
        id='graph_casos_nuevos_cumulativo_t',
        figure=make_fig_casos_nuevos_cumulativo_t()
    ),

    html.H2(id='h2_uci_t', className='mt-4',
            children='Gráfico 5. Pacientes críticos por región'),

    dcc.Markdown('''
        Pacientes en Unidades de Cuidados Intensivos.

        Opciones:
    '''),

    dbc.Form(inline=True, children=[
        dbc.FormGroup(className="mr-3", children=[
            dcc.RadioItems(
                id='graph_uci_t-value-type',
                className='form-check form-check-inline',
                options=[{'label': i, 'value': i} for i in ['Total', POR_MIL_HAB]],
                value=POR_MIL_HAB,
                labelStyle={'display': 'inline-block'},
                labelClassName='form-check-label mr-2'
            )
        ])
    ]),

    dcc.Graph(id='graph_uci_t', figure=make_fig_uci_t()),

    # ===========
    # Gráfico 6. Tests PCR aplicados
    # ===========

    html.H2(id='h2_pcr_t', className='mt-4', children='Gráfico 6. Tests PCR aplicados'),

    dcc.Markdown('''
        Los datos sobre tests PCR aplicados tienen muchos vacíos, lo que se traduce en líneas disconexas en el gráfico.

        Opciones:
    '''),

    dbc.Form(inline=True, children=[
        dbc.FormGroup(className="mr-3", children=[
            dcc.RadioItems(
                id='graph_pcr_t-value-type',
                className='form-check form-check-inline',
                options=[{'label': i, 'value': i} for i in ['Total', POR_MIL_HAB]],
                value=POR_MIL_HAB,
                labelStyle={'display': 'inline-block'},
                labelClassName='form-check-label mr-2'
            )
        ])
    ]),

    dcc.Graph(
        id='graph_pcr_t',
        figure=make_fig_pcr_t()
    ),

    html.H2(className='mt-4', children='Gráfico 7. Uso y capacidad de ventiladores'),

    dcc.Markdown('''
    Por ahora sólo hay cifras disponibles para el total nacional.
    '''),

    dcc.Graph(
        id='graph4',
        figure=make_fig4()
    ),

    # ===========
    # Gráfico 8. Casos nuevos por cada test
    # ===========

    html.H2(id='h2_casos_nuevos_per_test', className='mt-4',
            children='Gráfico 8. Casos nuevos por cada test'),

    dcc.Markdown('''
    Casos nuevos divididos en el número de tests que se realizaron. Este gráfico asume que todos los
    nuevos casos son confirmados a través de tests PCR.

    **Nota:** Hay errores en estos datos debido a que es imposible tener un valor por sobre 100% (ver Magallanes).
    '''),

    dcc.Graph(
        id='graph_casos_nuevos_per_test',
        figure=make_fig_casos_nuevos_per_test()
    ),

])


@dash_app.callback(
    Output('graph_fallecidos_cumulativo_t', 'figure'),
    [Input('graph_fallecidos_cumulativo_t-value-type', 'value')])
def update_graph_fallecidos_cumulativo_t(value_type):
    return make_fig_fallecidos_cumulativo_t(value_type=value_type)


@dash_app.callback(
    Output('graph1', 'figure'),
    [Input('graph1-yaxis-type', 'value'),
     Input('graph1-value-type', 'value')])
def update_graph1(yaxis_type, value_type):
    return make_fig1(yaxis_type=yaxis_type, value_type=value_type)


@dash_app.callback(
    Output('graph_casos_nuevos_cumulativo_t', 'figure'),
    [Input('graph_casos_nuevos_cumulativo_t-value-type', 'value')])
def update_graph_casos_nuevos_cumulativo_t(value_type):
    return make_fig_casos_nuevos_cumulativo_t(value_type=value_type)


@dash_app.callback(
    Output('graph_pcr_t', 'figure'),
    [Input('graph_pcr_t-value-type', 'value')])
def update_graph_pcr_t(value_type):
    return make_fig_pcr_t(value_type=value_type)


@dash_app.callback(
    Output('graph_uci_t', 'figure'),
    [Input('graph_uci_t-value-type', 'value')])
def update_graph_uci_t(value_type):
    return make_fig_uci_t(value_type=value_type)


if __name__ == '__main__':
    dash_app.run_server(debug=True)
