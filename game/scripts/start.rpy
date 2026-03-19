

default saw_photos = False
default saw_flowers = False
default saw_phone = False

label start:

    $ player_name = renpy.input("What is your name?", length=32)
    $ player_name = player_name.strip()  

    if player_name == "":
        $ player_name = "March"

    scene black with fade
    
    centered "Today is the first snowfall of this year."
    
    #centered "It's my second time spending it without you."
    
    scene bg snowpath with fade
    
    #play music "audio/snowpath2.mp3" 
    play music2 "audio/snowamb.mp3" 
    play sound "audio/snow_footsteps.mp3" 

    "The sunlight filters through snowy branches, casting soft shadows onto the path ahead."
    "During winter, all the animals hide, leaving behind a quiet white landscape where it seems you are the only one awake."
    "The air is crisp and still, carrying the faint scent of pine and snow."
    "You can see your breath in the cold air as you walk, each step crunching on the ground."
    "You keep your eyes on the ground, as if facing the light would blind you." #Even if the light is weak, you feel weaker."
    "This is your second year visiting the wind phone; a disconnected phone booth out in the woods."
    "Some say the phone carries on your messages on the wind, to loved ones who have passed on."
    "But truthfully, it didn't matter if the phone worked or not."
    "The one way conversations and quiet walks through the snow were what you needed."
    
    scene bg windphone
    
    "The cold nips at your skin."
    "You approach the familiar weathered booth."
    "Your gloved hand reaches for the metalhandle."

    stop sound
    stop music2
    play sound "audio/door-open.mp3"

    scene bg boothinterior

    "The glass walls shelter you from the wind, its a bit warmer inside."
    "It seems that previous visitors have left some items behind."

    jump booth_examination


label booth_examination:
    scene bg boothinterior 
    
    menu:

        #"It seems that previous visitors have left some items behind."

        "Photos" if not saw_photos:
            $ saw_photos = True
            "Printed photos of various subjects have been placed here. Sunsets, beaches, wildlife, and food. It seems whoever took these had a great understanding of photography."
            jump booth_examination

        "Flowers" if not saw_flowers:
            $ saw_flowers = True
            "Someone has left a bundle of flowers behind. You don't recognize the species. They are a bit wilted."
            jump booth_examination

        "Phone" if not saw_phone:
            $ saw_phone = True
            "It feels heavy and cold. It hasn't seen a dial tone in years."
            jump booth_examination

        "Pick up the receiver" if saw_photos and saw_flowers and saw_phone:
            jump start_phone_call

