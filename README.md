# Cosna-LED module

![Cosna Bluetooth LED](https://www.harald-nyborg.dk/media/images/145/3818_248586.jpg)

I was out shopping on day and found this strange device. So I bought it with the goal to see if I could reverse engeneer it. 
By looking at the android application that belongs to the LED, I figured out how the protocol for changing its color works, and have made this python implementation for my own and others usage.

## Working
* Connecting/Disconnecting
* Changing color

## To-do
* Implement different effects

# Setup
This implementation is for Python 2.7 - It is build on a Debian based system.

## Install dependencies
```Debian/Ubuntu
sudo apt-get update
sudo apt-get install libbluetooth-dev python-dev python-pip
```

```python
pip install PyBluez
```

# Usage
Import the module, then create an instance of the Cosna object with the MAC-address for your Cosna-LED as a parameter. Then you can connect, change color and disconnect agian as follows:
```python
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

```
