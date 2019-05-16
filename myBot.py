#! /usr/bin/python
#-*- coding: utf-8 -*-

from robot import Robot #Import a base Robot

class MyBot(Robot): #Create a Robot

    def init(self):    #To initialyse your robot
        
        
        #Set the bot color in RGB
        self.setColor(0, 0, 0)
        self.setGunColor(66, 134, 244)
        self.setRadarColor(226, 111, 111)
        self.setBulletsColor(45, 0, 0)

        self.radarVisible(True) # if True the radar field is visible
        
        #get the map size
        size = self.getMapSize()
        
        self.lockRadar("gun")
        self.count = True #count when shots missed
        self.turnNo = 0 #counts every time run is exected
        self.direction = 1 # direction of movement when not in range
        
    
    def run(self): #main loop to command the bot
        
        self.turnNo = self.turnNo + 1 # increment turn
        self.gunTurn(-20) # rotate gun
        if(self.turnNo > 40):# if not in range move
            self.turn(5*self.direction)
            self.move(40)


    def onHitWall(self):
        self.reset() #To reset the run fonction to the begining
        self.turn(30)
        self.move(25)
        self.rPrint('ouch! a wall !')
        self.direction = -self.direction

    def sensors(self): #NECESARY FOR THE GAME
        pass
        
    def onRobotHit(self, robotId, robotName): # when My bot hit another
        self.rPrint('collision with:' + str(robotId))
        
    def onHitByRobot(self, robotId, robotName):
        self.rPrint("damn a bot collided me!")

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): #NECESARY FOR THE GAME
        """ When i'm hit by a bullet"""
        self.rPrint ("hit by " + str(bulletBotId) + "with power:" +str( bulletPower))
        self.turn(-20)
        self.move(-40)
        
    def onBulletHit(self, botId, bulletId):#NECESARY FOR THE GAME
        """when my bullet hit a bot"""
        self.rPrint ("fire done on " +str( botId))
        self.count = 0
        
    def onBulletMiss(self, bulletId):#NECESARY FOR THE GAME
        """when my bullet hit a wall"""
        self.rPrint ("the bullet "+ str(bulletId) + " fail")
        #if missing for two turns move
        self.count = self.count + 1
        if(self.count > 2):
            self.Turn(-20)
            self.move(-30)
            self.count = 0
        
    def onRobotDeath(self):#NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint ("damn I'm Dead")
        
    def onTargetSpotted(self, botId, botName, botPos):#NECESARY FOR THE GAME
        "when the bot see another one"
        self.setRadarField("thin")
        self.rPrint("I see the bot:" + str(botId) + "on position: x:" + str(botPos.x()) + " , y:" + str(botPos.y()))

        #Scatter fire
        self.fire(4)
        self.gunTurn(-2)
        self.stop()
        self.fire(6)
        self.gunTurn(2)
        self.stop()
        self.fire(4)
        self.gunTurn(-4)
        
        self.turnNo = 0 #Reset turn counter
