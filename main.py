# LIBSVM initialization
import sys
path = './libsvm-3.23/python'
sys.path.append(path)
from svmutil import *
from func import *

# Main
label, sample = svm_read_problem('./data/formatted_training.txt')
'''没进行归一化'''
model = svm_train(label[1:len(label)-10], sample[1:len(sample)-10], '-s 2')
p_label = svm_predict(label[10:], sample[10:], model)
print(p_label)

