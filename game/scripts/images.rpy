
#Bgs
image bg snowpath = "images/bg/snowpath.png"
image bg windphone = "images/bg/windphone.png"
image bg boothinterior = "images/bg/boothinterior.png"
image bg boothinterior_night = "images/bg/boothinterior_night.png"
image bg snowpath_night = "images/bg/snowpath_night.png"
image bg windphone_night = "images/bg/windphone_night.png"
image bg peak = "images/bg/peak.png"
image bg peak_night = "images/bg/speak_night.png"
image bg peak_day = "images/bg/peak_day.png"
image bg traintracks = "images/bg/traintracks.png"
image bg trainout = "images/bg/trainout.png"
image bg trainsea = "images/bg/trainsea.png"
image bg traintree = "images/bg/traintree.png"
image bg hallway = "images/bg/hallway.png"
image bg hallway_day = "images/bg/hallway_day.png"
image bg bath = "images/bg/bath.png"
image bg beach = "images/bg/beach.png"


#Sprites
image dad = "images/dad.png"
image mom = "images/mom.png"
image mom happy = "images/mom_happy.png"

#Cori
layeredimage coripose1:

    always "images/corifem.png"
    
    group light:
        attribute light:
            "images/corifem.png" 
    
    group blush:
        attribute blush:
            "images/corifem.png"
    
    group flowers:
        attribute flowers:
            "images/corifem.png"

    group camera:
        attribute camera default:
            "images/corifem.png"

    group eyes:
        attribute direct default:
            "images/corifem.png"
        attribute side:
            "images/corifem.png"

    group eyebrows: 
        attribute worried:
            "images/corifem.png"
        attribute raised default:
            "images/corifem.png"
        attribute norm:
            "images/corifem.png"

    group mouth:
        attribute neutral default:
            "images/corifem.png"
        attribute closedsmile:
            "images/corifem.png"
        attribute smile:
            "images/corifem.png"
        attribute teethsmile:
            "images/corifem.png"
        attribute open:
            "images/corifem.png"


layeredimage coritrain:

    always "images/cori/train/base.png"

    group blush:
        attribute blush:
            "images/cori/train/blush.png"   
    
    group eyebrows:
        attribute worried:
            "images/cori/train/worried.png"
        attribute neutral default:
            "images/cori/train/neutral.png"
    
    group mouth:
        attribute smallsmile default:
            "images/cori/train/smallsmile.png"
        attribute open:
            "images/cori/train/open.png"
    
    group eyes:
        attribute direct default:
            "images/cori/train/direct.png"
        attribute side:
            "images/cori/train/side.png"
        


