from cosna import Cosna
from time import sleep

# bt_remote_addr = "00:E0:4C:XX:XX:XX"
# replace the mac address to be the one for your the device
mac_address = "00:E0:4C:XX:XX:XX"
cos = Cosna(mac_address, True)

# Connect to device
cos.connect()

# Change color three times, with 2 seconds between
print 'changing color to blue'
cos.change_color(00,00,99)
sleep(2)
print 'changing color to green'
cos.change_color(00,99,00)
sleep(2)
print 'changing color to red'
cos.change_color(99,00,00)
sleep(2)

# Disconnecting
cos.disconnect()

print 'Test is done!'
