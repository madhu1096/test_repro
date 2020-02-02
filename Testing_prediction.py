import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import keras

classifier = load_model('eleliotig_10.h5')


path='images/test/Tiger/000093.jpg'

test_image = image.load_img(path, target_size=(32,32))

test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict_classes(test_image)
result



