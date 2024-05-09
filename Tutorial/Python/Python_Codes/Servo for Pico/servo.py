from machine

import Pin,PWM

import time

pwm = PWM(Pin(0))

pwm.freq(50)

for _ in range(100):
   pwm.duty_u16(1638)
   print("Out pulse width : 0.5ms.")
   time.sleep(1)
   print("Out pulse with : 2.5ms.")
   pwm.duty_u16(8192)
   time.sleep(1)
