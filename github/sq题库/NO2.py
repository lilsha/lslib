#author:lls time:2020-11-22
#!/usr/bin/python3

def reverse(l):
    #方式原来序列发生改变
    b = [i for i in l]
    b.reverse()
    return b


print(reverse([1,2,3,4,5,6,7,8]) )
