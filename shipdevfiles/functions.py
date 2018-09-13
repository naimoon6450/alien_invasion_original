import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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
    elif event.key == pygame.K_q:
        sys.exit()



#if key is pressed down
def check_kup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_set, screen, ship, alien, bullets):
    screen.fill(ai_set.bg_color)
    ship.blitme()
    #draw vs  blitme
    alien.draw(screen)
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

def update_bullets(ai_set, screen, ship, aliens, bullets):
        #group for bullets
        bullets.update()
        #get rid of bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        check_collisions(ai_set, screen, ship, aliens, bullets)



def check_collisions(ai_set, screen, ship, aliens, bullets):
    #check if bullets collided, you can set first True to False for a super powered bullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        #destroy existing bullets and respawn
        bullets.empty()
        create_fleet(ai_set, screen, ship, aliens)

def get_alien_num_x(ai_set, alien_width):
    #num of aliens fit in a row
    avail_space_x = ai_set.screen_width - 2*alien_width
    num_alien_x = int(avail_space_x / (2*alien_width))
    return num_alien_x

def create_alien(ai_set, screen, aliens, alien_num, row_num):
    #create alien and place in row
    alien = Alien(ai_set, screen) #for dimensional purposes
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_num
    aliens.add(alien)

def create_fleet(ai_set, screen, ship, aliens):
    #create fleet of aliens
    #create aliens and find number of aliens in row
    #spacing between aliens is 1 alien
    alien = Alien(ai_set, screen)
    num_alien_x = get_alien_num_x(ai_set, alien.rect.width)
    num_rows = get_rows(ai_set, ship.rect.height, alien.rect.height) - 2

    #first row of aliens
    for row_number in range(num_rows):
        for alien_num in range(num_alien_x):
            #create alien and place in row
            create_alien(ai_set, screen, aliens, alien_num, row_number)

def get_rows(ai_set, ship_height, alien_height):
    avail_space_y = (ai_set.screen_height - (3*alien_height) - ship_height)
    num_rows = int(avail_space_y / (2*alien_height))
    return num_rows

def check_fleet_edges(ai_set, aliens):
    #respond to edges
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_dir(ai_set, aliens)
            break

def change_fleet_dir(ai_set, aliens):
    #drop ensire fleet and change dir
    for alien in aliens.sprites():
        alien.rect.y += ai_set.fleet_drop_speed
    ai_set.fleet_direction *= -1

def update_aliens(ai_set, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_set, aliens)
    #update positions of aliens
    aliens.update()

    #look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_set, stats, screen, ship, aliens, bullets)

def ship_hit(ai_set, stats, screen, ship, aliens, bullets):
    #Decrement if ship gets hit
    stats.ships_left -= 1

    #empty list of aliens and bullets
    aliens.empty()
    bullets.empty()

    #create new fleet and center a ship
    create_fleet(ai_set, screen, ship, aliens)
    ship.center_ship()

    #pause
    sleep(0.5)
