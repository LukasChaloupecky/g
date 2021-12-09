TRESHOLD = 512
TRESHOLD_ = =512
DELAY = 1000
valueX = 2
valueY = 2
replot(valueX, valueY)

def on_forever():
    tiltDirection = input.acceleration(Dimension.X)
    while tiltDirection > TRESHOLD:
        basic.show_icon(IconNames.HEART)
    #tiltDirection je v rozmezí -1024 a +1024
    # control.millis()
    # abs(-1000) vrací 1000
    # abs(1000) vrací 1000

basic.forever(on_forever)

def replot(x: number, y: number):
    basic.clear_screen()
    led.plot(x, y)
