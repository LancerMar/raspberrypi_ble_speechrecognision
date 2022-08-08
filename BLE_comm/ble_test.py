# dev_num1="6C:79:B8:D3:6E:BE"
# dev_num2="B0:B1:13:2D:D6:44"

from ble_device import device
from ble_comm import q_ble_sending_msg
import time
import threading


class mysend_data_ble_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # print("start receiving data from " + self.dev_name)
        send_data_ble()


def send_data_ble():
    print("@@@@@@@@@@@@@@@@@operate send_data_ble.......")
    while(True):
        time.sleep(0.1)
        if(q_ble_sending_msg.empty()):
            continue

        send_data = q_ble_sending_msg.get()
        if(send_data[2] == 0x01):
            # dev_lefthand.send(send_data)
            print("========================send data to left hand====================")
        
        if(send_data[2] == 0x02):
            print("==================send data to right hand=========================")
            dev_righthand.send(send_data)





# dev_lefthand_mac = "6C:79:B8:D3:6E:BE"

dev_righthand_mac = "B0:B1:13:2D:D6:44"
dev_ultrasonic_mac ="6C:79:B8:D3:80:56"

# dev_lefthand = device(dev_lefthand_mac,"lefthand_ble_deveice")
dev_righthand = device(dev_righthand_mac,"righthand_ble_deveice")
dev_ultrasonic = device(dev_ultrasonic_mac,"ultrasonic_ble_deveice")

# dev_lefthand.receive()
dev_righthand.receive()
dev_ultrasonic.receive()
print("receiving data ...........")
# test_send_vib_data =  bytes([0x80,0x81,0x01,0x30,0xff,0xff])
# time.sleep(3)

print("send data")
# dev_ultrasonic.send(test_send_vib_data)

t_send_ble_data = mysend_data_ble_Thread()
t_send_ble_data.start()


dev_ultrasonic.join()
t_send_ble_data.join()

# dev_lefthand.send(test_send_vib_data)

# time,sleep(3)
# dev_righthand.send(test_send_vib_data)



