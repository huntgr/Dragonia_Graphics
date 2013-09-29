import pygame, random, sys,time,copy
from pygame.locals import *
from classes import *

WINDOWWIDTH = 896
WINDOWHEIGHT = 504
TEXTCOLOR = (255,255,255)
BACKGROUNDCOLOR = (0,0,0)
FPS = 60
PLAYERMOVERATE = 5

def gameover():
    gameoverImage = pygame.image.load('gameover_.png')
    gameoverRect = gameoverImage.get_rect()
    data = [gameoverImage, gameoverRect]
    return data

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                elif event.key == K_RETURN:
                    return

def playerHasHitEnemy(playerRect, the_enemies):
    i = 0
    while i != len(the_enemies):
        if playerRect.colliderect(the_enemies[i][1]):
            return i
        i += 1
    return -1

def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    #print textrect
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def battle(place,player,enemy):
    alive = True
    if player[2].cls == 'mage':
        img = pygame.image.load('mage_dragonia.png')
        rect = img.get_rect()
        plyr = [img,rect]
    elif player[2].cls == 'warrior':
        img = pygame.image.load('warrior_dragonia.png')
        rect = img.get_rect()
        plyr = [img,rect]
    elif player[2].cls == 'cleric':
        img = pygame.image.load('cleric.png')
        rect = img.get_rect()
        plyr = [img,rect]
    elif player[2].cls == 'warlock':
        img = pygame.image.load('warlock.png')
        rect = img.get_rect()
        plyr = [img,rect]
    enemy_place = enemy    
    plyr[1].topleft = (200,400)
    enemy_place[1].topleft = (500,200)
    enemy_place[0] = pygame.transform.scale(enemy[0],(300,330))
#    player_place = player
##    enemy_place = enemy
##    player_place[1].topleft = (200,400)
##    enemy_place[1].topleft = (500,200)
##    enemy_place[0] = pygame.transform.scale(enemy[0],(300,330))
    while alive == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()   
                if event.key == ord('1'):
                    attack1 = True
                    drawText('You pressed 1!',font,windowSurface,0,0,TEXTCOLOR)
                    pygame.display.update()
                    time.sleep(1)
                    alive = False
                    player = 1
                    enemy = 0
                if event.key == ord('2'):
                    attack1 = True
                    drawText('You pressed 2!',font,windowSurface,0,0,TEXTCOLOR)
                    pygame.display.update()
                    time.sleep(1)
                    alive = False
                    player = 0
                    enemy = 1
                if event.key == ord('3'):
                    attack1 = True
                    drawText('You pressed 3!',font,windowSurface,0,0,TEXTCOLOR)
                    pygame.display.update()
                    time.sleep(1)
                    alive = False
                    player = 0
                    enemy = 0
                if event.key == ord('4'):
                    attack1 = True
                    drawText('You pressed 4!',font,windowSurface,0,0,TEXTCOLOR)
                    pygame.display.update()
                    time.sleep(1)
                    alive = False
                    player = 1
                    enemy = 1
                    
        windowSurface.blit(place[0],place[1])
        windowSurface.blit(enemy_place[0],enemy_place[1])
        windowSurface.blit(plyr[0],plyr[1])
        pygame.display.update()
    alive = [player,enemy]
    return alive

def pick_enemy(enemies):
    rand = random.randint(0,len(enemies)-1)
    enemyImage = pygame.image.load(enemies[rand])
    enemyRect = enemyImage.get_rect()
    enemyType = rand
    data = [enemyImage,enemyRect,enemyType]
    return data

def all_enemies(enemies,locations):
    rand = random.randint(2,6)
    all_enemies = []
    x = 0
    while x != rand:
        all_enemies.append(pick_enemy(enemies))
        loc = random.randint(0,len(locations)-1)
        all_enemies[x][1].topleft = locations[loc]
        locations.remove(locations[loc])
        x += 1
    return all_enemies

def pick_hero(heroes):
    pygame.display.update()
    drawText('Welcome to Dragonia', font, windowSurface, 0, 0,TEXTCOLOR)
    drawText('Mage(1)', font, windowSurface, 0, 30,(65,105,225))
    drawText('Warrior(2)',font,windowSurface,87, 30,(178,34,34))
    drawText('Cleric(3)',font,windowSurface,195, 30,(0,255,255))
    drawText('Warlock(4)',font,windowSurface,289, 30,(0,100,0))
    pygame.display.update()
    choosing = True
    while choosing == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()   
                if event.key == ord('1'):
                    windowSurface.fill(BACKGROUNDCOLOR)
                    drawText('You chose Mage!',font,windowSurface,0,0,TEXTCOLOR)
                    pygame.display.update()
                    time.sleep(1)
                    choice = 0
                    class_ = mage('Kripte')
                    choosing = False
                if event.key == ord('2'):
                    windowSurface.fill(BACKGROUNDCOLOR)
                    drawText('You chose Warrior!',font,windowSurface,0,0,TEXTCOLOR)
                    pygame.display.update()
                    time.sleep(1)
                    choice = 1
                    class_ = warrior('Kripte')
                    choosing = False
                if event.key == ord('3'):
                    windowSurface.fill(BACKGROUNDCOLOR)
                    drawText('You chose Cleric!',font,windowSurface,0,0,TEXTCOLOR)
                    pygame.display.update()
                    time.sleep(1)
                    choice = 2
                    class_ = cleric('Kripte')
                    choosing = False
                if event.key == ord('4'):
                    windowSurface.fill(BACKGROUNDCOLOR)
                    drawText('You chose Warlock!',font,windowSurface,0,0,TEXTCOLOR)
                    pygame.display.update()
                    time.sleep(1)
                    choice = 3
                    class_ = warlock('Kripte')
                    choosing = False
                    
    heroImage = pygame.image.load(heroes[choice])
    heroRect = heroImage.get_rect()
    data = [heroImage,heroRect,class_]
    return data

