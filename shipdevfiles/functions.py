import sys
import pygame
from bullet import Bullet

def check_events(ai_set, screen, ship, bullets):
    #Keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kdown_events(event, ai_set, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_kup_events(event, ship)

#if key is pressed up
def check_kdown_events(event, ai_set, screen, ship, bullets):
    #move ship to the right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_set, screen, ship, bullets)


#if key is pressed down
def check_kup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_set, screen, ship, bullets):
    screen.fill(ai_set.bg_color)
    ship.blitme()
    #redraw all bullets behind ships and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #make the drawscreen visible
    pygame.display.flip()

def fire_bullet(ai_set, screen, ship, bullets):
    #create new bullet and add into group
    if len(bullets) < ai_set.bullets_allowed:
        new_bullet = Bullet(ai_set, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
        #group for bullets
        bullets.update()
        #get rid of bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
