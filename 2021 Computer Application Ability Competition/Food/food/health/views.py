from django.shortcuts import render

from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
import numpy as np
import pandas as pd
model = load_model('NN_Model.h5')

def health_check(request):
    if request.method == "POST":

        age = request.POST.get("age")
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        water = request.POST.get('water')

        gender = request.POST.get('sex')
        vegetable = request.POST.get('vegetable')
        activity = request.POST.get('activity')
        mobile = request.POST.get('mobile')

        overweight = request.POST.get('overweight')
        calorie = request.POST.get('calorie')
        meal = request.POST.get("meal")
        snack = request.POST.get("snack")

        smoke = request.POST.get("smoke")
        drink = request.POST.get("drink")
        attention = request.POST.get("attention")
        out = request.POST.get("out")

        if int(water)>3:
            water=3
        if int(vegetable)>3:
            vegetable=3
        if int(activity)>3:
            activity=3
        if int(mobile)>2:
            mobile=2

        x1, x2, x3, x4 = [], [], [], []

        x1.append(int(gender))
        x1.append(int(age))
        x1.append(int(height))
        x1.append(int(weight))

        x2.append(int(calorie))
        x2.append(int(vegetable))
        x2.append(int(meal))
        x2.append(int(water))

        x3.append(int(snack))
        x3.append(int(drink))
        x3.append(int(smoke))

        x4.append(int(overweight))
        x4.append(int(attention))
        x4.append(int(activity))
        x4.append(int(mobile))
        x4.append(int(out))

        x1, x2, x3, x4 = np.array(x1), np.array(x2), np.array(x3), np.array(x4)
        x1, x2, x3, x4 = x1.reshape(1, -1), x2.reshape(1, -1), x3.reshape(1, -1), x4.reshape(1, -1)
        print(x1, x2, x3, x4)
        
        #load model
        model = load_model('NN_Model.h5')
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
        if pred=='Normal_Weight':
            pred='体重正常'
        
        if pred=='Obesity':
            pred='肥胖'

        if pred=='Overweight':
            pred='超重'

        if pred=='Insufficient_Weight':
            pred='体重过轻'

        message1='您有{}%的几率身体状况是：{} '.format(prob,pred)

        return render(request, 'health_check.html',{'message1':message1})
    return render(request, 'health_check.html')