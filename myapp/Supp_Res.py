
class Supp_Res:
    def __init__(self, tycker, exp_value, area, timeframe, ranges):
        self.tycker = tycker
        self.range_price = [exp_value-area, exp_value + area]  
        self.exp_value = exp_value
        self.timeframe = timeframe
        self.ranges = ranges 
        self.sigName = 'SUPP_RES'

   
