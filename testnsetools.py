from nsetools import Nse
from pprint import pprint

nse = Nse()
q = nse.get_quote('cipla')  # it's ok to use both upper or lower case for codes.
all_stock_codes = nse.get_stock_codes()

#pprint (all_stock_codes)
index_codes = nse.get_index_list()
adv_dec = nse.get_advances_declines()

pprint (adv_dec )
pprint (type(adv_dec) )