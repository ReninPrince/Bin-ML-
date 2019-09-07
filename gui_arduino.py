from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import random
from tkinter import messagebox
from tkinter import simpledialog
import serial
import datetime
import time

arduinoData = serial.Serial('COM7',9600,timeout = 60000)
time1 = 0
bt = 0
base = [19,23]
binnum = []
distance = []


all_val = []

dataset = pd.read_csv('bin0.csv')
x = dataset.iloc[:,[0]] #bin number
y = dataset.iloc[:,1] #filled percent


X1 = pd.DataFrame()
y1 = pd.DataFrame()

def second():
    root1 = Tk()
    root1.overrideredirect(True)
    root1.geometry("{0}x{1}+0+0".format(root1.winfo_screenwidth(), root1.winfo_screenheight()))
    root1.title("Garbage management system")
    #-------------------------------------------------------------------------------------------------------------------------------------------
    Titlecard = Frame(root1, width = 1280, height = 100, bd = 7, bg = 'blue', relief = GROOVE)
    Titlecard.pack(side = 'top', anchor = CENTER, fill = X)
    rt = time.strftime("%d/%m/%y")
    body  = Frame(root1, width = 1280, height = 600, bd = 9, bg = 'dodgerblue3', relief = FLAT)
    body.pack(side = 'top',expand = 1,fill = BOTH)
    login = Frame(body, width = 1000, height = 600, bd = 7, bg = 'dodgerblue3', relief = RAISED)
    login.pack(side = TOP, anchor = CENTER,expand=1, fill = BOTH, ipady = 40,ipadx = 10) 
    #--------------------------------------------------------------------------------------------------------------------------------------
    binnum0 = StringVar()
    fill_percent0 = StringVar()
    notetime0 = StringVar()
    rate_of_fill0 = StringVar()
    desn0 = StringVar()
    
    binnum1 = StringVar()
    fill_percent1 = StringVar()
    notetime1 = StringVar()
    rate_of_fill1 = StringVar()
    desn1 = StringVar()
    
    week1 = StringVar()
    predicted0 =StringVar()
    predicted1 =StringVar()
    
    def ask():
        global X1,y1,bt
        week = week1.get()
        for i in range(int(week)):
            machine(X1,y1)
        predicted0.set(y1[len(y1)-2])
        predicted1.set(y1[len(y1)-1])
       

    def machine(x,y):
        global X1,y1,binnum
        from sklearn.ensemble import RandomForestRegressor
        regressor = RandomForestRegressor(n_estimators = 500, random_state = 0)
        regressor.fit(x, y)

        new_values = []
        new_values1 = []
        
        for i in range(len(binnum)):
            y_pred = regressor.predict(i)
    ##        print(i,y_pred)
            new_values.append(int(i))
            new_values1.append(round(float(y_pred),2))
    ##    print(new_values,new_values1)
        new_df = pd.DataFrame({"Bin number":new_values})
        new_df1 = pd.DataFrame({"filled percent":new_values1})
        new_df = new_df.iloc[:,[0]] #bin number
        new_df1 = new_df1.iloc[:,0] #filled percent

        
        x = x.append(new_df, ignore_index = True)
        y = y.append(new_df1, ignore_index = True)
        X1 = x
        y1 = y
    machine(x,y)
    def iExit():
        qExit = messagebox.askyesno("Garbage management system", "Do you want to exit the system")
        if qExit > 0:
            root1.destroy()
            return
        
    def rate(bt,dist,base,binnum):
        global all_val
        distance =  int(base - dist)
        if distance <= base:
            cur = distance
            filper = (cur /base) * 100
            fill_percent = str(round(filper,2))
            notetime = int(bt)
            check_time = str(notetime)
            rate1 = cur / notetime
            rate_of_fill = str(round(rate1,2))
            endtime = float(base) / float(rate1)
            if endtime > 60:
                endtime = endtime / 60
                endtime = round(endtime,2)
                est_endtime = str(endtime)
            else:
                endtime = round(endtime,2)
                est_endtime = str(endtime)
            
            remtime = endtime - (notetime / 60)
            if remtime > 60:
                remtime = remtime / 60
                remtime = round(remtime,2)
                rem_endtime = str(remtime)
            else:
                remtime = round(remtime,2)
                rem_endtime = str(remtime)
            if remtime < 1:
                desn = 1
            else:
                desn = 0
            all_val.append(binnum)
            all_val.append(fill_percent)
            all_val.append(notetime)
            all_val.append(rate_of_fill)
            all_val.append(desn)



                                ##            for i in range(len(binnum)):
                
