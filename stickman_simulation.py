from tkinter import VERTICAL
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

m = -5

character_verticies = [
        (0,0,0),
        (1,0,0),
        (0,1,0),
        (0,2,0),
        (-1,2.2,0),
        (1,2.2,0),
        (0,2.4,0)
    ]

character_edges = [
    (0,2),
    (2,1),
    (2,3),
    (3,4),
    (3,5),
    (3,6)
    ]

floor_verticies = [
    (-1000,0,0),
    (1000,0,0)
]
floor_edges = [
    (0,1)
]

meteorite_verticies = [
    (0,20,0),
    (3, 20,0),
    (0, 18, 0),
    (3, 18,0)
]
meteorite_edges = [
    (0,1),
    (0,2),
    (1,3),
    (2,3)
]

last_direction = 1

class Object:
    def __init__(self, type, verticies, edges, vel, on_thef_floor, falling_time):
        self.type = type
        self.verticies = verticies
        self.edges = edges
        self.vel = vel
        self.on_thef_floor = on_thef_floor
        self.falling_time = falling_time

def Cube():
    glBegin(GL_LINES)
    for edge in character_edges:
        for vertex in edge:
            
            glVertex3fv(character_verticies[vertex])
    glEnd()

def Floor():
    glBegin(GL_LINES)
    for edge in floor_edges:
        for vertex in edge:
            
            glVertex3fv(floor_verticies[vertex])
    glEnd()

