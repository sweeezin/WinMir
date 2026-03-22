
default saw_photos = False

default saw_flowers = False

default saw_phone = False

label start:

    $ player_name = renpy.input("What is your name?", length=32)

    $ player_name = player_name.strip()  

    if player_name == "":

        $ player_name = "March"

    scene black with fade
    
    centered "\"This is what I like about photographs. They're proof that once, even if just for a heartbeat, everything was perfect.\""

    $ snow_on = True
    
    play music "audio/lofi1.mp3" fadein 2.0

    play music2 "audio/snowamb.mp3" 

    play audio "audio/snow_footsteps.mp3" volume 0.8

    scene bg snowpath with fade 

    "The sunlight filters through snowy branches, casting soft shadows onto the path ahead."

    "It's quiet, maybe too quiet for you."

    "During this time of year, most the animals hide, it seems as if you are the only one awake."

    "The morning air is crisp and still, you smell the faint scent of pine and snow."

    "The cold bites at your face. Snowflakes stick to your coat."

    "You can see your breath in the cold air as you walk, each step crunching on the ground."

    "You keep your eyes focused on the ground ahead, as if facing the light would blind you."

    "You drag your feet."

    scene bg windphone

    "Your eyes fall on the wind phone, a disconnected phone booth here in the woods."

    "It's an unlikely shelter here in the woods."

    "You've been returning here every winter, since you were a child."

    "Some say the phone carries on your messages on the wind, to loved ones who have passed on."

    "But truthfully, it didn't matter if the phone worked or not."

    "You found solace in the one way conversations."
    
    "The cold nips at your skin."

    "You approach the familiar weathered booth."

    "Your gloved hand reaches for the metal handle."

    stop audio #the footsteps dont stop LMAFO
    
    stop music2 fadeout 3.0

    stop music fadeout 5.0

    play sound "audio/door-open.mp3"

    scene bg boothinterior

    "It's glass walls shelter you from the wind."

    "It seems some previous visitors have left some items behind."

    jump booth_examination


label booth_examination:

    scene bg boothinterior 
    
    menu:

        "Photos" if not saw_photos:

            $ saw_photos = True

            "Printed photos of various subjects have been placed here. Sunsets, beaches, wildlife, and food. It seems whoever took these had a great understanding of photography."
            
            jump booth_examination

        "Flowers" if not saw_flowers:

            $ saw_flowers = True

            "Someone has left a bundle of flowers behind. Their petals are a soft pink. You don't recognize the species. They are a bit wilted."
            
            jump booth_examination

        "Phone" if not saw_phone:

            $ saw_phone = True

            "It feels heavy and cold. It hasn't seen a dial tone in years."

            jump booth_examination

        "Pick up the receiver" if saw_photos and saw_flowers and saw_phone:
            
            jump start_phone_call

