import datetime as dt

from data_client import DataCache


def prepare_report(dfs: DataCache):
    today = dt.date.today()
    yesterday = today - dt.timedelta(days=1)
    report = {}

    report['total_deaths'] =\
        dfs['fallecidos_cumulativo_t']['Total'][today]\
        if today in dfs['fallecidos_cumulativo_t'].index\
        else '?'

    report['deaths_today'] =\
        dfs['fallecidos_cumulativo_t']['Total'][today] - dfs['fallecidos_cumulativo_t']['Total'][yesterday]\
        if today in dfs['fallecidos_cumulativo_t'].index\
        else '?'

    report['top_3_deaths'] =\
        sorted(dfs['fallecidos_cumulativo_t'].loc[today].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]\
        if today in dfs['fallecidos_cumulativo_t'].index\
        else '?'

    report['top_3_deaths_last_day'] =\
        sorted(dfs['fallecidos_cumulativo_t'].diff().loc[today].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]\
        if today in dfs['fallecidos_cumulativo_t'].index\
        else '?'

    report['top_3_uci'] =\
        sorted(dfs['uci_t'].loc[today].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]\
        if today in dfs['uci_t'].index\
        else '?'

    report['top_3_new_cases'] =\
        sorted(dfs['casos_nuevos_cumulativo_t'].loc[today].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]\
        if today in dfs['casos_nuevos_cumulativo_t'].index\
        else '?'

    report['top_3_new_cases_per_k'] =\
        sorted(dfs['casos_nuevos_cumulativo_t_per_k'].loc[today].to_dict().items(), key=lambda item: item[1], reverse=True)[1:4]\
        if today in dfs['casos_nuevos_cumulativo_t_per_k'].index\
        else '?'

    report['tests_today'] =\
        dfs['pcr_t'].loc[today]['Total']\
        if today in dfs['pcr_t'].index\
        else '?'

    report['tests_yesterday'] =\
        dfs['pcr_t'].loc[yesterday]['Total']\
        if yesterday in dfs['pcr_t'].index\
        else '?'

    report['tests_diff'] =\
        report['tests_today'] - report['tests_yesterday']\
        if today in dfs['pcr_t'].index and yesterday in dfs['pcr_t'].index\
        else '?'

    report['top_10_comunas_total'] =\
        [comuna for comuna, cases in sorted(dfs['p1_casos_acumulados_comuna'].loc[today, :].to_dict().items(), key=lambda item: -item[1])[:10]]\
        if today in dfs['p1_casos_acumulados_comuna'].index\
        else [comuna for comuna, cases in sorted(dfs['p1_casos_acumulados_comuna'].iloc[-1, :].to_dict().items(), key=lambda item: -item[1])[:10]]

    return report