def Meteorite(meteorite):
    glBegin(GL_LINES)
    for edge in meteorite.edges:
        for vertex in edge:
            
            glVertex3fv(meteorite.verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1500,800)
    
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 800.0)
    
    glTranslatef(0.0,-3, -15)
    
    leg = 1
    t = 0
    meteorite_t = 0
    character_verticies[2] = (character_verticies[2][0] + 1, character_verticies[2][1], character_verticies[2][2])
    character_verticies[3] = (character_verticies[3][0] + 1, character_verticies[3][1], character_verticies[3][2])
    character_verticies[4] = (character_verticies[4][0] + 1, character_verticies[4][1], character_verticies[4][2])
    character_verticies[5] = (character_verticies[5][0] + 1, character_verticies[5][1], character_verticies[5][2])
    character_verticies[6] = (character_verticies[6][0] + 1, character_verticies[6][1], character_verticies[6][2])
    meteorite = Object("meteorite", meteorite_verticies, meteorite_edges, 0, False, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pressed = pygame.key.get_pressed()
            if (pressed[K_LEFT] or pressed[K_a]):
                if meteorite.on_thef_floor == True:
                    for i in character_verticies:
                        if meteorite.verticies[1][0] >= i[0] + 1 and meteorite.verticies[0][0] < i[0] -1:
                            break
                        elif i == character_verticies[-1]:
                            leg = move(leg, -1)                        
                else:
                    leg = move(leg, -1)
            if (pressed[K_RIGHT] or pressed[K_d]):
                if meteorite.on_thef_floor == True:
                    for i in character_verticies:
                        if meteorite.verticies[0][0] <= i[0] - 1 and meteorite.verticies[1][0] > i[0] + 1:
                            break
                        elif i == character_verticies[-1]:
                            leg = move(leg, 1)                        
                else:
                    leg = move(leg, 1)
            if (pressed[K_DOWN] or pressed[K_s]):
                sneak()  
            if (pressed[K_UP] or pressed[K_w]):
                jump()
        if character_verticies[0][1] > 0:
            t += 1
            f = t * 0.081
            character_verticies[0] = (character_verticies[0][0], character_verticies[0][1] - f, character_verticies[0][2])
            if character_verticies[0][1] >= 0:

                character_verticies[1] = (character_verticies[1][0], character_verticies[1][1] - f, character_verticies[1][2])

                character_verticies[2] = (character_verticies[2][0], character_verticies[2][1] - f, character_verticies[2][2])
                character_verticies[3] = (character_verticies[3][0], character_verticies[3][1] - f, character_verticies[3][2])
                character_verticies[4] = (character_verticies[4][0], character_verticies[4][1] - f, character_verticies[4][2])
                character_verticies[5] = (character_verticies[5][0], character_verticies[5][1] - f, character_verticies[5][2])
                character_verticies[6] = (character_verticies[6][0], character_verticies[6][1] - f, character_verticies[6][2])
            else:
                co = character_verticies[0][1]
                character_verticies[0] = (character_verticies[0][0], character_verticies[0][1] - co, character_verticies[0][2])
                character_verticies[1] = (character_verticies[1][0], character_verticies[1][1] - f - co, character_verticies[1][2])

                character_verticies[2] = (character_verticies[2][0], character_verticies[2][1] - f - co, character_verticies[2][2])
                character_verticies[3] = (character_verticies[3][0], character_verticies[3][1] - f - co, character_verticies[3][2])
                character_verticies[4] = (character_verticies[4][0], character_verticies[4][1] - f - co, character_verticies[4][2])
                character_verticies[5] = (character_verticies[5][0], character_verticies[5][1] - f - co, character_verticies[5][2])
                character_verticies[6] = (character_verticies[6][0], character_verticies[6][1] - f - co, character_verticies[6][2])
        else:
            t = 0
            f = 0
        if meteorite.verticies[2][1] > 0:
            meteorite.falling_time += 1
            meteorite.vel = meteorite.falling_time * 0.081
            meteorite.verticies[2] = (meteorite.verticies[2][0], meteorite.verticies[2][1] - meteorite.vel, meteorite.verticies[2][2])
            if meteorite.verticies[2][1] >= 0:
                meteorite.verticies[1] = (meteorite.verticies[1][0], meteorite.verticies[1][1] - meteorite.vel, meteorite.verticies[1][2])

                meteorite.verticies[0] = (meteorite.verticies[0][0], meteorite.verticies[0][1] - meteorite.vel, meteorite.verticies[0][2])
                meteorite.verticies[3] = (meteorite.verticies[3][0], meteorite.verticies[3][1] - meteorite.vel, meteorite.verticies[3][2])
            else:
                co = meteorite.verticies[2][1]
                meteorite.verticies[2] = (meteorite.verticies[2][0], meteorite.verticies[2][1] - co, meteorite.verticies[2][2])
                meteorite.verticies[1] = (meteorite.verticies[1][0], meteorite.verticies[1][1] - meteorite.vel - co, meteorite.verticies[1][2])

                meteorite.verticies[0] = (meteorite.verticies[0][0], meteorite.verticies[0][1] - meteorite.vel - co, meteorite.verticies[0][2])
                meteorite.verticies[3] = (meteorite.verticies[3][0], meteorite.verticies[3][1] - meteorite.vel - co, meteorite.verticies[3][2])
        else:
            meteorite.falling_time = 0
            meteorite.vel = 0
            meteorite.on_thef_floor = True
            new = []
            m = random.randint(-5,5)

            new.append((meteorite_verticies[0][0] + m, meteorite_verticies[0][1], meteorite_verticies[0][2]))
            new.append((meteorite_verticies[1][0] + m, meteorite_verticies[1][1], meteorite_verticies[1][2]))
            new.append((meteorite_verticies[2][0] + m, meteorite_verticies[2][1], meteorite_verticies[2][2]))
            new.append((meteorite_verticies[3][0] + m, meteorite_verticies[3][1], meteorite_verticies[3][2]))




            # meteorite = Object("meteorite", new, meteorite_edges, 0, False, 0)

        for i in character_verticies:
            if meteorite.verticies[0][0] < i[0] < meteorite.verticies[1][0] and meteorite.verticies[2][1] < i[1] < meteorite.verticies[0][1] and meteorite.on_thef_floor == False:
                print("Game Over")
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        Floor()
        Meteorite(meteorite)
        
        pygame.display.flip()
        pygame.time.wait(100)
def move(leg, direction):
    global last_direction
    store_character_verticies = character_verticies
    if leg == 1:
        if direction * character_verticies[1][0] - direction * character_verticies[0][0] >= 0:
            character_verticies[0] = (character_verticies[0][0] + 1 * direction, character_verticies[0][1], character_verticies[0][2])
        else:
            leg = 2
            character_verticies[2] = (character_verticies[2][0] + 1 * direction, character_verticies[2][1], character_verticies[2][2])
            character_verticies[3] = (character_verticies[3][0] + 1 * direction, character_verticies[3][1], character_verticies[3][2])
            character_verticies[4] = (character_verticies[4][0] + 1 * direction, character_verticies[4][1], character_verticies[4][2])
            character_verticies[5] = (character_verticies[5][0] + 1 * direction, character_verticies[5][1], character_verticies[5][2])
            character_verticies[6] = (character_verticies[6][0] + 1 * direction, character_verticies[6][1], character_verticies[6][2])
    else:
        if direction * character_verticies[0][0] - direction * character_verticies[1][0] >= 0:
            character_verticies[1] = (character_verticies[1][0] + 1 * direction, character_verticies[1][1], character_verticies[1][2])
        else:
            leg = 1
            character_verticies[2] = (character_verticies[2][0] + 1 * direction, character_verticies[2][1], character_verticies[2][2])
            character_verticies[3] = (character_verticies[3][0] + 1 * direction, character_verticies[3][1], character_verticies[3][2])
            character_verticies[4] = (character_verticies[4][0] + 1 * direction, character_verticies[4][1], character_verticies[4][2])
            character_verticies[5] = (character_verticies[5][0] + 1 * direction, character_verticies[5][1], character_verticies[5][2])
            character_verticies[6] = (character_verticies[6][0] + 1 * direction, character_verticies[6][1], character_verticies[6][2])
       
    if character_verticies[1][0] == character_verticies[0][0]:
          
        glTranslatef(-0.5 * direction,0,0)
    last_direction = direction
    return leg
def sneak():
    if character_verticies[2][1] > 0:
        character_verticies[2] = (character_verticies[2][0], character_verticies[2][1] - 1, character_verticies[2][2])
        character_verticies[3] = (character_verticies[3][0], character_verticies[3][1] - 1, character_verticies[3][2])
        character_verticies[4] = (character_verticies[4][0], character_verticies[4][1] - 1, character_verticies[4][2])
        character_verticies[5] = (character_verticies[5][0], character_verticies[5][1] - 1, character_verticies[5][2])
        character_verticies[6] = (character_verticies[6][0], character_verticies[6][1] - 1, character_verticies[6][2])
    else:
        character_verticies[2] = (character_verticies[2][0], character_verticies[2][1] + 1, character_verticies[2][2])
        character_verticies[3] = (character_verticies[3][0], character_verticies[3][1] + 1, character_verticies[3][2])
        character_verticies[4] = (character_verticies[4][0], character_verticies[4][1] + 1, character_verticies[4][2])
        character_verticies[5] = (character_verticies[5][0], character_verticies[5][1] + 1, character_verticies[5][2])
        character_verticies[6] = (character_verticies[6][0], character_verticies[6][1] + 1, character_verticies[6][2])

def jump():
    if character_verticies[0][1] or character_verticies[1][1] == 0:
        character_verticies[0] = (character_verticies[0][0], character_verticies[0][1] + 3, character_verticies[0][2])
        character_verticies[1] = (character_verticies[1][0], character_verticies[1][1] + 3, character_verticies[1][2])

        character_verticies[2] = (character_verticies[2][0], character_verticies[2][1] + 3, character_verticies[2][2])
        character_verticies[3] = (character_verticies[3][0], character_verticies[3][1] + 3, character_verticies[3][2])
        character_verticies[4] = (character_verticies[4][0], character_verticies[4][1] + 3, character_verticies[4][2])
        character_verticies[5] = (character_verticies[5][0], character_verticies[5][1] + 3, character_verticies[5][2])
        character_verticies[6] = (character_verticies[6][0], character_verticies[6][1] + 3, character_verticies[6][2])
main()
