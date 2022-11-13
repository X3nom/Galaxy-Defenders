# version used for testing    
#Controls: left shift- dash, a- machinegun, s- shield, d- guided bullet
from math import e
import pygame,sys,random
from pygame import display
from pygame.constants import KEYDOWN, KEYUP


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()

#variables
score = 0
gravity = 0.25
asteroid_movement = 0
spaceship_movement = 300
spaceship_movement_y = 700
bullet_movement = 0
bullet_cooldown = 40
guided_bullet_y = -100
guided_bullet_x = 0
guided_bullet_kills = 0
enemy_bullet_movement = 900
enemy_bullet_countdown = 120
enemy_guided_bullet_y = 900
enemy_guided_bullet_x = 0
enemy_guided_bullet_countdown = 900
left = False
right = False
up = False
down = False
player_lifes = 5
damage_cooldown = 0
power_percent = 0
power_cooldown = 0
power_color = 255
shield = False
machinegun = False
lifes_color = 255
font = pygame.font.SysFont("Small Fonts",30)
#surfaces, rectangles
bg_surface = pygame.image.load(r"galaxy defenders\galaxydefenders_images\SpaceBackground1.jpg").convert()
bg_surface = pygame.transform.scale(bg_surface,(600,800))
spaceship = pygame.image.load(r"galaxy defenders\galaxydefenders_images\SpaceShip1.png")
spaceship = pygame.transform.scale(spaceship,(100,100))
spaceship_r = spaceship.get_rect(center = (300,700))
asteroid = pygame.image.load(r"galaxy defenders\galaxydefenders_images\asteroid1.png")
asteroid = pygame.transform.scale(asteroid,(100,100))
asteroid_r = asteroid.get_rect(center = (random.randint(0,600),0))
bullet = pygame.image.load(r"galaxy defenders\galaxydefenders_images\laser_bullet_red.png")
bullet = pygame.transform.scale(bullet,(30,50))
bullet_r = bullet.get_rect(center = (spaceship_r.centerx,spaceship_r.centery))
guided_bullet = pygame.image.load(r"galaxy defenders\galaxydefenders_images\sphere_bullet_red.png")
guided_bullet = pygame.transform.scale(guided_bullet,(50,50))
guided_bullet_r = guided_bullet.get_rect(center = (0,0))
enemy_bullet = pygame.image.load(r"galaxy defenders\galaxydefenders_images\laser_bullet_green.png")
enemy_bullet = pygame.transform.scale(enemy_bullet,(30,50))
enemy_bullet_r = enemy_bullet.get_rect(center = (0,0))
enemy_guided_bullet = pygame.image.load(r"galaxy defenders\galaxydefenders_images\sphere_bullet_green.png")
enemy_guided_bullet = pygame.transform.scale(enemy_guided_bullet,(50,50))
enemy_guided_bullet_r = enemy_guided_bullet.get_rect(center = (0,0))
explosion = pygame.image.load(r"galaxy defenders\galaxydefenders_images\explosion.png")
explosion = pygame.transform.scale(explosion,(100,100))
explosion_r = explosion.get_rect(center = (0,0))
shield_picture = pygame.image.load(r"galaxy defenders\galaxydefenders_images\sphere_bullet_blue.png")
shield_picture = pygame.transform.scale(shield_picture,(100,100))
game_over = pygame.image.load(r"galaxy defenders\galaxydefenders_images\GameOver.jpg")
game_over = pygame.transform.scale(game_over,(600,300))

