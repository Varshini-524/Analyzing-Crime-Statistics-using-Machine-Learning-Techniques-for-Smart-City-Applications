import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
#import geopandas as gpd
from shapely.geometry import Point
import shapely
import numpy as np5
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.tsa.stattools as sm
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
import itertools
from dateutil import rrule, parser

def daycount(data):
    start_date = list(map(str, data['Start Date'].value_counts().keys().tolist()))
    if (len(start_date)!=365):
        start_date.append("04-23")
    start_date.sort()
    ugh = [0 for i in range(0,len(start_date))]
    for index,row in data.iterrows():
        a = start_date.index(row["Start Date"])
        ugh[a] += 1.0
    start_date = list(rrule.rrule(rrule.DAILY,
                         dtstart=parser.parse("2017-01-01"),
                         until=parser.parse("2017-12-31")))
    for i in range (0,len(start_date)):
        start_date[i] =start_date[i].date()
    march = pd.DataFrame({"Crime Count": ugh, "Date":start_date} )
    #ax = march.plot(kind = "line", y = "Crime Count", figsize = (40,10), title = ("2017" +str(title)), xticks = [0,31,59,90,120,151,181,212,243,273,304,334,365], grid = True)
    #fig = ax.get_figure()
    #fig.savefig("2017" + title + ".png")
    return march
def daycount_2018(data):
    start_date = ['01-01', '01-02', '01-03', '01-04', '01-05', '01-06', '01-07', '01-08', '01-09', '01-10', '01-11', '01-12', '01-13', '01-14', '01-15', '01-16', '01-17', '01-18', '01-19', '01-20', '01-21', '01-22', '01-23', '01-24', '01-25', '01-26', '01-27', '01-28', '01-29', '01-30', '01-31', '02-01', '02-02', '02-03', '02-04', '02-05', '02-06', '02-07', '02-08', '02-09', '02-10', '02-11', '02-12', '02-13', '02-14', '02-15', '02-16', '02-17', '02-18', '02-19', '02-20', '02-21', '02-22', '02-23', '02-24', '02-25', '02-26', '02-27', '02-28', '03-01', '03-02', '03-03', '03-04', '03-05', '03-06', '03-07', '03-08', '03-09', '03-10', '03-11', '03-12', '03-13', '03-14', '03-15', '03-16', '03-17', '03-18', '03-19', '03-20', '03-21', '03-22', '03-23', '03-24', '03-25', '03-26', '03-27', '03-28', '03-29', '03-30', '03-31', '04-01', '04-02', '04-03', '04-04', '04-05', '04-06', '04-07', '04-08', '04-09', '04-10', '04-11', '04-12', '04-13', '04-14', '04-15', '04-16', '04-17', '04-18', '04-19', '04-20', '04-21', '04-22', '04-23', '04-24', '04-25', '04-26', '04-27', '04-28', '04-29', '04-30', '05-01', '05-02', '05-03', '05-04', '05-05', '05-06', '05-07', '05-08', '05-09', '05-10', '05-11', '05-12', '05-13', '05-14', '05-15', '05-16', '05-17', '05-18', '05-19', '05-20', '05-21', '05-22', '05-23', '05-24', '05-25', '05-26', '05-27', '05-28', '05-29', '05-30', '05-31', '06-01', '06-02', '06-03', '06-04', '06-05', '06-06', '06-07', '06-08', '06-09', '06-10', '06-11', '06-12', '06-13', '06-14', '06-15', '06-16', '06-17', '06-18', '06-19', '06-20']
    ugh = [0 for i in range(0,len(start_date))]
    for index,row in data.iterrows():
        a = start_date.index(row["Start Date"])
        ugh[a] += 1.0
    start_date = list(rrule.rrule(rrule.DAILY,
                         dtstart=parser.parse("2018-01-01"),
                         until=parser.parse("2018-06-20")))
    for i in range (0,len(start_date)):
        start_date[i] =start_date[i].date()
    march = pd.DataFrame({"Crime Count": ugh, "Date":start_date} )
    #ax = march.plot(kind = "line", y = "Crime Count", figsize = (40,10), title = ("2017" +str(title)), xticks = [0,31,59,90,120,151,181,212,243,273,304,334,365], grid = True)
    #fig = ax.get_figure()
    #fig.savefig("2017" + title + ".png")
    return march

