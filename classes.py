import random
import sys
import time
import pygame

WINDOWWIDTH = 896
WINDOWHEIGHT = 504
TEXTCOLOR = (255,255,255)
BACKGROUNDCOLOR = (0,0,0)
pygame.init()
font = pygame.font.SysFont('centaur', 30)
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    #print textrect
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class warlock:
    def __init__(self,name):
        self.cls = 'warlock'
        self.dead = 0
        self.name = name
        self.stamina = 14
        self.wisdom = 15
        self.intellect = 16
        self.dexterity = 9
        self.strength = 7
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.miss = 150/self.intellect
        self.crit = self.intellect
        self.dict = ['drains','depletes','consumes','leeches','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Power Siphon','Entropic Assault']
        self.xp = 0
        self.lvl = 1
    def f_displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name,"\nLevel: ",self.lvl, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def f_abilities(self):
        print "Power Siphon(1).  This ability does {0} to {1} damage".format((self.intellect+self.stamina*3/2),((self.intellect+self.stamina)*7/3))
        print "Heals you for a portion of damage dealt\n"
        print "Entropic Assault(2). This ability does {0} to {1} damage".format((self.intellect+self.wisdom+self.stamina)/2,(self.intellect+self.wisdom+self.stamina)*7/2)
        print "Consumes a portion of you current health. Even if you miss!\n"
        print "Blood Armor(3). This ability sacrafices {0} health to create a {1} damage shield.".format(self.health*0.1,self.health*0.3)
        print " "
    def f_ability0(self):
        damage = random.randrange(((self.intellect+self.stamina)*3/2),((self.intellect+self.stamina)*7/3))
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            drawText('You MISS completely!',font,windowSurface,0,0,TEXTCOLOR)
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            heal_control = round(((self.wisdom/2)+((self.stamina*11)/self.health))/3, 0)
            self.health += (self.damage/5)+heal_control
            dam = str(self.damage)
            heal = str((self.damage/5)+heal_control)
            drawText('Your Power Siphon hits for '+dam,font,windowSurface,0,0,TEXTCOLOR)
            drawText('and heals you for '+heal,font,windowSurface,0,25,TEXTCOLOR)
            print 'Your Power Siphon {0} for {1} damage.'.format(self.dict[5],self.damage)
            print 'and heals you for {0}.'.format((self.damage/5)+heal_control)
            
        else:
            self.damage = damage
            heal_control = round(((self.wisdom/2)+((self.stamina*11)/self.health))/3, 0)
            self.health += (damage/6)+heal_control
            dam = str(self.damage)
            heal = str((damage/6)+heal_control)
            drawText('Your Power Siphon hits for '+dam,font,windowSurface,0,0,TEXTCOLOR)
            drawText('and heals you for '+heal,font,windowSurface,0,25,TEXTCOLOR)
            print 'Your Power Siphon {0} for {1} damage.'.format(self.dict[random.randrange(0,4)],self.damage)
            print 'and heals you for {0}.'.format((damage/6)+heal_control)
            
    def f_ability1(self):
        damage = random.randrange((self.intellect+self.wisdom+self.stamina)/2,(self.intellect+self.wisdom+self.stamina)*7/2)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        sac_hp = round(self.health * (0.17),0)
        if miss <= self.miss:
            self.damage = 0
            self.health -= sac_hp
            dam = str(sac_hp)
            drawText('Your MISS completely!',font,windowSurface,0,0,TEXTCOLOR)
            drawText(dam+' health consumed.',font,windowSurface,0,25,TEXTCOLOR)
            print "You MISS completely!"
            print "{0} health consumed.".format(sac_hp)
        elif crit <= self.crit:
            self.damage = damage*2
            self.health -= sac_hp
            dam = str(self.damage)
            hp = str(sac_hp)
            drawText('Your Entropic Assault crits for '+dam,font,windowSurface,0,0,TEXTCOLOR)
            drawText(hp+' health consumed.',font,windowSurface,0,25,TEXTCOLOR)
            print "Your Entropic Assault crits for {0} damage.".format(self.damage)
            print "{0} health consumed.".format(sac_hp)
        else:
            self.damage = damage
            self.health -= sac_hp
            dam = str(self.damage)
            hp = str(sac_hp)
            drawText('Your Entropic Assault crits for '+dam,font,windowSurface,0,0,TEXTCOLOR)
            drawText(hp+' health consumed.',font,windowSurface,0,25,TEXTCOLOR)
            print "Your Entropic Assault deals {0} damage.".format(self.damage)
            print "{0} health consumed.".format(sac_hp)
            
    def f_ability2(self):
        self.damage = 0
    	sac_hp = self.health*0.1
    	sac_shield = self.health*0.3
    	self.health -= sac_hp
    	self.shield += sac_shield
    	shield = str(sac_shield)
    	hp = str(sac_hp)
    	drawText('You sacrafice '+hp+' health for '+shield+' shield',font,windowSurface,0,25,TEXTCOLOR)
    	print "You sacrafice {0} health for {1} shield.".format(sac_hp, sac_shield)
    	
    def f_health(self):
        print "You have {0} health and {1} shield remaining".format(self.health, self.shield)
    def f_level(self):
        self.stamina += 6
        self.wisdom += 3
        self.intellect += 4
        self.dexterity += 1
        self.strength += 1
        self.health = self.stamina*10
        self.miss = 100/self.intellect
        self.crit = self.intellect
        self.lvl += 1
        lvl = str(self.lvl)
        drawText('You reached level '+lvl,font,windowSurface,0,0,TEXTCOLOR)
        print "\nYou've reached level {0}".format(self.lvl)
    def f_sword(self):
        self.intellect += 30
    def f_offhand(self):
        self.stamina += 10
    def f_belt(self):
        self.stamina += 2
    def f_cloak(self):
        self.stamina += 20
    def f_trinket(self):
        self.intellect += 45
    def f_legendary_weapon(self):
        self.intellect += 100

