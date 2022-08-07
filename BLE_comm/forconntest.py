from ble_device import device



dev_righthand_mac = "B0:B1:13:2D:D6:44"
dev_righthand = device(dev_righthand_mac,"righthand_ble_deveice")

dev_righthand.receive()
print("receiving data ...........")