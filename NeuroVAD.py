from keras.models import load_model
import numpy as np 
model = load_model('model.h5')
model.summary()
scores = model.evaluate(X)
scores = np.array(scores)
scores[scores>=0.8] = 1
scores[scores<0.8] = 0