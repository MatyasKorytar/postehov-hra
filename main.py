pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
random = randint(3000, 10000)
is_pin1 = input.pin_is_pressed(TouchPin.P1)
is_pin2 = input.pin_is_pressed(TouchPin.P2)

def on_forever():
        is_pin1 = input.pin_is_pressed(TouchPin.P1)
        is_pin2 = input.pin_is_pressed(TouchPin.P2)
        basic.pause(random)
        basic.show_leds("""
        . . . . .
        # # # # #
        # . . . #
        # # # # #
        . . . . . """)
        music.play_tone(Note.FSHARP, music.beat(1500))
     
        is_pin1 = input.pin_is_pressed(TouchPin.P1)
        is_pin2 = input.pin_is_pressed(TouchPin.P2)

        console.log_value("p1", is_pin1)

        if is_pin1 and is_pin2 == True:
             basic.show_leds("""
            . # # # .
            . # . . #
            . # # # .
            . # . # .
            . # . . #
            """)
        if is_pin1 == True:
            basic.show_number(1)
        if is_pin2 == True:
            basic.show_number(2)


        
        


basic.forever(on_forever)