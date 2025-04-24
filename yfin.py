import yfinance as yf
import pandas as pd
import numpy as np


def get_yfin_data(ticker, start_date, end_date, interval):
    return (
        yf.download(ticker, start=start_date, end=end_date, interval=interval)
        .pipe(lambda x: x.set_axis(x.columns.droplevel(1), axis=1))
        .pipe(lambda x: x.rename_axis(None, axis=1))
    )
