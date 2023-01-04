#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv(r'C:\Users\User\Desktop\DL\Assignments\day2\Salary_Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values


# In[2]:


import tensorflow as tf
tf.__version__


# In[3]:


dataset.head()


# In[4]:


dataset.shape


# In[5]:


from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(X)
x_scaled=scaler.transform(X)
x_scaled


# In[ ]:





# In[6]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
X_train.shape


# In[7]:


X_test.shape


# In[8]:


###Creating artificial neural network ANN
from tensorflow.python.keras.layers.core import Activation
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

### constructing neural network

model=Sequential()
#model.add(Dense(4,activation="relu"))
model.add(Dense(6,activation="relu")) ### 1st hidden layer with 3 neural  and relu is activation
model.add(Dense(6,activation="relu")) ### 2nd hidden layer with 2 neural  and relu is activation
model.add(Dense(1,activation="sigmoid")) ### 3rd hidden layer with 1 neural  and relu is activation

from keras import optimizers
### to optimize the weight and to reduce the weight to attain global minimum
model.compile(optimizer="rmsprop" ,loss="mse")

### epoch= number of time data passed
###batch_size =1 means every epoch will be having all training data
### if batch_size=2 then every epoch will be having 400 data 
model.fit(X_train,y_train,epochs=50,batch_size=1)


# In[9]:


model.history.history.keys()


# In[10]:


###check all statistics of the neuron and weight
model.summary()


# In[11]:


model.history.history["loss"]


# In[12]:


plt.plot(model.history.history["loss"],marker="o")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()


# In[13]:


ypred=model.predict(X_test)
### calculate score for regression models
from sklearn.metrics import explained_variance_score
explained_variance_score(y_test,ypred)


# In[14]:


result=pd.DataFrame(ypred,columns=["ypred"])
result["ytest"]=y_test
result["error"]=result["ytest"]-result["ypred"]

result


# In[15]:


###Save ANN model
import tensorflow
tensorflow.keras.models.save_model(model,"ANN_Assign_Mpdel.h5")


# In[16]:


###Load/reuse the saved model
loaded_model=tensorflow.keras.models.load_model("ANN_Assign_Mpdel.h5",compile=False)


# In[17]:


loaded_model.predict(scaler.transform([[3.7]]))


# In[18]:


from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

rmse = np.sqrt(mean_squared_error(y_test,ypred))
r2 = r2_score(y_test,ypred)                           #built-in function r2_score() indicates R-squared value 

print("RMSE =", rmse)
print("R2 Score=",r2)


# In[ ]:





# In[ ]:




