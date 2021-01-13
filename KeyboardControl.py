# Manual Control of the Drone with Keyboard
# Arrow Keys for directions
# e = takeoff
# q = land
# d = right a = left
# w = up s = down
# No camera in this version

from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


