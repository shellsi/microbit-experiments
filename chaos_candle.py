from microbit import * 
import math

def wick(r):
    display.clear()
    for i in range(0,4):
        display.set_pixel(0, i, 1 if r > i else 0)
        display.set_pixel(i, 4, 1 if r - int(r) > i*0.2 else 0)

t = 0
r = 4.0
x = 0.1
steps = 10
while r > 0:
    next_x = r * x * (1.0 - x)
    dx = (next_x - x) / steps
    for i in range(0, steps):
        #pin2.write_analog(math.sin(t) * 300 + 700) # 1023 is max.  Yellow LED ok with this.
        pin0.write_analog((x + i*dx) * 1023) # 1023 is max.  Yellow LED ok with this.
        if button_b.was_pressed():
            r += 0.1
            display.scroll(r, wait=False)
        if button_a.was_pressed():
            r -= 0.1
            display.scroll(r, wait=False)
        sleep(6)
    t = t+1 % 360
    x = next_x
    r -= 0.001
    wick(r)
    