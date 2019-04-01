'''

'''

class OptionHistInfo:
    def __init__(self, p_date,p_expiry,p_strike,p_type,p_high,p_low,p_close,p_comment):
        self.p_tradedate=p_date
        self.p_expiry = p_expiry
        self.p_strike=p_strike
        self.p_type = p_type
        self.p_low = p_low
        self.p_high = p_high
        self.p_close=p_close
        self.p_comment=p_comment
        pass

    def __str__(self) -> str:
        return super().__str__()

