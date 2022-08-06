from bluepy import btle
from ble_comm import myThread
from ble_comm import MyDelegate

class device:
    def __init__(self,mac,name):
        self.mac = mac
        self.name = name

        self.dev=btle.Peripheral(self.mac).withDelegate(MyDelegate(self.mac))
        self.dev_serice = self.dev.getServiceByUUID("dfb0")
        self.dev_ch = self.dev_serice.getCharacteristics("dfb1")[0]

    def receive(self):
        self.thread_receive = myThread(dev,self.name)
        self.thread_receive.start()
        self.thread_receive.join()

    def send(self,data):
        self.dev_ch.write(data)

    def exit(self):
        self.thread_receive.exit()