##                Label(login, text=binnum[i], relief=FLAT,width=20, bd = 4, fg = 'black',bg = 'dodgerblue3',
##                      font = ('arial', 15, 'bold')).grid(row=i+1,column=0,padx = 15, pady = 15,ipady = 2)
            try:
                binnum1.set(all_val[len(all_val)-10])
                fill_percent1.set(all_val[len(all_val)-9])
                notetime1.set(all_val[len(all_val)-8] )
                rate_of_fill1.set(all_val[len(all_val)-7] )
                desn1.set(all_val[len(all_val)-6] )
                
                binnum0.set(all_val[len(all_val)-5])
                fill_percent0.set(all_val[len(all_val)-4])
                notetime0.set(all_val[len(all_val)-3] )
                rate_of_fill0.set(all_val[len(all_val)-2] )
                desn0.set(all_val[len(all_val)-1])
            except:
                pass
            Label(login, text="Enter \nweek(s): ", relief=FLAT,width=16, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=3,column=3,padx = 15, pady = 15,ipady = 2)

            Entry(login, textvariable=week1, relief=FLAT,width=16, bd = 4,
                       font = ('arial', 15, 'bold')).grid(row=3,column=4,padx = 15, pady = 15,ipady = 2)

            btn0 = Button(login, text = "FIND" ,command=ask, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                               fg = 'blue2', font = ('arial', 20, 'italic')).grid(row=4,column=4,padx = 15, pady = 15,ipady = 2)

            Label(login, text="PREDICTED", relief=FLAT,width=14, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=0,column=5,padx = 12, pady = 15,ipady = 2)
            
            Label(login, textvariable=predicted0, relief=FLAT,width=14, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=1,column=5,padx = 12, pady = 15,ipady = 2)
            Label(login, textvariable=predicted1, relief=FLAT,width=14, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=2,column=5,padx = 12, pady = 15,ipady = 2)



    def arduino():
        global dist0,dist1
        bin0 = arduinoData.readline().decode('ascii')
        bin1 = arduinoData.readline().decode('ascii')
        bin0 = bin0.split(' ')
        bin1 = bin1.split(' ')
        binnum.append(bin0[0])
        binnum.append(bin1[0])
        bin0a = bin0[1].split( '\r')
        bin1a = bin1[1].split( '\r')
        distance.append(int(bin0a[0]))
        distance.append(int(bin1a[0]))
        print(binnum,distance)
        
    def timefun():
        global bt,binnum,distance
        timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        time1 = str(timestamp[-5] + timestamp[-4])
        if int(time1) % 1 == 0:
            bt =  time1
            binnum = []
            distance = []
            arduino()
            for i in range(len(binnum)):
##                try:
                rate(bt,distance[i],base[i],binnum[i])
##                except:
##                    pass
####            print(bt,dist1,base1,binnum1)bt,dist,base,binnum
    #--------------------------------------------------------------------------------------------------------------------------------------


    date1 = Label(Titlecard, text = "DATE:" + rt,relief = GROOVE, width = 17, bd  = 7,bg = 'white', fg = 'black',font = ('arial', 15, 'italic'))
    date1.pack(side = RIGHT, anchor = NW, pady = 15)

    Title = Label(Titlecard, text = "GARBAGE MANAGEMENT SYSTEM", relief = GROOVE, width = 30 , bd = 7, bg = 'dodgerblue4',
                  fg = 'lightSkyblue2', font = ('arial', 20, 'italic'))
    Title.pack(side = LEFT,pady = 15, ipadx = 35, padx =45)

    Label(login, text="Bin number: ", relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=0,column=0,padx = 15, pady = 15,ipady = 2)
    Label(login, text="Current level: ", relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=0,column=1,padx = 25, pady = 15,ipady = 2)
    Label(login, text="Last checked \ntime(mins) : ", relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=0,column=2,padx = 15, pady = 15,ipady = 2)
    Label(login, text="Rate of fill: ", relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=0,column=3,padx = 15, pady = 15,ipady = 2)
    Label(login, text="Call truck: ", relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=0,column=4,padx = 15, pady = 15,ipady = 2)


    

    
    Label(login, textvariable=binnum1, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=1,column=0,padx = 15, pady = 15,ipady = 2)
    Label(login, textvariable=fill_percent1, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=1,column=1,padx = 25, pady = 15,ipady = 2)
    Label(login, textvariable=notetime1, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=1,column=2,padx = 15, pady = 15,ipady = 2)
    Label(login, textvariable=rate_of_fill1, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=1,column=3,padx = 15, pady = 15,ipady = 2)
    Label(login, textvariable=desn1, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=1,column=4,padx = 15, pady = 15,ipady = 2)
    
    Label(login, textvariable=binnum0, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=2,column=0,padx = 15, pady = 15,ipady = 2)
    Label(login, textvariable=fill_percent0, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=2,column=1,padx = 25, pady = 15,ipady = 2)
    Label(login, textvariable=notetime0, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=2,column=2,padx = 15, pady = 15,ipady = 2)
    Label(login, textvariable=rate_of_fill0, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=2,column=3,padx = 15, pady = 15,ipady = 2)
    Label(login, textvariable=desn0, relief=FLAT,width=15, bd = 4, fg = 'black',bg = 'dodgerblue3',
               font = ('arial', 15, 'bold')).grid(row=2,column=4,padx = 15, pady = 15,ipady = 2)

    
 
    
    btn1 = Button(body, text = "CHECK" ,command=timefun, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 10)
    btn2 = Button(body, text = "CLEAR", relief = FLAT, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'Steelblue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 10)
    btn3 = Button(body, text = "EXIT",command = iExit, relief = RAISED, width = 10 , bd = 6, bg = 'Steelblue2',
                       fg = 'blue2', font = ('arial', 20, 'italic')).pack(side =LEFT, anchor = CENTER,expand = 2, fill = X,ipady = 10)

 #-------------------------------------------------------------------------------------------------------------------------------------------
    root1.mainloop()


##while 1:
##    timefun()
##    second()
##    time.sleep(50)


second()





