class mage:
    def __init__(self,name):
        self.cls = 'mage'
        self.dead = 0
        self.name = name
        self.stamina = 8
        self.wisdom = 19
        self.intellect = 20
        self.dexterity = 7
        self.strength = 6
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.miss = 150/self.intellect
        self.crit = self.intellect
        self.dict = ['burns','incinertes','scourches','glances','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Fireball']
        self.xp = 0
        self.lvl = 1
    def f_displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name, "\nLevel: ",self.lvl,"\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def f_abilities(self):
        print "Fireball(1).  This ability does {0} to {1} damage.\n".format(self.intellect*2,self.intellect*7)
        print "Barrier(2). This ability creates a magical shield that absorbs {0} to {1} damage.".format(self.intellect+(self.wisdom/2),(self.intellect+(self.wisdom/2))*2)
        print " "
    def f_ability0(self):
        damage = random.randrange(self.intellect*2,self.intellect*7)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            drawText('You MISS completely!',font,windowSurface,0,0,TEXTCOLOR)
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            dam = str(self.damage)
            drawText('Your Fireball CRITS for '+dam,font,windowSurface,0,0,TEXTCOLOR)
            print 'Your Fireball {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            dam = str(self.damage)
            drawText('Your Fireball hits for '+dam,font,windowSurface,0,0,TEXTCOLOR)
            print 'Your Fireball {0} for {1} damage.'.format(self.dict[random.randrange(0,4)],self.damage)
    def f_ability1(self):
    	self.damage = 0
        shield = random.randrange(self.intellect+(self.wisdom/2),(self.intellect+(self.wisdom/2))*2)
        self.shield = shield
        shield = str(shield)
        drawText('You create a '+shield+' point shield.',font,windowSurface,0,0,TEXTCOLOR)
        print "You create a {0} point shield".format(shield)
     
    #def f_ability2(self):
       
    def f_health(self):
        print "You have {0} health and {1} shield remaining".format(self.health, self.shield)
        
    def f_level(self):
        self.stamina += 2
        self.wisdom += 4
        self.intellect += 9
        self.dexterity += 1
        self.strength += 1
        self.health = self.stamina*10
        self.miss = 100/self.intellect
        self.crit = self.intellect
        self.lvl += 1
        lvl = str(self.lvl)
        drawText('You reached level '+lvl,font,windowSurface,0,0,TEXTCOLOR)
        print "\nYou've reached level {0}".format(self.lvl)
    def f_sword(self):
        self.intellect += 30
    def f_offhand(self):
        self.stamina += 10
    def f_belt(self):
        self.stamina += 2
    def f_cloak(self):
        self.stamina += 20
    def f_trinket(self):
        self.intellect += 45
    def f_legendary_weapon(self):
        self.intellect += 100
    def f_eye(self):
        self.stamina += 50
            