#read 2017
data = pd.read_excel('/Users/VarshiniSelvadurai/Documents/Internship/Crime_Edited.xlsx', sheet_name = '2017')
#data = pd.read_excel('C:\\Users\\vns8\\Documents\\Crime_Edited.xlsx', sheet_name = '2017')
data = data.loc[data["Crime Name1"] != "Not a Crime"]
data = data.drop(columns = ["Police District Number","Address Number","Victims","CR Number","NIBRS Code","Beat","PRA","State","Incident ID","Offence Code","Sector","Police District Name","Crime Name2","Crime Name3","Agency","Place","End Date/Time","Dispatch Date/Time","Block_Address"])
ugh = list(map(str, data["Start Time"]))
for i in range (0, len(ugh)):
    ugh[i] = ugh[i][:2]
data["Start Time"] = ugh
ugh = (list(map(str,data['Start Date'])))
ughh = []
for i in range(0,len(ugh)):
    ugh[i] = ugh[i][5:]
    ugh[i] = ugh[i][:5]
data['Start Date'] = ugh

#read 2018
data_2018 = pd.read_excel('/Users/VarshiniSelvadurai/Documents/Internship/Crime_Edited.xlsx', sheet_name = '2018')
#data_2018 = pd.read_excel('C:\\Users\\vns8\\Documents\\Crime_Edited.xlsx', sheet_name = '2018')
data_2018 = data_2018.loc[data_2018["Crime Name1"] != "Not a Crime"]
data_2018 = data_2018.drop(columns = ["Police District Number","Address Number","Victims","CR Number","NIBRS Code","Beat","PRA","State","Incident ID","Offence Code","Sector","Police District Name","Crime Name2","Crime Name3","Agency","Place","End Date/Time","Dispatch Date/Time","Block_Address"])
ugh = list(map(str, data_2018["Start Time"]))
for i in range (0, len(ugh)):
    ugh[i] = ugh[i][:2]
data_2018["Start Time"] = ugh
ugh = (list(map(str,data_2018['Start Date'])))
ughh = []
for i in range(0,len(ugh)):
    ugh[i] = ugh[i][5:]
    ugh[i] = ugh[i][:5]
data_2018['Start Date'] = ugh

z_20902 = data.loc[data["Zip Code"] == 20902]
z_20906 = data.loc[data["Zip Code"] == 20906]
z_20904 = data.loc[data["Zip Code"] == 20904]
z_20910 = data.loc[data["Zip Code"] == 20910]
z_20874 = data.loc[data["Zip Code"] == 20874]
z_20902_2018 = data_2018.loc[data_2018["Zip Code"] == 20902]
z_20906_2018 = data_2018.loc[data_2018["Zip Code"] == 20906]
z_20904_2018 = data_2018.loc[data_2018["Zip Code"] == 20904]
z_20910_2018 = data_2018.loc[data_2018["Zip Code"] == 20910]
z_20874_2018 = data_2018.loc[data_2018["Zip Code"] == 20874]

day_20902 = daycount(z_20902)
day_20906 = daycount(z_20906)
day_20904 = daycount(z_20904)
day_20910 = daycount(z_20910)
day_20874 = daycount(z_20874)
day_20902_2018 = daycount_2018(z_20902_2018)
day_20906_2018 = daycount_2018(z_20906_2018)
day_20904_2018 = daycount_2018(z_20904_2018)
day_20910_2018 = daycount_2018(z_20910_2018)
day_20874_2018 = daycount_2018(z_20874_2018)

y = day_20906["Crime Count"]
p = d = q = range(0, 8)
# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))
# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 52) for x in list(itertools.product(p, d, q))]
warnings.filterwarnings("ignore") # specify to ignore warning messages
ugh = []
ughh = []
ughhh = []
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = SARIMAX(y,
                            order=param,
                            seasonal_order=param_seasonal,
                            enforce_stationarity=False,
                            enforce_invertibility=False)

            results = mod.fit()
            ugh.append(param)
            ughh.append(param_seasonal)
            ughhh.append(results.aic)
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            print('ARIMA{}x{}12 - AIC:NOPEEEEEEEE'.format(param, param_seasonal))
print(ugh[ughhh.index(min(ughhh))])
print(ughh[ughhh.index(min(ughhh))])
