"""
This is the code for the refactoring of the code: adding the functions. 
I added a parameter for the speeds of the Moving Man and the Moving Wall. 
See the last line to change the speeds of them. Line 355 and 357
I've kept all of the old code and comments as well; this is the one where you need the minim library
"""


"""
Title: Gallo in Classo
Created by: Sridhar Sairam
Last modification made on: Tuesday October 23, 2018

This project was created for:
    Landscape Homework Assignment - Due: Tuesday October 23, 2018
    (Teacher: Daniel Gallo)

You will also need the minim library which you can download at the following link:
    (This is for audio)
http://code.compartmental.net/minim/

This Code does the following:
    When any key is pressed and held:
        The character will move across the screen.
        The students, desks, chairs and the posters will stop moving and the students will be surprised.
    When the character is on the screen:
        Chopin's Revolutoinary Etude will play
    When the characater is off screen:
        The music will pause
    When keys are not pressed:
        The character will stop moving
        The posters, students, desks and chairs will loop around.
        
EXTRA NOTES:

I spent a LONG time trying to get the MINIM library to work. All of the documentation that I found
was all in Java, despite the library being compatible with Python. Wow.

This landscape is basically a portrayal of our ICS3U1b Period 1 Classroom. I just exaggerated just A LITTLE bit. hehehe

I downloaded your picture for this project, that's why. I thought it would be funny.

Man I had an AMAZING time; this being my first time using processing, I loved it!

I had to make my own isPlaying() function as I couldn't get it to work ... If you know how to use this please explain it to me. It would be amazing!

Hope you enjoy
"""

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
    
    #VaRiAbLeS
    
    global minim
    global player
    
    global playing
    
    global for_loop_x
    global for_loop_y
    
    global wild_x
    global wild_y
    
    global while_loop_x
    global while_loop_y
    
    global waist_x
    global waist_y
    
    global right_foot_x
    global right_foot_y
    
    global left_foot_x
    global left_foot_y
    
    global shoulder_x
    global shoulder_y
    
    global left_palm_x
    global left_palm_y
    
    global right_palm
    global left_palm_y
    
    global neck_x
    global neck_y
    
    global head_x
    global head_y
    
    global face_x
    global face_y
    
    global desk_x
    global desk_y
    
    global chair_x
    global chair_y
    
    global chair1_x
    global chair1_y
    global desk1_x
    
    global chair1_x
    global chair1_y
    global desk1_x
    
    global face
    global wild_poster
    global while_poster
    global for_poster
    global student_normal
    global student_scared
    
    #import and load stuff so that the music works
    add_library('minim')
    minim = Minim(this)
    player = minim.loadFile("/home/robuntu/Sairam/Gallo_in_Classo/Data/Chopin - Revolutionary Etude.mp3")
    
    #Loading images ... Beep boop beep boop...
    face = loadImage("/home/robuntu/Sairam/Gallo_in_Classo/Data/Gallo.png") #face
    wild_poster = loadImage("/home/robuntu/Sairam/Gallo_in_Classo/Data/Wild-Things.jpg") #poster
    while_poster = loadImage("/home/robuntu/Sairam/Gallo_in_Classo/Data/While-loop.png") #while loop poster
    for_poster = loadImage("/home/robuntu/Sairam/Gallo_in_Classo/Data/For-loop.png") #for loop poster
    student_normal = loadImage("/home/robuntu/Sairam/Gallo_in_Classo/Data/Normal.png") #student face normal
    student_scared = loadImage("/home/robuntu/Sairam/Gallo_in_Classo/Data/Scared.png") #student face when Mr. Gallo is near\

def moving_wall(move_by):    
    
    global desk_x
    global chair_x
    global chair1_x
    global desk1_x
    
    global for_loop_x
    global while_loop_x
    global wild_x
    
    desk_x += move_by
    chair_x += move_by
    chair1_x += move_by
    desk1_x += move_by

    for_loop_x += move_by
    while_loop_x += move_by
    wild_x += move_by
    
    ##print("For loop: " + str(for_loop_x))
    ##print("While loop: " + str(while_loop_x))
    ##print("Wild: " + str(wild_x))
    
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

def moving_man(move):
    global left_foot_x
    global right_foot_x
    global waist_x
    global neck_x
    global shoulder_x
    global right_palm_x
    global left_palm_x
    global head_x
    global face_x
    
    
    if left_foot_x - 50 >= right_foot_x:
        left_foot_x, right_foot_x = right_foot_x, left_foot_x #swapping legs for moving
        ##print("Right re: " + str(right_foot_x)) #Here for debugging purposes
        ##print("Left re: "  + str(left_foot_x)) #Here for debugging purposes
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
        ##print("Right: " + str(right_foot_x))
        ##print("Left: "  + str(left_foot_x))

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
        #print(playing)
        if playing == True:
            player.pause()
            playing = False
        #print(playing)
    else:
        image(student_scared, chair_x - 2, chair_y - 62, 25, 25) #face scared
        image(student_scared, chair1_x - 2, chair1_y - 62, 25, 25)    
        #print(playing)
        if playing == False:
            player.loop()
            playing = True
        #print(playing)
            
    #BODY
    line(right_foot_x, right_foot_y, waist_x, waist_y) #right leg
    line(left_foot_x, left_foot_y, waist_x, waist_y) #left leg
    line(waist_x, waist_y, neck_x, neck_y) #back +1 for darker line (as it is diagonal)
    line(shoulder_x, shoulder_y, left_palm_x, left_palm_y) #left hand
    line(shoulder_x, shoulder_y, right_palm_x, left_palm_y) #right hand
    
    ellipse(head_x, head_y, 40, 40) #head
    image(face, face_x, face_y, 50, 50) #just to make it accurate
    
    if keyPressed:
        moving_man(77) #parameter changes the speed
    else:
        moving_wall(99) #parameter change the speed
