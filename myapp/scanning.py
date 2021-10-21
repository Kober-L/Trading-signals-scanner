import yfinance as yf
from yfinance.utils import empty_df
import telegramMex as tm
from Signal import Signal 
import json
import time 
import handleJson as hj
import instruments as ins
from Supp_Res import Supp_Res as sr


def checks(ranges_list, actual_price, file_name):
    with open(file_name) as f:
        signals = json.load(f)
    for range in ranges_list:
        if actual_price >= range.range_price[0] and actual_price <= range.range_price[1]:
            create_signal = True
            th_id = f"{range.tycker}SUPP_RES"    
            for signal in signals:
                if signal['id'] == th_id:
                    create_signal = False
            if create_signal:
                new_signal = Signal(actual_price, range)
                new_signal = hj.convertToDict(new_signal)  
                signals = signals + [new_signal]
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(signals, f, ensure_ascii=False, indent=4) 
                tm.send(f"new signal for {range.tycker}----                            "  
                        f"The signal is {new_signal['sigName']}----                    "  
                        f"The supp/res is at {range.exp_value}----                     "
                        f"Price that crossed is {actual_price}----                     "
                        f"The timeframe of the supp/res is {range.timeframe}----                                                 "
                        f"The other ranges are:                                        "
                        f"{range.ranges}----                                           "
                        "END TRANSMISSION ")
                time.sleep(1)

