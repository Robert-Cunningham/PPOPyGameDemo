import pygame
import game_settings
import random

class GameObject():
    """framework for all objects in the game"""
    def __init__(self, image, screen, width, height):
        self.image = image
        self.pos = self.image.get_rect()
        self.screen = screen
        self.width= width
        self.height= height

    def show(self):
        """blit to screen"""
        self.screen.blit(self.image, self.pos)

    def set_pos(self):
        xCoordinate=random.randint(0,(self.width*.9))
        yCoordinate=random.randint(0,(self.height*.9))
        self.pos.x= xCoordinate
        self.pos.y= yCoordinate

    def check_collision(self, other):
        other_rect = other.pos
        return self.pos.colliderect(other_rect)

class PlayerObject(GameObject):
    def __init__(self, image, screen, width, height, speed):
        GameObject.__init__(self, image, screen, width, height)
        self.speed = speed
        self.pos= image.get_rect()
        self.width = width
        self.height = height

    

    def moveUp(self):
        if self.pos.top >= 0:
            self.pos.y -= self.speed

    def moveDown(self):
        if self.pos.bottom <= self.height:
            self.pos.y += self.speed

    def moveLeft(self):
        if self.pos.left >= 0:
            self.pos.x -= self.speed

    def moveRight(self):
        if self.pos.right <= self.width:
            self.pos.x += self.speed
        
    def returnPlayerPos(self):
        self.my_player_pos=(self.pos.x, self.pos.y)
        return self.my_player_pos

class EnemyObject(GameObject):
    def __init__(self, image, screen, width, height):
        GameObject.__init__(self, image, screen, width, height)
        self.pos= image.get_rect()

    def returnEnemyPos(self):
        self.my_enemy_pos=(self.pos.x, self.pos.y)
        return self.my_enemy_pos
        
class DestinationObject(GameObject):
    def __init__(self, image, screen, width, height):
        GameObject.__init__(self, image, screen, width, height)
        self.pos= image.get_rect()
        
    def returnDestinationPos(self):
        self.my_dest_pos=(self.pos.x, self.pos.y)
        return self.my_dest_pos
        
