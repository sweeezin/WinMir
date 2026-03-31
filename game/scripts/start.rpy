

default saw_photos = False

default saw_flowers = False

default saw_phone = False

label start:

    $ player_name = renpy.input("Your name?", length=32)

    $ player_name = player_name.strip()  

    if player_name == "":

        $ player_name = "March"

    scene black with fade
    
    centered "The first snowfall of every year is different."

    centered "Some years, its light and fluffly, other years its heavy and wet."

    centered "You'd think they blur together."

    centered "But I remeber them all."
    
    centered "Except for one."

    $ snow_on = True
    
    play music "audio/lofi1.mp3" fadein 2.0 volume 0.7

    play music2 "audio/snowamb.mp3" 

    play audio "audio/snow_footsteps.mp3" volume 0.8

    scene bg snowpath with fade 

    "The sunlight filters through snowy branches, casting soft shadows onto the path ahead."

    "During this time of year, most the animals hide, it seems as if you are the only one awake."

    "The morning air is crisp and still, you smell the faint scent of pine and snow."

    "It's quiet, maybe too quiet for you."

    "The cold bites at your face. Snowflakes stick to your coat."

    "You can see your breath in the cold air as you walk, each step crunching on the ground."

    "You keep your eyes focused on the ground ahead, as if facing the light would blind you."

    scene bg windphone

    "Your eyes fall on the wind phone, a disconnected phone booth here in the woods."

    "It's an unlikely shelter here in the woods."

    "You've been returning here every winter, since you were a child."

    "However, these past couple of years you had a reason to pick up the phone."

    "Some say the phone carries on your messages on the wind, to loved ones who have passed on."

    "But truthfully, it didn't matter if the phone worked or not."

    "You found solace in the one way conversations."
    
    "The cold nips at your skin."

    "You approach the familiar weathered booth."

    "Your gloved hand reaches for the metal handle."

    "It's colder than you expect."

    stop audio 
    
    stop music2 fadeout 3.0

    stop music fadeout 5.0

    play sound "audio/door-open.mp3"

    scene bg boothinterior

    $ snow_on = False

    "It's glass walls shelter you from the wind."

    "The sun casts through the grided windows."

    "It's a bit warmer inside."

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

    "... "

    pause 2.0

    u "Hi... Dad."

    "You brush away a stray snow flake off your coat, watching it melt into the fabric."

    u "It’s been snowing the entire night. You always said the first snow was the hardest to light."

    u "Too much bounce, or whatever it was..."

    u "I moved back with Mom. She’s doing okay. She’s finally started moving your things into the spare room." 

    u "Those heavy black boxes you used to lug through airports, they’re just sitting in a stack now."

    u "I have to walk past them to get to the bathroom."

    u "Even when you're not here you take up so much space."

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

    $ snow = True

    play music "audio/lofi1.mp3" fadein 3.0

    play music2 "audio/snowamb.mp3" fadein 3.0

    play sound "audio/door-open.mp3"

    "You inhale as you step outside, the cold mountain air fills your lungs."

    "You hear a mechanical click."

    play sound "audio/shutter.mp3"

    show coripose1 light flowers side neutral with dissolve

    "Someone's standing there, a few strides away."

    "Unlike you, he doesn't look dressed for the cold."

    "No scarf, no gloves, no hat." 

    "He seems to be taking photos."

    pause 1.0

    play sound "audio/shutter.mp3"

    cori "... Too much stray light..."

    "He mutters to himself. His expression is focused."

    pause 1.0

    u "If you use a lens hood it should help with that."

    "The words leave your mouth before you could stop yourself."

    "The stranger turns to you, surprised by your presence."

    cori "Oh uhh, thanks, that's good advice actually."

    u "Yea... the snow tends to reflect a lot of light, so it can be hard to get the right exposure without a lens hood."

    cori "Wow, I've never thought of that."

    "Your eyes are drawn to a pink hue from his pocket."

    "It's a flower. The same one from inside the phone booth."

    pause 2.0

    show coripose1 direct raised

    "Slowly, he traces your gaze."

    pause 2.0

    show coripose1 open

    cori "Oh,"
    cori "they're called cyclamens."

    show coripose1 neutral

    "You blink."

    show coripose1 open

    cori "The flowers."

    cori "I grow them in my garden"
    
    cori "Unlike other flowers, they bloom in the winter."

    show coripose1 neutral

    "He steps towards you, closing the distance between you."

    show coripose1 open

    cori "They're my favorite cause the leaves are heart-shaped."

    show coripose1 closedsmile

    "His voice is soft against the morning ambience."

    "You glance at his camera."

    u "I assume those photographs in the booth are also yours?"

    show coripose1 teethsmile

    "His eyes flicker to yours and he grins."

    show coripose1 worried open

    cori "They're quite amateur aren't they? I didn't expect anyone to see them, people rarely come here, it seems."

    show coripose1 closedsmile

    "You pause for a moment, wondering how to respond."

    u "They're not bad." 

    show coripose1 raised teethsmile

    "He grins."

    show coripose1 open

    cori "That's generous."

    show coripose1 neutral

    u "Photos don't need to be good to be appreciated."

    show coripose1 side open

    pause 1.0

    cori "Yea... You're probably right."

    cori "They're for my sister."

    cori "She couldn't see but she loved exploration." 

    cori "We use to walk this path all the time." 

    cori "Back then I had to lead her, but we've walked this path so many times she could probably do it all by herself now."

    show coripose1 neutral

    "His tone is casual."

    "Listening to the stranger reminisce, it feels familiar."

    u "You must miss her a lot. It sounds like she was lucky to have you as a guide."
    
    show coripose1 direct open

    cori "I think it was the other way around, at that time at least."

    cori "She got annoyed with me taking so much time taking photos, but she was always so interested in what they looked like."

    cori "I'm no poet or anything but I'd try my best to describe them."

    show coripose1 neutral

    "You shift your weight, your boots crunching loudly in the silence. It’s an awkward bit of vulnerability from a stranger."

    u "I know how that is. My dad was the same way."

    u "When I was a kid I felt like he loved the camera more than me."

    "You scoff."

    show coripose1 worried open

    cori "Was he good at least? With the camera."

    show coripose1 closedsmile

    "You gently fidget with the edge of your sleeve between your fingertips."

    "You remember watching his films and looking at his photos."

    "He wasn't just good, he was exceptional- with storytelling, composition, and technical skill."

    "You loved his work, of course. But you also found it incredibly frustrating."

    "He made it look so effortless."

    u "He was alright."

    u "He did it for work."

    u "Sometimes it felt like it was all he ever did, like he was never in the same reality." 

    "The man listens intently."

    show coripose1 open

    cori "They do say that no artist tolerates reality."

    cori "I actually think its the contrary, I think art is a way to cope with reality, by capturing parts of it you learn to accept reality as it is." #is this contrary??? might need to change
    
    show coripose1 neutral

    "You glance at him, surprised by his response."

    "You think for a bit."

    u "Is that why you take photos? To accept reality as it is?" 

    show coripose1 side

    "The man grins."

    cori "Hmmm."

    show coripose1 open

    cori "Something like that."

    show coripose1 closedsmile

    "His answer is vague, but you don't press the issue further."

    pause 1.0

    show coripose1 direct raised open

    cori "What about you? Do you take photos?"

    show coripose1 neutral

    u "Me?"

    u "No not really anymore, I just like looking at them. The camera is so finicky, I don't have the patience for it."

    show coripose1 open

    "He looks at you with curiosity."

    cori "Is that so? Whens the last time you took a photo?"

    show coripose1 neutral side

    "You pause and think."

    "It was a few years ago, you were photographing for a project, a collection of photos during the blue hour."

    "A brief time before sunrise, when the sky is a deep shade of blues, violets, and purples."

    "Come to think of it, what was that project for? You can't remember."

    u "It's been awhile."
    
    show coripose1 direct teethsmile

    "He cracks a smile"

    cori "How bout giving it another go now?"

    show coripose1 side closedsmile

    "He gestures to the camera hanging from his neck."

    "You hesistate. You really didn't have any interest of touching a camera again."

    show coripose1 open

    cori "It can just be really simple, don't overthink it, just take a photo of something you find interesting."

    show coripose1 neutral

    "He peers into your eyes."

    "You look at the camera, then back at him."

    u "I guess it couldn't hurt."

    show coripose1 -camera

    "You take the camera from him and hold it in your hands, feeling the weight of it."

    "The cold metal feels foreign in your hands, but you find yourself drawn to it."

    "You look through the viewfinder, adjusting the settings and trying to find something interesting to take a photo of."

    jump take_photo

    default photo_trees = False
    default photo_cori = False
    default photo_flower = False

    label take_photo:

        hide coripose1 with dissolve

        menu:

            "Look at the trees" if not photo_trees:

                $ photo_trees = True

                "Most of the trees are barren, but a few stubborn leaves cling to the branches, their colors faded but still visible against the snow."

                "From where you're standing, the sun is just peeking through the branches, creating a soft glow that illuminates the snow and casts long shadows on the ground."

                "There is a pine tree nearby, its needles are green, it stands out against the white snow."

                play sound "audio/shutter.mp3"

                "You take a photo of the snow-covered pine tree."

                show coripose1 light open flowers with dissolve

                cori "The trees are my favorite part of this path, they look so different in every season. I love how the snow clings to the branches, it makes them look like they're made of glass."

                jump take_photo

            "Look at the man" if not photo_cori:

                $ photo_cori = True

                show coripose1 light closedsmile flowers with dissolve

                "You look at the man. The morning light casts a soft flow on his face."

                show coripose1 open

                cori "You want to take a photo of me? I can't promise it'll look good, but go ahead."

                show coripose1 teethsmile

                "He stands in front of the phone booth and smiles."

                "You line up the man's figure in the viewfinder, adjusting the settings to capture the soft morning light on his face."

                play sound "audio/shutter.mp3"

                "You take a photo."

                "It seems the lens flare has blocked out his face."

                "He almost looks transparent."

                jump take_photo

            "Look at the flower" if not photo_flower:

                $ photo_flower = True

                show coripose1 light side flowers with dissolve

                "You look at the flower in his pocket, once again drawn to its vibrant pink color."
                
                show coripose1 direct 

                "The man notices."

                show coripose1 -flowers

                "He takes the flower out of his pocket and holds it towards you."

                show coripose1 closedsmile 

                cori "An execellent choice for a subject."

                "You gently take the flower from him, his fingers are soft against yours, like a daft of air."

                hide coripose1 with dissolve

                "You stick the flowers into the snow."
                
                play sound "audio/shutter.mp3"

                "The sun illuminates the petals, they look as if they've just bloomed."

                show coripose1 open direct worried
                cori "You can have the flower, I have plenty more at home."

                jump take_photo

            "That's enough photos for now" if photo_trees and photo_cori and photo_flower:

                pass
    
    show coripose1 light direct raised open with dissolve 

    cori "Very interesting..."

    "He's looking through your photos on the camera's screen."

    cori "I thought I told you not to overthink it."

    cori "Or maybe you just have a strong instinct for it?"

    show coripose1 closedsmile

    u "What do you mean?"

    show coripose1 open

    cori "Not only do you have a good eye for composition, but it seems like with every shot you're following a theme."

    cori "The pine tree, its an evergreen tree, the kind that stays green year round, even in the harshest winters."

    cori "The wind phone, an out of place shelter in an otherwise desolate location."

    cori "And lastly, the cyclamens, a flower that only blooms in the winter, when everything else is dormant."

    cori "Even if its just a few photos, they follow a cohesive theme."

    show coripose1 side 

    cori "They are all representations of resilience in bleak settings."

    show coripose1 closedsmile

    "You pause for a moment, taking in his words."

    "Was that really what you were trying to do?"

    show coripose1 direct

    "His eyes peer into yours."

    show coripose1 open worried

    cori "What do you think?"
    
    show coripose1 closedsmile

    u "I think... your camera has a mind of its own and it has possesed me."

    show coripose1 open raised

    "He laughs."

    cori "So humble."

    show coripose1 neutral camera

    "You loop the camera strap off your neck and around your wrist and hand it back to him."

    u "Thanks uhh, I don't even know your name."

    $ coriname = "Cori"

    $ cori.name = coriname    

    show coripose1 open

    cori "I'm Cori."

    show coripose1 neutral

    u "Cori, thanks for letting me use your camera. I'm [player_name]."

    show coripose1 open

    cori "Anytime, [player_name]. I hope you continue to take photos, you have a real talent for it."

    show coripose1 neutral

    "You glance at the phone booth."

    u "I shouldn't keep you here any longer, I'm sure someone is waiting for your call."

    show coripose1 open worried

    cori "Alright then, I'll see you again, soon."

    scene bg snowpath with fade
    
    "You look down at the cyclamen in your hand, its petals a defiant pink against the grey morning scene."
    "It won't last forever, but you know the next winter its kin will bloom again, with the same resilient shade of pink."

    jump day2
    ##########################################################
    #DAY 2
    ##########################################################

