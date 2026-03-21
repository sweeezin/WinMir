
init python:
    #renpy.music.register_channel("typing",, loop=True)
    
    config.overlay_screens.append("snow_overlay")

define narrator = Character(None, callback=text_sounds)
define cori = Character("Cori", callback=text_sounds)
define u = Character("You", callback=text_sounds)
define cs = Character("Girl", callback=text_sounds)
define d = Character("Dad", callback=text_sounds)

default preferences.text_cps = 20
image bg snowpath = "images/bg/snowpath.png"
image bg windphone = "images/bg/windphone.png"
image bg boothinterior = "images/bg/boothinterior.png"


default snow_on = False

screen snow_overlay():
    if snow_on:
        add "snow"


