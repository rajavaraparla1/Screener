from nsetools import Nse
from bsedata.bse import BSE

import json

from conf import constants as const
from classes import OLHBasicClass
from datetime import datetime,date,timedelta

from pprint import pprint
nse = Nse()
bse= BSE()

ol_stocks = dict()
oh_stocks = dict()

for nse_stk,bse_stk in const.NSE_BSE_SYMBOLS.items():
    print ("# Processing {}".format(nse_stk))
    bse_quote = bse.getQuote(bse_stk) 
    bse_data = OLHBasicClass.OLHBasicClass(nse_stk
        , date.today()
        , bse_quote.get('previousOpen')
        , bse_quote.get('dayHigh')
        , bse_quote.get('dayLow')
        , bse_quote.get('currentValue')
        , bse_quote.get('totalTradedQuantity')
        , bse_quote.get('weightedAvgPrice')
        ,bse_quote.get('previousClose')
        ,'BSE')
      
    if bse_quote.get('previousOpen') ==  bse_quote.get('dayLow') :
        if nse_stk in ol_stocks:
            ol_stocks[nse_stk].append(bse_data)
        else:
            ol_stocks[nse_stk] = [bse_data, ]
        print (bse_data)
    if bse_quote.get('previousOpen') ==  bse_quote.get('dayHigh') :
        if nse_stk in oh_stocks:
            oh_stocks[nse_stk].append(bse_data)
        else:
            oh_stocks[nse_stk] = [bse_data, ]

    nse_quote = nse.get_quote(nse_stk)

    # pprint (bse_quote)
    nse_data = OLHBasicClass.OLHBasicClass(nse_stk
        , date.today()
        , nse_quote.get('open')
        , nse_quote.get('dayHigh')
        , nse_quote.get('dayLow')
        , nse_quote.get('closePrice')
        , nse_quote.get('totalTradedValue')
        , nse_quote.get('averagePrice')
        , nse_quote.get('previousClose')
        ,'NSE')
    
    if nse_quote.get('open') ==  nse_quote.get('dayLow') :
        if nse_stk in ol_stocks:
            ol_stocks[nse_stk].append(nse_data)
        else:
            ol_stocks[nse_stk] = [nse_data, ]
    if nse_quote.get('open') ==  nse_quote.get('dayHigh') :
        if nse_stk in oh_stocks:
            oh_stocks[nse_stk].append(nse_data)
        else:
            oh_stocks[nse_stk] = [nse_data, ]

    #print (str(nse_data))
    current_fut_quote = nse.get_fo_quote(nse_stk,const.CURRENT_EXPIRY)
    if not current_fut_quote :
        continue
    #pprint(current_fut_quote)
    current_fut_data = OLHBasicClass.OLHBasicClass(nse_stk
        , date.today()
        , current_fut_quote.get('openPrice')
        , current_fut_quote.get('highPrice')
        , current_fut_quote.get('lowPrice')
        , current_fut_quote.get('closePrice')
        , current_fut_quote.get('numberOfContractsTraded')
        , current_fut_quote.get('vwap')
        , current_fut_quote.get('prevClose')
        ,const.CURRENT_EXPIRY)
    
    if current_fut_quote.get('openPrice') ==  current_fut_quote.get('lowPrice') :
        if nse_stk in ol_stocks:
            ol_stocks[nse_stk].append(current_fut_data)
        else:
            ol_stocks[nse_stk] = [current_fut_data, ]
    if current_fut_quote.get('openPrice') ==  current_fut_quote.get('highPrice') :
        if nse_stk in oh_stocks:
            oh_stocks[nse_stk].append(current_fut_data)
        else:
            oh_stocks[nse_stk] = [current_fut_data, ]


    next_fut_quote = nse.get_fo_quote(nse_stk,const.NEXT_EXPIRY)
    next_fut_data = OLHBasicClass.OLHBasicClass(nse_stk
        , date.today()
        , next_fut_quote.get('openPrice')
        , next_fut_quote.get('highPrice')
        , next_fut_quote.get('lowPrice')
        , next_fut_quote.get('closePrice')
        , next_fut_quote.get('numberOfContractsTraded')
        , next_fut_quote.get('vwap')
        , next_fut_quote.get('prevClose')
        ,const.NEXT_EXPIRY)
    
    if next_fut_quote.get('openPrice') ==  next_fut_quote.get('lowPrice') :
        if nse_stk in ol_stocks:
            ol_stocks[nse_stk].append(next_fut_data)
        else:
            ol_stocks[nse_stk] = [next_fut_data, ]
    if next_fut_quote.get('openPrice') ==  next_fut_quote.get('highPrice') :
        if nse_stk in oh_stocks:
            oh_stocks[nse_stk].append(next_fut_data)
        else:
            oh_stocks[nse_stk] = [next_fut_data, ]


    
    # pprint (current_fut_quote)
    # pprint(next_fut_quote['lastPrice'])
    #print (json.dumps(next_fut_quote,indent=4))
 
for stk_name,ol_stock in ol_stocks.items():
    print(ol_stock)
for stk_name,oh_stock in oh_stocks.items():
    print(oh_stock)

#all_stock_codes = nse.get_stock_codes()

#pprint (all_stock_codes)
#index_codes = nse.get_index_list()
#adv_dec = nse.get_advances_declines()

#pprint (adv_dec )
#pprint (type(adv_dec) )