
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
image bg sunset = "images/bg/sunset.png"


#Sprites
image dad = "images/dad.png"
image mom = "images/mom.png"
image mom happy = "images/mom_happy.png"

#Cori
layeredimage coripose1:

    always "images/cori/pose1/cori_pose1_base.png"
    
    group light:
        attribute light:
            "images/cori/pose1/cori_light.png" 
    
    group blush:
        attribute blush:
            "images/cori/pose1/cori_blush.png"
    
    group flowers:
        attribute flowers:
            "images/cori/pose1/cori_flowers.png"

    group camera:
        attribute camera default:
            "images/cori/pose1/cori_camera.png"

    group eyes:
        attribute direct default:
            "images/cori/pose1/cori_eyes_direct.png"
        attribute side:
            "images/cori/pose1/cori_eyes_side.png"

    group eyebrows: 
        attribute worried:
            "images/cori/pose1/cori_eyebrows_worried.png"
        attribute raised default:
            "images/cori/pose1/cori_eyebrows_neutral.png"
        attribute norm:
            "images/cori/pose1/cori_eyebrows_concerned.png"

    group mouth:
        attribute neutral default:
            "images/cori/pose1/cori_mouth_neutral.png"
        attribute closedsmile:
            "images/cori/pose1/cori_mouth_closedsmile.png"
        attribute smile:
            "images/cori/pose1/cori_mouth_frown.png"
        attribute teethsmile:
            "images/cori/pose1/cori_mouth_teethsmile.png"
        attribute open:
            "images/cori/pose1/cori_mouth_open.png"


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
        


