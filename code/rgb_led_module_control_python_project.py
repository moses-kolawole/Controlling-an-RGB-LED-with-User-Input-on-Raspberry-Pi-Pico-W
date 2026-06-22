from machine import Pin, PWM
from time import sleep
redpin = 13
greenpin = 14
bluepin = 15
redled = PWM(Pin(redpin))
greenled = PWM(Pin(greenpin))
blueled = PWM(Pin(bluepin))

redled.freq(1000)
redled.duty_u16(0)

greenled.freq(1000)
greenled.duty_u16(0)

blueled.freq(1000)
blueled.duty_u16(0)

while True:
    print('Good day, Here are the list of colours available for this project/n')
    print('1. Red')
    print('2. Green')
    print('3. Blue')
    print('4. White')
    print('5. pink')
    
    mycolor = input('What color do you want?: ').strip()
    if mycolor.lower() == 'red':
        redbright = 65550
        greenbright = 0
        bluebright = 0
        redled.duty_u16(redbright)
        greenled.duty_u16(greenbright)
        blueled.duty_u16(bluebright)
        
    elif ( mycolor.lower() == 'green' ):
        redbright = 0
        greenbright = 65550
        bluebright = 0
        redled.duty_u16(redbright)
        greenled.duty_u16(greenbright)
        blueled.duty_u16(bluebright)
        
    elif ( mycolor.lower() == 'blue' ):
        redbright = 0
        greenbright = 0
        bluebright = 65550
        redled.duty_u16(redbright)
        greenled.duty_u16(greenbright)
        blueled.duty_u16(bluebright)
        
    elif ( mycolor.lower() == 'white' ):
        redbright = 65550
        greenbright = 65550
        bluebright = 65550
        redled.duty_u16(redbright)
        greenled.duty_u16(greenbright)
        blueled.duty_u16(bluebright)
        
    elif ( mycolor.lower() == 'pink' ):
        redbright = 65535
        greenbright = 49344
        bluebright = 52171
        redled.duty_u16(redbright)
        greenled.duty_u16(greenbright)
        blueled.duty_u16(bluebright)
        
    else:
        redbright = 65535
        greenbright = 55255
        bluebright = 0
        redled.duty_u16(redbright)
        greenled.duty_u16(greenbright)
        blueled.duty_u16(bluebright)