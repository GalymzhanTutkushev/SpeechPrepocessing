# Create your first MLP in Keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
import numpy as np
import csv
# fix random seed for reproducibility
np.random.seed(7)
# load pima indians dataset
# dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
# Read CSV file
with open('inputMFCC.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    inputs = [row for row in reader]  
# Read CSV file
with open('targetSpeech.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    targets = [row for row in reader]     
X=inputs
Y=targets
dataset = np.zeros((8,9))
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


model.save("model.h5")
model = load_model('model.h5')
model.summary()