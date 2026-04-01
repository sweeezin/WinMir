
init python:
    renpy.music.register_channel("typing", "sound", loop=True)

    config.overlay_screens.append("snow_overlay")

    
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/bleep018.ogg", channel="typing", loop=True)
            
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="typing")

    renpy.music.register_channel("music2", "music", loop=True)


default coriname = "???"
default player_name = "March"
define narrator = Character(None, callback=type_sound)
define cori = Character("Cori", callback=type_sound)
define u = Character("You", callback=type_sound)
define cs = Character("Girl", callback=type_sound)
define d = Character("Dad", callback=type_sound)
define m = Character("Mom", callback=type_sound)

default snow_on = False

screen snow_overlay():
    if snow_on:
        add "snow"


default preferences.text_cps = 35



