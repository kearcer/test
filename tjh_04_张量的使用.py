import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
# 使用张量记录中间结果
a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a + b

# 直接计算向量的和，这样可读性会比较差
result = tf.constant([1.0, 2.0], name="a") + tf.constant([2.0, 3.0], name="b")
