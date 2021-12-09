let TRESHOLD = 512
let DELAY = 1000
let valueX = 2
let valueY = 2
replot(valueX, valueY)
// tiltDirection je v rozmezí -1024 a +1024
//  control.millis()
//  abs(-1000) vrací 1000
//  abs(1000) vrací 1000
basic.forever(function on_forever() {
    let tiltDirection = input.acceleration(Dimension.X)
})
function replot(x: number, y: number) {
    basic.clearScreen()
    led.plot(x, y)
}