#gameloop
while True:
#events         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True

        if event.type == KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False

            if power_percent >= 20 and event.key == pygame.K_LSHIFT:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    power_percent -= 20
                if left == True and spaceship_movement > 300:
                    spaceship_movement -= 300
                elif left == True:
                    spaceship_movement = 50

                if right == True and spaceship_movement < 300:
                    spaceship_movement += 300
                elif right == True:
                    spaceship_movement = 550

                if up == True and spaceship_movement_y > 300:
                    spaceship_movement_y -= 300
                elif right == True:
                    spaceship_movement_y = 0

                if down == True and spaceship_movement_y < 400:
                    spaceship_movement_y += 300
                elif right == True:
                    spaceship_movement_y = 700
            if power_percent >= 35 and event.key == pygame.K_d:
                power_percent -= 35
                guided_bullet_kills = 0
                guided_bullet_y = spaceship_r.centery
                guided_bullet_x = spaceship_r.centerx
            if power_percent >= 70 and event.key == pygame.K_s:
                shield = True
                power_cooldown = 400
                power_percent -= 70
            if power_percent == 100 and event.key == pygame.K_a:
                machinegun = True
                power_cooldown = 600
                power_percent -= 100
    #game over
    if asteroid_movement > 800 or player_lifes <= 0:
        player_lifes = 0
        screen.blit(game_over,(0,-100))
        scoretext = font.render(f"Score: {score}",False,(255,255,255))
        screen.blit(scoretext,(200,130))
        text2 = font.render(f"Press <space> to restart...",False,(random.randint(10,255),random.randint(10,255),random.randint(10,255)))
        screen.blit(text2,(200,150))
        pygame.display.update()
        while player_lifes == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #reset variables
                        score = 0
                        gravity = 0.25
                        asteroid_movement = 0
                        spaceship_movement = 300
                        spaceship_movement_y = 700
                        bullet_movement = 0
                        guided_bullet_y = -100
                        guided_bullet_x = 0
                        enemy_bullet_movement = 900
                        enemy_guided_bullet_y = 900
                        enemy_guided_bullet_x = 0
                        enemy_guided_bullet_countdown = 900
                        left = False
                        right = False
                        enemy_bullet_countdown = 120
                        player_lifes = 5
                        power_percent = 0
                        shield = False
                        machinegun = False
                        lifes_color = 255
#background
    screen.blit(bg_surface,(0,0))
#spaceship movement
    if left == True:
        if spaceship_movement > 0:
            spaceship_movement -= 10
    if right == True:
        if spaceship_movement < 600:
            spaceship_movement += 10
    if up == True:
        if spaceship_movement_y > 0:
            spaceship_movement_y -= 10
    if down == True:
        if spaceship_movement_y < 700:
            spaceship_movement_y += 10
    spaceship_r.centerx = spaceship_movement
    spaceship_r.centery = spaceship_movement_y
    screen.blit(spaceship,spaceship_r)
#asteroid
    asteroid_movement += gravity
    asteroid_r.centery = asteroid_movement
    screen.blit(asteroid,asteroid_r)
#bullet movement
    if machinegun == True:
        bullet_cooldown -= 4
        bullet_movement -= 100
    else:
        bullet_cooldown -= 1
        bullet_movement -= 20
    if bullet_cooldown <= 0:
        bullet_cooldown = 40
        bullet_movement = spaceship_r.centery
        bullet_r.centerx = spaceship_r.centerx
    bullet_r.centery = bullet_movement
    screen.blit(bullet,bullet_r)
#guided bullet movement
    if guided_bullet_y < (asteroid_r.centery) and guided_bullet_y > 0 and guided_bullet_kills <=3:
        guided_bullet_y += 10
    else:
        guided_bullet_y -= 8
    if guided_bullet_x < asteroid_r.centerx and guided_bullet_kills <= 3:
        guided_bullet_x += 6
    if guided_bullet_x > asteroid_r.centerx and guided_bullet_kills <= 3:
        guided_bullet_x -= 6
    guided_bullet_r.centery = guided_bullet_y
    guided_bullet_r.centerx = guided_bullet_x
    screen.blit(guided_bullet,guided_bullet_r)
