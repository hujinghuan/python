# -*- coding: utf-8 -*-  

import sys
sys.path.append(r'D:\Python27\libsvm-3.21\python')
from svmutil import *

y,x= svm_read_problem('../heart_scale')
m = svm_train(y[:200], x[:200], '-c 4')
p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)