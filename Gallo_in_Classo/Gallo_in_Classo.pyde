"""
The following code is for our Landscape assignment

By: Sridhar Sairam
October 20, 2018

Mr. Gallo, I downloaded your picture for this amazing project.

So... yea. There was a reason.

You will also need the minim library which you can download at the following link:
    (This is for audio)
    (I just went overboard...)
http://code.compartmental.net/minim/

I spent a LOT of time finding out how to ust the isPlaying() function
... to not be able to
I just created my own boolean to see if it is playing or not playing
I also spent A LOOOT of time finding out how the player. function works.

WOW! There is barely ANY python documentation about this, yet there is a python library

I went crazy for the first time using Processing....
Coding is fun.

LANDSCAPE INFO:
Based on a kinda true story
The landscape is ICS3U1b
Our classroom
Might have taken a bit of writers liberty

The two different things you can do:
    1. Press and hold any key
    2. Don't press any key
Two different landscapes will loop through

Hope you enjoy!
"""
#VaRiAbLeS
playing = False

for_loop_x = 20
for_loop_y = 10

wild_x = 430
wild_y = 10

while_loop_x = 210
while_loop_y = 10

waist_x = 320 - 400
waist_y = 430

right_foot_x = 350 - 400
right_foot_y = 480

left_foot_x = 300 - 400
left_foot_y = 480

shoulder_x = 320 - 400
shoulder_y = 380

left_palm_x = 295 - 400
left_palm_y = 400

right_palm_x = 345 - 400
left_palm_y = 400

neck_x = 321 - 400
neck_y = 350

head_x = 321 - 400
head_y = 350

face_x = 296 - 400
face_y = 330

desk_x = 50
desk_y = 180

chair_x = desk_x + 125
chair_y = 205

chair1_x = chair_x + 250
chair1_y = chair_y
desk1_x = desk_x + 250


def setup():
    size(640, 480) #size of display
    
    #import and load stuff so that the music works
    add_library('minim')
    minim = Minim(this)
    player = minim.loadFile("Chopin - Revolutionary Etude.mp3")
    global minim
    global player

def moving_wall():    
    global desk_x
    global chair_x
    global chair1_x
    global desk1_x
    
    global for_loop_x
    global while_loop_x
    global wild_x
    
    desk_x += 2
    chair_x += 2
    chair1_x += 2
    desk1_x += 2

    for_loop_x += 2
    while_loop_x += 2
    wild_x += 2
    
    #print("For loop: " + str(for_loop_x))
    #print("While loop: " + str(while_loop_x))
    #print("Wild: " + str(wild_x))
    
    left_by = 850
    lim = 650
    
    if for_loop_x >= lim:
        for_loop_x -= left_by
    if while_loop_x >= lim:
        while_loop_x -= left_by
    if wild_x >= lim:
        wild_x -= left_by
    
    if desk_x >= lim:
        desk_x -= left_by
    if chair_x >= lim:
        chair_x -= left_by
    if chair1_x >= lim:
        chair1_x -= left_by
    if desk1_x >= lim:
        desk1_x -= left_by
    

def moving_man():
    global left_foot_x
    global right_foot_x
    global waist_x
    global neck_x
    global shoulder_x
    global right_palm_x
    global left_palm_x
    global head_x
    global face_x
    
    move = 25
    
    if left_foot_x - 50 > right_foot_x:
        left_foot_x, right_foot_x = right_foot_x, left_foot_x #swapping legs for moving
        #print("Right re: " + str(right_foot_x)) #Here for debugging purposes
        #print("Left re: "  + str(left_foot_x)) #Here for debugging purposes
    else:
        #FORWARD MARCH!
        left_foot_x += 2 * move
        waist_x += 1 * move
        neck_x += 1 * move
        shoulder_x += 1 * move
        right_palm_x += 1 * move
        left_palm_x += 1 * move
        head_x += 1 * move
        face_x += 1 * move
        #print("Right: " + str(right_foot_x))
        #print("Left: "  + str(left_foot_x))

    if left_palm_x >= 650:
        come_from_left = 775 #distance to loop back 
        #(how far until person comes back from left of screen)
        
        #moving all body parts back
        right_foot_x -= come_from_left
        left_foot_x -= come_from_left
        waist_x  -= come_from_left
        neck_x -= come_from_left
        shoulder_x -= come_from_left
        right_palm_x -= come_from_left
        left_palm_x -= come_from_left
        head_x -= come_from_left
        face_x -= come_from_left

