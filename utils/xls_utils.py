'''
This contains all the excel related utilities.
'''

import pandas as pd
from conf import constants
from nsetools import Nse
import numpy as np



def write_advdec_to_excel(excel_name,sheet_name,rownum):
    # Get advances and declines per sector.
    start_col=0
    nse=Nse()
    adv_dec = nse.get_advances_declines()
    df = pd.DataFrame(adv_dec)
    df = df[~ df.indice.isin(constants.DEL_ADVDEC) ]


    #df['A/D'] = df.apply(lambda row: round(row.advances / row.declines,2), axis=1)
    #df['A/D'] = round(df.advances.div( df.declines.where (df.declines !=0,np.nan)),2)
    writer = pd.ExcelWriter(path=excel_name,engine="xlsxwriter")
    df.to_excel(excel_writer=writer,sheet_name=sheet_name,columns=constants.ADV_DEC_COLUMNS,index=False,startrow=rownum,startcol=start_col)

    workbook = writer.book

    worksheet = writer.sheets[sheet_name]

    num_rows = len(df.index)+1
    format_bear = workbook.add_format({'bg_color': constants.BEAR_BGCOLOR})
    format_bull = workbook.add_format({'bg_color': constants.BULL_BGCOLOR})
    format_nutral = workbook.add_format({'bg_color': constants.NUTRAL_BGCOLOR})

    worksheet.conditional_format(rownum,0,rownum+len(df.index),len(constants.ADV_DEC_COLUMNS)+1,
                                 {"type": "formula",
                                  "criteria": '=INDIRECT("B"&ROW())> INDIRECT("B"&ROW())',
                                  "format": format_bull
                                  }
                                 )
    # Create a new chart object. In this case a column chart.
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'name':'advances',
        'categories': [sheet_name, rownum+1, 0, rownum + len(df.index) + 1, 0],
        'values': [sheet_name, rownum+1, 1, rownum + len(df.index) + 1, 1]
    })

    chart.add_series({
        'name': 'declines',
        'categories': [sheet_name, rownum+1, 0, rownum + len(df.index) + 1, 0],
        'values': [sheet_name, rownum+1, 2, rownum + len(df.index) + 1, 2]
    })
    chart.set_x_axis({
        'name': 'Indice',
        'name_font': {'size': 14, 'bold': True},
        'num_font': {'italic': True},
    })

    chart.set_y_axis({
        'name': 'Adv/Dec',
        'name_font': {'size': 14, 'bold': True},
        'num_font': {'italic': True},
    })


    #chart.set_y_axis({'major_gridlines': {'visible': False}})
    chart.set_legend({'position': 'none'})
    worksheet.insert_chart('F2', chart,{'x_scale': 2, 'y_scale': 1.5})

    rownumber=0
    rownumber = rownumber+rownum+len(df.index)+5

    # Get TOP 10 GAINERS

    top_gainers = nse.get_top_gainers()
    gainers = pd.DataFrame(top_gainers)
    gainers.rename(columns={"symbol": "Symbol",'openPrice':'Open','highPrice':'High','lowPrice':'Low','ltp':'Close','netPrice':'%Change','tradedQuantity':'Volume'}, inplace=True)
    gainers.to_excel(excel_writer=writer, sheet_name=sheet_name, columns=constants.TOP10_COLUMNS,index=False,startrow=rownumber,startcol=start_col)

    #rownumber = rownumber+len(gainers.index)+5

    # Get TOP 10 LOOSERS

    top_losers = nse.get_top_losers()
    losers = pd.DataFrame(top_losers)
    losers.rename(columns={"symbol": "Symbol",'openPrice':'Open','highPrice':'High','lowPrice':'Low','ltp':'Close','netPrice':'%Change','tradedQuantity':'Volume'}, inplace=True)
    losers.to_excel(excel_writer=writer, sheet_name=sheet_name, columns=constants.TOP10_COLUMNS,index=False,startrow=rownumber,startcol=start_col+len(constants.TOP10_COLUMNS)+3)

    writer.save()
    workbook.close()
    pass