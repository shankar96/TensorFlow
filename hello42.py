import tensorflow as tf
import numpy as np

a=np.random.rand(5).astype(np.float32)

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
print a
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))
print 'https://github.com/shankar96/TensorFlow.git'