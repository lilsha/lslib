#author:lls time:2020-11-08
import pypinyin
import random
import time
list('我的小棉袄')

import random
b=[1,2,3,4,5,6,7,8]
random.shuffle(b)
print(b)

#文档中读取一行内容形成列表，并删除重复的元素
with open('C:\\Users\\THINK\\Desktop\\read.txt','r',encoding='utf-8') as fr:
    aList=list( fr.readline() )
    print('1',aList)
    #删除重复的元素
    bList=sorted(set(aList), key = aList.index)
for i in range(len(bList)-3):
    #列表随机重新排列
    random.shuffle(bList)
    new3Py = [pypinyin.pinyin(bList[0])[0][0]]
    getWord = bList[0]
    #print(i,'次 bList',len(bList),'',bList[0])
    #删除第一个元素
    del bList[0]
    #获取除第一个元素之外的随机3个元素，并形成列表，随机排列
    new3 = random.sample(bList, 3)
    for arg in new3:
        new3Py.append( pypinyin.pinyin( arg )[0][0] )
    random.shuffle(new3Py)
    new3Py.append(getWord)
    print(i,'次new3Py', new3Py)
    time.sleep(1)
