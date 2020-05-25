"""Functions for downloading data from API."""
import datetime as dt
import logging
from typing import Dict, Tuple

import pandas as pd

from constants import URLS, REGION_TO_POPULATION


logger = logging.getLogger('data_client')
logger.setLevel(logging.INFO)


class DataCache():
    def __init__(self):
        self.cache: Dict[str, Tuple[dt.datetime, pd.DataFrame]] = {}
        self.expiry_time = dt.timedelta(hours=6)
    
    def will_download(self, dataset_name: str):
        dataset_dt, dataset = self.cache.get(dataset_name, (None, None))
        current_dt = dt.datetime.now()
        return dataset is None or dataset_dt is None or current_dt - dataset_dt > self.expiry_time
    
    def get_with_timestamp(self, dataset_name: str) -> Tuple[dt.datetime, pd.DataFrame]:
        if dataset_name.endswith('_per_k'):
            base_dataset_name = dataset_name.replace('_per_k', '')
            base_dataset_dt, base_dataset = self.get_with_timestamp(base_dataset_name)
            per_k_dataset = base_dataset.apply(lambda col: col * 1_000.0 / REGION_TO_POPULATION[col.name])
            return (base_dataset_dt, per_k_dataset)
        
        if dataset_name == 'casos_nuevos_per_test':
            dt1, df_casos_nuevos_cumulativo_t = self.get_with_timestamp('casos_nuevos_cumulativo_t')
            dt2, df_pcr_t = self.get_with_timestamp('pcr_t')
            ans = (df_casos_nuevos_cumulativo_t / df_pcr_t).loc['2020-04-09':, :]  # type: ignore
            return (min(dt1, dt2), ans)

        dataset_dt, dataset = self.cache.get(dataset_name, (None, None))
        current_dt = dt.datetime.now()

        if dataset is None or dataset_dt is None or current_dt - dataset_dt > self.expiry_time:
            logging.warn(f'Cache miss for {dataset_name}: {dataset_dt}')
            dataset = self._download(dataset_name)
            self.cache[dataset_name] = (current_dt, dataset)

        return self.cache[dataset_name]
    
    def get(self, dataset_name: str):
        return self.get_with_timestamp(dataset_name)[1]
    
    def __getitem__(self, dataset_name: str):
        return self.get(dataset_name)

    def _download(self, dataset_name: str):
        name_to_func = {
            'p1_casos_acumulados_comuna': download_p1_casos_acumulados_comuna,
            'casos_totales_cumulativo_t': download_casos_totales_cumulativo_t,
            'fallecidos_cumulativo_t': download_fallecidos_cumulativo_t,
            'fallecidos_etario_t': download_fallecidos_etario_t,
            'uci_t': download_uci_t,
            'casos_nuevos_cumulativo_t': download_casos_nuevos_cumulativo_t,
            'numero_ventiladores_t': download_numero_ventiladores_t,
            'pcr_t': download_pcr_t,
        }

        func = name_to_func[dataset_name]
        return func()


def download_p1_casos_acumulados_comuna():
    ans = pd.read_csv(URLS['p1_casos_acumulados_comuna'], index_col='Region')
    ans.columns = ans.loc['Comuna']
    ans = ans.iloc[4:-1]
    ans = ans.astype(float)
    return ans


def download_casos_totales_cumulativo_t():
    ans = pd.read_csv(URLS['casos_totales_cumulativo_t'], index_col='Region')
    return ans


def download_fallecidos_cumulativo_t():
    ans = pd.read_csv(URLS['fallecidos_cumulativo_t'], index_col='Region')
    return ans


def download_fallecidos_etario_t():
    ans = pd.read_csv(URLS['fallecidos_etario_t'], index_col='Grupo de edad')
    return ans


def download_uci_t():
    ans = pd.read_csv(URLS['uci_t'], index_col='Region')
    ans = ans.loc['2020-04-01':, :]  # type: ignore
    ans['Total'] = ans.sum(axis=1)
    return ans


def download_casos_nuevos_cumulativo_t():
    ans = pd.read_csv(URLS['casos_nuevos_cumulativo_t'], index_col='Region')
    return ans


def download_numero_ventiladores_t():
    ans = pd.read_csv(URLS['numero_ventiladores_t'], index_col='Ventiladores')
    ans = ans.drop(columns=['disponibles'])
    return ans


def download_pcr_t():
    ans = pd.read_csv(URLS['pcr_t'], index_col='Region', na_values='-')
    ans = ans.loc['2020-04-09':, :]  # type: ignore
    ans['Total'] = ans.sum(axis=1)
    return ans

# casos_totales_evolucion
# def get_start_days(df):
#     """Build a series with regions as an index, values being date at which 10 cases was reached."""
#     df_is_day_0 = ((df >= 1).astype(int).cumsum() == 1).astype(int)
#     start_days = df_is_day_0.apply(lambda col: df.index.values * col).sum(axis=0)
#     return start_days


# def days_to_shift(col):
#     earliest_date = dt.datetime.strptime('2020-03-03', '%Y-%m-%d')
#     return (earliest_date - dt.datetime.strptime(dias_iniciales[col.name], '%Y-%m-%d')).days


# dias_iniciales = get_start_days(DFS['casos_totales_cumulativo_t'])
# DFS['casos_totales_evolucion'] = DFS['casos_totales_cumulativo_t'].apply(lambda col: col.shift(days_to_shift(col)))\
#                                                                   .reset_index()\
#                                                                   .drop(columns=['Region'])

