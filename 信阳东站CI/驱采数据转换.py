# 先驱动后采集
from xml.dom.minidom import parse
import xml.dom.minidom

class IOTransform(object):
    def __init__(self) -> None:
        with open('CBI继电器配置_信阳东.txt', 'wt') as self._out_file:
            self.write_relays('OutputIO.xml', False)
            self.write_relays('InputIO.xml', True)

    def write_relays(self, file_name:str, is_input:bool) -> None:
        dom = xml.dom.minidom.parse(file_name)
        collection = dom.documentElement
        relays = collection.getElementsByTagName('RelayModel')
        for relay in relays:
            self.write_relay(relay, is_input)

    def write_relay(self, relay, is_input):
        device_name = relay.getAttribute('DeviceName')
        relay_name = self.get_relay_name(relay)
        type_name = 'DI' if is_input else 'SDO'
        self._out_file.write(f'{device_name}-{relay_name}-{type_name}\n')

    def get_relay_name(self, relay):
        relay_name = relay.getAttribute('Name')

        if relay_name == 'GJ':
            return 'GJQ'
        
        if relay_name == 'DGJ':
            return 'DGJQ'

        return relay_name

if __name__ == '__main__':
    IOTransform()