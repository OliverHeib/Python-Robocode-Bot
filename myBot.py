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
        self.gt = True
        self.count = True
        
    
    def run(self): #main loop to command the bot
        
        #self.move(90) # for moving (negative values go back)
        #self.stop()
        self.gunTurn(-20)

        self.count = self.count + 1

        if (self.count == 10):
            self.gt = True
            self.count = 0

        #self.stop()


    def onHitWall(self):
        self.reset() #To reset the run fonction to the begining (auomatically called on hitWall, and robotHit event) 
        self.pause(100)
        self.turn(30)
        self.move(-100)
        self.rPrint('ouch! a wall !')

    def sensors(self): #NECESARY FOR THE GAME
        pass
        
    def onRobotHit(self, robotId, robotName): # when My bot hit another
        self.rPrint('collision with:' + str(robotId))
        
    def onHitByRobot(self, robotId, robotName):
        self.rPrint("damn a bot collided me!")

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower): #NECESARY FOR THE GAME
        """ When i'm hit by a bullet"""
        self.rPrint ("hit by " + str(bulletBotId) + "with power:" +str( bulletPower))
        self.turn(20)
        self.move(30)
        
    def onBulletHit(self, botId, bulletId):#NECESARY FOR THE GAME
        """when my bullet hit a bot"""
        self.rPrint ("fire done on " +str( botId))
        #self.stop()
        
    def onBulletMiss(self, bulletId):#NECESARY FOR THE GAME
        """when my bullet hit a wall"""
        self.rPrint ("the bullet "+ str(bulletId) + " fail")
        self.gt = True
        #self.gunTurn(-45)
        
    def onRobotDeath(self):#NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint ("damn I'm Dead")
        
    def onTargetSpotted(self, botId, botName, botPos):#NECESARY FOR THE GAME
        "when the bot see another one"
        self.setRadarField("thin")
        self.rPrint("I see the bot:" + str(botId) + "on position: x:" + str(botPos.x()) + " , y:" + str(botPos.y()))
        #self.gunTurn(-1)
        #self.gt = False

        #self.stop()
        
        self.fire(10)
        self.gunTurn(-5)