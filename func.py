import os
import math

# Data converter
'''将数据转化成libsvm使用的格式'''
def dataConvert(file):
    print('Converting...')
    with open('./data/'+file, 'r') as f:
        for line in f.readlines():
            edited_line = line.replace('\n','').split()
            edited_line.insert(0, edited_line.pop())
            for each in range(1, 7):
                t = str(each) + ':' + edited_line[each]
                edited_line[each] = t
            with open('./data/formatted_training.txt', 'a') as nf:
                new_line = ' '.join(edited_line)
                nf.write(new_line + '\n')
    print('Done!')

# 数据分组器，将学习数据按照比例分为训练数据和检验数据
def dataDivide(label, feature, train_size):
    train_label = label[0:math.ceil(len(label)*train_size)]
    train_feature = feature[0:math.ceil(len(feature)*train_size)]
    test_label = label[math.ceil(len(label)*train_size):len(label)]
    test_feature = feature[math.ceil(len(feature)*train_size):len(feature)]
    return train_label, train_feature, test_label, test_feature