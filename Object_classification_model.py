from keras.models import Sequential
from keras.layers import Conv2D,BatchNormalization
from keras.layers import MaxPooling2D,Activation
from keras.layers import Flatten
from keras.layers import Dense,Dropout

data_dir ='/content/gdrive/My Drive/images/train'
data_dir1 ='/content/gdrive/My Drive/images/test'

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory(data_dir,
                                                 target_size = (32,32),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory(data_dir1,
                                            target_size = (32,32),
                                            batch_size = 32,
                                            class_mode = 'categorical')

model = Sequential()
model.add(Conv2D(32, kernel_size=(3 ,3),
                 input_shape=(32,32,3)))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
##500
model.add(Dense(200, activation='relu'))
model.add(Dense(500, activation='relu'))
model.add(Dropout(0.25))

model.add(Dense(8, activation='softmax'))

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

model.fit_generator(training_set,
                         steps_per_epoch = 2110,
                         epochs = 3 ,
                         validation_data = test_set,
                         validation_steps = 375 ,
                    workers = 4)

'''Epoch 1/3
2110/2110 [==============================] - 1020s 484ms/step - loss: 0.4826 - acc: 0.8413 - val_loss: 1.3628 - val_acc: 0.7555
Epoch 2/3
2110/2110 [==============================] - 1025s 486ms/step - loss: 0.1840 - acc: 0.9600 - val_loss: 1.4501 - val_acc: 0.7856
Epoch 3/3
2110/2110 [==============================] - 1024s 485ms/step - loss: 0.1992 - acc: 0.9669 - val_loss: 1.8999 - val_acc: 0.7838
<keras.callbacks.History at 0x7f6a5f205198>'''


#prediction_part

import numpy as np
from keras.preprocessing import image


path='/content/gdrive/My Drive/my-image.png'

test_image = image.load_img(path, target_size=(32,32))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = model.predict_classes(test_image)
print(result)

#saving model
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive 
from google.colab import auth 
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()          
gdrive = GoogleDrive(gauth)

model.save('natural_categories.v1.2.h5')
model_file = gdrive.CreateFile({'title' : 'natural_categories.v1.2.h5'})                     
model_file.SetContentFile('natural_categories.v1.2.h5')      
model_file.Upload()

 


 