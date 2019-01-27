import sys, pygame
import game_settings as gs
import game_objects as go
import time

should_render = True


#call function reset board
#return list with how the board looks (x y coord) for each player
#call function step (take left or right or up or down)
#return three things state of world, game over or not//if the game is over (did I win or lose)//(lost: return -1)(other wise: distance b/w me and the flag) 

pygame.init()


class BestGameEver():
    def __init__(self):
        self.myDestination = go.DestinationObject(gs.greenImage, gs.screen,gs.size[0], gs.size[1])
        self.myPlayer= go.PlayerObject(gs.blueImage,gs.screen,gs.size[0], gs.size[1], gs.player_speed)
        self.enemies=[]
        self.total_steps = 0
        
    def reset(self):
        self.total_steps = 0
        self.myPlayer= go.PlayerObject(gs.blueImage,gs.screen,gs.size[0], gs.size[1], gs.player_speed)
        self.myPlayer.set_pos()
        self.myDestination= go.DestinationObject(gs.greenImage, gs.screen,gs.size[0], gs.size[1])
        dest_valid_pos= False
        while not dest_valid_pos:
            self.myDestination.set_pos()
            if not (self.myDestination.check_collision(self.myPlayer)):
                dest_valid_pos=True
                break
    
        self.enemies=[]
    
    
        # Generating 15 new enemy objects, randomly generating their position, whilst checking that they are not
        # in the same location as myPlayer, myDestination, or other enemy objects
        for i in range(15):
            myEnemy= go.EnemyObject(gs.redImage, gs.screen,gs.size[0], gs.size[1])
            pos_valid = False
            while not pos_valid:
                myEnemy.set_pos()
                if not(myEnemy.check_collision(self.myPlayer) and myEnemy.check_collision(self.myDestination)):
                    pos_valid = True
                    for enemy in self.enemies:
                        if enemy.check_collision(myEnemy):
                            pos_valid = False      
            self.enemies.append(myEnemy)

        return self.findAllCoordinates()
    
    
    def findAllCoordinates(self):
        coordinates=[]
        coordinates.extend(self.myPlayer.returnPlayerPos())
        coordinates.extend(self.myDestination.returnDestinationPos())
        for enemy in self.enemies:
            coordinates.extend(enemy.returnEnemyPos())
    
        return [float(x)/500 for x in coordinates]
        
    
    def distanceToTarget(self):
        
        dist = ((self.myDestination.pos.x-self.myPlayer.pos.x)**2 + (self.myDestination.pos.y-self.myPlayer.pos.y)**2)**0.5
        return dist
    
    
    def step(self,move, slow=False):
        global should_render

        self.total_steps += 1

        if self.total_steps > 100:
            return (None, -1000, True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        if should_render:
            gs.screen.fill((0,0,0))
            self.myPlayer.show()
            self.myDestination.show()
            for enemy in self.enemies:
                enemy.show()
            
        if (gs.game_state=='ongoing'):
            if move== 0:
                self.myPlayer.moveLeft()
            elif move==2:
                self.myPlayer.moveRight()
            elif move==1:
                self.myPlayer.moveUp()
            elif move==3:
                self.myPlayer.moveDown()
    
        pygame.display.flip()
        gs.game_state= gs.check_game_state(self.myPlayer, self.enemies, self.myDestination, gs.game_state)
    

        if slow or True:
            #time.sleep(.05)
            pygame.time.delay(5)
    
    
        reward = None
        done = False
        if gs.game_state == 'victory':
            reward = 200000
            done = True
            print('We win, motherfucker')
        elif gs.game_state == 'defeat':
            reward = -1000
            done = True
        elif gs.game_state == 'ongoing':
            reward = -self.distanceToTarget() / 5
        
        game_coordinates=self.findAllCoordinates()     

        gs.game_state = 'ongoing'
        return (game_coordinates, reward, done)




