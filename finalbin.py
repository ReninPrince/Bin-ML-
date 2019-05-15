from random import randint
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



dataset = pd.read_csv('datasetbin.csv')
X = dataset.iloc[:,[0]] #bin number
yval = dataset.iloc[:,2] #filled percent
z = []
for i in range(len(yval)):
    u1 = (yval[i])
    uv3 = u1.split('%')
    um1 = []
    for i in range(len(uv3)):
        if uv3[i].isdigit() == True:
            um1.append(uv3[i])
    if len(um1) < 2:
        Yval = (float(um1[0])) 
    z.append(Yval)
y = pd.DataFrame({'filled percent':z})
    

X1 = pd.DataFrame()
y1 = pd.DataFrame()


    
                        
def ask():
    global X1,y1
    week = input("enter how many weeks:")
    for i in range(int(week)):
        machine(X1,y1)

def machine(X,y):
    global X1,y1
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators = 500, random_state = 0)
    regressor.fit(X, y)

    new_values = []
    new_values1 = []

    for i in range(10):
        y_pred = regressor.predict(i)
        new_values.append(i)
        new_values1.append(float(y_pred))
    new_df = pd.DataFrame({"Bin number":new_values})
    new_df1 = pd.DataFrame({"filled percent":new_values1})
    
    X = X.append(new_df, ignore_index = True)
    y = y.append(new_df1, ignore_index = True)
    X1 = X
    y1 = y

machine(X,y)
ask()

fpdf = y1[-10:]



fp = []
final_ar = []
for i in range(len(fpdf)):
    tfp = (fpdf.iloc[i])
    fp.append(tfp)
##print(fp)
for i in range(len(fp)):    
        def rate(fp):
            binbasehgt = int(100)
        ##    houses = input("enter number of houses:")
            binfilhgt = fp[i]
            binfil = (int(binfilhgt) / int(binbasehgt)) * 100
            pbinfill = (str((binfil)) + "%")
            binfiltime = int(360)
            binfiltime1 = (binfiltime) / 60
            timehrs = (str((binfiltime1)) + "hr")
            rateoffil = (binfil) / (binfiltime1)
            rfph = (str((rateoffil)) + "cm/hr")
            binendtim = (float(binbasehgt) / float(rateoffil))
            binendtim = round(binendtim, 2)
            binendtim2 = binendtim - binfiltime1
            binendtim2 = round(binendtim2, 2)
            if binendtim < 1:
                binendtim = binendtim * 60
                fill1 =  (str(int(binendtim))+ " min")
            elif binendtim > 1:
                p = binendtim
                k = (str(p).split('.'))
                j = (int(k[1]) * .60)
                fill1 = ( str(int(k[0]))+ " hr " + str(int(j)) + " min")
            else:
                fill1 = ( str(int(binendtim))+ " hr")
                
            if binendtim2 < 1:
                binendtim2 = binendtim2 * 60
                fill = (str(int(binendtim2))+ " min")    
            elif binendtim2 > 1:
                p = binendtim2
                k = (str(p).split('.'))
                j = (int(k[1]) * .60)
                fill = (str(int(k[0]))+ " hr " + str(int(j)) + " min")
            else:
                fill = (str(int(binendtim2))+ " hr")
            u = fill
            uv = u.split(' ')
            um = []
            for j in range(len(uv)):
                if uv[j].isdigit() == True:
                    um.append(uv[j])
            if len(um) < 2:
                time = (float('.' + um[0]))  
            else:
                time = (float(um[0]+ '.' + um[1]))
            if time < 3.0:
                desn = 'yes'
            else:
                desn = 'no'
            final_data = {"Base height":binbasehgt,"filled percent":pbinfill,"Checking time(hours)":timehrs,
                          "Rate of filling per  hour":rfph,
                          "Calculated time":fill1,"Remaining time to fill":fill,"Call truck":desn}
            final_ar.append(final_data)
        rate(fp)
for i in range(len(final_ar)):
    print(final_ar[i])

















                  

