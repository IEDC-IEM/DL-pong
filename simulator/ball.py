from .paddle import *

def move(p1_score, p2_score,p1_y_pos, p2_y_pos):
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # If the ball hits a wall at the sides without the paddles
    if ball_y < 0 or ball_y > d_height - BALL_RADIUS:
        ball_speed_y = -ball_speed_y
    # If the ball reaches player 1
    if ball_x - pad_width< 0:
        # Is the paddle there to make contact?
        if p1_y_pos < ball_y < p1_y_pos + pad_length:
            # Reverse the ball's x direction
            ball_speed_x = -ball_speed_x
        else:
            # Update scores and re-initialize the ball
            p2_score += 1
            ball_x = d_width // 2
            ball_y = d_height // 2
            ball_speed_x = -ball_speed_x
            ball_speed_y = -ball_speed_y
    # If the ball reaches player 2
    elif ball_x > d_width - pad_width:
        # Is the paddle there to make contact ?
        if p2_y_pos < ball_y < p2_y_pos + pad_length:
            # Reverse the ball's x direction
            ball_speed_x = -ball_speed_x
        else:
            # Update scores and re-initialize the ball
            p1_score += 1
            ball_x = d_width // 2
            ball_y = d_height // 2
            ball_speed_x = -ball_speed_x
            ball_speed_y = -ball_speed_x
    return p1_score, p2_score, ball_x, ball_y