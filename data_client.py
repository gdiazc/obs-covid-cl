"""Functions for downloading data from API."""
import pandas as pd

from constants import URLS


# casos acumulados por comuna:
def download_p1_casos_acumulados_comuna():
    ans = pd.read_csv(URLS['p1_casos_acumulados_comuna'], index_col='Region')
    ans.columns = ans.loc['Comuna']
    ans = ans.iloc[4:-1]
    ans = ans.astype(float)
    return ans
