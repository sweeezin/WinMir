
init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/blip.wav", loop=True)
            
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    renpy.music.register_channel("music2", "music", loop=True)


define narrator = Character(None, callback=type_sound)
define cori = Character("???", callback=type_sound)
define u = Character("You", callback=type_sound)

default preferences.text_cps = 100
image bg snowpath = "images/bg/snowpath.png"
image bg windphone = "images/bg/windphone.png"
image bg boothinterior = "images/bg/boothinterior.png"


