import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_set, screen, stats, sb, play_button, ship, aliens, bullets):
    #Keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kdown_events(event, ai_set, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_kup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_set, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_set, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    #start new game on click
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset game settings
        ai_set.initialize_dynamic_settings()
        #hide mouse cursor
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #reset scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
    #empty list of aliens and bullets
    aliens.empty()
    bullets.empty()

    #create new fleet and center ship
    create_fleet(ai_set, screen, ship, aliens)
    ship.center_ship()

#if key is pressed up
def check_kdown_events(event, ai_set, screen, stats, ship, bullets):
    #move ship to the right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_set, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        stats.game_active = True



#if key is pressed down
def check_kup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_set, screen, stats, sb, ship, alien, bullets, play_button):
    screen.fill(ai_set.bg_color)
    ship.blitme()
    #draw vs  blitme
    alien.draw(screen)
    #redraw all bullets behind ships and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet(stats)

    #draw scoreboard
    sb.show_score()

    #drwa play button if gam eis inactive
    if not stats.game_active:
        play_button.draw_button()

    #make the drawscreen visible
    pygame.display.flip()

def fire_bullet(ai_set, screen, ship, bullets):
    #create new bullet and add into group
    if len(bullets) < ai_set.bullets_allowed:
        new_bullet = Bullet(ai_set, screen, ship)
        bullets.add(new_bullet)

def update_bullets(ai_set, screen, stats, sb, ship, aliens, bullets):
        #group for bullets
        bullets.update()
        #get rid of bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        check_collisions(ai_set, screen, stats, sb, ship, aliens, bullets)

def new_level(ai_set, screen, stats, sb, ship, aliens, bullets):
    #destroy existing bullets and respawn
    bullets.empty()
    ai_set.inc_speed()
    #increase level
    stats.level += 1
    sb.prep_level()
    create_fleet(ai_set, screen, ship, aliens)

def check_collisions(ai_set, screen, stats, sb, ship, aliens, bullets):
    #check if bullets collided, you can set first True to False for a super powered bullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_set.alien_points #update score if there is a collision
            sb.prep_score() #keep showing scores every time it updates
        check_high_score(stats, sb)

    if len(aliens) == 0:
        new_level(ai_set, screen, stats, sb, ship, aliens, bullets)


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

def update_aliens(ai_set, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_set, aliens)
    #update positions of aliens
    aliens.update()

    #look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_set, stats, screen, sb, ship, aliens, bullets)

    #look for aliens at bottom screen
    bottom_hit(ai_set, stats, screen, sb, ship, aliens, bullets)

def ship_hit(ai_set, stats, screen, sb, ship, aliens, bullets):
    #Decrement if ship gets hit
    if stats.ships_left > 0:
        stats.ships_left -= 1
        #update number of ships
        sb.prep_ships()

        #empty list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create new fleet and center a ship
        create_fleet(ai_set, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def bottom_hit(ai_set, stats, screen, sb, ship, aliens, bullets):
    #check if reached bottom
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_set, stats, screen, sb, ship, aliens, bullets)

            break

def check_high_score(stats, sb):
    #check to see if there's a new high score
    hs_file = open('highscore.txt', 'w')
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        #write high score to file
        hs_file.write(str(stats.score))

        sb.prep_high_score()
    hs_file.close()
