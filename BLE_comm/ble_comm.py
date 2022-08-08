from bluepy import btle
import threading
import time
import struct
import queue

import sys
sys.path.append('../Audio_sys')

from textToSpeeh import speek

# "6C:79:B8:D3:6E:BE"
q_ble_sending_msg = queue.Queue()

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
        Proc_data(data)


def receive_data(dev):
    while(True):
    #     # handleNotification() was called
        dev.waitForNotifications(1.0)
        print("waiting...")

def Proc_data(data):
    print("the received data : ")
    print(data)
    if(7 == len(data)):

        obstacle_alert = "Obstacle"
        obstacle_direction = ""
        obstacle_distance = ""
        data_send_ble = bytearray([0x80,0x81,0xef,0xef,0xff,0xff])

        # print("len:"+str(len(data)))
        data_unpack = struct.unpack('7B',data)
        # print(data_unpack)
        if(data_unpack[0] == 0x80 
        and data_unpack[1] == 0x82
        and data_unpack[5] == 0xef
        and data_unpack[6] == 0xef):
            print("data package completed")

        if(data_unpack[4] == 0x0a):
            print("within 300 centimeter")
            obstacle_distance = " within 300 centimeter"
            data_send_ble[3] = 0x33

        elif(data_unpack[4] == 0x0b):
            print("within 300 centimeter to 500 centimeter")
            obstacle_distance = " within 300 centimeter to 500 centimeter"
            data_send_ble[3] = 0x32

        elif(data_unpack[4] == 0x0c):
            print("within 500 centimeter to 1000 centimeter")
            obstacle_distance = " within 500 centimeter to 1000 centimeter"
            data_send_ble[3] = 0x31

        elif(data_unpack[4] ==0x0d):
            print("over 1000 centimeter")
            obstacle_distance = " over 1000 centimeter"
            data_send_ble[3] = 0x30
        else: 
            print("wrong package!")
            return

        if(data_unpack[3] == 0x00):
            print("above")
            obstacle_direction = " above"
        elif(data_unpack[3] == 0x01):
            print("below")
            obstacle_direction = " below"
        elif(data_unpack[3] == 0x02):
            print("left")
            obstacle_direction = " left"
            data_send_ble[2] = 0x01
            q_ble_sending_msg.put(data_send_ble)
        elif(data_unpack[3] == 0x03):
            print("right")
            obstacle_direction = " right"
            data_send_ble[2] = 0x02
            q_ble_sending_msg.put(data_send_ble)
        else:
            print("wrong package!")
            return

        obstacle_alert = obstacle_alert + obstacle_distance + obstacle_direction
        print(obstacle_alert)
        
        speek(obstacle_alert)

        
        # if(data_unpack[0] == 0x80):
        #     print("data0 check\r\n")

        # if(data_unpack[1] == 0x82):
        #     print("data1 check\r\n")

        # if(data_unpack[2] == 0x01):
        #     print("data2 check\r\n")

        # if(data_unpack[3] == 0x00):
        #     print("data3 check\r\n")

        # if(data_unpack[4] == 0x0a):
        #     print("data4 check\r\n")

        # if(data_unpack[5] == 0xef):
        #     print("data5 check\r\n")

        # if(data_unpack[6] == 0xef):
        #     print("data6 check\r\n")
    



# dev_num1="6C:79:B8:D3:6E:BE"
# dev_num2="B0:B1:13:2D:D6:44"
# dev=btle.Peripheral(dev_num1).withDelegate(MyDelegate(dev_num1))  
# dev2=btle.Peripheral(dev_num2).withDelegate(MyDelegate(dev_num2))  
# # dev.connect() 


# dev_serice = dev.getServiceByUUID("dfb0")
# dev_ch = dev_serice.getCharacteristics("dfb1")[0]

# dev_serice2 = dev2.getServiceByUUID("dfb0")
# dev_ch2 = dev_serice2.getCharacteristics("dfb1")[0]



# thread_test = myThread(dev,"test001")
# thread_test.start()
# thread_test2 = myThread(dev2,"test002")
# thread_test2.start()

# time.sleep(5)

# data = bytes([0x80,0x81,0x01,0x30,0xff,0xff])
# dev_ch.write(data)

# time.sleep(2)

# dev_ch2.write(data)

# thread_test.join()
# thread_test2.join()

