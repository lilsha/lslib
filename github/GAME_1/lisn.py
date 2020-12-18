import time
import threading

exitFlag = 0
class myThread (threading.Thread):
    def __init__(self ,threadID, name , counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('开始进程 %s' % (self.name))
        with open('e:\\lisha\\11.txt','a+') as f:
            while True:
                f.write(self.name+'1111111111111111111111111111111111111\r\n')
                f.write(self.name+'22222222222222222222222222222222222\r\n')
                f.truncate()
                print( self.name, self.counter, 5)
        print('退出进程%s'%(self.name))



def print_time (threadName, delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" %( threadName , time.ctime( time.time())))
        counter -=1


thread_1 = myThread(1, "Thread-1",10)
thread_2 = myThread(1, "Thread-2",20)

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print( " 退出线程 ")