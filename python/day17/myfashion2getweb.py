import tensorflow as tf
import cv2
import os


fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

img = cv2.imread('image/shoes2.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img, (28,28))
img2 = img2.reshape((1, 28 * 28))
img2 = img2.astype('float32') / 255
img3 = 1-img2

train_images = train_images / 255.0
test_images = test_images / 255.0
 
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
 
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
 
model.fit(train_images, train_labels, epochs=10)

model.save("mymodel")
 
 
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
num = model.predict_classes(img3)[0]
print('The Answer is ', class_names[num])



