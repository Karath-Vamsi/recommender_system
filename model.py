import tensorflow as tf
import keras
import numpy as np

class Model_builder:
    def __cost_function(self, X, W, b, Y, R, lambda_):

        j = (tf.linalg.matmul(X, tf.transpose(W)) + b - Y)*R
        J = 0.5 * tf.reduce_sum(j**2) + (lambda_/2) * (tf.reduce_sum(X**2) + tf.reduce_sum(W**2))
        return J
    
    def __normalize(self, Y, R):

        Ymean = (np.sum(Y*R,axis=1)/(np.sum(R, axis=1)+1e-12)).reshape(-1,1)
        Ynorm = Y - np.multiply(Ymean, R) 
        return Ynorm, Ymean
    
    def model(self, Y, R, lambda_):
        
        num_movies, num_users = Y.shape
        num_features = 100

        tf.random.set_seed(1234) 
        W = tf.Variable(tf.random.normal((num_users,  num_features),dtype=tf.float64),  name='W')
        X = tf.Variable(tf.random.normal((num_movies, num_features),dtype=tf.float64),  name='X')
        b = tf.Variable(tf.random.normal((1,          num_users),   dtype=tf.float64),  name='b')

        optimizer = keras.optimizers.Adam(learning_rate=0.1)

        Ynorm, Ymean = self.__normalize(Y, R)

        iterations = 200
        for iter in range(iterations):

            with tf.GradientTape() as tape:
                cost_value = self.__cost_function(X, W, b, Ynorm, R, lambda_)

            grads = tape.gradient( cost_value, [X,W,b] )
            optimizer.apply_gradients( zip(grads, [X,W,b]) )
            
            if iter % 10 == 0:
                print(f"Training loss at iteration {iter}: {cost_value:0.1f}")

        return X, W, b, Ymean