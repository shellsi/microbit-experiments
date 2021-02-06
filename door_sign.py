from microbit import *
import radio

radio.on()
radio.config(channel=33)
radio.config(power=7)

images = ['YES', 'SQUARE', 'HAPPY', 'SAD', 'MEH', 'HEART', 'ANGRY','MUSIC_QUAVERS']
index = 0

while True:
    incoming = radio.receive()
    if incoming is not None:
        if(hasattr(Image, incoming)): 
            display.show(getattr(Image, incoming))
            pin1.write_analog(0)
        else:
            display.scroll(incoming, loop=True, wait=False)
            pin1.write_analog(255)
        
    sleep(300)
    
    if(button_b.was_pressed()):
        display.show(getattr(Image, images[index]))
        display.show('?')
        radio.send('?')
        sleep(100)
        radio.send('?')

        
    if(button_a.was_pressed()):
        pin1.write_analog(0)
        index += 1
        index = index % len(images)
        display.show(getattr(Image, images[index]))
        radio.send(images[index])
        sleep(100)
        radio.send(images[index])