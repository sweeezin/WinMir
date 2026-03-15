

default saw_photos = False
default saw_flowers = False
default saw_phone = False

label start:

   

    scene black with fade
    
    centered "Today is the first snowfall of this year."
    
    centered "It's my second time spending it without you."
    
    scene bg snowpath with fade
    

    play music "snowpath.mp3" 
    play music2 "snowamb.mp3" 

    "The sunlight filters through snowy branches, casting soft shadows onto the path ahead."

    "You keep your eyes on the ground, as if facing the light would blind you. Even if the light is weak, you feel weaker."

    "During winter, all the animals hide, leaving behind a quiet white landscape where it seems you are the only one awake."
    "This is your second year visiting the wind phone-- a disconnected phone booth that you call in hopes that it will carry your words onto the wind."
    
    
    scene bg windphone
    

    "The snow crunches beneath your feet, and the cold nips at your skin as you approach the familiar weathered booth."
    
    "Your gloved hand reaches for the handle."

    scene bg boothinterior

    "The glass walls block out the wind, its a bit warmer inside."
    "It seems that previous visitors have left some items behind."

    jump booth_examination


label booth_examination:
    scene bg boothinterior 
    
    menu:
        "It seems that previous visitors have left some items behind."

        "Photos" if not saw_photos:
            $ saw_photos = True
            "Printed photos of various subjects have been placed here. Sunsets, beaches, wildlife, and food. It seems whoever took these had a great understanding of photography"
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
    "No one will answer, but you decide to speak."
    pause 2.0
    u "Hi, Dad."
    "You brush away a stray snow flake off your coat, watching it melt into the fabric."
    u "It’s been snowing the entire night. You always said the first snow was the hardest to light. Too much bounce, or whatever it was..."
    "I’m back at the house. Mom’s okay. She’s finally started moving your things into the spare room. All those heavy black boxes you used to lug through airports... they’re just sitting in a stack now. I have to walk past them to get to the bathroom."
    "It’s... it’s a lot of black plastic. I haven’t opened them. I told her I’d sell the rigs, but I just end up staring at the latches."
    "You gaze at the photographs and swallow thickly."
    "The object is so mundane yet it stirs something inside you, something you don't want to face."
    u "Someone left some photographs here. I feel like the composition is a little amateur but you would probably have a better critique." 
    "You think of how your father always critiqued your work."
    "\"You have symmetry but you have no subject. The path and trees lead the eyes directly to the left center but theres nothing there.\""
    "\"Next time shoot with more exposure to increase contrast between the trees and horizon.\""
    "Back when you were younger you often got offended. It hurt your ego. You'd regret showing him at all."
    "But as you fell more and more in love with photography, you realized his knowledge was inexpendable."
    "It felt as if you couldn't improve anymore if he wasn't here. You'd never be able to reach his level of exception."
    u "Anyway, it's really cold out here, I’ll talk to you again soon, ok? Byebye."
    "You place down the phone gently, as if you’re afraid of waking someone up."
    
    scene bg windphone   
    "You inhale and you step outside, the cold mountain air fills your lungs."
    "As you exit the booth you hear a mechanical click."
    show cori with dissolve
    "There's a man taking photos outside. He doesn't look dressed for this weather but seems unbothered by it." 
    "Your eyes are drawn to a pink hue from his pocket. You see a flower, the same flower from inside the phone booth."
    pause 2.0
    "He notices you and traces your gaze."
    pause 1.0
    cori "Cyclamens."
    "He smiles."
    u "Huh?"
    cori "I grow them in my garden, unlike other flowers, they bloom in the winter."
    "He puts his camera down, letting it hang from his neck, and steps towards you."
    cori "They're my favorite cause the leaves are heart-shaped"
    "His voice is soft against the quiet morning ambience."
    u "I assume those photographs in the booth are also yours?"
    "His eyes flicker to yours and he chuckles slightly."
    cori "I recently picked it up. They're quiet amateur aren't they? I didn't expect anyone to see them, people rarely come here nowadays."
    "You pause for a moment, wondering how to respond."
    u "Photography is subjective anyway, I'm sure whoever you took them for will appreciate them."
    "He grins."
    cori "I hope you're right, she didn't couldn't see but she loved exploration-- my sister. We used to walk this path all the time"
    cori "Back then I had to lead her, but we've walked this path so many times she could probably do it all by herself now."
    "His somber tone when he reminisces about his sister is familiar, and you can feel the weight of his memories in the air."
    u "You must miss her a lot. It sounds like she was lucky to have such a great guide."
    "He looks at the trees, smiling softly."
    cori "I think it was the other way around, at that time at least."
    cori "I'd take my camera on every walk, she'd get annoyed with me taking so much time taking photos, but she was always so interested in what they looked like, so I'd describe them for her."
    "You shift your weight, your boots crunching loudly in the silence. It’s an awkward bit of vulnerability from a stranger."
    u "I know how that is. My dad was the same way. "
    u " "
    "You gently fidget with the edge of your sleeve between your fingertips."
    u "I could pass on some tricks with the camera he taught me."
    "The man grins."
    cori "Well I couldn't pass up that offer."
    cori "Will you be here next week?"
    "You nod."
    cori "I'm Cori, by the way, I'm better at growing things than capturing them, but I'm a fast learner."
    u "I admire your confidence, I'm PLAYERNAME"
    "Your eyes linger to the booth."
    u "I shouldn't keep you here any longer, I'm sure someone is waiting for your call."
    cori "Alright then, PLAYERNAME, I'll see you again, soon."
    "The two of you bid your farewells"

    scene bg snowpath
    
    "You look down at the cyclamen, its petals a defiant pink against the grey morning scene."
    "It won't last forever, but you know the next winter its kin will bloom again, with the same resilient shade of pink."