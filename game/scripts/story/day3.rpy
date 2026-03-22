
label day3:

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
    "Cori's expression turns neutral."

    cori "It looks like my convincing didn't work then, huh?"
    "The two of you sit on a bench by the water."
    "Theres a long silence before you decide to speak."
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
