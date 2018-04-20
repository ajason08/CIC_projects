
# coding: utf-8

# In[51]:


from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn.model_selection import train_test_split
from sklearn.metrics import *

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)


# In[4]:


# load pima indians dataset
dataset = numpy.loadtxt("C:/my_temp/pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]


# In[5]:


# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# In[10]:


'''
loss function = it evaluates how good is a set of weights, 
optimizer = it searchs through different weights for the network 
Now, we will use logarithmic loss, which for a binary classification problem is defined in Keras as “binary_crossentropy“
We will also use the efficient gradient descent algorithm “adam” for no other reason that it is an efficient default.
'''
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[9]:


'''
We must specify 
# epochs = iterations,
batch_size or = # of instances evaluated before a weight update
'''
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)


# In[21]:


# evaluate the model
'''
This will only give us an idea of how well we have modeled the dataset (e.g. train accuracy),
but no idea of how well the algorithm might perform on new data
'''
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


# In[14]:


# Splitting dataset
# first way to split (using a keras method)
model.fit(X, Y, validation_split=0.33, epochs=150, batch_size=10)


# In[23]:


# Splitting dataset
# second way to split (using a sklearn method)
# we are getting 3 sets: Train(50%), development(25%) and test(25%) ; %amount of data
X_train, X_aux, y_train, y_aux = train_test_split(X, Y, test_size=0.5, random_state=seed)
X_dev, X_test, y_dev, y_test = train_test_split(X_aux, y_aux, test_size=0.5, random_state=seed)

model.fit(X_train, y_train, validation_data=(X_dev,y_dev), epochs=150, batch_size=10)


# In[60]:


# predicting
predictions = model.predict(X_test)
predictions = [round(x[0]) for x in predictions]
print(predictions)


# In[61]:


# metrics/scorer
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