def draw():
    frameRate(30)
    #Loading images ... Beep boop beep boop...
    face = loadImage("Gallo.png") #face
    wild_poster = loadImage("Wild-Things.jpg") #poster
    while_poster = loadImage("While-loop.png") #while loop poster
    for_poster = loadImage("For-loop.png") #for loop poster
    student_normal = loadImage("Normal.png") #student face normal
    student_scared = loadImage("Scared.png") #student face when Mr. Gallo is near
    
    #RESETTING BACKGROUND
    background(255, 235, 205) #wall
    
    strokeWeight(6)
    rect(for_loop_x, for_loop_y, 173, 51) #for loop poster border
    rect(wild_x, wild_y, 161, 120) #wild poster border
    rect(while_loop_x, while_loop_y, 200, 51) #while loop poster border)
    strokeWeight(1)
    
    image(for_poster, for_loop_x, for_loop_y, 173, 51) #for loop poster
    image(wild_poster, wild_x, wild_y, 161, 120) #wild poster
    image(while_poster, while_loop_x, while_loop_y, 200, 51) #while loop poster
    
    #STUDENT DESKS
    fill(139, 69, 19) #Chair and colour
    #Desk 0
    rect(desk_x, desk_y, 75, 10) #table top
    rect(desk_x, desk_y, 10, 75) #left leg
    rect(desk_x + 65, desk_y, 10, 75) #right leg
    
    #Desk 1
    rect(desk1_x, desk_y, 75, 10) #table top
    rect(desk1_x, desk_y, 10, 75) #left leg
    rect(desk1_x + 65, desk_y, 10, 75) #right leg
    
    #chair 0
    rect(chair_x, chair_y, 50, 5) #seat top
    rect(chair_x, chair_y, 5, 50) #left leg
    rect(chair_x + 50, chair_y, 5, 50) #right leg
    rect(chair_x + 50, chair_y - 50, 5, 50) #back rest
    
    #chair 1
    rect(chair1_x, chair_y, 50, 5) #seat top
    rect(chair1_x, chair_y, 5, 50) #left leg
    rect(chair1_x + 50, chair_y, 5, 50) #right leg
    rect(chair1_x + 50, chair_y - 50, 5, 50) #back rest
    
    #STUDENTS
    #student 1
    line(chair_x - 20, chair_y + 50, chair_x + 10, chair_y) #leg 1
    line(chair_x - 30, chair_y + 50, chair_x + 10, chair_y) #leg 2
    line(chair_x + 10, chair_y, chair_x + 10, chair_y - 50) #back
    line(chair_x + 10, chair_y - 40, chair_x - 25, chair_y) #lower arm
    line(chair_x + 10, chair_y - 30, chair_x - 15, chair_y) #upper arm
    ellipse(chair_x + 10, chair_y - 50, 25, 25) #head
    #student 2
    line(chair1_x - 20, chair1_y + 50, chair1_x + 10, chair1_y) #leg 1
    line(chair1_x - 30, chair1_y + 50, chair1_x + 10, chair1_y) #leg 2
    line(chair1_x + 10, chair1_y, chair1_x + 10, chair1_y - 50) #back
    line(chair1_x + 10, chair1_y - 40, chair1_x - 25, chair1_y) #lower arm
    line(chair1_x + 10, chair1_y - 30, chair1_x - 15, chair1_y) #upper arm
    ellipse(chair1_x + 10, chair1_y - 50, 25, 25) #head
    
    global playing
    global minim
    global player
    
    #Changing faces and audio when teacher leaves/enters
    if (left_foot_x >= 680 and right_foot_x >= 680 or 
        right_foot_x <= 0 and left_foot_x <= 0):
        image(student_normal, chair_x - 2, chair_y - 62, 25, 25) #normal face
        image(student_normal, chair1_x - 2, chair1_y - 62, 25, 25)
        print(playing)
        if playing == True:
            player.pause()
            playing = False
        print(playing)
    else:
        image(student_scared, chair_x - 2, chair_y - 62, 25, 25) #face scared
        image(student_scared, chair1_x - 2, chair1_y - 62, 25, 25)    
        print(playing)
        if playing == False:
            player.loop()
            playing = True
        print(playing)
            
    #BODY
    line(right_foot_x, right_foot_y, waist_x, waist_y) #right leg
    line(left_foot_x, left_foot_y, waist_x, waist_y) #left leg
    line(waist_x, waist_y, neck_x, neck_y) #back +1 for darker line (as it is diagonal)
    line(shoulder_x, shoulder_y, left_palm_x, left_palm_y) #left hand
    line(shoulder_x, shoulder_y, right_palm_x, left_palm_y) #right hand
    
    ellipse(head_x, head_y, 40, 40) #head
    image(face, face_x, face_y, 50, 50) #just to make it accurate
    
    if keyPressed:
        moving_man()
    else:
        moving_wall()
