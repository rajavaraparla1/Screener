from constants import tickers,constants
from utils import extract_utils as eu,db_utils
from conf import creds
from upstox_api.utils import OHLCInterval
from upstox_api.api import *
import datetime
from datetime import timedelta

api_key = creds.upstox_creds['api_key']
api_secret = creds.upstox_creds['api_secret']
redirect_uri = creds.upstox_creds['redirect_uri']

#login_code = 'bc66088a3e6fc7363f86f6fa51c3351f1a7bc4fb'
#eu.login_histdata_system(api_key=api_key, api_secret=api_secret, redirect_uri=redirect_uri,code=login_code)

usObj=Upstox(api_key,'8304dbebefac385e523d67a378f3d9b9d1b51cad')
usObj.get_master_contract(exchange='NSE_EQ');
usObj.get_master_contract(exchange='BSE_EQ');

exchanges = ['BSE_EQ']

all_tickers = tickers.ALL_CONTRACTS
for pExchange in exchanges :
    for ticker in all_tickers:
        # df=eu.get_ieod_nmin_data(usObj=usObj, exchange='NSE_EQ', ticker=ticker, from_date=datetime.datetime.strptime('08/08/2018', '%d/%m/%Y').date(), to_date=datetime.datetime.strptime('13/08/2018', '%d/%m/%Y').date(), nmin=tickers.OHLC_60MIN)
        # db_utils.load_db_table(ticker, df, creds.DB_NAME, creds.DB_HOST, creds.DB_USER, creds.DB_PASSWORD, creds.DB_IEOD_HOUR_TABLE)
        # df = eu.get_ieod_5min_data(usObj=usObj, exchange=pExchange, ticker=ticker,
        #                            from_date=datetime.datetime.strptime('08/08/2018', '%d/%m/%Y').date(),
        #                            to_date=datetime.datetime.strptime('13/08/2018', '%d/%m/%Y').date())
        # df = eu.get_ieod_5min_data(usObj=usObj, exchange=pExchange, ticker=ticker,
        #                            from_date=datetime.datetime.strptime('08/08/2018', '%d/%m/%Y').date(),
        #                            to_date=datetime.datetime.strptime('13/08/2018', '%d/%m/%Y').date())
        TIME_DELTA = 90
        START_DATE = date.today() - timedelta(TIME_DELTA)
        END_DATE = date.today()
        df = eu.get_ieod_5min_data(usObj=usObj, exchange=pExchange, ticker=ticker,from_date=START_DATE,to_date=END_DATE)
        #print(df.head(40))
        db_utils.load_db_table(ticker, df, creds.DB_NAME, creds.DB_HOST, creds.DB_USER, creds.DB_PASSWORD,
                               creds.DB_IEOD_5MIN_TABLE,exchange=pExchange)
        TIME_DELTA = 150
        START_DATE = date.today() - timedelta(TIME_DELTA)
        END_DATE = date.today()

        df = eu.get_ieod_10min_data(usObj=usObj, exchange=pExchange, ticker=ticker,from_date=START_DATE,to_date=END_DATE)
        db_utils.load_db_table(ticker, df, creds.DB_NAME, creds.DB_HOST, creds.DB_USER, creds.DB_PASSWORD,
                               creds.DB_IEOD_10MIN_TABLE,exchange=pExchange)
        #print(df)
        TIME_DELTA = 240
        START_DATE = date.today() - timedelta(TIME_DELTA)
        END_DATE = date.today()

        df = eu.get_ieod_30min_data(usObj=usObj, exchange=pExchange, ticker=ticker,from_date=START_DATE,to_date=END_DATE)
        #print(df)

        db_utils.load_db_table(ticker, df, creds.DB_NAME, creds.DB_HOST, creds.DB_USER, creds.DB_PASSWORD,
                               creds.DB_IEOD_30MIN_TABLE,exchange=pExchange)

        TIME_DELTA = 240
        START_DATE = date.today() - timedelta(TIME_DELTA)
        END_DATE = date.today()

        df = eu.get_ieod_60min_data(usObj=usObj, exchange=pExchange, ticker=ticker,from_date=START_DATE,to_date=END_DATE)
        db_utils.load_db_table(ticker, df, creds.DB_NAME, creds.DB_HOST, creds.DB_USER, creds.DB_PASSWORD,
                               creds.DB_IEOD_HOUR_TABLE,exchange=pExchange)
        #print(df)


    #print(df)

