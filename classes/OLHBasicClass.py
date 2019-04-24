"""
    This is the basic class OLH Class.
    All the further classes will be inherited from this.

"""


class OLHBasicClass:
    """
    Basic class for OpenHighLow
    """

    def __init__(
            self,
            script,
            trade_time,
            p_open,
            high,
            low,
            ltp,
            volume,
            vwap,
            pclose=None,
            exchange='NSE'):
        self.script = script
        self.trade_time = trade_time
        self.p_open = p_open  # Current Candle Open.
        self.high = high
        self.low = low
        self.ltp = ltp
        self.volume = volume
        self.vwap = vwap
        self.pclose = pclose
        self.exchange = exchange


    def __repr__(self):
        ''' Representation of OLHBasicClass '''
        olh_str = 'OLHBasicClass({},{},{},{},{},{},{},{},{},{})'.format(
            self.script,
            self.trade_time,
            self.p_open,
            self.high,
            self.low,
            self.ltp,
            self.volume,
            self.vwap,
            self.pclose,
            self.exchange)
        return olh_str

    def __str__(self):
        ''' String representation of OLHBasicClass '''
        olh_str = 'SCRIPT:{};EXCHANGE:{};TradeTime={};OPEN={};HIGH={};LOW={};LTP={};VOLUME={};VWAP={};PCLOSE={}'.format(
            self.script, self.exchange, self.trade_time, self.p_open, self.high, self.low, self.ltp, self.volume, self.vwap,self.pclose)
        return olh_str
