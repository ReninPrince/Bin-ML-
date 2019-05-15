from random import randint
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



dataset = pd.read_csv('datasetbin.csv')
##datasetbin

X = dataset.iloc[:,[0]] #bin number, week
##y = dataset.iloc[:,2] #fill percent


##X = dataset.iloc[:,[1]] #houses
##y = dataset.iloc[:,-1] #choice
##x = dataset.iloc[:,0] #bin number
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
##X['filled percent'] = z
y = pd.DataFrame({'filled percent':z})
    

X1 = pd.DataFrame()
y1 = pd.DataFrame()

##from sklearn.cross_validation import train_test_split
##X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


##from sklearn.preprocessing import StandardScaler
##sc_X = StandardScaler()
##X_train = sc_X.fit_transform(X_train)
##X_test = sc_X.transform(X_test)
##try2 = sc_X.transform(try1)
##print(X_test)

##from sklearn.tree import DecisionTreeRegressor
##regressor = DecisionTreeRegressor( random_state = 0)
##regressor.fit(X, y)

def ask():
    global X1,y1
    k = input("do u wann run again?")
    if k == 'y':
        machine(X1,y1)
        ask()
    else:
        pass

##allX = []
##ally = []
##u = pd.DataFrame()
##def show(allX,ally):
##    final_X = allX[-1]
##    final_y = ally[-1]
##    global u
##    u = final_X
def machine(X,y):
    global X1,y1
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators = 500, random_state = 0)
    regressor.fit(X, y)

    new_values = []
    new_values1 = []

    ##from sklearn.preprocessing import PolynomialFeatures
    ##poly_reg = PolynomialFeatures(degree = 2)
    ##X_poly = poly_reg.fit_transform(X)
    ##
    ##reg2 = LinearRegression()
    ##reg2.fit(X_poly, y)

    print(len(X))
    for i in range(10):
        y_pred = regressor.predict(i)
##        print(y_pred)
        new_values.append(i)
        new_values1.append(float(y_pred))
    new_df = pd.DataFrame({"Bin number":new_values})
    new_df1 = pd.DataFrame({"filled percent":new_values1})
    
    X = X.append(new_df, ignore_index = True)
    y = y.append(new_df1, ignore_index = True)
    X1 = X
    y1 = y
    gp = input("do u wanna c graph?")
    if gp == 'y':
        plt.scatter(X1, y1, color = 'red')
        plt.plot(X1, regressor.predict(X1), color = 'blue')
        plt.title('versus')
        plt.xlabel('bin numbers')
        plt.ylabel('percentages')
        plt.show()
        ask()
    else:
        ask()
##    allX.append(X)
##    ally.append(y)
##    print(len(X))
##    machine(X,y)

##from sklearn.metrics import confusion_matrix
##cm = confusion_matrix(y_test, y_pred)

##X_grid = np.arange(min(X), max(X), 0.1)
##X_grid = X_grid, reshape((len(X_grid), 1))
##plt.scatter(X, y, color = 'red')
##plt.plot(X, regressor.predict(X), color = 'blue')
##plt.title('versus')
##plt.xlabel('bin numbers')
##plt.ylabel('percentages')
##plt.show()

machine(X,y)





ask()
##show(allX,ally)





