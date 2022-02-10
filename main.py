pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
x = False
y = False
console.log_value("p1", pins.analog_read_pin(AnalogPin.P1))

def on_pin_pressed_p1():
        x = True
        input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_pin_pressed_p2():
        y = True
        input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

random = randint(3000, 10000)

start = False

def on_forever():
    def run_parallel():
        if start == False:
            if x == True:
                basic.show_leds("""
                . # # . .
                . # . # .
                . # # . .
                . # . # .
                . # # . .
                """)
            if y == True:
                basic.show_leds("""
                . . . . .
                . . # . .
                . # . # .
                # # # # #
                # . . . #
                """)
            if x and y == True:
                basic.show_leds("""
                . . # # .
                . # . . .
                # . . . .
                . # . . .
                . . # # .
                """)
    control.in_background(run_parallel)
    basic.pause(random)
    start = True
    basic.show_leds("""
        . . . . .
        # # # # #
        # . . . #
        # # # # #
        . . . . . """)
    music.play_tone(Note.FSHARP, music.beat(1500))
    
    if x and y == True:
            basic.show_leds("""
            . # # # .
            . # . . #
            . # # # .
            . # . # .
            . # . . #
            """)
            
    if x == True:
                basic.show_number(1)
    if y == True:
            basic.show_number(2)
         

        
        


basic.forever(on_forever)