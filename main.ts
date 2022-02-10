pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let x = false
let y = false
console.logValue("p1", pins.analogReadPin(AnalogPin.P1))
let random = randint(3000, 10000)
let start = false
basic.forever(function on_forever() {
    let start: boolean;
    control.inBackground(function run_parallel() {
        if (start == false) {
            if (x == true) {
                basic.showLeds(`
                . # # . .
                . # . # .
                . # # . .
                . # . # .
                . # # . .
                `)
            }
            
            if (y == true) {
                basic.showLeds(`
                . . . . .
                . . # . .
                . # . # .
                # # # # #
                # . . . #
                `)
            }
            
            if (x && y == true) {
                basic.showLeds(`
                . . # # .
                . # . . .
                # . . . .
                . # . . .
                . . # # .
                `)
            }
            
        }
        
    })
    basic.pause(random)
    start = true
    basic.showLeds(`
        . . . . .
        # # # # #
        # . . . #
        # # # # #
        . . . . . `)
    music.playTone(Note.FSharp, music.beat(1500))
    if (x && y == true) {
        basic.showLeds(`
            . # # # .
            . # . . #
            . # # # .
            . # . # .
            . # . . #
            `)
    }
    
    if (x == true) {
        basic.showNumber(1)
    }
    
    if (y == true) {
        basic.showNumber(2)
    }
    
})
