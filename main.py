# LIBSVM initialization
import sys
path = './libsvm-3.23/python'
sys.path.append(path)
from svmutil import *
from func import *

# Main
# -------------Start from here------------
# Divide training data
label, feature = svm_read_problem('./data/scaled_training.txt')
train_label = label[0:len(label)-100]
train_feature = feature[0:len(feature)-100]
test_label = label[len(label)-100:len(label)]
test_feature = feature[len(feature)-100:len(feature)]

# Save training result
if not os.path.exists('./model/demo_model.model'):
    # Create model
    prob = svm_problem(train_label, train_feature)
    param = svm_parameter('-s 2 -t 2 -h 0') # 学习器训练参数待调整
    model = svm_train(prob, param)
    svm_save_model('./model/demo_model.model', model)
    print('成功创建模型！')
else:
    print('已经有训练好的模型，直接进行预测！')
    model = svm_load_model('./model/demo_model.model')

# Predict and check
p_label, p_acc, p_val = svm_predict(test_label, test_feature, model)
#print('---------------------')
#print('测试集正确标签：', test_label)
#print('测试集预测标签：', p_label)