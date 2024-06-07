from machine import *
start = Pin(18, Pin.OUT) #motor enable drive select
start.value(1)
dirsel = Pin(26,Pin.OUT)
dirsel.value(1)
hstep = Pin(28,Pin.OUT)
hstep.value(1)