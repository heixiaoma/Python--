# coding=utf-8
'''''
by 黑小马
demo，学习或者下次项目遇见即可复制代码
主要是对锁概念举例子
'''
import threading
#共用数据
my_list=[]
#创建锁
gLock=threading.Lock()
def 生产者():
    for x in range(10):
        #开启锁
        gLock.acquire()
        my_list.append(x)
        #释放锁
        gLock.release()
def 消费者():
    while True:
        # 开启锁
        gLock.acquire()
        if len(my_list)>0:
            print(my_list.pop())
        else:
            continue
        # 释放锁
        gLock.release()
def main():
    #2个生产者线程
    for x in range(2):
        th=threading.Thread(target=生产者)
        th.start()
    #3个消费者线程
    for x in range(3):
        th=threading.Thread(target=消费者)
        th.start()

if __name__ == '__main__':
    main()