label day2:

    stop music
    stop music2

    scene black with fade

    centered "A week passes, the flower turns dull."

    centered "..."

    centered "Another sleepless night."

    "What time is it now?"

    "You check your phone, 6:17 am."

    "Theres no use staying in bed anymore, you might as well go for a walk"

    "You put on your coat and boots, and step outside into the cold morning air."

    play sound "audio/door-open.mp3"
    scene bg snowpath_night with fade

    play music2 "audio/snowamb.mp3" loop fadein 3.0
    play sound "audio/snow_footsteps.mp3" fadein 2.0 volume 0.8
    play music "audio/lofi2.mp3" loop fadein 3.0 volume 0.7

    $ snow_on = True

    "The sun hasn't risen yet, its still dark outside, it almost looks like the middle of the night."

    "You find yourself walking towards a familiar path."

    "The cold air fills your lungs, you leave fresh footsteps in the snow as you walk."
    
    "The only sound is the quiet crunch beneath your feet."

    "The paths are empty except for one figure."

    show coripose1 side norm neutral with dissolve

    "Only an eccentric photographer would be out here at this hour, you recognize him immediately."
    
    show coripose1 open direct raised

    "He also notices you as your footsteps grow closer."

    cori "Oh hey."

    cori "It's good to see you again."

    cori "Quite the early bird, aren't you?"

    show coripose1 neutral

    "You notice hes carrying his camera again."

    "You let out a slight sigh."

    u "It's the opposite."

    u "I couldn't sleep, so I thought I'd go for a walk."

    show coripose1 teethsmile

    "You walk alongside him."

    cori "Were you planning to see the sunrise?"

    "He glances at you as he asks."

    u "I don't know, I just wanted to get out of the house for a bit."

    "You tuck your hands deeper into your sleeves."

    cori "Yea... "

    cori "I get the feeling."


    pause 2.0

    show coripose1 neutral side

    "The two of you walk together."

    "Your steps fall into an easy rhythm, shoes pressing softly into the gravel."

    "It's a comfortable silence."

    pause 2.0

    show coripose1 open

    cori "The sunrise is pretty, but I think the time just before it is my favorite part."

    show coripose1 neutral
    "He keeps his eyes on the horizon."

    "The sky is still dark, but it’s beginning to thin."

    u "You mean the blue hour?"

    show coripose1 direct teethsmile

    cori "Is that what it's called?"

    "He glances at you, a small smile forming."


    show coripose1 neutral 

    u "It only happens for a brief time."


    u "30 minutes give or take, but its truly a shame that the best part of the day is so short."

    u "The blue happens because the sun is below the horizon, so the light has to pass through more of the atmosphere, scattering the shorter blue wavelengths."
    "You look ahead, where the sky fades into a muted blue-gray."

    show coripose1 teethsmile

    cori "Wow, you really know your stuff."
    "He lets out a quiet breath, almost a laugh."

    
    show coripose1 neutral 

    "You keep walking."

    "The sky shifts slowly, almost too gradual to notice."

    
    show coripose1 open side raised

    cori "So..."
    
    cori "Did you end up taking up photography again?"
    
    show coripose1 

    "You pause for a moment, thinking about the camera in your hands a week ago."
    
    u "No, I haven't."

    show coripose1  neutral worried
    
    "Cori’s expression dips slightly."

    show coripose1 open
    
    cori "You really seemed to enjoy it last time, I thought you might want to do it again."

    cori "You really have a talent for it, I'd love to see what you could do, if you gave it a chance."
    
    pause 2.0

    cori "If I'm not overstepping, can I ask if theres a reason?"

    show coripose1 neutral

    "You pause and think for a moment."

    u "I guess... I just don't see a point to it."
    
    show coripose1 open worried

    cori "Is having fun not a point?"

    show coripose1 neutral

    u "It's not that."

    u "It's just, I started photography because I wanted to capture memories."

    u "I mean, human memory is flawed at best."

    u "You could never remember the details of a moment perfectly, no matter how important it was to you."

    u "I thought if I took a photo, I could preserve the memory of that moment, and look back on it whenever I wanted."

    u "But even with a photo, these things are still so forgetable."

    u "Photos are far too one dimensional."

    "You prefer it that way though."

    "It's easier to not linger and reminisce on things you could no longer return to."

    "Even if the past was once important, the future holds more promises."

    pause 1.0

    show coripose1 open raised side

    "Cori hums in thought."

    cori "Then, can I ask you another question? This one you don't have to answer, just think about it."
    
    show coripose1 neutral

    u "Alright."

    show coripose1 open direct

    cori "Why do you visit the wind phone?"
    
    cori "I mean, we both know there's no one at the end of the line, so why do you keep coming back here?"

    "Why do you keep coming back here?"

    cori "You pick up the reciever anyway. Is there no point? Or is the point the attempt to connect, even if you know it won't work?"

    "He pauses to take a breath."

    pause 1.0

    cori "I think... to some degree, photography is the same."

    cori "I agree with you, that no one would ever be able to capture a moment perfectly."

    cori "You'll never be able to experience a moment twice, no matter how many angles, or frames you take of it."

    cori "But, the point of photography isn't to capture a moment perfectly, don't you think?"

    #cori "To say, you were here, you experienced this, and this is how you want to remember it."
    
    cori "Even if a photo is flawed and only captures one percent of a moment, its better to have nothing at all, right?"
    
    show coripose1 neutral

    pause 1.0
    
    u "..."
    
    u "I see where you're coming from."
    
    u "I guess, I just have a hard time accepting that."

    scene bg peak with fade

    stop music 

    play music "audio/lofi3.mp3" loop fadein 3.0 volume 0.7

    "The two of you continue walking until the summit of the path."

    "The sun is just starting to rise, the sky is a gradient of pinks, purples, and blues."

    "The city can be seen in the distance, its dyed in a vivid blue, its lights twinkling as the sun rises behind it, its covered in a thin mist."
    
    show coripose1 teethsmile side with dissolve 

    "Cori gazes out at the view."

    cori "This is perfect."
    
    cori "Even from this distance, you can see the city is still waking up."
    
    cori "The streets are so empty, it almost looks like a ghost town."
    
    pause 2.0 

    cori "You know, in japanese folklore, they say that the blue hour is when the boundary between the living and the dead is thinnest."
    
    "He gives a mischievous smile."

    show coripose1 direct

    cori "Would you be scared if you met a ghost right now?"

    show coripose1 smile

    "You stare out into the city, it really does look like a ghost town, but you don't feel scared at all."
    
    u "I think this view would keep me from being scared."
    
    "Cori laughs."

    show coripose1 teethsmile
    
    cori "Makes sense."

    play audio "audio/shutter.mp3"

    "Cori takes a photo of the city."

    hide coripose1 

    "You find a nearby bench, dust off the snow, and sit down, taking in the view."

    play audio "audio/shutter.mp3"

    "You watch as Cori takes a few more photos."

    "He's completely absorbed in his work, adjusting the settings and trying to capture the perfect shot."

    pause 3.0

    "The two of you sit on the bench in silence, watching the sunrise and taking in the view."

    show coripose1 open side raised with dissolve

    cori "I think the snow reflecting the blue light makes the blue hour in winter even more special."

    cori "That's why winter is my favorite season."

    show coripose1 neutral

    "It sounds familiar."

    u "I prefer spring."

    u "Everything seems to come back to life after winter."

    show coripose1 open  

    cori "Thats poetic of you."

    show coripose1 neutral

    scene bg peak_day with fade

    show coripose1 light 

    "The sun continues to rise, the sky gradually brightening with a spectrum of colors."

    pause 2.0

    "Eventually, the sun is fully up, and the city is bathed in warm golden light."

    "Cori stands up and stretches."

    show coripose1 open side

    cori "Hey, why don't we take a different path down this time?"

    show coripose1 neutral

    "You raise your eyebrows."

    u "Different how?"

    "He stands in front of you."

    "He learns towards you, grasping your fingers with his own."

    "He pulls you up to your feet, then tugs your sleeve."

    cori "You'll have to follow me to find out."
    
    "He grins."

    scene snowpath with fade

    "He nods past you, toward the lower part of the trail."

    "Your sleeve is still being pulled by him."

    "The path thins out the further you go."

    cori "... "

    "He looks back at you, then to your sleeve, then back at you again."

    "Swiftly, he lets go of your sleeve and holds on to your hand instead."

    "He gives a smile, then turns back around before you could say anything."

    "His hand is neither cold or warm."

    "But the feeling of it is strangely comforting."

    "Snow gives way to gravel, then to rusted rails half-buried in ice."

    scene bg trainout with fade

    stop music2

    play music2 "audio/trainchug.mp3" loop fadein 3.0 volume 0.7
    
    "A boxcar train lugs idly on the tracks ahead."

    show coripose1 open side with dissolve

    cori "Its not moving fast yet."

    show coripose1 neutral

    "He steps closer to it anyway, running a hand along the cold metal."

    show coripose1 open side

    cori "You ever done it before?"

    show coripose1 teethsmile

    cori "Train-hopping."

    show coripose1 neutral

    "Up close, it’s moving faster than it looked."

    "The wheels grind louder. The gaps between cars don’t seem so forgiving."

    u "No, I haven't."

    show coripose1 direct teethsmile

    "Cori cracks a mischievous grin."

    cori "Want to?"

    u "You're not serious."

    cori "I am so serious."

    "The train seems to be picking up speed."

    u "It's going too fast for us to get on."

    show coripose1 side open worried

    cori "I can make it work..."

    u "That’s not convincing."

    show coripose1 direct teethsmile norm

    "He peers into your eyes."

    cori "I can make it work."

    "You stare back at him."

    cori "Close your eyes."

    u "What? Are you gonna perform a magic trick?"

    show coripose1 side

    cori "Do you trust me?"
    
    "You hesitate."

    "You close your eyes."

    scene black with fade
    hide coripose1

    "First, you feel him loop his camera around your neck."

    cori "Hold on to this for me."

    pause 1.0

    "Then suddenly--"

    "Your feet leave the ground."

    play sound "audio/rustle.mp3"

    "An arm around your back. Another under your knees."

    "You don’t have time to react."

    "The sound of metal gets louder. Closer."

    pause 0.5

    play sound "audio/jumpland.mp3"

    "Your weight drops again."

    scene bg traintree with fade

    "When you open your eyes, you're already in the train cart."

    show coripose1 teethsmile direct -camera with dissolve

    cori "Abracadabra!"

    show coripose1 smile

    pause 1.0

    u "…You could’ve warned me."

    show coripose1 open worried

    cori "Would you have said yes?"

    show coripose1 smile

    "You don’t answer."

    "You sit by the edge and look out."

    hide coripose1 with dissolve

    "The ground is already sliding past outside."

    "The train rocks beneath your feet."

    "Not violently. Just enough to remind you you’re not standing still."

    "Wind cuts through the open frame."

    "Your heartbeat quickens with the speed."

    "The ground slides past in long streaks of white and green."

    "Trees. Fences. The occasional pole."

    "Nothing stays long enough to look at properly."

    "A pair of hands press lightly against the sides of your head."

    "He tilts your gaze upward."

    show coritrain open direct with dissolve

    cori "Don’t look right at it."

    cori "Pick something further out."

    show coritrain side smallsmile

    play sound "audio/rustle.mp3"

    "He lets go, sits next to you, looking out past everything."

    show coritrain open 

    cori "It's less dizzy that way."

    show coritrain smallsmile

    pause 1.5

    "You follow his line of sight."

    "The horizon holds still longer than everything else."

    "Or at least it feels like it does."

    show coritrain open

    cori "Looks like we’re heading south."

    show coritrain smallsmile
    
    "You hum, not really checking."

    pause 1.5

    "You try to picture it--"

    "where the tracks go."

    "Past the trees. Past whatever comes after."

    "Snow thinning out. Colors coming back."

    "You don’t know if that’s true."

    u "It's a strange feeling."

    u "Standing still but watching everything whiz by."

    "Cori hums in agreement."
    
    u "It makes me think if humans are meant to travel so fast at all."

    pause 2.0

    show coritrain open direct worried

    cori "If you ask someone from the 1800s they'll tell you women weren't meant to travel on trains."

    cori "Their uteruses would fly out or something."
    
    show coritrain smallsmile

    "You blink."

    show coritrain neutral blush direct
    
    "The absurdity of his comment makes you laugh."
    
    "The movement makes you notice the camera around you neck."

    show coritrain -blush neutral
    
    "You didn't mean to be holding it on for so long."
    
    "You take it off then nudge Cori."
    
    u "I should give this back to you."
    
    "He turns to you, accepting the camera."
    
    show coritrain side worried open
    
    cori "Oh yea, that reminds me."

    show coritrain smallsmile
    
    "He reaches into his pocket."

    "He pulls out a few photographs."

    show coritrain direct open 

    cori "These are yours."

    show coritrain smallsmile

    "He holds them out."

    "You take them."

    pause 1.0

    "A pine tree, a flower, and a photo of Cori in front of the phone booth."

    "The same ones from before."

    pause 1.5

    u "You printed them out?"

    "He shrugs."

    pause 1.5

    show coritrain open side

    cori "Figured you might want them."

    show coritrain smallsmile

    "You look down at the photos."

    "You didn't ask for them."

    "They feel heavier than they should."

    u "Thanks."

    "The train hums beneath you."

    "The horizon stretches out, steady in the distance."

    "You tuck the photos into your coat."

    show coritrain teethsmile 

    cori "My favorite part is coming up soon, I think you'll like it."

    show coripose1 neutral

    "You look at him, curious about what he means."

    "Suddenly, the blur of trees thin out."

    "You find yourself looking upon a vast expanse of water."

    hide coripose1 with dissolve

    cori "It's usually a long hike up here."

    cori "But breaking a few rules gets you here a lot faster."

    pause 1.0

    "Cori gives a smile."

    show coripose1 open direct raised with dissolve

    cori "We should probably get off here,"

    show coripose1 teethsmile

    cori "Unless you want to walk the length of an interstate highway."

    show coripose1 neutral

    "You nod to agree."

    "Cori gives a teasing grin."

    show coripose1 teethsmile worried direct

    cori "Do you need me to carry you back down?"

    "You blink."

    u "..."

    u "I can do it myself."

    show coripose1 side

    cori "If you say so."

    show coripose1 open direct raised 

    cori "When you land, don't lock your knees."

    hide coripose1 with dissolve

    "You learn at the edge, staring at the rapidly moving floor."

    "You wait for it to... feel manageable."

    "You take a breath."

    scene black with fade

    "Then jump off."

    play audio "audio/jumpland.mp3"

    "Your boots hit gravel."

    "You stumble forward, catching yourself after a few uneven steps."

    scene traintracks with fade

    pause 1.0

    "The train keeps moving behind you."

    pause 1.0

    show coripose1 neutral side raised

    "Cori lands beside you."

    "Lighter. Quieter."

    pause 2.0

    "You both turn back."

    "Watch it pass, car after car."

    u "It feels slower now."

    show coripose1 direct open 

    cori "You’re not on it anymore."

    show coripose1 neutral

    "You nod."

    "The last car disappears down the line."

    "The sound fades with it."

    "Cori lets out a sigh."

    show coripose1 direct open worried

    cori "I guess we should head back. I bet you're tired."

    show coripose1 neutral

    "The restless night has caught up with you, you feel yourself getting more fatigued."

    "You nod."

    play audio "gravelsteps.mp3" 

    "The two of you begin walking parallel to tracks, heading back towards the city."

    u "I wish I could have stayed a little longer."

    show coripose1 direct worried open

    cori "Really? Even though you don't know where you'll end up?"

    show coripose1 neutral 

    u "Yea."

    u "That's the fun part."

    u "I wouldn't have to think about where to go, or when to leave."

    u "I could just let the train take me wherever."

    "Cori scoffs."

    show coripose1 open

    cori "Whats the point of being a human? If you want to live as a train."

    show coripose1 neutral 

    u "It's just a fun idea."

    show coripose1 side 

    cori "Hmmm."

    show coripose1 direct teethsmile

    cori "Maybe we could try it out some day."
    
    scene black with fade

    stop music
    stop music2

    centered "You return home and collapse on your bed."

    centered "You ended up sleeping through the rest of the day, only awakening when the sun goes down."

    "The first thing you notice is the three photographs on your nightstand."

    "They seemed so out of place."

    u "I guess I should stash them away."

    scene bg hallway with fade

    "You drag yourself out of the bed, stumbling through the hallways filled with black boxes and cases."

    "Your house had plenty of space for them. Binders, folders, albums."

    "Most of these were your father's, but you knew your work was buried somewhere in there too."

    play audio "audio/searching.mp3"

    "You rummage through the boxes of tapes, photos, looking for a place to store the photographs."

    "Your hand lays on a black binder."

    "It's familiar."

    "You pull it out, and lay it open on the dimly lit hallway."

    "Inside, it is unmistakably filled with photographs of your own."

    "Buildings, landscapes, flora and fauna."

    "Some had been cut up, glued into neatly arranged collages."

    u "When did I take these?"

    play audio "pageflip.mp3"

    "You flip through the pages until you reach the last one."

    "Three photographs fill three quadrants of the page."

    "The fourth one is missing."

    "The three photographs are of the blue hour, on that very summit."

    "Spring, summer, and fall... "

    "Winter is missing."

    scene black with fade

    centered "People often confuse feeling something after a long time with feeling it for the first time."

    "Your eyes droop with fatigue."

    scene bg bath

    play music "audio/ominous.mp3" loop fadein 3.0 volume 0.7

    "The water you've drawn in the basin has cooled."

    "You soak the cloth in the water."

    "His back is slouched forward, skin thinner than you remember."

    show dad with dissolve

    d "It's cold."

    u "I know, it'll be over in a second."

    "You continue to wipe his back."

    pause 2.0

    d "Did you finish your homework?"

    "Your hand stills for a second."

    u "Yeah. I finished it."

    "He nods faintly, like he’s checking something off."

    d "You always leave it to the last minute."

    "That’s not true."

    "It never was."

    "You don’t correct him."

    "You reach for the towel and start drying his back."

    "Careful. Routine."

    "He shifts under your hands."

    d "…You cut your hair."

    "You didn’t."

    u "Yeah."

    d "It suits you."

    "You’ve never had this haircut."

    "... "

    "You guide his arm through his sleeve."

    "He resists for a second, then relaxes."

    d "Your hands are cold."

    u "Sorry."

    d "It’s fine."

    "... "

    "He looks down at his own hands."

    d "When did these get so old?"

    "His voice sounds so fragile."

    "You don’t answer."

    "He mutters something quietly to himself."

    "You pull his shirt back over his shoulders."

    "You guide his arms through the sleeves."

    "He doesn’t help."

    "He used to."

    "Smooth out the fabric like it matters."

    d "Thank you."

    "... "

    u "Yeah."

    hide dad with dissolve

    "You just carry the basin to the sink."

    "The water sloshes with each step."

    "You watch it for a moment before pouring it out."

    "It disappears too quickly."

    jump day3

    ################################################
    #DAY 3
    ################################################

