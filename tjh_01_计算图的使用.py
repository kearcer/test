<<<<<<< HEAD
import tensorflow as tf
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b

print(a.graph is tf.get_default_graph())
=======
import tensorflow as tf
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b

print(a.graph is tf.get_default_graph())
>>>>>>> 04f31502109879962a3370d70d14530ad3247c75
