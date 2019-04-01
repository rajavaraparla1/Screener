
from utils import  trade_utils
from nsetools import Nse
from datetime import datetime,date,timedelta
from conf import constants
import nsepy

symbols = ['HDFC','MARUTI']

nse = Nse()

from utils import  trade_utils
from nsetools import Nse
from datetime import datetime,date,timedelta
from conf import constants
from nsepy import get_history


symbols = ['MARUTI']
strike_prices = [7100,7200,7300,7400,7500,7600]
START_DATE = date.today() - timedelta(constants.TIME_DETLA)
END_DATE = date.today()
print (START_DATE)
nse = Nse()
for symbol in symbols:
    for row in strike_prices:
        opt_hist_ce_data = get_history(symbol=symbol
                                          ,start=date(2018,9,30)
                                          ,end=date(2018,10,10)
                                          ,option_type="CE"
                                          ,strike_price=row
                                             , expiry_date=date(2018,10,25))
        print(opt_hist_ce_data)
    pass

