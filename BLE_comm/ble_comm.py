from bluepy import btle
import threading
import time

# "6C:79:B8:D3:6E:BE"

class myThread(threading.Thread):
    def __init__(self, dev_ble,dev_name):
        threading.Thread.__init__(self)
        self.dev_ble = dev_ble
        self.dev_name = dev_name

    def run(self):
        print("start receiving data from " + self.dev_name)
        receive_data(self.dev_ble)

class MyDelegate(btle.DefaultDelegate):
    def __init__(self,params):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self,cHandle,data):
        # data_decoded = data.decode('utf-8')
        print("notify from"+str(cHandle)+" : "+str(data))


def receive_data(dev):
    while(True):
    # if 
    #     # handleNotification() was called
    #     continue
        dev.waitForNotifications(1.0)
        print("waiting...")

dev_num1="6C:79:B8:D3:6E:BE"
dev_num2="B0:B1:13:2D:D6:44"
dev=btle.Peripheral(dev_num1).withDelegate(MyDelegate(dev_num1))  
dev2=btle.Peripheral(dev_num2).withDelegate(MyDelegate(dev_num2))  
# dev.connect() 


dev_serice = dev.getServiceByUUID("dfb0")
dev_ch = dev_serice.getCharacteristics("dfb1")[0]

dev_serice2 = dev2.getServiceByUUID("dfb0")
dev_ch2 = dev_serice2.getCharacteristics("dfb1")[0]



thread_test = myThread(dev,"test001")
thread_test.start()
thread_test2 = myThread(dev2,"test002")
thread_test2.start()

time.sleep(5)

data = bytes([0x80,0x81,0x01,0x30,0xff,0xff])
dev_ch.write(data)

time.sleep(2)

dev_ch2.write(data)

thread_test.join()
thread_test2.join()

