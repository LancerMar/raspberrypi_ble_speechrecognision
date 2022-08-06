# dev_num1="6C:79:B8:D3:6E:BE"
# dev_num2="B0:B1:13:2D:D6:44"

from ble_device import device
import time


dev_lefthand_mac = "6C:79:B8:D3:6E:BE"
dev_righthand_mac = "B0:B1:13:2D:D6:44"

dev_lefthand = device(dev_lefthand_mac,"lefthand_ble_deveice")
dev_righthand = device(dev_righthand_mac,"righthand_ble_deveice")

dev_lefthand.receive()
dev_righthand.receive()

test_send_vib_data =  bytes([0x80,0x81,0x01,0x30,0xff,0xff])
time.sleep(3)



dev_lefthand.send(test_send_vib_data)

time,sleep(3)
dev_righthand.send(test_send_vib_data)



