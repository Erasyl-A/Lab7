import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)

# Load images
background = pygame.image.load(r"C:\Users\Th\.vscode\Lab1\clock.png") 
minute_hand = pygame.image.load(r"C:\Users\Th\.vscode\Lab1\min_hand.png")  
second_hand = pygame.image.load(r"C:\Users\Th\.vscode\Lab1\sec_hand.png")  

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (500, 500))
second_hand = pygame.transform.scale(second_hand, (500, 500))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

def rotate_hand(image, angle, pivot, offset):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(pivot[0] + offset[0], pivot[1] + offset[1]))
    return rotated_image, new_rect

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    minute_angle = -(minutes * 6) 
    second_angle = -(seconds * 6)  
    
    rotated_minute_hand, minute_rect = rotate_hand(minute_hand, minute_angle, CENTER, (0, 0))
    rotated_second_hand, second_rect = rotate_hand(second_hand, second_angle, CENTER, (0, 0))
    
    screen.blit(rotated_minute_hand, minute_rect.topleft)
    screen.blit(rotated_second_hand, second_rect.topleft)
    
    pygame.display.flip()
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)  

pygame.quit()