label start_phone_call:

    "You pick up the phone and hold it up to your ear."

    "..."

    pause 2.0

    u "Hi... Dad."

    "You brush away a stray snow flake off your coat, watching it melt into the fabric."

    u "It’s been snowing the entire night. You always said the first snow was the hardest to light."

    u "Too much bounce, or whatever it was..."

    u "I moved back with Mom. She’s doing okay. She’s finally started moving your things into the spare room." 

    u "Those heavy black boxes you used to lug through airports, they’re just sitting in a stack now."

    u "I have to walk past them to get to the bathroom."

    u "Even when you're dead you take up so much space."

    "You scoff."

    u "It’s a lot of black plastic. I haven’t opened them. I told her I’d sell what we could, but I just end up staring at the latches."

    u "You gaze at the photographs and swallow thickly."

    u "It makes your skin itch." 

    u "Someone left some photographs here. I feel like the composition is a little amateur but you would probably have a better critique."

    "Your father always critiqued your work."

    "\"You have symmetry but you have no subject. The path and trees lead the eyes directly to the left center but theres nothing there.\""

    "\"Next time shoot with more exposure to increase contrast between the trees and horizon.\""

    "Back when you were younger you often got offended. It hurt your ego. You'd regret showing him at all."

    "But as you fell more and more in love with photography, you realized his knowledge was inexpendable."

    "It felt as if you couldn't improve anymore if he wasn't here. You'd never be able to reach his level of exception."

    u "Anyway, it's really cold out here, I’ll talk to you again soon, ok?"

    u "Bye."

    "You place down the phone gently."
    
    scene bg windphone   

    play music2 "audio/snowamb.mp3"

    play sound "audio/door-open.mp3"

    "You inhale as you step outside, the cold mountain air fills your lungs."

    "As you exit the booth you hear a mechanical click."

    play sound "audio/shutter.mp3"

    show cori with dissolve

    "Someone's standing there, a few steps away."

    "Unlike you, he doesn't look dressed for the cold."

    "No scarf, no gloves, no hat." 

    "There's a flash of pink from his pocket."

    "It's a flower. The same one from inside the phone booth."

    pause 2.0

    "He lowers his camera when he notices you looking."

    "Slowly, he traces your gaze."

    pause 2.0

    cori "Cyclamens."

    "You blink."

    u "Huh?"

    cori "The flowers."

    cori "I grow them in my garden, unlike other flowers, they bloom in the winter."

    "He puts his camera down, letting it hang from his neck, and steps towards you."

    cori "They're my favorite cause the leaves are heart-shaped."

    "His voice is soft against the morning ambience."

    "You glance at his camera."

    u "I assume those photographs in the booth are also yours?"

    "His eyes flicker to yours and he chuckles slightly."

    cori "I recently picked it up. They're quiet amateur aren't they? I didn't expect anyone to see them, people rarely come here it seems."

    "You pause for a moment, wondering how to respond."

    u "They're not bad." 

    "He grins."

    cori "That's generous."

    u "Photographs don't need to be good to be appreciated."

    cori "You're probably right."

    cori "They were for my sister."

    cori "She couldn't see but she loved exploration." 

    cori "We use to walk this path all the time." 

    cori "Back then I had to lead her, but we've walked this path so many times she could probably do it all by herself now."

    "His tone is casual."

    "Listening to the stranger reminisce, it feels familiar."

    u "You must miss her a lot. It sounds like she was lucky to have you as a guide."

    cori "I think it was the other way around, at that time at least."

    cori "She got annoyed with me taking so much time taking photos, but she was always so interested in what they looked like."

    cori "I'm no poet or anything but I'd try my best to describe them."

    "You shift your weight, your boots crunching loudly in the silence. It’s an awkward bit of vulnerability from a stranger."

    u "I know how that is. My dad was the same way."
    u "When I was a kid I felt like he loved the camera more than me."
    "You scoff."
    cori "Was he good at least? With the camera."
    "You gently fidget with the edge of your sleeve between your fingertips."
    "You remember watching his films and looking at his photos."
    "He wasn't just good, he was exceptional-- with storytelling, composition, and technical skill."
    "You loved his work, of course. But you also found it incredibly annoying."
    u "He was the kind of good that made you like nothing you ever made would amount to his work."
    u "I think it comes with a cost though."
    u "Sometimes it felt like it was all he ever did, like he was never in the same reality." 
    cori "They do say that no artist tolerates reality."
    cori "I actually think its the contrary, I think art is a way to cope with reality, by capturing parts of it you learn to accept reality as it is." #is this contrary??? might need to change
    u "Is that why you take photos? To make accept reality as it is?" 
    "The man grins."
    cori "Hmmm."
    cori "I guess so, in a way."
    "His answer is vague, but you don't press the issue further."
    cori "What about you?"
    u "Me?"
    u "I don't take photos anymore really, I just like looking at them. The camera is so finicky, I don't have the patience for it."
    cori "Is that so? Whens the last time you took a photo?"
    "You pause and think."
    "It was a few years ago, you were photographing for a project, a collection of photos during the blue hour."
    "A brief time before sunrise, when the sky is a deep shade of blues, violets, and purples." #expand
    "Come to think of it, what was that project for? You can't remember."
    u "It's been awhile."
    cori "How bout giving it another go now?"
    "He gestures to the camera hanging from his neck."
    "You hesistate. You really didn't have any interest of touching a camera again."
    cori "It can just be really simple, don't overthink it, just take a photo of something you find interesting."
    "You look at the camera, then back at him."
    u "I guess it couldn't hurt."
    "You take the camera from him and hold it in your hands, feeling the weight of it."
    "The cold metal feels foreign in your hands, but you find yourself drawn to it."
    "You look through the viewfinder, adjusting the settings and trying to find something interesting to take a photo of."

    jump take_photo

    default photo_trees = False
    default photo_cori = False
    default photo_flower = False

    label take_photo:
        hide cori with dissolve
        menu:
            "Look at the trees" if not photo_trees:
                $ photo_trees = True
                "Most of the trees are barren, but a few stubborn leaves cling to the branches, their colors faded but still visible against the snow."
                "From where you're standing, the sun is just peeking through the branches, creating a soft glow that illuminates the snow and casts long shadows on the ground."
                "There is a pine tree nearby, its needles a vibrant green that stands out against the white snow. The contrast between the green and white creates a striking visual effect"
                play sound "audio/shutter.mp3"

                "You take a photo of the snow-covered pine trees, the branches creating intricate patterns against the white backdrop."
                show cori with dissolve
                cori "The trees are my favorite part of this path, they look so different in every season. I love how the snow clings to the branches, it makes them look like they're made of glass."
                jump take_photo

            "Look at the man" if not photo_cori:
                $ photo_cori = True
                show cori with dissolve
                "You look at the man. The morning light casts a soft flow on his face."
                cori "You want to take a photo of me? I can't promise it'll look good, but go ahead."
                "He stands in fron of the phone booth and smiles."
                "You line up the man's figure in the viewfinder, adjusting the settings to capture the soft morning light on his face."
                play sound "audio/shutter.mp3"
                "You take a photo."
                "It seems the lens flare has blocked out his face."


                jump take_photo

            "Look at the flower" if not photo_flower:
                $ photo_flower = True
                show cori with dissolve
                "You look at the flower in his pocket, once again drawn to its vibrant pink color."
                "The man notices."
                "He takes the flower out of his pocket and holds it towards you."
                "You gently take the flower from him, his fingers are soft against yours, like a daft of air."
                play sound "audio/shutter.mp3"
                "You take a photo of the flower, the vibrant pink color contrasting against the snow."
                cori "You can have the flower, I have plenty more at home."
                jump take_photo

            "That's enough photos for now" if photo_trees and photo_cori and photo_flower:
                pass
    
    show cori with dissolve 

    cori "How interesting."
    cori "I thought I told you not to overthink it."
    cori "Or maybe you just have a strong instinct for it?"
    u "What do you mean?"
    cori "Not only do you have a good eye for composition, but it seems like with every shot you're following a theme."
    cori "The pine tree, its an evergreen tree, the kind that stays green year round, even in the harshest winters."
    cori "The photo of me next to the phone booth, an out of place shelter in a desolate location."
    cori "And lastly, the flower, its a cyclamen, a flower that only blooms in the winter, when everything else is dormant."
    cori "Even if its just a few photos, they follow a cohesive theme."
    cori "Resilience in bleak settings."
    "You pause for a moment, taking in his words."
    "Was that really what you were trying to do?"
    "His eyes scan yours."
    cori "What do you think?"
    u "I think... your camera has a mind of its own and it has possesed me."
    "He laughs."
    cori "So humble."
    "You loop the camera strap off your neck and around your wrist and hand it back to him."
    u "Thanks uhhh, I don't even know your name."
    $ coriname = "Cori"
    $ cori.name = coriname    
    cori "I'm Cori."
    u "Cori, thanks for letting me use your camera. I'm [player_name]."
    cori "It was my pleasure, [player_name]. I hope you continue to take photos, you have a real talent for it."

    u "I shouldn't keep you here any longer, I'm sure someone is waiting for your call."
    cori "Alright then, I'll see you again, soon."


    scene bg snowpath
    
    "You look down at the cyclamen in your hand, its petals a defiant pink against the grey morning scene."
    "It won't last forever, but you know the next winter its kin will bloom again, with the same resilient shade of pink."

    jump day2