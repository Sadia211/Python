import pygame
import random

#start pygame
pygame.init

#Create screen
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Rock Paper Scissors")

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)

#Font
font=pygame.font.SysFont(None,60)

#Choices
choices=["rock","paper","scissors"]

#Scores
player_score=0
computer_score=0

class Button:
    def __init__(self,text,x,y,width,height):
     self.text=text
     self.rect=pygame.Rect(x,y,width,height)

    def draw(self):
       pygame.draw.rect(screen,WHITE,self.rect)
       text_surface=font.render(self.text,True,BLACK)
       screen.blit(text_surface,(self.rect.x+20,self.rect.y+20))
       
    def clicked(self,pos):
       return self.rect.collidepoint(pos)
       
    rock_button=Button("Rock",50,450,200,100)
    paper_button=Button("Paper",300,450,200,100)
    scissors_button=Button("Scissor",550,450,200,100)

    #Game loop
    running=True

    player_choice=" "
    computer_choice=" "
    result=" "