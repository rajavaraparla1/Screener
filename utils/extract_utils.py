'''
    Utilities related extract historical ieod data.
'''

from datetime import datetime
from upstox_api.api import *
from upstox_api.utils import OHLCInterval
import pypyodbc
from selenium import webdriver
from constants import constants, tickers, urls
import pandas as pd

def get_login_code(api_key, api_secret, redirect_uri):
    """
    :param api_key:
    :type string:
    :param api_secret:
    :type string:
    :param redirect_uri:
    :type string:
    :return: login code
    :rtype: string
    """
    session = Session(api_key)
    session.set_redirect_uri(redirect_uri)
    session.set_api_secret(api_secret)
    login_uri = session.get_login_url()
    # print (login_uri)
    code = openurl_function(login_uri)
    return code


def login_histdata_system(api_key, api_secret, redirect_uri, code):
    """
    :param api_key:
    :type api_key:
    :param api_secret:
    :type api_secret:
    :param redirect_uri:
    :type redirect_uri:
    :param code:
    :type code:
    :return:Upstox object
    :rtype:
    """
    # print(api_key)
    # print(api_secret)
    # print(redirect_uri)
    session = Session(api_key)
    session.set_redirect_uri(redirect_uri)
    session.set_api_secret(api_secret)
    session.set_code(code)
    access_token = session.retrieve_access_token()
    print(access_token)
    us = Upstox(api_key, access_token)
    print(us)
    return True


# def openurl_function(login_uri):
#     """
#     :param login_uri:
#     :type string:
#     :return:code
#     :rtype:string
#     """
#     driver = webdriver.Chrome()
#     driver.get(login_uri)
#     driver.find_element_by_id("name").send_keys("172340")
#     driver.find_element_by_id("password").send_keys("Abhinai@123#")
#     driver.find_element_by_id("password2fa").send_keys("1982")
#     driver.find_element_by_id("password2fa").submit()
#     driver.find_element_by_id("allow").submit()
#     url = driver.current_url
#     code = url.split("=")
#     return (code[1])
#

def openurl_function(login_uri):
    """
    :param login_uri:
    :type string:
    :return:code
    :rtype:string
    """
    driver = webdriver.Chrome()
    driver.get(login_uri)
    driver.find_element_by_id("name").send_keys("142643")
    driver.find_element_by_id("password").send_keys("zJ6nk@<UN;")
    driver.find_element_by_id("password2fa").send_keys("1980")
    driver.find_element_by_id("password2fa").submit()
    driver.find_element_by_id("allow").submit()
    url = driver.current_url
    code = url.split("=")
    return (code[1])


def get_ieod_5min_data(usObj, exchange, ticker, from_date, to_date):
    """
    :param usObj:
    :type usObj:
    :param exchange:
    :type string:
    :param ticker:
    :type ticker:
    :param from_date:
    :type date object of form 13/08/2018:
    :param to_date:
    :type 13/08/2018:
    :param nmin:
    :type string:
    :return:
    :rtype:
    """
    return get_ieod_nmin_data(usObj, exchange, ticker, from_date, to_date, nmin=tickers.OHLC_5MIN)

def get_ieod_10min_data(usObj, exchange, ticker, from_date, to_date):
    """
    :param usObj:
    :type usObj:
    :param exchange:
    :type string:
    :param ticker:
    :type ticker:
    :param from_date:
    :type date object of form 13/08/2018:
    :param to_date:
    :type 13/08/2018:
    :param nmin:
    :type string:
    :return:
    :rtype:
    """
    return get_ieod_nmin_data(usObj, exchange, ticker, from_date, to_date, nmin=tickers.OHLC_10MIN)

def get_ieod_30min_data(usObj, exchange, ticker, from_date, to_date):
    """
    :param usObj:
    :type usObj:
    :param exchange:
    :type string:
    :param ticker:
    :type ticker:
    :param from_date:
    :type date object of form 13/08/2018:
    :param to_date:
    :type 13/08/2018:
    :param nmin:
    :type string:
    :return:
    :rtype:
    """
    return get_ieod_nmin_data(usObj, exchange, ticker, from_date, to_date, nmin=tickers.OHLC_30MIN)

def get_ieod_60min_data(usObj, exchange, ticker, from_date, to_date):
    """
    :param usObj:
    :type usObj:
    :param exchange:
    :type string:
    :param ticker:
    :type ticker:
    :param from_date:
    :type date object of form 13/08/2018:
    :param to_date:
    :type 13/08/2018:
    :param nmin:
    :type string:
    :return:
    :rtype:
    """
    return get_ieod_nmin_data(usObj, exchange, ticker, from_date, to_date, nmin=tickers.OHLC_60MIN)


def get_ieod_nmin_data(usObj, exchange, ticker, from_date, to_date, nmin=tickers.OHLC_60MIN):
    out_data = usObj.get_ohlc(usObj.get_instrument_by_symbol(exchange, ticker), nmin, from_date, to_date)
    rows = []
    columns = ['TradeTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'TradeDate']
    for data in out_data:
        ts = data['timestamp']
        TradeTime = datetime.fromtimestamp(ts / 1000)
        data['tradetime'] = TradeTime.strftime(constants.TIME_FORMAT)
        data['tradedate'] = TradeTime.strftime(constants.DATE_FORMAT)
        data['idx'] = TradeTime.strftime(constants.TIME_FORMAT)
        data['ticker'] = ticker
        data['exchange'] = exchange
        rows.append(data)

    if len(rows) > 0:
        df = pd.DataFrame.from_dict(rows)
        df = df.set_index('idx')
        df = df.drop(['timestamp', 'cp'], 1)
        # print(df['tradetime'])
    return df

def get_eod_ndays_daily_data(usObj, exchange, ticker, from_date, to_date):
    df = get_eod_ndays_data(usObj, exchange, ticker, from_date, to_date, nmin=tickers.OHLC_DAY)
    return df

def get_eod_ndays_weekly_data(usObj, exchange, ticker, from_date, to_date):
    df = get_eod_ndays_data(usObj, exchange, ticker, from_date, to_date, nmin=tickers.OHLC_WEEK)
    return df

def get_eod_ndays_monthly_data(usObj, exchange, ticker, from_date, to_date):
    df = get_eod_ndays_data(usObj, exchange, ticker, from_date, to_date, nmin=tickers.OHLC_MONTH)
    return df


def get_eod_ndays_data(usObj, exchange, ticker, from_date, to_date, nmin):
    out_data = usObj.get_ohlc(usObj.get_instrument_by_symbol(exchange, ticker), nmin, from_date, to_date)
    rows = []
    columns = ['TradeTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'TradeDate']
    for data in out_data:
        ts = data['timestamp']
        TradeTime = datetime.fromtimestamp(ts / 1000)
        data['tradedate'] = TradeTime.strftime(constants.DATE_FORMAT)
        data['idx'] = TradeTime.strftime(constants.DATE_FORMAT)
        data['ticker'] = ticker
        data['exchange'] = exchange
        #print(data)
        rows.append(data)

    if len(rows) > 0:
        df = pd.DataFrame.from_dict(rows)
        df = df.set_index('idx')
        df = df.drop(['timestamp', 'cp'], 1)
        # print(df['tradetime'])
    return df
