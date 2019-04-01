'''
    This will contain function used in common.
'''
from sqlalchemy import create_engine, MetaData, TEXT, Integer, Float, Table, Column, \
    ForeignKey, String, BIGINT, DATE, DATETIME, text, exc, select
from conf import constants
import datetime
from conf import config
from utils import db_utils

import pandas as pd

def get_eod_ohlc_data(from_date=datetime.date.today(),to_date=datetime.date.today(),ticker=''):
    '''
        This will get pandas object that contains Open,High,Low,Close,VWAP and volume from eod table for the specified date range.
    :param from_date (start date of the range - inclusive)
    :param from_end (end date of the range - inclusive)
    :return:
        pandas dataset with result of the query
    '''
    if(ticker != ''):
        query = "select ticker, TradeDate, Open, High, Low, Close, VWAP, Volume from {table} where (TradeDate>='{fromdate}' AND TradeDate<='{todate}') AND ticker = '{ticker}'".format(table=config.DB_EOD_TABLE,fromdate=from_date,todate=to_date,ticker=ticker)
    else:
        query = "select ticker, TradeDate, Open, High, Low, Close, VWAP, Volume from {table} where (TradeDate>='{fromdate}' AND TradeDate<='{todate}') ".format(table=config.DB_EOD_TABLE,fromdate=from_date,todate=to_date)
    print("query : ", query)
    ohlc_ds = db_utils.execute_simple_db_query(query, config.DB_NAME,config.DB_HOST, config.DB_USER, config.DB_PASSWORD)
    print (ohlc_ds)

