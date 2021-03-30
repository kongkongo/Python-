import threading
import time

exitFlag=0

class myThread(threading.Thread):   #继承父类threading.Thread
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    
    def run(self):
        # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
    #    否则超时后将返回False
        print("Starting "+self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        #释放锁
        # print("Exiting "+self.name)
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        # if exitFlag:
        #     (threading.Thread).exit()
        time.sleep(delay)
        print("%s:%s "%(threadName,time.ctime(time.time())))
        counter-=1

if  __name__=="__main__":


    threadLock=threading.Lock()
    threads=[]

    # 创建新线程
    thread1=myThread(1,"Thread-1",1)
    thread2=myThread(2,"Thread-2",2)

    # 开启线程
    thread1.start()
    thread2.start()

    #添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    #等待所有线程完成
    for t in threads:
        t.join()
        print ("Exiting Main Thread")




