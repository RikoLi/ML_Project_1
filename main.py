# LIBSVM initialization
import sys
import math
path = './libsvm-3.23/python'
sys.path.append(path)
from svmutil import *
from func import *
path = './libsvm-3.23/tools'
sys.path.append(path)
from grid import *

# Main
# -------------Start from here------------
# Divide training data
train_size = 0.9
label, feature = svm_read_problem('./data/scaled_training.txt')
train_label, train_feature, test_label, test_feature = dataDivide(label, feature, train_size)

# Create model
#print('训练中...')
#prob = svm_problem(label, feature)
#param = svm_parameter('-s 0 -t 2 -h 0 -c 50 -g 5 -v 5') # 学习器训练参数待调整
#model = svm_train(prob, param)

# 用libsvm自带的Python工具寻找C-SVM最优参数对(c, g)
print('开始寻找最优参数...')
accuracy, param_cg = find_parameters('./data/scaled_training.txt', '-log2c 1,11,2 -log2g 1,8,0.5')
print('ACC:', accuracy, 'Param:', param_cg)

#print('成功创建模型，开始预测...')

# Predict and check
#svm_predict(test_label, test_feature, model)