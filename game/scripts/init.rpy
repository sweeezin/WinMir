
init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/blip.wav", loop=True)
            
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()


define narrator = Character(None, callback=type_sound)
define cori = Character("Cori", callback=type_sound)
define u = Character("You", callback=type_sound)

default preferences.text_cps = 100
image bg snowpath = "images/bg/snowpath.png"
image bg windphone = "images/bg/windphone.png"
image bg boothinterior = "images/bg/boothinterior.png"

image snow1 = Snow("gui/snow1.png", 40, 50, 30, (20,50), (100,200))
image snow2 = Snow("gui/snow2.png", 40, 50, 30, (20,50), (100,200))