def place():
    places = ['cave_dragonia.png','desert.png','water.png']
    rand = random.randint(0,len(places)-1)
    placeImage = pygame.image.load(places[rand])
    placeRect = placeImage.get_rect()
    place = [placeImage,placeRect]
    return place

def draw_enemies(the_enemies):
    i = 0
    while i != len(the_enemies):
        windowSurface.blit(the_enemies[i][0],the_enemies[i][1])
        i += 1
        #pygame.display.update()
    
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dragonia')
pygame.display.set_icon(pygame.image.load('dragonia!.png'))
# set up fonts
font = pygame.font.SysFont(None, 30)

# set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background_.ogg')

#enemy locations
locations = [(120,0),(240,0),(360,0),(480,0),(600,0),(720,0),(0,130),(120,130),(240,130),(360,130),(480,130),(600,130),(720,130),(0,260),(120,260),(240,260),(360,260),(480,260),(600,260),(720,260),(0,390),(120,390),(240,390),(360,390),(480,390),(600,390),(720,390)]
#enemy setup
enemies = ['ogre.png','snake.png','garg_dragonia_small.png','dragon.png','cyclops.png']
enemy = pick_enemy(enemies)

#test
the_enemies = all_enemies(enemies,locations)
print len(the_enemies)
#topScore = 0
while True:
    # set up the start of the game
    locations = [(120,0),(240,0),(360,0),(480,0),(600,0),(720,0),(0,130),(120,130),(240,130),(360,130),(480,130),(600,130),(720,130),(0,260),(120,260),(240,260),(360,260),(480,260),(600,260),(720,260),(0,390),(120,390),(240,390),(360,390),(480,390),(600,390),(720,390)]
    score = 0
    moveLeft = moveRight = moveUp = moveDown = False
    pygame.mixer.music.play(-1, 0.0)
    heroes = ['mage_dragonia.png','warrior_dragonia.png','cleric.png','warlock.png']
    windowSurface.fill(BACKGROUNDCOLOR)
    player = pick_hero(heroes)
    player[1].topleft = (0,0)
    the_enemies = all_enemies(enemies,locations)
    you_win = False
    while True: # the game loop runs while the game part is playing
        #score += 1 # increase score

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

        # Move the player around.
        if moveLeft and player[1].left > 0:
            player[1].move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and player[1].right < WINDOWWIDTH:
            player[1].move_ip(PLAYERMOVERATE, 0)
        if moveUp and player[1].top > 0:
            player[1].move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and player[1].bottom < WINDOWHEIGHT:
            player[1].move_ip(0, PLAYERMOVERATE)

       
        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the player's rectangle
        windowSurface.blit(player[0], player[1])
        draw_enemies(the_enemies)
        
        # Check if any of the enemies have hit the player.
        current_enemy = playerHasHitEnemy(player[1], the_enemies)
        if current_enemy != -1:
            moveLeft = moveRight = moveUp = moveDown = False
            drawText('You have encountered an enemy! Prepare to fight!',font,windowSurface,0,0,TEXTCOLOR)
            pygame.display.update()
            time.sleep(1)
            alive = battle(place(),player,the_enemies[current_enemy])
            if alive[0] == 0:
                break
            elif alive[1] == 0:
                the_enemies.remove(the_enemies[current_enemy])
                if the_enemies == []:
                    you_win = True
                    break
            draw_enemies(the_enemies)
            windowSurface.blit(player[0], player[1])
        pygame.display.update()   
        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    if you_win == True:
        windowSurface.fill((0,0,0))
        drawText('You have slain all the enemies!', font, windowSurface, 0, 0,(255,255,255))
        drawText('Press ENTER to start a new game', font, windowSurface, 0, 30,(255,255,255))
        pygame.display.update()
        waitForPlayerToPressKey()
    else:
        pygame.mixer.music.stop()
        gameOverSound.play()
        windowSurface.fill((255,0,0))
        gover = gameover()
        windowSurface.blit(gover[0],gover[1])
        drawText('GAME OVER', font, windowSurface, 0, 0,(0,0,0))
        drawText('Press ENTER to start a new game.', font, windowSurface, 0, 30,(0,0,0))
        pygame.display.update()
        waitForPlayerToPressKey()
        gameOverSound.stop()
    



