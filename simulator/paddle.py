import pygame
from .env_vars import *

def p1_handle_event(event):
    global p1_move_up, p1_move_down

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            p1_move_up = True
            p1_move_down = False
        elif event.key == pygame.K_s:
            p1_move_down = True
            p1_move_up = False
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            p1_move_up = False
        elif event.key == pygame.K_s:
            p1_move_down = False

def p2_handle_event(event):
    global p2_move_up, p2_move_down

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            p2_move_up = True
            p2_move_down = False
        elif event.key == pygame.K_DOWN:
            p2_move_down = True
            p2_move_up = False
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            p2_move_up = False
        elif event.key == pygame.K_DOWN:
            p2_move_down = False

def move():
    global p1_y_pos, p2_y_pos
    if p1_move_up:
        p1_y_pos -= pad_speed
        if p1_y_pos < 0:
            p1_y_pos = 0
    elif p1_move_down:
        p1_y_pos += pad_speed
        if p1_y_pos > d_height - pad_length:
            p1_y_pos = d_height - pad_length
    if p2_move_up:
        p2_y_pos -= pad_speed
        if p2_y_pos < 0:
            p2_y_pos = 0
    elif p2_move_down:
        p2_y_pos += pad_speed
        if p2_y_pos > d_height - pad_length:
            p2_y_pos = d_height - pad_length
    return p1_y_pos, p2_y_pos