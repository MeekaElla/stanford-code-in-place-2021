import pygame
import random

pygame.init()

# initialize clock
clock = pygame.time.Clock()
speed = 30

display_width = 500
display_height = 300

# ball settings
x = 100
y = 100
radius = 10
dx = 3
dy = 3

# paddle settings
paddle_x = 10
paddle_y = 10
paddle_width = 3
paddle_height = 40

# score settings
play_score = 0


def hit_back():
    if x + radius > display_width:
        return True
    return False


def hit_sides():
    # top
    if y - radius < 0:
        return True
    # bottom
    if y + radius > display_height:
        return True
    return False


def hit_paddle():
    global play_score

    if (
            x - radius <= paddle_x + paddle_width
            and paddle_y < y < paddle_y + paddle_height
    ):
        play_score += 100
        return True


def game_over():
    global play_score

    end_game = True
    display.fill(color=(0,0,0))

    font_title = pygame.font.Font(None, 36)
    font_instructions = pygame.font.Font(None, 24)

    announcement = font_title.render("Game Over!", True, (255,255,255))
    announcement_rect = announcement.get_rect(center=(int(display_width/2), (int(display_height/3))))
    display.blit(source=announcement, dest=announcement_rect)

    qinstructions = font_instructions.render("Press q to quit", True, (255, 255, 255))
    qinstructions_rect = qinstructions.get_rect(center=(int(display_width / 2), (int(display_height / 1.5))))
    display.blit(source=qinstructions, dest=qinstructions_rect)

    rinstructions = font_instructions.render("Press r to replay", True, (255, 255, 255))
    rinstructions_rect = rinstructions.get_rect(center=(int(display_width / 2), (int(display_height / 1.3))))
    display.blit(source=rinstructions, dest=rinstructions_rect)

    final_score = "Final score: " + str(play_score)
    score_announce = font_instructions.render(final_score, True, (255, 255, 255))
    score_announce_rect = score_announce.get_rect(center=(int(display_width / 2), (int(display_height /2))))
    display.blit(source=score_announce, dest=score_announce_rect)

    pygame.display.flip()

    while end_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    end_game = False


def randomized_start():
    global x, y, dy

    x = random.randint(int(display_width/4), display_width - 20)
    y = random.randint(10, display_height - 10)

    if random.randint(0, 2) % 2 == 0:
        dy *= -1

# display
display = pygame.display.set_mode(size=(display_width, display_height))
display.fill(color=(0,0,0))
pygame.display.set_caption("Lets Play Pong!")

welcome_screen = pygame.font.Font(None, 30)
welcome = welcome_screen.render("Let's Play Pong!", True, (255, 255, 255))
welcome_rect = welcome.get_rect(center=(int(display_width/2), (int(display_height/3))))
display.blit(welcome, welcome_rect)

# start message
startmsg = welcome_screen.render("Hit y to start, or autostart in 10 seconds", True, (255, 255, 255))
startmsg_rect = startmsg.get_rect(center=(int(display_width/2), (int(display_height/2))))
display.blit(startmsg, startmsg_rect)

pygame.display.flip()

pygame.time.set_timer(event=pygame.USEREVENT, millis=10000)
timer_active = True

while timer_active:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            timer_active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                timer_active = False


# main game
randomized_start()
while True:
    # set fps
    clock.tick(speed)

    # set key press event
    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        if paddle_y + paddle_height + 10 <= display_height:
            paddle_y += 10

    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y - 10 >= 0:
            paddle_y -= 10


    display.fill(color=(0,0,0))
    x += dx
    y += dy

    # draw ball
    pygame.draw.circle(
        surface= display,
        color=(255,255,255),
        center=(x,y),
        radius=radius
    )

    # draw paddle
    pygame.draw.rect(
        surface=display,
        color=(255,255,255),
        rect=(paddle_x, paddle_y, paddle_width, paddle_height)
    )

    if x < radius:
        game_over()
        randomized_start()
        dx = abs(dx)
        play_score = 0


    if hit_back() or hit_paddle():
        dx *= -1

    if hit_sides():
        dy *= -1
    #if x < radius or x > display_width-radius:
    #    dx *= -1
    #if y < radius or y > display_height-radius:
    #    dy *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.update()