
from utils import trade_utils
from nsetools import Nse
from datetime import datetime, date, timedelta
from conf import constants
import pandas as pd
import nsepy
import json
from classes import OptionHistInfo
#symbols = ['ACC', 'COALINDIA', 'DRREDDY', 'MARUTI']
symbols = constants.nifty50_list

nse = Nse()
row_list=[]
for symbol in symbols:
    print ("# PROCESSING {}".format(symbol))
    opt_chain=trade_utils.get_option_chain(symbol)
    live_quote = nse.get_quote(symbol)
    s_ltp = live_quote['lastPrice']
    opt_chain.rename(columns={"Strike Price":"Strike_Price"},inplace=True)
    df_up_strikeprices = opt_chain.loc[opt_chain['Strike_Price'].astype(float) > s_ltp].head(3)
    df_dn_strikeprices = opt_chain.loc[opt_chain['Strike_Price'].astype(float) < s_ltp].iloc[::-1].head(3)

    #print (df_up_strikeprices)
    #print (df_dn_strikeprices)
    #print ("ltp {}" , s_ltp)
    # for index,row in df_up_strikeprices.iterrows():
    #     print (row['Strike_Price'])
    # for index,row in df_dn_strikeprices.iterrows():
    #     print (row['Strike_Price'])

    START_DATE = date.today() - timedelta(constants.TIME_DETLA)
    END_DATE = date.today()

    # for index,row in df_up_strikeprices.iterrows():
    #     print (row['Strike_Price'])
    #     opt_hist_ce_data = nsepy.get_history(symbol=symbol
    #                                       ,start=START_DATE
    #                                       ,end=END_DATE
    #                                       ,option_type="CE"
    #                                       ,strike_price=round(float(row['Strike_Price']))
    #                                          , expiry_date=date(2018,10,25))
    #     print(opt_hist_ce_data)
    for index,row in df_up_strikeprices.iterrows():
        #print (row['Strike_Price'])
        opt_hist_ce_data = nsepy.get_history(symbol=symbol
                                          ,start=START_DATE
                                          ,end=END_DATE
                                          ,option_type="CE"
                                          ,strike_price=round(float(row['Strike_Price']))
                                          , expiry_date=date(2019,4,25))
        if len(opt_hist_ce_data) == 0:
            continue
        opt_hist_ce_data['TradeDate'] = opt_hist_ce_data.index
        opt_hist_ce_data = opt_hist_ce_data.rename(columns=constants.HIST_OPT_COLS)
        opt_hist_ce_data.drop(['PR_TO','OI','OI_CH','Last', 'SETTLE_PRICE', 'NUM_CONTRACTS', 'Turnover','Underlying'],axis=1,inplace=True)
        latest_ce_row = opt_hist_ce_data.iloc[-1]
        latest_ce_high = int(latest_ce_row['High'])
        latest_ce_low = int(latest_ce_row['Low'])
        latest_ce_date = latest_ce_row['TradeDate']
        #print (type(latest_low))
        #print("High:{} Low : {} Date : {}".format(latest_ce_high,latest_ce_low,latest_ce_date))
        multi_ce_tops = opt_hist_ce_data[opt_hist_ce_data.High.astype(int) == latest_ce_high]
        multi_ce_tops = multi_ce_tops[(multi_ce_tops.High.astype(int)).isin(constants.FIBO_SERIES)]
        #print (multi_tops)
        multi_ce_bottoms = opt_hist_ce_data[opt_hist_ce_data.Low.astype(int) == latest_ce_low]
        multi_ce_bottoms = multi_ce_bottoms[(multi_ce_bottoms.Low.astype(int)).isin(constants.FIBO_SERIES)]
        if(len(multi_ce_bottoms.index) > 1):
            for index,p_row in multi_ce_bottoms.iterrows():
                p_tradedate = p_row['TradeDate']
                p_high = p_row['High']
                p_low = p_row['Low']
                p_close = p_row['Close']
                p_strikeprice = p_row['STRIKE_PRICE']
                comment=''
                if(len(multi_ce_bottoms.index) ==2):
                    comment = constants.DOUBLE_BOT
                if(len(multi_ce_bottoms.index) ==3):
                    comment = constants.TRIPPLE_BOT
                if(len(multi_ce_bottoms.index) >3):
                    comment = constants.MULTI_BOT

                p_expiry = p_row['Expiry']
                opt_hist_info = OptionHistInfo.OptionHistInfo(p_tradedate,p_expiry,p_strikeprice,constants.CALL,p_high,p_low,p_close,comment)
                #options_list.append(opt_hist_info)
                #master_df.append(p_tradedate,p_expiry,p_strikeprice,constants.CALL,p_high,p_low,p_close,comment)
                p_dict = {'Date':p_tradedate,'Symbol':symbol,'Expiry':p_expiry,'Strike':p_strikeprice,'Type':constants.CALL,'High':p_high,'Low':p_low,'Close':p_close,'Comment':comment}
                row_list.append(p_dict)
            #print(multi_ce_bottoms)

        if(len(multi_ce_tops.index) > 1):
            for index,p_row in multi_ce_tops.iterrows():
                p_tradedate = p_row['TradeDate']
                p_high = p_row['High']
                p_low = p_row['Low']
                p_close = p_row['Close']
                p_strikeprice = p_row['STRIKE_PRICE']
                comment=''
                if(len(multi_ce_tops.index) ==2):
                    comment = constants.DOUBLE_TOP
                if(len(multi_ce_tops.index) ==3):
                    comment = constants.TRIPPLE_TOP
                if(len(multi_ce_tops.index) >3):
                    comment = constants.MULTI_TOP

                p_expiry = p_row['Expiry']
                p_dict = {'Date':p_tradedate,'Symbol':symbol,'Expiry':p_expiry,'Strike':p_strikeprice,'Type':constants.CALL,'High':p_high,'Low':p_low,'Close':p_close,'Comment':comment}
                row_list.append(p_dict)


        # if(len(multi_ce_tops.index) > 1):
        #     print(multi_ce_tops)

        #print(multi_tops.columns)



        opt_hist_pe_data = nsepy.get_history(symbol=symbol
                                          ,start=START_DATE
                                          ,end=END_DATE
                                          ,option_type="PE"
                                          ,strike_price=round(float(row['Strike_Price']))
                                          , expiry_date=date(2019,4,25))
                                             
        if len(opt_hist_pe_data) == 0:
            continue

        opt_hist_pe_data['TradeDate'] = opt_hist_pe_data.index
        opt_hist_pe_data = opt_hist_pe_data.rename(columns=constants.HIST_OPT_COLS)
        opt_hist_pe_data.drop(['PR_TO','OI','OI_CH','Last', 'SETTLE_PRICE', 'NUM_CONTRACTS', 'Turnover','Underlying'],axis=1,inplace=True)
        latest_pe_row = opt_hist_pe_data.iloc[-1]
        #print (opt_hist_ce_data)
        latest_pe_high = int(latest_pe_row['High'])
        latest_pe_low = int(latest_pe_row['Low'])
        latest_pe_date = latest_pe_row['TradeDate']
        #print (type(latest_low))
        #print("High:{} Low : {} Date : {}".format(latest_pe_high,latest_pe_low,latest_pe_date))
        multi_pe_tops = opt_hist_pe_data[opt_hist_pe_data.High.astype(int) == latest_pe_high]
        multi_pe_tops = multi_pe_tops[(multi_pe_tops.High.astype(int)).isin(constants.FIBO_SERIES)]
        #print (multi_tops)
        multi_pe_bottoms = opt_hist_pe_data[opt_hist_pe_data.Low.astype(int) == latest_pe_low]
        multi_pe_bottoms = multi_pe_bottoms[(multi_pe_bottoms.Low.astype(int)).isin(constants.FIBO_SERIES)]



        if(len(multi_pe_bottoms.index) > 1):
            for index, p_row in multi_pe_bottoms.iterrows():
                p_tradedate = p_row['TradeDate']
                p_high = p_row['High']
                p_low = p_row['Low']
                p_close = p_row['Close']
                p_strikeprice = p_row['STRIKE_PRICE']
                comment = ''
                if (len(multi_pe_bottoms.index) == 2):
                    comment = constants.DOUBLE_BOT
                if (len(multi_pe_bottoms.index) == 3):
                    comment = constants.TRIPPLE_BOT
                if (len(multi_pe_bottoms.index) >3):
                    comment = constants.MULTI_BOT
                p_expiry = p_row['Expiry']
                p_dict = {'Date': p_tradedate, 'Symbol': symbol, 'Expiry': p_expiry, 'Strike': p_strikeprice,
                          'Type': constants.PUT, 'High': p_high, 'Low': p_low, 'Close': p_close, 'Comment': comment}
                row_list.append(p_dict)

            #print(multi_pe_bottoms)
        if(len(multi_pe_tops.index) > 1):
            for index, p_row in multi_pe_tops.iterrows():
                p_tradedate = p_row['TradeDate']
                p_high = p_row['High']
                p_low = p_row['Low']
                p_close = p_row['Close']
                p_strikeprice = p_row['STRIKE_PRICE']
                comment = ''
                if (len(multi_pe_tops.index) == 2):
                    comment = constants.DOUBLE_TOP
                if (len(multi_pe_tops.index) == 3):
                    comment = constants.TRIPPLE_TOP
                if (len(multi_pe_tops.index) > 3):
                    comment = constants.MULTI_TOP

                p_expiry = p_row['Expiry']
                p_dict = {'Date': p_tradedate, 'Symbol': symbol, 'Expiry': p_expiry, 'Strike': p_strikeprice,
                          'Type': constants.PUT, 'High': p_high, 'Low': p_low, 'Close': p_close, 'Comment': comment}
                row_list.append(p_dict)


            #print(multi_pe_tops)

        #exit(1)


    pass

#print (master_df)
df = pd.DataFrame(row_list)
df.sort_values(by=['Symbol','Strike','Type'],inplace=True)
df = df[df.High != 0]
df = df[df.Low != 0]
print (df)
writer = pd.ExcelWriter(path="fibo_opt.xlsx",engine="xlsxwriter")
df.to_excel(writer,columns=constants.FIBO_OPT_EXCEL_COLUMNS,index=False)
writer.save()

