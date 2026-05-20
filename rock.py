import pygame
import random

# Start pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 60)

# Choices
choices = ["rock", "paper", "scissors"]

# Scores
player_score = 0
computer_score = 0

# Button class
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 20, self.rect.y + 20))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create buttons
rock_button = Button("Rock", 50, 450, 200, 100)
paper_button = Button("Paper", 300, 450, 200, 100)
scissors_button = Button("Scissors", 550, 450, 200, 100)

# Game loop
running = True

player_choice = ""
computer_choice = ""
result = ""

while running:

    screen.fill((100, 150, 200))

    # Draw buttons
    rock_button.draw()
    paper_button.draw()
    scissors_button.draw()

    # Show text
    player_text = font.render(f"Player: {player_choice}", True, WHITE)
    computer_text = font.render(f"Computer: {computer_choice}", True, WHITE)
    score_text = font.render(f"{player_score} : {computer_score}", True, WHITE)
    result_text = font.render(result, True, WHITE)

    screen.blit(player_text, (50, 50))
    screen.blit(computer_text, (50, 120))
    screen.blit(score_text, (350, 250))
    screen.blit(result_text, (250, 350))

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            # Player choice
            if rock_button.clicked(mouse_pos):
                player_choice = "rock"

            elif paper_button.clicked(mouse_pos):
                player_choice = "paper"

            elif scissors_button.clicked(mouse_pos):
                player_choice = "scissors"

            # Computer choice
            if player_choice != "":
                computer_choice = random.choice(choices)

                # Decide winner
                if player_choice == computer_choice:
                    result = "Draw!"

                elif (
                    (player_choice == "rock" and computer_choice == "scissors") or
                    (player_choice == "paper" and computer_choice == "rock") or
                    (player_choice == "scissors" and computer_choice == "paper")
                ):
                    result = "You Win!"
                    player_score += 1

                else:
                    result = "Computer Wins!"
                    computer_score += 1

    pygame.display.update()

pygame.quit()