from random import randint

#Putting values of first 100 stars
stars_xy = []
for i in range(100):
    stars_xy.append([randint(0, 640), randint(0, 480)])
    

def setup():
    size(640, 480)

def draw():
    background(0)
    
    #Colour of stars
    noStroke()
    fill(255)
    
    #Drawing the stars
    for i in range(len(stars_xy)):
        ellipse(stars_xy[i][0], stars_xy[i][1], 5, 5)

    #Moving the stars forward
    for i in range(len(stars_xy)):
        stars_xy[i][0] += 1
        
    #Adding a star every second
    if frameCount % 60 == 0:
        stars_xy.append([0, randint(0, 480)])
    
    #Removing stars that go off screen
    while True:
        for pp in range(len(stars_xy)):
            if stars_xy[pp][0] >= 640:
                stars_xy.pop(pp)
                break
        break
    
    #print("X:", len(stars_xy)) #For Debugging
