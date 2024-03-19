# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

print(screen.get_height())
while running:
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    print(player_pos)
    pygame.draw.circle(screen, "red", player_pos, 25)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_pos.y > 30:
                player_pos.y -= 20
            if event.key == pygame.K_DOWN and player_pos.y < screen.get_height() - 30:
                player_pos.y += 20
            if event.key == pygame.K_LEFT and player_pos.x > 30:
                player_pos.x -= 20
            if event.key == pygame.K_RIGHT and player_pos.x < screen.get_width() - 30:
                player_pos.x += 20
            

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pygame.quit()