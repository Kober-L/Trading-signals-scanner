from Supp_Res import Supp_Res
import scanning as sc
import handleJson as hj
import instruments as ins



def automatize(tycker, tycker_yf, area, valuesSuppRes, filename):
  i = 1
  dict_of_values = {}
  Supp_Res_List = []
  for value in valuesSuppRes:
    dict_of_values.update({f'1w_{i}': value})
    i = i + 1
  for key, value in dict_of_values.items():
    Supp_Res_List = Supp_Res_List + [Supp_Res(tycker, value, area, '1w', dict_of_values)]
    
  price = ins.getPrice(tycker_yf)
  hj.json_scraper(filename, price, tycker)
  sc.checks(Supp_Res_List, price, filename)

  return 'done'


automatize('EURUSD', 'EURUSD=X', 0.01150, [1.05243, 1.07815, 1.16990, 1.16021, 1.13721, 1.22431], 'forex.json')
automatize('USDCAD', 'CAD=X', 0.01150, [1.46845, 1.20519, 1,25186], 'forex.json')
automatize('GBPUSD', 'GBPUSD=X', 0.01150, [1.20354, 1.27431,  1.46979, 1.42148, 1.37093, 1.36045], 'forex.json')
automatize('AUDUSD', 'AUDUSD=X', 0.01150, [0.56918, 0.59166, 0.66795, 0.81099, 0.78715, 0.70269, 0.73470], 'forex.json')
automatize('GBPJPY', 'GBPJPY=X', 0.796, [124.916, 129.116, 135.698, 156.1, 153.138, 149.189], 'forex.json')
automatize('USDJPY', 'JPY=X', 0.263, [102.439, 100.187, 104.626, 114.558, 113.624, 111.602, 111.011, 108.883, 108.144], 'forex.json')
automatize('EURJPY', 'EURJPY=X', 0.5, [115.757, 121.708, 137.324, 134.036, 133.069, 128.339], 'forex.json')
automatize('GBPAUD', 'GBPAUD=X',0.01150, [1.71201, 1.75122, 1.95262, 2.04, 1.91318, 1.79542], 'forex.json')
automatize('USDCHF', 'CHF=X', 0.0035 , [0.956, 0.94365, 0.92012, 0.90172], 'forex.json')
automatize('EURCHF', 'EURCHF=X', 0.00250, [1.05011, 1.06264, 1.07272, 1.10998, 1.10541], 'forex.json')


automatize('TSLA', 'TSLA', 30, [544.50, 876.26, 757.91], 'stocks.json')
automatize('AMC', 'AMC', 3.5, [30.50, 61.80], 'stocks.json')
automatize('BABA', 'BABA', 8, [128.13, 151.75, 300.46, 274.32,], 'stocks.json')
automatize('AMZN', 'AMZN', 40, [2887.67, 3085.53, 3749.63, 3519.56], 'stocks.json')
automatize('QQQ', 'QQQ', 10, [340.21, 315.40, 359.11], 'stocks.json')
automatize('BBIG', 'BBIG', 1.2, [1.39, 5.10, 11.62], 'stocks.json')
automatize('NVDA', 'NVDA', 10, [147.9, 123.3], 'stocks.json')
automatize('NIO', 'NIO', 2.2 , [34.6, 37.41, 64.85, 55], 'stocks.json')
automatize('AMD', 'AMD', 3, [94.85, 74.19], 'stocks.json')
automatize('NFLX', 'NFLX', 8, [591.72, 571.04, 473.42, 490.68, 510.29], 'stocks.json')


automatize('BTCUSD', 'BTC-USD', 1000 , [31508, 62306, 59190, 40496], 'stocks.json')
automatize('ETHUSD', 'ETH-USD', 100, [1972.26, 3197.26, 4006.11], 'stocks.json')
automatize('XRPUSD', 'XRP-USD', 0.12, [0.20177, 0.64547, 1.35045, 1.68076], 'stocks.json')





