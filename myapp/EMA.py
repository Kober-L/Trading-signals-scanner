class EMA:
    def __init__(self, tycker, timeFrame, period):
        self.tycker = tycker
        self.timeFrame = timeFrame
        self.period = period 
        self.sigName = 'EMA'