class warrior:
    def __init__(self,name):
        self.cls = 'warrior'
        self.dead = 0
        self.name = name
        self.stamina = 17
        self.wisdom = 7
        self.intellect = 4
        self.dexterity = 12
        self.strength = 21
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.tactics = 0
        self.miss = 100/self.strength
        self.crit = self.strength/1.5
        self.dict = ['SLICES','WOUNDS','HITS','GLANCES','DEMOLISHES','CRITS','MISSES']
        self.target = 'unknown'
        self.abilities = ['Heroic Slash']
        self.xp = 0
        self.lvl = 1
    def f_displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name,"\nLevel: ",self.lvl, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def f_abilities(self):
        print "Heroic Slash(1).  This ability does {0} to {1} damage.\n".format(self.strength*2,self.strength*4)
        print "Combat Tactics(2). This ability boosts your damage output and crit chance for three turns."
        print "Furious Barrage(3). Deals three swift strikes dealing {0} to {1} damage.".format(self.dexterity/2,(self.dexterity*2)+self.strength)
        print " "
    def f_ability0(self):
    	if(self.tactics > 0):
    		bonus_damage = round(self.strength*1.5, 0)
    		crit_cap = 85
    		self.tactics -= 1
    		drawText('Primed for battle...',font,windowSurface,0,0,TEXTCOLOR)
    		print "Primed for battle..."
    	else:
    		bonus_damage = 0
    		crit_cap = 100
        damage = random.randrange(self.strength*2,self.strength*4)+bonus_damage
        crit = random.randrange(1,crit_cap)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            drawText('You MISS completely!',font,windowSurface,0,25,TEXTCOLOR)
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            dam = str(self.damage)
            drawText('Your Heroic Slash CRITS for '+dam,font,windowSurface,0,25,TEXTCOLOR)
            print 'Your Heroic Slash {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            dam = str(self.damage)
            drawText('Your Heroic Slash hits for '+dam,font,windowSurface,0,25,TEXTCOLOR)
            print 'Your Heroic Slash {0} for {1} damage.'.format(self.dict[random.randrange(0,5)],self.damage)
    
    def f_ability1(self):
    	self.tactics = 3
        drawText('Your prepare yourself for battle!',font,windowSurface,0,0,TEXTCOLOR)
    	print "You prepare your self for battle!"
    	
    def f_ability2(self):
    	damage = 0
    	furious_bar = []
    	bonus_damage = 0;
    	if (self.tactics > 0):
    		bonus_damage = self.dexterity/2
    		crit_cap = 85
    		self.tactics -= 1
    	else:
    		bonus_damage = 0;
    		crit_cap = 100
    	for i in range(0,3):
    		crit = random.randrange(0,100)
    		miss = random.randrange(0,crit_cap)
    		if miss <= self.miss:
    			temp_damage = 0
    			furious_bar.append(temp_damage)
    		elif crit <= self.crit:
    			temp_damage = random.randrange(self.dexterity/2,((self.dexterity*2)+self.strength))*2+bonus_damage
    			furious_bar.append(temp_damage)
    		else:
    			temp_damage = random.randrange(self.dexterity/2,(self.dexterity*2)+self.strength)+bonus_damage
    			furious_bar.append(temp_damage)
    	damage += furious_bar[0] + furious_bar[1] + furious_bar[2]
    	self.damage = damage
    	dam1 = str(furious_bar[0])
    	dam2 = str(furious_bar[1])
    	dam3 = str(furious_bar[2])
        drawText('Primed for battle...',font,windowSurface,0,0,TEXTCOLOR)
        drawText('Your furious barrage of blows deal',font,windowSurface,0,25,TEXTCOLOR)
        drawText(dam1+', '+dam2+' and '+dam3,font,windowSurface,0,50,TEXTCOLOR)
    	print "Primed for battle..."
    	print "Your furious barrage of blows deal {0}, {1}, and {2} damage".format(furious_bar[0],furious_bar[1],furious_bar[2])
    		
    def f_health(self):
        print "You have {0} health remaining".format(self.health)
    def f_level(self):
        self.stamina += 6
        self.wisdom += 1
        self.intellect += 1
        self.dexterity += 3
        self.strength += 7
        self.health = self.stamina*10
        self.miss = 100/self.strength
        self.crit = self.strength/1.5
        self.lvl += 1
        lvl = str(self.lvl)
        drawText('You reached level '+lvl,font,windowSurface,0,0,TEXTCOLOR)
        print "\nYou've reached level {0}".format(self.lvl)
    def f_sword(self):
        self.strength += 30
    def f_offhand(self):
        self.strength += 15
    def f_belt(self):
        self.stamina += 2
    def f_cloak(self):
        self.stamina += 20
    def f_trinket(self):
        self.strength += 95
    def f_legendary_weapon(self):
        self.strength += 200
    def f_eye(self):
        self.stamina += 50

