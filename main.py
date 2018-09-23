# LIBSVM initialization
import sys
import math
path = './libsvm-3.23/python'
sys.path.append(path)
from svmutil import *
from func import *

# Main
# -------------Start from here------------
# Divide training data
train_size = 0.8
label, feature = svm_read_problem('./data/scaled_training.txt')
train_label, train_feature, test_label, test_feature = dataDivide(label, feature, train_size)

# Create model
print('训练中...')
prob = svm_problem(label, feature)
param = svm_parameter('-s 0 -t 2 -h 0 -c 100 -g 10 -v 5') # 学习器训练参数待调整
model = svm_train(prob, param)
#svm_save_model('./model/demo_model.model', model)
#model = svm_load_model('./model/demo_model.model')
print('成功创建模型，开始预测...')

# Predict and check
#svm_predict(test_label, test_feature, model)