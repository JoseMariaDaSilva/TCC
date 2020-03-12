import keras
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from keras.preprocessing import image


#transformando dados em categoricos
from keras.utils import to_categorical
from keras.preprocessing import image


#Inicializando a CNN
class CNN(Sequential):


    def Number_conv(self, number, n_classes):

        for _ in range(number):

            #Passo 1 - Convolução
            self.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3),activation='relu'))

            #Passo 2 - MaxPooling
            self.add(MaxPooling2D(pool_size=(2, 2)))

        #Passo 3 - Achatamento
        self.add(Flatten())

        #Passo 4 - Conexão completa
        self.add(Dense(output_dim=128, activation='relu'))
        self.add(Dense(output_dim=n_classes, activation='softmax'))

    #Compilando CNN
    def optm(self):
        self.compile(optimizer = "Adam", loss = 'binary_crossentropy', metrics=['accuracy'])

        from keras.preprocessing.image import ImageDataGenerator

        train_datagen = ImageDataGenerator(
                rescale=1./255,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True)

        test_datagen = ImageDataGenerator(rescale=1./255)

        self.training_set = train_datagen.flow_from_directory(
                                                        'C:/Users/ZZZZZZ/Desktop/TCC/new_project/images/train_',
                                                        target_size=(64, 64),
                                                        batch_size=32,
                                                        class_mode='categorical')

        self.test_set = test_datagen.flow_from_directory(
                                                    'C:/Users/ZZZZZZ/Desktop/TCC/new_project/images/test_',
                                                    target_size=(64, 64),
                                                    batch_size=32,
                                                    class_mode='categorical')


    def run(self,step_epoch,epoch,valid_step):
        self.fit_generator(self.training_set,
                                steps_per_epoch = step_epoch,
                                epochs = epoch,
                                validation_data = self.test_set,
                                validation_steps = valid_step)
        
        return self.history.history
    
    
    def predict(self,predict_image):
        
        test_image = image.load_img(predict_image, target_size=(64,64))

        test_image = image.img_to_array(test_image)/255
        test_image = np.expand_dims(test_image, axis=0)
        for proba, label in zip(self.predict_proba(test_image)[0])
        
    def clear_session(self):
        keras.backend.clear_session()
