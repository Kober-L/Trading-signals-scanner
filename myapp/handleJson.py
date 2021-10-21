import json
from Supp_Res import Supp_Res as sr
from Signal import Signal


def delete_fromJson(json_name, id):
    with open(json_name) as f:
        data = json.load(f)
    i = 0
    for element in data:
        if element['id'] == id:
            data.pop(i)
            break
        i = i + 1
    with open(json_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def json_scraper(file_name, actual_price, tycker):
    with open(file_name) as f:
        signals = json.load(f)
    i = 0
    for element in signals:  
        if (actual_price <= element['range_price'][0] or actual_price >= element['range_price'][1]) and element['tycker'] == tycker:
            signals.pop(i)
        i = i + 1
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(signals, f, ensure_ascii=False, indent=4)


def convertToDict(signal):
    return {'id': signal.id,
            'actual_price': signal.actual_price, 
            'date': signal.date,
            'tycker': signal.signal_type.tycker,
            'range_price': signal.signal_type.range_price,
            'exp_value': signal.signal_type.exp_value,
            'ranges': signal.signal_type.ranges,
            'sigName': signal.signal_type.sigName,
            'timeframe': signal.signal_type.timeframe
            }
     
