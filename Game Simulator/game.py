import pygame
import env_vars as ev       #Module containing variables defining the enviornment
import paddle as p          #Module describing the paddle
import ball as b            #Module describing the ball

p1_score = 0                #Zero initialization of the scores
p2_score = 0

pygame.init()                                                       #initialize the enviornment
screen = pygame.display.set_mode(ev.d_size)                         #Define the Window size
pygame.display.set_caption("Pong Simulator")
clock = pygame.time.Clock()                                         #Set a clock for the game instances
pygame.mouse.set_visible(False)                                     #Disabling visibility of the mouse cursor
while (True):
    for event in pygame.event.get():                                #Iterate through the events in each frame
        if event.type == pygame.QUIT:                               #If the event is to quit
            pygame.quit()                                           #Quit
            exit()                                                  #Exit

        p.p1_handle_event(event)                                    #Handle the events to player 1's paddle
        p.p2_handle_event(event)                                    #Handle the events to player 2's paddle
    p1_y_pos, p2_y_pos = p.move()                                   #Define how the paddles move and retrieve new paddle locations            
    p1_score, p2_score ,ball_x, ball_y = b.move(p1_score,p2_score,p1_y_pos, p2_y_pos)
                                                                    #Make the ball move and retrieve scores and new position of the ball
    #Start drawing the new frame
    screen.fill(ev.background)                                      

    pygame.draw.circle(screen, ev.ball_color, (ball_x, ball_y), ev.BALL_RADIUS)             #Drawing the ball
    pygame.draw.rect(screen, ev.pad_color, (0, p1_y_pos, ev.pad_width, ev.pad_length))      #Drawing the paddle for player 1
    pygame.draw.rect(screen, ev.pad_color,(ev.d_width - ev.pad_width, p2_y_pos, ev.pad_width, ev.pad_length))   #Drawing the paddle for player 2

    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (ev.d_width / 2, 0, 1, ev.d_height))     #Seperator
    
    #Print the scores onto the screen
    score_font = pygame.font.Font(None, 30)         

    p1_score_text = str(p1_score)
    p1_score_render = score_font.render(p1_score_text, 1, pygame.Color(255, 255, 255, 255))
    screen.blit(p1_score_render, (ev.d_width / 2 - 50, 50))


    p2_score_text = str(p2_score)
    p2_score_render = score_font.render(p2_score_text, 1, pygame.Color(255, 255, 255, 255))
    screen.blit(p2_score_render, (ev.d_width / 2 + 50, 50))

    pygame.display.flip()                                           #Update the current frame to the display
    clock.tick(ev.FPS)                                              #Set Game clock frequency