class cleric:
    def __init__(self,name):
        self.cls = 'cleric'
        self.dead = 0
        self.name = name
        self.stamina = 15
        self.wisdom = 10
        self.intellect = 10
        self.dexterity = 9
        self.strength = 18
        self.health = self.stamina*10
        self.shield = 0
        self.damage = 0
        self.empowered = 0
        self.miss = 100/(self.intellect + self.strength)
        self.crit = (self.wisdom + self.intellect)/1.5
        self.dict = ['cleanses','pierces','glances','devastates','hits','CRITS','misses']
        self.target = 'unknown'
        self.abilities = ['Holy Blow']
        self.xp = 0
        self.lvl = 1
    def f_displayStats(self):
        print "Class: ", self.cls, "\nName: ", self.name,"\nLevel: ",self.lvl, "\nStamina: ", self.stamina, "\nWisdom: ", self.wisdom, "\nIntellect: ",self.intellect, "\nDexterity: ",self.dexterity, "\nStrength: ",self.strength, "\nMiss: ",self.miss,"\nCrit: ",self.crit
    def f_abilities(self):
        print "Holy Blow(1).  This ability does {0} to {1} damage.\n".format(self.strength+self.intellect,(self.strength + self.intellect)*3)
        print "Devine Judgment(2). This ability does {0} to {1} damage.".format(self.wisdom*2, self.wisdom*5)
        print "You enter a state of devine empowerment adding addition effects to your next attack."
        print "Holy Blow will deal additional damage, Devine Judgment will heal you, Devine Sagicity grants 2 wisdom."
        print "Devine Sagicity(3) deals {0} damage, heals, and increases your wisdom by 1".format(self.wisdom)
    def f_ability0(self):
        damage = random.randrange((self.strength + self.intellect)*2,(self.strength + self.intellect)*3)
        crit = random.randrange(1,100)
        miss = random.randrange(1,100)
        if (self.empowered):
        	damage = round(damage*1.25,0)
        	self.empowered = 0
        if miss <= self.miss:
            self.damage = 0
            drawText('You MISS completely!',font,windowSurface,0,0,TEXTCOLOR)
            print "You MISS completely!"
        elif crit <= self.crit:
            self.damage = damage*2
            dam = str(self.damage)
            drawText('Your Holy Blow CRITS for '+dam,font,windowSurface,0,0,TEXTCOLOR)
            print 'Your Holy Blow {0} for {1} damage.'.format(self.dict[5],self.damage)
        else:
            self.damage = damage
            dam = str(self.damage)
            drawText('Your Holy Blow hits for '+dam,font,windowSurface,0,0,TEXTCOLOR)
            print 'Your Holy Blow {0} for {1} damage.'.format(self.dict[random.randrange(0,5)],self.damage)
        
    def f_ability1(self):
    	damage = random.randrange(self.wisdom*2, self.wisdom*5)
    	crit = random.randrange(1,100)
    	miss = random.randrange(1,100)
    	if (self.empowered):
    		self.health += round(damage*0.8, 0)
    		self.empowered = 0
    		heal = str(damage*0.8)
                drawText('You are healed for '+heal,font,windowSurface,0,0,TEXTCOLOR)
    		print "You are healed for {0}".format(damage*0.8)
    	else:
    		self.empowered = 1
                drawText('You feel empowered by a divine force!',font,windowSurface,0,0,TEXTCOLOR)
    		print "You feel empowered by a devine force!"
    	if miss <= self.miss:
    		self.damage = 0
                drawText('You MISS completely!',font,windowSurface,0,0,TEXTCOLOR)
    		print "You Missed!"
    	elif crit <= self.crit:
    		self.damage = damage * 2
    		dam = str(self.damage)
                drawText('Your Devine Judment CRITS for '+dam,font,windowSurface,0,25,TEXTCOLOR)
    		print "Your Devine Judgment CRITS for {0} damage.".format(self.damage)
    	else:
    		self.damage = damage
    		dam = str(self.damage)
                drawText('Your Devine Judment CRITS for '+dam,font,windowSurface,0,25,TEXTCOLOR)
    		print "Your Devine Judgment deals {0} damage.".format(self.damage)
    
    def f_ability2(self):
    	damage = self.wisdom
    	wisdom_gain = 1
    	heal_amt = round(self.wisdom*3.14, 0)
    	if (self.empowered):
    		wisdom_gain = 2
    		self.empowered = 0
    	else:
    		widsom_gain = 1
    	self.damage = damage
    	self.wisdom += wisdom_gain
    	self.health += heal_amt
    	wis = str(wisdom_gain)
    	dam = str(self.damage)
    	heal = str(heal_amt)
    	drawText(dam+' damage dealt',font,windowSurface,0,0,TEXTCOLOR)
    	drawText('Healed for '+heal,font,windowSurface,0,25,TEXTCOLOR)
    	drawText('Wisdom boosted by '+wis,font,windowSurface,0,50,TEXTCOLOR)
    	print "{0} damage dealt, healed for {1}, wisdom boosted by {2}.".format(damage, heal_amt, wisdom_gain)
    	
    def f_health(self):
        print "You have {0} health remaining".format(self.health)
    def f_level(self):
        self.stamina += 4
        self.wisdom += 3
        self.intellect += 3
        self.dexterity += 1
        self.strength += 5
        self.health = self.stamina*10
        self.miss = 100/(self.intellect + self.strength)
        self.crit = (self.wisdom + self.intellect)/1.5
        self.lvl += 1
        lvl = str(self.lvl)
        drawText('You reached level '+lvl,font,windowSurface,0,0,TEXTCOLOR)
        print "\nYou've reached level {0}".format(self.lvl)
    def f_sword(self):
        self.intellect += 30
    def f_offhand(self):
        self.strength += 15
    def f_belt(self):
        self.stamina += 2
    def f_cloak(self):
        self.stamina += 20
    def f_trinket(self):
        self.strength += 45
        self.intellect += 45
    def f_legendary_weapon(self):
        self.strength += 100
        self.intellect += 75
    def f_eye(self):
        self.stamina += 50
