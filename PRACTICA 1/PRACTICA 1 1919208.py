import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime

def get_csv_from_url(url:str) -> pd.DataFrame:
    s=requests.get(url).content
    return pd.read_csv(io.StringIO(s.decode('windows-1252')))

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = get_csv_from_url("https://raw.githubusercontent.com/MainakRepositor/Datasets/master/HistoricalEsportData.csv")
print_tabulate(df)
df.to_csv("csv/HistoricalEsportData.csv", index=False)