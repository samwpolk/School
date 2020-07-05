
print('Problem 5')
Problem 5

import tensorflow as tf
ans = []
 
a = tf.constant(1.12)
b = tf.constant(2.34)
c = tf.constant(0.72)
d = tf.constant(0.81)
f = tf.constant(19.83)
 
x = 1 + tf.divide(a,b) + tf.divide(c,tf.square(f))
ans.append(x)
 
s = tf.divide((b - a),(d - c))
ans.append(s)
 
r = tf.math.reciprocal( tf.math.reciprocal(a)+ tf.math.reciprocal(b)+ tf.math.reciprocal(c)+ tf.math.reciprocal(d))
ans.append(r)
 
y = tf.divide(tf.multiply(tf.multiply(a,b),tf.square(f)),tf.multiply(2,c))
ans.append(y)
 
tf.print(ans)
[1.48046339, 13.5555582, 0.253571272, 715.676514]


