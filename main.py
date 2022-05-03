from tkinter import Y
import pygame
import random
from sys import exit

pygame.init()
width = 900
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Close the Gap')

#set fps
clock = pygame.time.Clock()
fps = 60

#font setup
font_size = 25 #operates also as enemy size
word_font = pygame.font.Font('surfaces/RobotoCondensed-Regular.ttf', font_size)

#set up game background and resize
bkg_surface = pygame.image.load('surfaces/game-bkg.jpg') 
bkg = pygame.transform.scale(bkg_surface,(width, 600))

platform_surface = pygame.image.load('surfaces/platform.png').convert_alpha() #converts file in to something pygame can work wth easily
platform_size = pygame.transform.scale(platform_surface,(1500,250))
platform_rect = platform_size.get_rect(midtop = (450,550))

#player setup
player = pygame.image.load('surfaces/face-forward.png').convert_alpha()
player_size = pygame.transform.scale(player, (100,100))
player_rect = player_size.get_rect(midbottom = (250, 600))
player_pos = [player_rect.x,player_rect.y]
#enemy setup
enemy_x = random.randrange(width-font_size)
enemy_y = 0
enemy_pos = (enemy_x,enemy_y)
enemy_speed = 5

enemy_1 = word_font.render('Wage Gap', True, 'White')
enemy_1_rect = enemy_1.get_rect(midtop = enemy_pos)
enemy_1_surf = pygame.draw.rect(screen, 'Black', enemy_1_rect)

enemy_2 = word_font.render('Gender Gap', True, 'White')
enemy_2_rect = enemy_2.get_rect(midtop = enemy_pos)
enemy_2_surf = pygame.draw.rect(screen, 'Black', enemy_2_rect)

enemy_3 = word_font.render('Sexism', True, 'White')
enemy_3_rect = enemy_3.get_rect(midtop = enemy_pos)
enemy_3_surf = pygame.draw.rect(screen, 'Black', enemy_3_rect)

enemy_4 = word_font.render('Isolation', True, 'White')
enemy_4_rect = enemy_4.get_rect(midtop = enemy_pos)
enemy_4_surf = pygame.draw.rect(screen, 'Black', enemy_4_rect)

enemy_5 = word_font.render('Bias', True, 'White')
enemy_5_rect = enemy_5.get_rect(midtop = enemy_pos)
enemy_5_surf = pygame.draw.rect(screen, 'Black', enemy_5_rect)

enemy_6 = word_font.render('Harrasment', True, 'White')
enemy_6_rect = enemy_6.get_rect(midtop = enemy_pos)
enemy_6_surf = pygame.draw.rect(screen, 'Black', enemy_6_rect)

enemy_lst = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6]

# def update_enemy_position(x,y, costume):
#     screen.blit(costume, (x,y))



enemy_coords = []
def enemies_fall(enemy_coords):
    if len(enemy_coords) < 10:
        enemy_x = random.randint(0, width-font_size)
        enemy_y = 0
        enemy_coords.append([enemy_x,enemy_y]) 
        

def choose_enemy(enemy_coords):
    for enemy in enemy_coords:
        enemy_surf = pygame.draw.rect(screen, 'Black', (enemy[0],enemy[1], 100, font_size))
        return enemy_surf


def update_fall(enemy_coords):
    for index, coord in enumerate(enemy_coords):
        if coord[1] >= 0 and coord[1] < height:
            coord[1] +=1
        else:
            enemy_coords.pop(index)

def collision(player_pos,enemy_pos):
        player_x = player_pos[0]
        player_y = player_pos[1]

        enemy_x = enemy_pos[0]
        enemy_y = enemy_pos[1]

        if (enemy_x >= player_x and enemy_x < (player_x + 100)) or (player_x >= enemy_x and player_x <(enemy_x + 100)):
            if (enemy_y >= player_y and enemy_y < (player_y + 25)) or (player_y >= enemy_y and player_y < (enemy_y + 25)):
                return True
        return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            speed = 1
            if event.key == pygame.K_LEFT:
                pygame.key.set_repeat(5) #holds down key
                player_rect.x -= speed
            elif event.key == pygame.K_RIGHT:
                pygame.key.set_repeat(5)
                player_rect.x += speed

    # enemy_y += enemy_speed
    # if enemy_y >= height:
    #     enemy_y = 0
    #     enemy_x = random.randrange(width-font_size)
    

    screen.blit(bkg,(0,0))
    screen.blit(platform_size, platform_rect)
    
    screen.blit(player_size, player_rect)
    # pygame.draw.rect(screen, 'Black', enemy_1_rect)
    # # pygame.draw.rect(screen, 'Green', enemy_1_rect, 10)
    # pygame.draw.rect(screen, 'Black', enemy_2_rect)
    # pygame.draw.rect(screen, 'Black', enemy_3_rect)
    # pygame.draw.rect(screen, 'Black', enemy_4_rect)
    # pygame.draw.rect(screen, 'Black', enemy_5_rect)
    # pygame.draw.rect(screen, 'Black', enemy_6_rect)

    # screen.blit(enemy_1,enemy_1_rect)
    enemies_fall(enemy_coords)
    choose_enemy(enemy_coords)
    update_fall(enemy_coords)
    
    if player_rect.colliderect(choose_enemy(enemy_coords)):
        print('collision')# should actually change score 

    clock.tick(fps)
    pygame.display.update()
    