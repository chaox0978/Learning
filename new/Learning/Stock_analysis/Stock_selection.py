
import pandas as pd
import requests
from io import StringIO
import time
import numpy as np
from pandas import Series, DataFrame

def monthly_report(year, month):
    # 假如是西元，轉成民國
    if year > 1990:
        year -= 1911

    url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_' + str(year) + '_' + str(month) + '_0.html'
    if year <= 98:
        url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_' + str(year) + '_' + str(month) + '.html'

    # 偽瀏覽器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    # 下載該年月的網站，並用pandas轉換成 dataframe
    r = requests.get(url, headers=headers)
    r.encoding = 'big5'

    dfs = pd.read_html(StringIO(r.text), encoding='big-5')

    df = pd.concat([df for df in dfs if df.shape[1] <= 11 and df.shape[1] > 5])

    if 'levels' in dir(df.columns):
        df.columns = df.columns.get_level_values(1)
    else:
        df = df[list(range(0, 10))]
        column_index = df.index[(df[0] == '公司代號')][0]
        df.columns = df.iloc[column_index]

    df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
    df = df[~df['當月營收'].isnull()]
    df = df[df['公司代號'] != '合計']

    # 偽停頓
    time.sleep(5)

    return df
report = monthly_report(2019, 7)
report_last = monthly_report(2019, 6)
#print(type(monthly_report(2019, 7)["當月營收"]))
new_report = report[pd.to_numeric(report["當月營收"], errors = "coerce") > pd.to_numeric(report["去年當月營收"], errors = "coerce")]
new_report1 = report_last[pd.to_numeric(report_last["當月營收"], errors = "coerce") > pd.to_numeric(report_last["去年當月營收"], errors = "coerce")]
new_report_1 = new_report["公司代號"]
new_report1_1 = new_report1["公司代號"]
#new_report2 = new_report_1.append([new_report1_1], ignore_index = True)
#new_report2 = pd.concat([new_report_1, new_report1_1], join = "outer")
new_report2 = pd.merge(new_report_1, new_report1_1, how = "inner")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth',100)
#print(new_report2)
#print(new_report2)
#print(new_report2.drop_duplicates)
#print(len(new_report))
#print(len(new_report1))

datestr = "20190816"
r = requests.get("https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="+ datestr + "&type=ALLBUT0999")
df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in " "})
    for i in r.text.split("\n")
    if len(i.split('",')) == 17 and i[0] != '='])), header = 0)
df_rate = df[pd.to_numeric(df["本益比"], errors = "coerce") < 13]
df_rate_new = df_rate[pd.to_numeric(df["本益比"], errors = "coerce") > 5]
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth',100)
#print(df_rate)
#print(df_rate[["證券代號","證券名稱", "本益比"]])
#print(df_rate["證券代號"])

df_rate_report = df_rate_new.rename(columns = {"證券代號": "公司代號"})

new_report3 = pd.merge(new_report2, df_rate_report, how = "inner")

print(new_report3)
