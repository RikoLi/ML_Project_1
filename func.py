import os
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
