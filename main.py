from __future__ import absolute_import

import pygame

import simulator.paddle as paddle
import simulator.ball as ball

# zero initialization of the scores
p1_score, p2_score = 0, 0

# initialize the enviornment
pygame.init()
screen = pygame.display.set_mode(paddle.d_size)
pygame.display.set_caption("Pong Simulator")
pygame.mouse.set_visible(False)

# set a clock for the game instances
clock = pygame.time.Clock()

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # handle the events to player's paddles
        paddle.p1_handle_event(event)
        paddle.p2_handle_event(event)
    
    # Define how the paddles move and retrieve new paddle locations
    p1_y_pos, p2_y_pos = paddle.move()
    #Make the ball move and retrieve scores and new position of the ball
    p1_score, p2_score ,ball_x, ball_y = ball.move(p1_score,p2_score,p1_y_pos, p2_y_pos)

    #Start drawing the new frame
    screen.fill(paddle.background)

    # Drawing the ball
    pygame.draw.circle(screen, paddle.ball_color, (ball_x, ball_y), paddle.BALL_RADIUS)
    # Drawing the paddle for player 1
    pygame.draw.rect(screen, paddle.pad_color, (0, p1_y_pos, paddle.pad_width, paddle.pad_length))
    # Drawing the paddle for player 2
    pygame.draw.rect(screen, paddle.pad_color,(paddle.d_width - paddle.pad_width, p2_y_pos, paddle.pad_width, paddle.pad_length))

    # Seperator
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (paddle.d_width / 2, 0, 1, paddle.d_height))
    
    # Print the scores onto the screen
    score_font = pygame.font.Font(None, 30)         

    p1_score_text = str(p1_score)
    p1_score_render = score_font.render(p1_score_text, 1, pygame.Color(255, 255, 255, 255))
    screen.blit(p1_score_render, (paddle.d_width / 2 - 50, 50))


    p2_score_text = str(p2_score)
    p2_score_render = score_font.render(p2_score_text, 1, pygame.Color(255, 255, 255, 255))
    screen.blit(p2_score_render, (paddle.d_width / 2 + 50, 50))

    # Update the current frame to the display
    pygame.display.flip()
    # Set Game clock frequency
    clock.tick(paddle.FPS)
