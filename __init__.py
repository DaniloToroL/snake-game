from snake import Snake
import pygame
from utils import hex2rgb
from random import randint
from time import sleep
from utils import Vector

size = width, height = 500, 500
color = hex2rgb("#292828")
frameRate = 0.1

if __name__ == "__main__":
    
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(color)

    snake = Snake(width=10)
    food = Vector(randint(snake.width, width), randint(snake.width, height))
    while True:
        
        screen.fill((25,25,25))
        snake.move()
        snake.show(screen)
        end = snake.dead()
        
        if snake.eat(food):
            food = Vector(randint(snake.width, width), randint(snake.width, height))

        rect = pygame.Rect(food.x, food.y, snake.width, snake.width)
        pygame.draw.rect(screen, (255, 0, 0), rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake.direction(0, 1)
                if event.key == pygame.K_UP:
                    snake.direction(0, -1)
                if event.key == pygame.K_LEFT:
                    snake.direction(-1, 0)
                if event.key == pygame.K_RIGHT:
                    snake.direction(1, 0)

        pygame.display.update()
        sleep(frameRate)