

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

    stop audio 
    
    stop music2 fadeout 3.0

    stop music fadeout 5.0

    play sound "audio/door-open.mp3"

    scene bg boothinterior

    $ snow_on = False

    "It's glass walls shelter you from the wind."

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

    show coripose1 closesmile

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

    ##########################################################
    #DAY 2
    ##########################################################

    scene black with fade

    centered "A week passes, the flower turns dull."

    centered "..."

    centered "Another sleepless night."

    "What time is it now?"

    "You check your phone, 6:17 am."

    "Theres no use staying in bed anymore, you might as well go for a walk"

    "You put on your coat and boots, and step outside into the cold morning air."

    scene bg snowpath_night with fade

    "The sun hasn't risen yet, its still dark outside, it almost looks like the middle of the night."

    "You find yourself walking towards a familiar path."

    "The cold air fills your lungs, you leave fresh footsteps in the snow as you walk."

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

    u "It's the opposite."

    u "I couldn't sleep, so I thought I'd go for a walk."

    show coripose1 teethsmile

    "You walk alongside him."

    cori "Are you also planning to see the sunrise?"

    u "I don't know, I just wanted to get out of the house for a bit."

    cori "I get that."

    pause 2.0

    show coripose1 neutral side

    "The two of you walk together."

    "It's a comfortable silence."

    pause 1.0

    show coripose1 open

    cori "The sunrise is beautiful, but I think the time just before it is my favorite part."

    show coripose1 neutral

    u "You mean the blue hour?"

    show coripose1 direct teethsmile

    cori "Is that what it's called?"

    show coripose1 neutral 

    u "It only happens for a brief time."

    u "30 minutes give or take, but its truly a shame that the best part of the day is so short."

    u "The blue happens because the sun is below the horizon, so the light has to pass through more of the atmosphere, scattering the shorter blue wavelengths."
    
    show coripose1 teethsmile

    cori "Wow, you really know your stuff."
    
    show coripose1 neutral 

    "The two of you continue walking in silence for a bit."
    
    show coripose1 open side raised

    cori "So..."
    
    cori "Did you end up taking up photography again?"
    
    show coripose1 

    "You pause for a moment, thinking about the camera in your hands a week ago."
    
    u "No, I haven't"

    show coripose1 worried
    
    "Cori frowns slightly."

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

    u "Human memory is flawed at best."

    u "You could never remember the details of a moment perfectly, no matter how important it was to you."

    u "I thought if I took a photo, I could preserve the memory of that moment, and look back on it whenever I wanted."

    u "But even with a photo, moments are still so forgetable."

    u "Photos are far too one dimensional."

    "You prefer it that way though."

    "It's easier to not linger and reminisce on memories you could no longer return to."

    "Even if the past was once important, the future holds more promises."

    pause 1.0

    show coripose1 open raised side

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
    
    "He gives a smirk."

    show coripose1 direct

    cori "Would you be scared if you met a ghost right now?"

    show coripose1 smile

    "You stare out into the city, it really does look like a ghost town, but you don't feel scared at all."
    
    u "I think the view would keep me from being scared."
    
    "Cori laughs."

    show coripose1 teethsmile
    
    cori "Makes sense."

    "Cori takes a photo of the city."

    "You find a nearby bench, dust off the snow, and sit down, taking in the view."

    "You watch as Cori takes a few more photos, he really seems to enjoy it."

    pause 3.0

    "The two of you sit on the bench in silence, watching the sunrise and taking in the view."

    cori "I think the snow reflecting the blue light makes the blue hour in winter even more special."

    cori "That's why winter is my favorite season."

    "It sounds familiar."

    u "I prefer spring."

    u "Everything seems to come back to life after winter."

    cori "Thats poetic and optimistic of you, I like it."
    scene bg peak_day with fade

    "The sun continues to rise, the sky gradually brightening with a spectrum of colors."

    pause 2.0


    "Eventually, the sun is fully up, and the city is bathed in warm golden light."

    "Cori stands up and stretches."

    cori "Hey, why don't we take a different path down this time?"
    u "Different how?"

    "He doesn’t answer right away."

    "Just nods past you, toward the lower part of the trail."
    "You hesitate, then follow."
    "The path thins out the further you go."

    "Snow gives way to gravel, then to rusted rails half-buried in ice."
    "A freight train lugs idly on the tracks ahead."

    cori "Its not moving fast yet."
    "He steps closer to it anyway, running a hand along the cold metal."
    cori "You ever done it before?"
    cori "Train-hopping."
    "Up close, it’s moving faster than it looked."
    "The wheels grind louder. The gaps between cars don’t seem so forgiving."

    u "No, I haven't."
    "Cori cracks a mischievous grin."
    cori "Want to?"
    u "You're not serious."
    cori "I am so serious."
    "The train seems to be picking up speed."
    u "It's going too fast for us to get on."
    cori "I can make it work..."
    u "That’s not convincing."
    "He peers into your eyes."
    cori "I can make it work."
    "You stare back at him."
    cori "Close your eyes."
    u "What? Are you gonna perform a magic trick?"
    cori "Do you trust me?"
    
    u "I..."
    "You hesitate."

    "You close your eyes."
    "First, you feel him loop his camera around your neck."
    cori "Hold on to this for me."
    pause 1.0
    "Then suddenly--"
    "Your feet leave the ground."
    "An arm around your back. Another under your knees."
    "You don’t have time to react."
    "The sound of metal gets louder. Closer."

    pause 0.5
    "Your weight drops again."

    "When you open your eyes, you're already on the train."
    cori "Abracadabra!"
    pause 0.5
    u "…You could’ve warned me."

    cori "Would you have said yes?"

    "You don’t answer."

    "You cling to the railing and look out."

    "The ground is already sliding past outside."

    "The train rocks beneath your feet."

    "Not violently. Just enough to remind you you’re not standing still."

    "Wind cuts through the open gaps."

    "Your heartbeat quickens with the speed."

    "The ground slides past in long streaks of white and green."

    "Trees. Fences. The occasional pole."

    "Nothing stays long enough to look at properly."

    "A hand presses lightly against the side of your head."

    "He tilts your gaze upward."

    cori "Don’t look right at it."

    cori "Pick something farther out."

    "He lets go."

    "Leans beside you, looking out past everything."

    cori "Less dizzy that way."

    pause 1.5

    "You follow his line of sight."

    "The horizon holds still longer than everything else."

    "Or at least it feels like it does."

    cori "Looks like we’re heading south."

    "You hum, not really checking."

    pause 1.5

    "You try to picture it—"

    "where the tracks go."

    "Past the trees. Past whatever comes after."

    "Snow thinning out. Colors coming back."

    "You don’t know if that’s true."

    u "It's a strange feeling."

    u "Standing still but watching everything whiz by."

    "Cori hums in agreement."
    
    u "It makes me think if humans are meant to travel so fast at all."

    pause 2.0

    cori "If you ask someone from the 1800s they'll tell you women weren't meant to travel on trains."
    cori "Their uteruses would fly out or something."
    
    "You blink."
    "The absurdity of his comment makes you laugh."
    "The movement makes you notice the camera around you neck."
    "You didn't mean to be holding it on for so long."
    "You take it off then nudge Cori."
    u "I should give this back to you."
    "He turns to you."
    cori "Oh yea, that reminds me."
    "He reaches into his pocket."
    "He pulls out a few photographs."
    cori "These are yours."

    "He holds them out."

    "You take them."

    pause 1.0

    "A pine tree."

    "The flower."

    "The booth."

    "The same ones from before."

    pause 1.5

    u "You printed them out?"
    "He shrugs."

    pause 1.5

    cori "Figured you might want them eventually."
    "You look down at the photos."
    "You didn't ask for them."

    "They feel heavier than they should."
    u "Thanks."

    "The train hums beneath you."

    "The horizon stretches out, steady in the distance."

    "You tuck the photos into your coat."

    cori "My favorite part is coming up soon, I think you'll like it."

    "You look at him, curious about what he means."

    "Suddenly, the blur of trees thin out."

    "You find yourself looking upon a vast expanse of water."

    cori "It's usually a long hike up here."

    cori "But breaking a few rules gets you here a lot faster."

    pause 1.0

    "Cori gives a smile."

    cori "Do you need me to carry you back down?"

    "You blink."

    u "I can do it myself."

    cori "When you land, don't lock your knees."

    "You learn at the edge, staring at the rapidly moving floor."

    "You wait for it to... feel manageable."

    "You take a breath."

    "Then step off."

    "Your boots hit gravel."

    "You stumble forward, catching yourself after a few uneven steps."

    pause 1.0

    "The train keeps moving behind you."

    pause 1.0

    "Cori lands beside you."

    "Lighter. Quieter."

    pause 2.0

    "You both turn back."

    "Watch it pass, car after car."

    u "It feels slower now."

    cori "You’re not on it anymore."

    "You nod."

    "The last car disappears down the line."

    "The sound fades with it."

    cori "I guess we should head back. I bet you're tired."

    "The restless night has caught up with you, you feel yourself getting more fatigued."

    "You nod."

    "The two of you walk alongside the water and tracks."

    "Back to the city."
    
    scene black with fade

    centered "You return home and collaspe on your bed."

    centered "You ended up sleeping through the rest of the day, only awakening when the sun goes down."

    "The first thing you notice is the three photographs on your nightstand."

    "They seemed so out of place."

    u "I guess I should stash them away."

    "Your house had plenty of space for them. Binders, folders, albums."

    "You drag yourself out of the bed, stumbling through the hallways filled with black boxes and cases."

    "Most of these were your father's, but you knew your work were buried somewhere in there too."

    "You dig through the boxes of tapes, photos, looking for a place to store the photographs."

    "Your hand lays on a black binder."

    "It's familiar."

    "You pull it out, and lay it open on the dimly lit hallway."

    "Inside, it is unmistakably filled with photographs of your own."

    "Buildings, landscapes, flora and fauna."

    "Some had been cut up, glued into neatly arranged collages."

    "You flip through the pages until you reach the last one."

    "Three photographs fill three quadrants of the page."

    "The fourth one is missing."

    "The three photographs are unmistakably of the blue hour, on that very mountain."

    "One of spring, one of summer, one of fall."

    "Winter is missing."

    "Your eyes flicker to that old camera your father gifted you."

    "It's lens stares into you, taunting you."

    centered "People confuse feeling something after a long time with feeling it for the first time."

    centered "Your eyes droop with fatigue."

    "The water you've drawn in the basin has cooled."

    "You soak the cloth in the water."

    "His back is slouched forward, skin thinner than you remember."

    d "It's cold."

    u "I know, it'll be over in a second."

    "You continue to wipe his back."

    pause 2.0

    d "Did you finish your homework?"

    "Your hand stills for a second."

    u "Yeah. I finished it."

    "He nods faintly, like he’s checking something off."

    pause 2.0

    d "You always leave it to the last minute."

    "That’s not true."

    "It never was."

    "You don’t correct him."

    pause 1.0

    "You reach for the towel and start drying his back."

    "Careful. Routine."

    "He shifts under your hands."

    d "…You cut your hair."

    "You didn’t."

    u "Yeah."

    "He hums, satisfied with the answer."

    pause 1.0

    d "It suits you."

    "You’ve never had this haircut."

    pause 1.0

    "You guide his arm through his sleeve."

    "He resists for a second, then relaxes."

    d "Your hands are cold."

    u "Sorry."

    d "It’s fine."

    pause 1.0

    "He looks down at his own hands."

    d "When did these get so old?"

    "His voice sounds so fragile."

    "You don’t answer."

    pause 1.0

    d "…Must’ve been working too much."

    "He mutters quietly to himself."

    pause 2.0

    "You pull his shirt back over his shoulders."

    "You guide his arms through the sleeves."

    "He doesn’t help."

    "He used to."

    "Smooth out the fabric like it matters."

    d "Thank you."

    "You nod."

    u "Yeah."

    "You just carry the basin to the sink."

    "The water sloshes with each step."

    "You watch it for a moment before pouring it out."

    "It disappears too quickly."

    ################################################
    #DAY 3
    ################################################

    centered "Another week has passed, that flower has wilted."

    centered "You're walking home, the sun is setting, the snow hasn't melted yet."

    "You've been looking for someone."

    "You've been looking for Cori."

    "Your intuition leads you to the beach."

    "There he is, lingering by the water."

    "Rather, he's lingering in the water."

    "His shoes are left on the shore, his pants are rolled up the his calf"

    "He's walking where the waves crash onto the sand."

    "His footsteps are light, almost transparent."
    
    u "Cori!"

    "You call out to him."

    "He turns around, a surprised expression on his face."

    cori "Woah, hey there, you here to catch the sunset too?"

    "His expression relaxes upon seeing you."

    u "I've been looking for you."

    "He tilts his head slightly."

    u "I... I wanted to give those photographs back to you."

    u "I remembered something important."

    u "I'm sorry but, I can't keep them."

    "Cori's expression turns neutral, it almost seems like he was expecting this."

    cori "It looks like my convincing didn't work then, huh?"

    "The two of you sit on a bench by the water."

    "Theres a long silence before you decide to speak."

    u "Can I ask you a personal question?"
    "Cori looks at you."
    cori "Yea."
    u "Have you"
    u "I think it was maybe 6 years ago?"
    u "My father developed a disease."
    u "It wasn't a physical one, it was mental, the kind that eats away at a person's mind and memories."
    u "I wasn't as good at the camera as him, but I started a collection for him."
    "Cori looks into your eyes, carefully listening."
    u "I collected pictures of important places and moments."
    u "I thought, maybe if his mind couldn't hold onto them, I could."
    u "He'd criticize my work, say I wasn't cut out for this kind of thing."
    u "But it didn't matter to me."
    u "I saw him slowly lose touch with reality."
    u "And it tore him apart."
    u "He became unrecognizable from the father and mentor he once was."
    u "At times, he would beg me to help him commit suicide."
    "You feel a pang of guilt."
    u "The last year, I started a collection of photographs."
    u "I started in spring, I photographed the view from the mountain during blue hour."
    u "Thought it would be nice, nice he was the one who taught me all about it."
    u "I continued through summer and fall."
    u "But when the snow came, my father had a moment of clarity, only to do something so stupid."
    u "He committed suicide that winter, and I never saw reason to finish the collection."
    "Theres a thick silence between the two of you."
    u "That's why I wanted to give them back to you."
    "Cori gazes out into the water."
    cori "Returning them to me, it's not just about the photographs is it?"
    "He pauses."
    cori "I'll take them today, but I want you to promise me something."
    "He grasps the photographs from your hands."
    cori "Tomorrow, before the dawn, I want you to finish that collection."
    cori "I don't care if you never touch a camera again."
    cori "I'll be there too, wait for me at the windphone."
    "You pause and think."
    "Maybe this will finally be the end."

    scene black with fade

    centered "The camera lens stares into your own, taunting you."
    centered "This time you taunt it back."

    "You check your phone, it's 6:17am."
    "Theres no reason to stay in bed anymore."
    "You put on your coat and boots, swing the camera strap around your neck, and step outside into the cold morning air."
    scene bg snowpath with fade
    "The sun hasn't risen yet, its still dark outside, it looks just like the middle of the night."
    "You walk towards a familiar path."
    "The cold air fills your lungs, you leave fresh footsteps in the snow as you walk."
    "There's no one ahead."
    scene bg windphone with fade
    "The cold nips at your skin."
    "You approach the familiar weathered booth."
    "It's a bit cold, so you seek shelter in the booth."
    "Your gloved hand reaches for the metalhandle."

    play sound "audio/door-open.mp3"

    scene bg boothinterior

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
                "Printed photos of a pine tree, a cyclamen flower, and a phone booth have been left here. They seem familiar."
                jump phone_booth_2

            "Flowers" if not saw_flowers2:
                $ saw_flowers2 = True
                "Some has left a bundle of cyclamens behind, they're fresh."
                jump phone_booth_2

            "Leave" if saw_photos2 and saw_flowers2:
                jump start_phone_call_2



    label start_phone_call_2:
    #PLAY SOUND EFFECT RING

    
    "The phone rings."
    "It's noise is out of place against the peaceful silence."
    pause 3.0
    "Tentatively, you pick up the phone and hold it up to your ear."

    cori "Hey, [player_name]."
    "It's Cori."
    cori "Ahm, sorry this is a recorded message so I won't be able to hear you."
    "You hear him take a breath"
    cori "remember when you asked me, why I take photographs?"
    cori "I told you it was to make reality more bearable."
    cori "This is my reality."
    cori "I'm sure you've already figured that much out."
    cori "I can't interact with your world anymore."
    cori "I stayed for as long as I could, I thought I had more time though."
    cori "I lingered, trying to desperately grab on to bits of my old life."
    "He scoffs."
    cori "I mean, how could I not? Have you seen how beautiful it is?"
    cori "At first, I couldn't understand your perspective at all, how could someone be so scared of looking back at the past?"
    cori "I realized we were both just viewing it as an excuse to not move forward."
    "Theres a long pause."
    cori "Thanks, [player_name]. I wish we would've met earlier."
    cori "Had more time to talk, to take photos, to explore."
    cori "I really enojoyed our little interactions, they're special to me."
    "There's another long pause."
    cori "But winter doesn't last forever, neither does the blue hour, right?"
    cori "You should hurry, go get that shot."
    cori "At the end will be a spring with new beginnings."
    "The line goes dead."

    scene black with fade
    centered "You're running."
    centered "Against the snow, against time."
    centered "Your camera thumbs against your core."
    centered "You're wearing booths but they do little against the cold."

    scene summit with fade
    "The sun hasn't risen yet."
    "The city can be seen in the distance, its dyed in a vivid blue, its lights twinkling as the sun rises behind it, its covered in a thin mist."
    u "This is perfect."
    "You say to yourself."
    "You fidget with your camera."
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
    pause 2.0

    cs "Eep!"
    cs "Oh, is that a person?"
    cs "I didn't mean to bump into"



