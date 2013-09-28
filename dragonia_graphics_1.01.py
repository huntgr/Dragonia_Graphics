import pygame, random, sys,time
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255,255,255)
BACKGROUNDCOLOR = (0,0,0)
FPS = 40
PLAYERMOVERATE = 5

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
                return

def playerHasHitEnemy(playerRect, enemy):
    if playerRect.colliderect(enemy):
        return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def battle(caveImage,caveRect):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()   
                if event.key == ord('1'):
                    attack1 = True
                    drawText('You pressed 1!',font,windowSurface,10,0)
                    pygame.display.update()
                    time.sleep(1)
                if event.key == ord('2'):
                    attack1 = True
                    drawText('You pressed 2!',font,windowSurface,10,0)
                    pygame.display.update()
                    time.sleep(1)
                if event.key == ord('3'):
                    attack1 = True
                    drawText('You pressed 3!',font,windowSurface,10,0)
                    pygame.display.update()
                    time.sleep(1)
                if event.key == ord('4'):
                    attack1 = True
                    drawText('You pressed 4!',font,windowSurface,10,0)
                    pygame.display.update()
                    time.sleep(1)
                    
        windowSurface.blit(caveImage,caveRect)
        pygame.display.update()

def pick_enemy(enemies):
    rand = random.randint(0,len(enemies)-1)
    enemyImage = pygame.image.load(enemies[rand])
    enemyRect = enemyImage.get_rect()
    data = [enemyImage,enemyRect]
    return data

def pick_hero(heroes):
    pygame.display.update()
    drawText('Mage(1), Warrior(2), Cleric(3), Warlock(4)', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
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
                    drawText('You chose Mage!',font,windowSurface,WINDOWWIDTH/2,WINDOWHEIGHT/2)
                    pygame.display.update()
                    time.sleep(1)
                    choice = 0
                    choosing = False
                if event.key == ord('2'):
                    attack1 = True
                    drawText('You chose Warrior!',font,windowSurface,WINDOWWIDTH/2,WINDOWHEIGHT/2)
                    pygame.display.update()
                    time.sleep(1)
                    choice = 1
                    choosing = False
                if event.key == ord('3'):
                    attack1 = True
                    drawText('You chose Cleric!',font,windowSurface,WINDOWWIDTH/2,WINDOWHEIGHT/2)
                    pygame.display.update()
                    time.sleep(1)
                    choice = 2
                    choosing = False
                if event.key == ord('4'):
                    attack1 = True
                    drawText('You chose Warlock!',font,windowSurface,WINDOWWIDTH/2,WINDOWHEIGHT/2)
                    pygame.display.update()
                    time.sleep(1)
                    choice = 3
                    choosing = False
                    
    heroImage = pygame.image.load(heroes[choice])
    heroRect = heroImage.get_rect()
    data = [heroImage,heroRect]
    return data

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dragonia')

# set up fonts
font = pygame.font.SysFont(None, 30)

# set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

#set up images
caveImage = pygame.image.load('cave.png')
caveRect = caveImage.get_rect()

#enemy setup
enemies = ['ogre.png','snake.png','gargoyle.png','dragon.png','cyclops.png']
enemy = pick_enemy(enemies)


# show the "Start" screen
drawText('Dragonia', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

#player setup
heroes = ['mage.png','warrior.png','cleric.png','warlock.png']
windowSurface.fill(BACKGROUNDCOLOR)
player = pick_hero(heroes)

#topScore = 0
while True:
    # set up the start of the game
    score = 0
    player[1].topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    enemy[1].topleft = (random.randint(0,WINDOWWIDTH-100),random.randint(0,WINDOWHEIGHT-110))
    moveLeft = moveRight = moveUp = moveDown = False
    pygame.mixer.music.play(-1, 0.0)

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
        windowSurface.blit(enemy[0], enemy[1])

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitEnemy(player[1], enemy[1]):
            drawText('You have encountered a dragon! Prepare to fight!',font,windowSurface,10,0)
            pygame.display.update()
            time.sleep(1)
            battle(caveImage,caveRect)
            
        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()
    windowSurface.fill((255,0,0))
    
    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()



