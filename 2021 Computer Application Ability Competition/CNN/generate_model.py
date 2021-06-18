import pandas as pd


# Data prepocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer

# Model
from keras.layers import Dense
from keras.optimizers import Adam
from keras.layers import Input
from keras.models import Model
from keras.layers import concatenate , Reshape , Dropout , Conv2D, MaxPool2D, Flatten
import tensorflow as tf
import keras.backend as K
from keras.callbacks import LearningRateScheduler



# warning
import warnings
import os
warnings.filterwarnings('ignore')



def data_preprocessing(data):
    x = data.drop(['Target','NObeyesdad'],axis=1)
    y = data['Target']

    # label encoder
    le = LabelEncoder()
    for column_name in x.columns:
        if x[column_name].dtype == object:
            x[column_name] = le.fit_transform(x[column_name])
        else:
            pass

    # train test split

    # multiple input train split
    x1 = x[['Gender', 'Age', 'Height', 'Weight']]

    x2 = x[['Frequent_consumption_of_high_caloric_food',
                 'Frequent_consumption_of_vegetables',
                 'Number_of_main_meals',
                 'Consumption_of_water']]
    x3 = x[['Consumption_of_food_between_meals',
                 'Consumption_of_alcohol',
                 'SMOKE',
                 ]]
    x4 = x[['family_history_with_overweight',
                 'Calories_consumption_monitoring',
                 'Physical_activity_frequency',
                 'Time_using_technology_devices',
                 'Transportation'
                 ]]

    # Y label binarizer
    LB = LabelBinarizer()
    y = LB.fit_transform(y)

    return x1 , x2 ,x3 , x4 , y


def scheduler(epoch): # learning rate decay
    # 每隔100个epoch，学习率减小为原来的1/2
    if epoch % 100 == 0 and epoch != 0:
        lr = K.get_value(model.optimizer.lr)
        K.set_value(model.optimizer.lr, lr * 0.5)
        print("lr changed to {}".format(lr * 0.5))
    return K.get_value(model.optimizer.lr)



def NN_Model():
    # define two sets of inputs
    inputA = Input(shape=(4,))
    inputB = Input(shape=(4,))
    inputC = Input(shape=(3,))
    inputD = Input(shape=(5,))

    # the 1 branch operates on the first input
    a = Dense(32, kernel_initializer='uniform', activation="sigmoid")(inputA)
    a = Dense(16, activation="tanh")(a)
    a = Model(inputs=inputA, outputs=a)

    # the 2 branch opreates on the second input
    b = Dense(32, kernel_initializer='uniform', activation="sigmoid")(inputB)
    b = Dense(16, activation="tanh")(b)
    b = Model(inputs=inputB, outputs=b)

    # the 3 branch opreates on the second input
    c = Dense(32, kernel_initializer='uniform', activation="sigmoid")(inputC)
    c = Dense(16, activation="tanh")(c)
    c = Model(inputs=inputC, outputs=c)

    # the 4 branch opreates on the second input
    d = Dense(32, kernel_initializer='uniform', activation="sigmoid")(inputD)
    d = Dense(16, activation="tanh")(d)
    d = Model(inputs=inputD, outputs=d)

    # combine the output of the two branches
    combined = concatenate([a.output, b.output, c.output, d.output])

    # combined outputs
    z = Reshape((16, 4, 1), input_shape=(64,))(combined)
    z = Conv2D(8, kernel_size=(3, 3), activation='sigmoid', input_shape=(16, 4))(z)
    z = MaxPool2D(pool_size=(2, 2), strides=(2, 2))(z)
    z = Conv2D(4, kernel_size=(4, 1), activation='sigmoid')(z)
    z = MaxPool2D(pool_size=(1, 1), strides=(1, 1))(z)
    z = Flatten()(z)
    z = Dense(8, activation="sigmoid")(z)
    z = Dense(4, activation="softmax")(z)

    # our model will accept the inputs of the two branches and
    # then output a single value
    model = Model(inputs=[a.input, b.input, c.input, d.input], outputs=z)

    opt = Adam(lr=0.0001)
    model.compile(loss='categorical_crossentropy', optimizer=opt,
                  metrics=['accuracy'])
    model.summary()
    H = model.fit([x1, x2, x3, x4], target,
                  epochs=2000, batch_size=20)
    return model




if __name__ == "__main__":

    # read data
    data = pd.read_csv('raw_data.csv')
    x1 , x2 , x3,x4 , target = data_preprocessing(data)
    print("the fist input shape {} , the second input shape {} ,the second input shape {} ,the second input shape {}  output shape {} ".format(
        x1.shape, x2.shape ,x3.shape, x4.shape,target.shape))

    # Distributed_Computing

    strategy = tf.distribute.MirroredStrategy()
    print(tf.__version__)
    print('Number of devices: {}'.format(strategy.num_replicas_in_sync))
    with strategy.scope():
        model = NN_Model()


    # save model
    model.save('NN_Model.h5')
    print('Save!')
