pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let random = randint(3000, 10000)
let is_pin1 = input.pinIsPressed(TouchPin.P1)
let is_pin2 = input.pinIsPressed(TouchPin.P2)
basic.forever(function on_forever() {
    let is_pin1 = input.pinIsPressed(TouchPin.P1)
    let is_pin2 = input.pinIsPressed(TouchPin.P2)
    basic.pause(random)
    basic.showLeds(`
        . . . . .
        # # # # #
        # . . . #
        # # # # #
        . . . . . `)
    music.playTone(Note.FSharp, music.beat(1500))
    is_pin1 = input.pinIsPressed(TouchPin.P1)
    is_pin2 = input.pinIsPressed(TouchPin.P2)
    console.logValue("p1", is_pin1)
    if (is_pin1 && is_pin2 == true) {
        basic.showLeds(`
            . # # # .
            . # . . #
            . # # # .
            . # . # .
            . # . . #
            `)
    }
    
    if (is_pin1 == true) {
        basic.showNumber(1)
    }
    
    if (is_pin2 == true) {
        basic.showNumber(2)
    }
    
})
