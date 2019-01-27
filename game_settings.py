import pygame
import game_objects

file_pc = 'blue.png'
file_ec = 'redd.png'
file_dc = 'green.png'

blueImage= pygame.image.load(file_pc)
blueImage=pygame.transform.scale(blueImage,(15,15))

redImage= pygame.image.load(file_ec)
redImage=pygame.transform.scale(redImage,(15,15))

greenImage= pygame.image.load(file_dc)
greenImage= pygame.transform.scale(greenImage,(25,25))


size = width, height = 500, 500
screen = pygame.display.set_mode(size)

player_speed = 6

game_state = 'ongoing'

def check_game_state(player, enemies, destination, game_state):
    if game_state == 'ongoing':
        # Game status flag variables
        lost_game = False
        won_game = False

        # Check status of game
        for enemy in enemies:
            if player.check_collision(enemy):
                lost_game = True
                break
            
        if player.check_collision(destination):
            won_game = True

        # Updating game_state
        if won_game:
            game_state = 'victory'
        if lost_game:
            game_state = 'defeat'
    return game_state