#enemy bullet movement
    enemy_bullet_countdown -= 1
    enemy_bullet_movement += 15
    if enemy_bullet_countdown == 0:
        enemy_bullet_r.centerx = spaceship_r.centerx
        enemy_bullet_movement = 0
        enemy_bullet_countdown = random.randint(60,600)
    enemy_bullet_r.centery = enemy_bullet_movement
    screen.blit(enemy_bullet,enemy_bullet_r)
#enemy guided bullet movement
    enemy_guided_bullet_countdown -= 1
    enemy_guided_bullet_y += 4
    if enemy_guided_bullet_y >= (spaceship_r.centery - 500):
        if enemy_guided_bullet_x < spaceship_r.centerx:
            enemy_guided_bullet_x += 2
        if enemy_guided_bullet_x > spaceship_r.centerx:
            enemy_guided_bullet_x -= 2
    if enemy_guided_bullet_countdown == 0: #guided bullet spawn
        enemy_guided_bullet_y = 0
        enemy_guided_bullet_x = random.randint(0,600)
        enemy_guided_bullet_countdown = random.randint(300,1000)
    enemy_guided_bullet_r.centerx = enemy_guided_bullet_x
    enemy_guided_bullet_r.centery = enemy_guided_bullet_y
    screen.blit(enemy_guided_bullet,enemy_guided_bullet_r)
    
#bullet collission
    if bullet_r.colliderect(asteroid_r):
        screen.blit(explosion,asteroid_r)
        asteroid_r.centerx = (random.randint(0,600))
        asteroid_r.centery = 0
        asteroid_movement = 0
        gravity += 0.05
        score += 1
        if (power_percent % 5) != 0:
            while (power_percent % 5) != 0:
                power_percent += 1
        if power_percent != 100 and machinegun != True:
            power_percent += 5
        elif power_percent != 100 and machinegun == True:
            power_percent += 2
#guided bullet collision
    if guided_bullet_r.colliderect(asteroid_r):
        screen.blit(explosion,asteroid_r)
        asteroid_r.centerx = (random.randint(0,600))
        asteroid_r.centery = 0
        asteroid_movement = 0
        gravity += 0.05
        score += 1
        power_percent += 1
        guided_bullet_kills += 1
#enemy bullet collision
    if damage_cooldown != 0:
        damage_cooldown -= 1
    elif shield == False:
        if enemy_bullet_r.colliderect(spaceship_r):
            screen.blit(explosion,spaceship_r)
            player_lifes -= 1
            damage_cooldown = 40
            lifes_color -= 45
    else:
        screen.blit(shield_picture,spaceship_r)
#enemy guided bullet collision
    if shield == False and damage_cooldown == 0:
        if enemy_guided_bullet_r.colliderect(spaceship_r):
            screen.blit(explosion,spaceship_r)
            player_lifes -= 1
            damage_cooldown = 40
            lifes_color -= 45

#power
    if shield == True or machinegun == True:
        power_cooldown -= 1
        if power_cooldown == 0:
            shield = False
            machinegun = False
    screen.blit(game_over,(0,750))
    scoretext = font.render(f"Score: {score}",False,(255,255,255))
    powerguidetext = [["[d]-homing missile",0], ["[s]-shield",250], ["[a]-machinegun",400]]
    power_needed = [35,70,100]
    lifestext = font.render(f"lifes: {player_lifes}",False,(255,lifes_color,lifes_color))
    power_color = (255 - power_percent * 2.55)
    powertext = font.render(f"power: {power_percent}%",False,(power_color,255,power_color))
    screen.blit(scoretext,(5,765))
    screen.blit(powertext,(240,765))
    screen.blit(lifestext,(450,(765)))

    for i in range(3):
        color = (255,0,0)
        if power_percent >= power_needed[i]:
            color = (0,255,0)
        screen.blit(font.render(powerguidetext[i][0],False,color),(powerguidetext[i][1],725))
#display update
    pygame.display.update()
    clock.tick(60)