label day3:

    stop music fadeout 3.0

    scene black with fade

    centered "Another week has passed, the flowers have wilted."

    "You're walking home as the sun dips low, staining the city in orange."
    
    "The light catches on windows and wet pavement, stretching everything thin."
    
    "The snow still hasn’t melted yet."

    "It’s turned gray at the edges, packed down into uneven footprints and tire marks."

    "You've been looking for someone."

    "You've been looking for Cori."

    scene bg beach

    play music "audio/sadcalm.mp3" loop volume 0.8 fadein 3.0

    play music2 "audio/waves.mp3" loop fadein 3.0 volume 0.7

    "Your intuition leads you to the beach."

    "The air shifts as you get closer. It's colder, heavier, tinged with salt."

    "You spot him before you’re fully there."

    "Not on the shore."

    "In the water."

    "His shoes sit off to the side, half-sunken into the damp sand."

    "His pants are rolled up to his calves, fabric darkened where it’s been splashed."

    "The tide pushes in and out around his legs."

    "He walks along the edge where the waves break, slow and steady."

    "Each step disappears as the water folds back over it."
    
    u "Cori!"

    "You rush to him."

    "Your voice carries over the sound of the water."

    "He turns around, a surprised expression on his face."

    show coripose1 light open direct worried with dissolve

    cori "Woah- hey."

    show coripose1 closedsmile raised

    "His expression softens upon seeing you."

    show coripose1 open 

    cori "Are you here to catch the sunset too?"

    show coripose1 closedsmile

    "The light hits his face at an angle, softening the edges of his expression."

    u " I've been... looking for you."

    "You say between breaths."

    show coripose1 neutral worried

    "He tilts his head slightly, studying you."

    u "I... I wanted to give those photographs back to you."
    
    "You hesitate, fingers tightening slightly at your sides."

    u "I remembered something important."

    u "I'm sorry but, I can't keep them."

    show coripose1 norm side

    "Cori's expression turns neutral, it almost seems like he was expecting this."

    show coripose1 open worried

    cori "It looks like my convincing didn't work then, huh?"

    show coripose1 neutral

    "A small, almost amused breath leaves him, but it doesn’t reach his eyes."

    hide coripose1 with dissolve

    pause 2.0 

    "You end up sitting beside him on a bench facing the water."

    "The wood is cold through your clothes."

    "The tide rolls in and out, steady, filling the space between words."

    "For a while, neither of you speak."

    show coripose1 side raised with dissolve

    "You glance at him."

    "He's watching the water, not you."

    u "Cori, can I ask you a personal question?"

    show coripose1 direct

    "Cori looks at you."
    
    show coripose1 open

    cori "Yea."

    show coripose1 neutral

    u "You already gave me an answer for this, sort of."

    u "But, why do you take photographs?"

    show coripose1 side norm

    "Cori pauses for a moment."

    "He looks away, his expression is hard to read."

    "You hear him scoff slightly."

    show coripose1 raised open

    cori "Did I get found out?"

    show coripose1 neutral

    "You don't answer."

    pause 2.0

    show coripose1 open

    cori "What gave it away?"

    show coripose1 neutral

    pause 1.0

    u "Those photos we took."

    u "All of them are the same as I remeber."
    
    u "Except for one."
    
    u "The one with you in front of the booth."
    
    u "Everything is the same, the booth, the lighting."
    
    u "But you've dissappeared."
    
    "... "
    
    u "You're always never bothered by the cold-"
    
    u "Your landings are too light-"
    
    u "You never get tired."
    
    "You gaze upon the sand in front of you."
    
    "There are only one pair of footprints leading to where you sit."
    
    u "And today, you're not even leaving footprints."
    
    "You turn to look at him."
    
    u "Cori."

    "He avoids your gaze."
    
    u "What are you?"
    
    "You already know the answer, but you want to hear it from him."
    
    cori ". . . "
    
    show coripose1 open worried 

    cori "I... I'm not sure myself."
    
    cori "A ghost? A wandering spirit? A figment of your imagination?"
    
    cori "I don't know, but I do know that I'm not really here anymore."

    show coripose1 neutral
    
    "You swallow thickly."

    u "What do you remember?"

    show coripose1 open 
    
    cori "I... "
    
    show coripose1 direct
    
    cori "I remeber you... "
    
    cori "...Last winter, you were at the summit, weren't you?"
    
    cori "It was clear that you were there for the intention of taking photos."
    
    cori "You brought your camera and everything."
    
    cori "But instead, you just sat there, and stared."

    show coripose1 side worried
    
    cori "You stared into the city, for hours."
    
    cori "You left your camera at the end of it."
    
    cori "And I picked it up."
    
    cori "I started using it."
    
    cori "Bit by bit."
    
    cori "I realized, whenever I took a photo."

    show coripose1 direct norm 
    
    cori "I would remeber a little bit more about myself."
    
    cori "I could exist in this world a little more."
    
    cori "Eventually I grew curious about you."
    
    cori "That curiosity drew me back."
    
    cori "I wondered if I'd meet you again."
    
    cori "So when it became winter again, I waited for you to come back."

    show coripose1 neutral
    
    u "That was the day we met."
    
    "Cori nods."

    show coripose1 side open raised
    
    cori "Yea."
    
    cori "I pushed you to take some photos."

    show coripose1 worried teethsmile
    
    cori "You didn't even recognize your own camera, did you?"
    
    cori "I wanted to know why you were so indifferent to something you loved so much..."
    
    pause 2.0
    
    cori "So, let me turn the question back to you..."
    
    cori "[player_name], why do you not take photos?"
    
    pause 2.0

    u ". . . "
    
    u "I think it was, maybe 6 years ago?"
    
    u "My father developed a disease."
    
    u "The kind that eats away at a person's mind and memories."
    
    u "I wasn't as good at the camera as him, but I started a collection for him."
    
    "Cori looks into your eyes, carefully listening."
    
    u "I collected pictures of important places and moments."
    
    u "I thought, maybe if his mind couldn't hold onto them, I could."
    
    u "He'd criticize my work, say I wasn't cut out for this kind of thing."
    
    u "But it didn't matter to me."
    
    u "I saw him slowly lose touch with reality."
    
    u "The last year before everything happened, I started a collection of photographs."
    
    u "I started in spring, I photographed the view from the mountain during blue hour."
    
    u "I thought it would be nice, he was the one who taught me all about it."
    
    u "I continued through summer and fall."
    
    u "But when the winter came, my father had a moment of clarity, only to do something so stupid."
    
    u "He took his own life that winter, and I never saw reason to finish the collection."
    
    "Theres a thick silence between the two of you."
    
    u "That's why I hate photography so much."
    
    u "It's pointless, it doesn't keep anything."
    
    u "After my dad passed, we had him cremated."
    
    u "It felt so strange carrying his ashes."
    
    u "I was holding him, but it wasn't him at all."
    
    u "Those ashes are nothing like him, they don't represent anything he was, or stood for, or..."
    
    "Your voice trails off."
    
    pause 2.0
    
    "The waves fill the space for you."

    show coripose1 side worried open
    
    cori "But you still kept them, didn't you?"
    
    cori "Even if they weren't really him."
    
    cori "His photos, his films, his ashes."
    
    cori "So why come back here and throw everything else away?" 

    show coripose1 direct neutral   
    
    "Cori watches you for a moment."

    show coripose1 norm open
    
    cori "You wish so desperately for these things to mean nothing."

    show coripose1 side open
    
    cori "But that's not true at all."
    
    cori "Even if they're just a fraction."
    
    cori "That's enough to make you hesistate."

    show coripose1 direct neutral
    
    "There's a long pause."
    
    "Cori leans over."
    
    "The bench doesn't creak."

    show coripose1 open
    
    cori "You want me to take these back so bad."

    show coripose1 neutral
    
    "He grasps the photos in his hand."

    show coripose1 open 
    
    cori "I'll keep them for you."
    
    cori "But, I want you to have something in return."

    show coripose1 neutral
    
    "He takes off his camera, and hands it to you."

    show coripose1 side open 
    
    cori "You won't be able to finish that collection without this camera right?"
    
    cori "Even if you don't want to."
    
    cori "I want you to have the option to."

    show coripose1 neutral
    
    "You don't refuse."

    show coripose1 open direct
    
    cori "But if you do, I'll be there to see it."
    
    cori "I promise."
    
    scene black with fade
    
    "It was a long walk home."
    
    "Long but quiet."

    scene bg hallway_day with fade
    
    "Someone's at the dining table."

    show mom with dissolve
    
    "It's Mom."
    
    "She looks up at you."
    
    m "Oh, you're back."
    
    m "I saw you left this on the table."
    
    "You left on the table?"
    
    m "These are yours aren't they?"
    
    m "How come you never showed me these?"
    
    u "You can tell they're mine?"
    
    "She wasn't a photographer herself, you were surprised she could tell just by looking at them."
    
    "She smiles just a bit."
    
    m "It was just a feeling."
    
    "She traces the edge of one of the photos."
    
    m "Yea, of course I can."
    
    m "It's different from your dad's work."
    
    m "I'm not sure how to describe it."
    
    m "His work felt... over-engineered."
    
    m "Yours feels more in the moment."
    
    m "Like I'm looking through your eyes."
    
    "She looks up at you again."
    
    m "They're pretty."
    
    m "You should keep them somewhere safe, [player_name]."
    
    "She hands you the binder."

    hide mom with dissolve
    
    scene black with fade

    centered "The camera sits on your nightstand."
    
    centered "It's lens' stares into your own, taunting you."
    
    "What time is it now?"
    
    "You check your phone, it's 6:17am."
    
    "Theres no reason to stay in bed anymore."
    
    "You put on your coat and boots, swing the camera strap around your neck, and step outside into the cold morning air."
    
    play sound "audio/door-open.mp3"
    
    scene bg snowpath_night with fade

    play music2 "audio/snowamb.mp3" loop fadein 3.0

    play sound "audio/snow_footsteps.mp3" loop fadein 1.0 volume 0.8

    play music "audio/lofi2.mp3" loop fadein 3.0 volume 0.7

    $ snow_on = True
    
    "The sun hasn't risen yet, its still dark outside, it looks just like the middle of the night."
    
    "You walk towards a familiar path."
    
    "The cold air fills your lungs, you leave fresh footsteps in the snow as you walk."
    
    "There's no one ahead."
    
    scene bg windphone_night with fade
    
    "The cold nips at your skin."
    
    "You approach the familiar weathered booth."
    
    "It's a bit cold, so you seek shelter in the booth."
    
    "Your gloved hand reaches for the metalhandle."

    play sound "audio/door-open.mp3"

    scene bg boothinterior_night

    "The glass walls shelter you from the wind, its a bit warmer inside."
    
    "You hold your coat a bit tighter, blowing air into your cupped hands."
    
    "It seems like previous visitors have left some things behind."

    jump phone_booth_2


    default saw_photos2 = False
    default saw_flowers2 = False
    
    label phone_booth_2:
        menu:
            "Photos" if not saw_photos2:

                $ saw_photos2 = True

                "Printed photos of a pine tree, a cyclamen flower, and a phone booth have been left here. "
                
                jump phone_booth_2

            "Flowers" if not saw_flowers2:

                $ saw_flowers2 = True

                "Some has left a bundle of cyclamens behind, they're fresh."

                jump phone_booth_2

            "Leave" if saw_photos2 and saw_flowers2:

                jump start_phone_call_2


    label start_phone_call_2:

    play sound "audio/ringringring.mp3" fadein 2.0 volume 0.8 

    "You hear a ring."

    "... It's coming from the phone."

    "Your heart beat quickens."

    "It's not suppose to be ringing."

    pause 3.0

    "Tentatively, you pick up the phone and hold it up to your ear."

    ". . . "

    cori "Hey, [player_name]."

    "It's Cori."

    cori "I thought you said you weren't an early bird." #owl?

    cori "The sun's not even up."
    
    cori "And you have your camera."
    
    cori "Are you planning to finish your collection?"
    
    u "Maybe."
    
    "You pause."
    
    u "I thought you said you'd be here to see it."
    
    "You hear him take a breath."
    
    cori "I am here."
    
    cori "Sort of... "
    
    cori "Sorry, I thought I had more time."
    
    cori "But it seems like I've lingered here for too long."
    
    cori "These sort of things have cycles."
    
    cori "Even if it shouldn't have happened in the first place."
    
    "He sounds far away."
    
    cori "Last winter, you brought me back."
    
    cori "This winter you'll send me off."
    
    cori "It all comes full circle."
    
    "You take in his words."
    
    u "...Are you really just going to disappear?"
    
    cori "Probably."
    
    cori "It's nothing to be sad about."
    
    cori "We weren't even suppose to meet in the first place."
    
    cori "But I'm glad we did."
    
    "... "

    u "I'm glad too."

    u "I'm glad it was you who picked up my camera."

    u "I'm glad you took me to the summit."

    u "And... "

    u "I'm glad you came back for me."

    "There's a pause."
    
    cori "I wish we had met earlier."
    
    cori "I also wish I could stay here forever."

    "A faint static hums between you."
    
    cori "But winter doesn't last forever."
    
    cori "Neither does the blue hour, right?"
    
    cori "You should hurry, Or you'll miss that shot."

    "You hum in response."

    cori "Remember, don't overthink it."

    cori "Just take the photo."

    u ". . . "

    u "Will you see it?"
    
    cori "Of course I will."

    cori "Or maybe..."

    cori "I'll be part of it."

    "Your chest tightens."

    "There's more you want to say."

    "But it doesn't come out."

    u "... Okay."

    "The line goes quiet."

    "...Then dead."

    scene snowpath_night with fade

    "The climb feels longer than you remember."

    "Your breath fogs in front of you."

    "Your camera thumbs against your core with each step."

    "You're wearing boots but they do little against the cold."

    "You don’t stop."

    "You're arriving at the end of the path."

    scene peak with fade

    "You step forward."

    "The wind is sharper up here."

    "You look around."

    "It's empty."
    
    "You swallow."

    "Your grip tightens slightly around the camera."

    "The wind moves past you."
    
    "It almost feels like something brushes against your hand."

    "You freeze."

    "You look down at your hand."

    "Don't overthink it."

    "Don't try to make it perfect."
    
    "You exhale slowly."

    "You raise the camera."

    "The view settles into frame."

    "You wonder if Cori is watching you."
    
    "Somewhere you can't see."
    
    "You line the shot up."
    
    "And click the shutter."
    
    pause 3.0

    centered "insert pic of a very beautiful shot"

    centered "uhhh credits yuh uyh hi robert"

    centered "epilouge."

    scene bg windphone with fade 
    
    "It's early spring now."
    
    "The world is awakening from its winter slumber."
    
    "The bushes are budding with new life."
    
    "In this season you like to look for birds to photograph."
    
    "You crouch down and peer through the viewfinder."

    "You stay as still as you can, waiting for a bird to come into frame."
    
    pause 2.0

    "Suddenly, you feel a tap by your foot."

    cs "Ah!"
    
    cs "Oh, is that a person?"
    
    cs "I'm so sorry I didn't mean to bump into you."



