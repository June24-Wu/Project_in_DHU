
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
import numpy as np
import pandas as pd

def get_input():

    Age = int(input("Age： "))
    Height = int(input("height： "))
    Weight = int(input("weight： "))

    Consumption_of_water = int(input("water: "))
    if Consumption_of_water > 3:
        Consumption_of_water = 3

    Frequent_consumption_of_vegetables = int(input("vegetable: "))
    if Frequent_consumption_of_vegetables > 3:
        Frequent_consumption_of_vegetables = 3

    Physical_activity_frequency  = int(input("activity: "))
    if Physical_activity_frequency  > 3:
        Physical_activity_frequency  = 3

    Time_using_technology_devices = int(input("game:"))
    if Physical_activity_frequency  > 2:
        Physical_activity_frequency  = 2



    # 到前端做成选择题
    Gender = int(input("0Female, 1Male："))
    family_history_with_overweight = int(input("overweight："))
    Frequent_consumption_of_high_caloric_food = int(input("calo"))
    Number_of_main_meals = int(input("meal: "))
    Consumption_of_food_between_meals = int(input("snack"))
    SMOKE = int(input("smoke: "))
    Consumption_of_alcohol =int(input("drink: "))
    Calories_consumption_monitoring = int(input("attention: "))
    Transportation = int(input("transport: "))


    x1 , x2,x3,x4 = [] , [], [] , []

    x1.append(Gender)
    x1.append(Age)
    x1.append(Height)
    x1.append(Weight)

    x2.append(Frequent_consumption_of_high_caloric_food)
    x2.append(Frequent_consumption_of_vegetables)
    x2.append(Number_of_main_meals)
    x2.append(Consumption_of_water)

    x3.append(Consumption_of_food_between_meals)
    x3.append(Consumption_of_alcohol)
    x3.append(SMOKE)

    x4.append(family_history_with_overweight)
    x4.append(Calories_consumption_monitoring)
    x4.append(Physical_activity_frequency)
    x4.append(Time_using_technology_devices)
    x4.append(Transportation)


    x1, x2 ,x3, x4 = np.array(x1), np.array(x2) ,np.array(x3), np.array(x4)
    x1, x2 ,x3,x4 = x1.reshape(1, -1), x2.reshape(1, -1) , x3.reshape(1, -1), x4.reshape(1, -1)

    return x1 , x2 ,x3 , x4




if __name__ == "__main__":

    # load model
    model = load_model('NN_Model.h5')

    # get input
    x1 , x2 ,x3,x4= get_input()
    print(x1,x2,x3,x4)

    # predict
    result = model.predict([x1, x2, x3, x4])

    # inverse transform

    data = pd.read_csv('raw_data.csv')
    y = data['Target']
    LB = LabelBinarizer()
    y = LB.fit_transform(y)
    result = result.reshape(4, 1)
    final = []
    for element in result:
        if element == max(result):
            final.append(1)
        else:
            final.append(0)
    final = np.array(final)
    final = final.reshape(1, 4)

    prob = str((max(result) * 100)[0].round(2))
    pred = LB.inverse_transform(final)[0]
    print('{}%health：{} '.format(prob,pred))


