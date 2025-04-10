from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time, sys


board = CustomTelemetrix()
RED_PIN = 4
GREEN_PIN = 5
SCREEN=11
BUTTON= 8
BUZZER=3
POTPIN = 0 
MAX_ANGLE = 270 # degrees- will count as seconds

value = 0

def PotChanged(data):
    global value
    value = data[2]

def setup():
    global board
    board.set_pin_mode_digital_input_pullup(BUTTON)
    board.set_pin_mode_digital_input(RED_PIN)
    board.set_pin_mode_digital_input(GREEN_PIN)
    board.set_pin_mode_digital_output(BUZZER)
    board.set_pin_mode_analog_input(POTPIN, callback=PotChanged, differential=10)
    time.sleep(0.1)


def loop(on):
    #set timer with the potentiometer on arduino
    #max 90 seconds
    timer = value * MAX_ANGLE/1023.0/3 
    board.displayShow(int(timer))

    pressed= board.digital_read(BUTTON)
    
    if pressed[0]== 0 and on==False: #check if the button is pressed and proceed
        on=True
        board.digital_write(GREEN_PIN,0)
        board.digital_write(RED_PIN,1)
        
        #countdown
        while int(timer)>=0:

            board.displayShow(int(timer))
            timer=int(timer)-1
            time.sleep(1)

        #buzz when the pizza is ready
        board.analog_write(BUZZER, 128) 
        time.sleep(1)
        board.analog_write(BUZZER, 0)

        
        board.displayShow("donE")
        board.digital_write(RED_PIN,0)
        board.digital_write(GREEN_PIN,1)
        time.sleep(2)
        board.displayShow("")
        time.sleep(2)


setup()

on=False

while True:
    try:
        loop(on)
        time.sleep(0.1)
    except KeyboardInterrupt:
        print('shutdown')
        board.shutdown()
        sys.exit(0)

