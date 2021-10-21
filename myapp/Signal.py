from datetime import datetime as dt

class Signal:
    def __init__(self, actual_price, signal_type):
        self.id = Signal.generateId(signal_type.tycker, signal_type.sigName)
        self.actual_price = actual_price
        self.date = dt.today().strftime('%d-%m-%Y')
        self.signal_type = signal_type
        


    def generateId(tycker, sigName):
        return f"{tycker}{sigName}"
