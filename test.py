import pygatt
from binascii import hexlify
import time

adapter = pygatt.GATTToolBackend()


def handle_data(handle, value):
    """
    handle -- integer, characteristic read handle the data was received on
    value -- bytearray, the data returned in the notification
    """
    print("Received data: %s" % hexlify(value))


try:
    adapter.start()
    device = adapter.connect("b2:3b:03:00:14:d6")

    device.subscribe("a1e8f5b1-696b-4e4c-87c6-69dfe0b0093b", callback=handle_data)

    # The subscription runs on a background thread. You must stop this main
    # thread from exiting, otherwise you will not receive any messages, and
    # the program will exit. Sleeping in a while loop like this is a simple
    # solution that won't eat up unnecessary CPU, but there are many other
    # ways to handle this in more complicated program. Multi-threaded
    # programming is outside the scope of this README.
    while True:
        time.sleep(10)
finally:
    adapter.stop()