label start_phone_call:

    "Tentatively, you pick up the phone and hold it up to your ear."
    "..."
    "You know that no one will pick up, but you still hope for a response."
    pause 2.0
    u "Hi, Dad."
    "You brush away a stray snow flake off your coat, watching it melt into the fabric."
    u "It’s been snowing the entire night. You always said the first snow was the hardest to light. Too much bounce, or whatever it was..."
    "I’m back at the house. Mom’s okay. She’s finally started moving your things into the spare room. All those heavy black boxes you used to lug through airports... they’re just sitting in a stack now.  I have to walk past them to get to the bathroom."
    "It’s a lot of black plastic. I haven’t opened them. I told her I’d sell the rigs, but I just end up staring at the latches."
    "You gaze at the photographs and swallow thickly."
    "The object is so mundane yet it stirs something inside you, it feels uncomfortale." #edit
    u "Someone left some photographs here. I feel like the composition is a little amateur but you would probably have a better critique." 
    "You think of how your father always critiqued your work."
    "\"You have symmetry but you have no subject. The path and trees lead the eyes directly to the left center but theres nothing there.\""
    "\"Next time shoot with more exposure to increase contrast between the trees and horizon.\""
    "Back when you were younger you often got offended. It hurt your ego. You'd regret showing him at all."
    "But as you fell more and more in love with photography, you realized his knowledge was inexpendable."
    "It felt as if you couldn't improve anymore if he wasn't here. You'd never be able to reach his level of exception."
    u "Anyway, it's really cold out here, I’ll talk to you again soon, ok?"
    "Byebye."
    "You place down the phone gently, as if you’re afraid of waking someone up."
    
    scene bg windphone   
    play music2 "audio/snowamb.mp3"
    play sound "audio/door-open.mp3"
    "You inhale as you step outside, the cold mountain air fills your lungs."
    "As you exit the booth you hear a mechanical click."
    play sound "audio/shutter.mp3"
    show cori with dissolve
    "There's a man taking photos outside. He doesn't look dressed for this weather but seems unbothered by it." 
    "Your eyes are drawn to a pink hue from his pocket. You see a flower, the same flower from inside the phone booth."
    pause 2.0
    "He notices you and traces your gaze."
    pause 2.0
    cori "Cyclamens."
    "He smiles."
    u "Huh?"
    cori "I grow them in my garden, unlike other flowers, they bloom in the winter."
    "He puts his camera down, letting it hang from his neck, and steps towards you."
    cori "They're my favorite cause the leaves are heart-shaped"
    "His voice is soft against the morning ambience."
    u "I assume those photographs in the booth are also yours?"
    "His eyes flicker to yours and he chuckles slightly."
    cori "I recently picked it up. They're quiet amateur aren't they? I didn't expect anyone to see them, people rarely come here nowadays."
    "You pause for a moment, wondering how to respond."
    u "Photography is subjective anyway, I'm sure whoever you took them for will appreciate them." #edit
    "He grins."
    cori "I hope you're right, she was blind but she loved exploration-- my sister. We would walk this path all the time." #"she could see"
    cori "Back then I had to lead her, but we've walked this path so many times she could probably do it all by herself now."
    "His somber tone when he reminisces about his sister is familiar." #edi t
    u "You must miss her a lot. It sounds like she was lucky to have such a great guide."
    #cori "Hmm."
    cori "I think it was the other way around, at that time at least."
    cori "I'd take my camera on every walk, she'd get annoyed with me taking so much time taking photos, but she was always so interested in what they looked like."
    cori "I'm no poet or anything but I'd try my best to describe them."
    "You shift your weight, your boots crunching loudly in the silence. It’s an awkward bit of vulnerability from a stranger."
    u "I know how that is. My dad was the same way. "
    u "When I was a kid I felt like he loved the camera more than me."
    "You scoff."
    cori "Was he good at least? With the camera."
    "You gently fidget with the edge of your sleeve between your fingertips."
    "You remeber watching his films and looking at his photos."
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


    scene black with fade
    centered "A week passes, the flower turns dull."
    centered "..."
    centered "Another sleepless night."

    "What time is it now?"
    "You check your phone, 6:17 am."
    "Theres no use staying in bed anymore, you might as well go for a walk"
    "You put on your coat and boots, and step outside into the cold morning air."

    scene bg snowpath with fade
    "The sun hasn't risen yet, its still dark outside, it almost looks like the middle of the night."
    "You find yourself walking towards a familiar path."
    "The cold air fills your lungs, you leave fresh footsteps in the snow as you walk."
    "Theres a figure ahead."
    show cori with dissolve
    "Only an eccentric photographer would be out here at this hour, you recognize him immediately."
    cori "Oh hey, I didn't expect to see you again so soon."
    "You notice hes carrying his camera again."
    u "I couldn't sleep, so I thought I'd go for a walk."
    cori "Are you also planning to see the sunrise?"
    u "I don't know, I just wanted to get out of the house for a bit."
    "The two of you walk together."
    cori "The sunrise is beautiful, but I think the time just before it is my favorite part."
    u "You mean the blue hour?"
    cori "Is that what it's called?"
    #cori "You're so knowledgeable!"
    u "It only happens for a brief time."
    u "30 minutes give or take, but its truly a shame that the best part of the day is so short."
    u "The blue happens because the sun is below the horizon, so the light has to pass through more of the atmosphere, scattering the shorter blue wavelengths."
    cori "Wow, you really know your stuff."
    "The two of you continue walking in silience for a bit."
    cori "Sooo..."
    cori "Did you end up takin up photography again?"
    "You pause for a moment, thinking about the camera in your hands a week ago."
    u "Nope."
    "Cori frowns slightly."
    cori "You really seemed to enjoy it last time, I thought you might want to do it again."
    cori "You really have a talent for it, I'd love to see what you could do, if you gave it a chance."
    cori "If I'm not overstepping, can I ask if theres a reason?"
    "You pause and think for a moment."
    u "I guess... I just don't see a point to it."
    cori "Is having fun not a point?"
    u "It's not that."
    u "It's just, I started photography because I wanted to capture memories."
    u "The human memory is so flawed, you could never remember the details of a moment perfectly, no matter how important it was to you."
    u "I thought if I took a photo, I could preserve the memory of that moment, and look back on it whenever I wanted."
    u "But even with a photo, I still forget things."
    u "The smells, the sensations... A photo is just a flat image."
    cori "Then, can I ask you another question? This one you don't have to answer, just think about it."
    u "Alright."
    cori "Why do you visit the wind phone?"
    cori "I mean, we both know there's no one at the end of the line, so why do you keep coming back here?"
    "Why do I keep coming back here?"
    cori "You pick up the reciever anyway. Is there no point? Or is the point the attempt to connect, even if you know it won't work?"
    "He pauses to take a breath."
    cori "I think photography is the same."
    cori "You'll never be able to capture a moment perfectly."
    cori "You're right, you'll never be able to experience a moment twice, no matter how many angles, or frames you take of it."
    cori "I think the point of photography isn't to capture a moment perfectly, but to capture it imperfectly."
    cori "To say, you were here, you experienced this, and this is how you want to remeber it."
    cori "Even if a photo is flawed and only captures a slice of a moment, it still holds value, because it represents your perspective, your memory, and your experience of that moment."
    u "..."
    u "I see where you're coming from."
    u "I guess I just have a hard time accepting that."
    "The two of you continue walking until the summit of the path."
    "The sun is just starting to rise, the sky is a gradient of pinks, purples, and blues."
    "The city can be seen in the distance, its dyed in a vivid blue, its lights twinkling as the sun rises behind it, its covered in a thin mist."
    cori "This is perfect."
    cori "Even from this distance, you can see the city is still waking up."
    cori "The streets are so empty, it almost looks like a ghost town."
    cori "You know, in japanese folklore, they say that the blue hour is when the boundary between the living and the dead is thinnest."
    cori "Would you be scared if you met a ghost right now?"
    u "I think the view would keep me from being scared."
    "Cori laughs."
    cori "I guess you're right."
    "Cori takes a photo of the city, the vivid blue hue makes it look otherworldly."
    "You find a nearby bench, dust off the snow, and sit down, taking in the view."
    "You watch as Cori takes a few more photos, he really seems to enjoy it."
    pause 3.0
    "The two of you sit on the bench in comfortable silence, watching the sunrise and taking in the view."
    cori "I think the snow reflecting the blue light makes the blue hour in winter even more special."
    cori "That's why winter is my favorite season."
    u "I prefer spring."
    u "I like the feeling of new beginnings, and the way the world seems to come back to life after winter."
    cori "Thats poetic and optimistic of you, I like it."
    "The sun continues to rise, the sky gradually brightening with a spectrum of colors."
    pause 2.0
    "Eventually, the sun is fully up, and the city is bathed in warm golden light."


