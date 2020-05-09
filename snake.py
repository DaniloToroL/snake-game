import pygame
from utils import hex2rgb, calculate_vector_distance, Vector

class Snake:

    def __init__(self, width=5, color="#FFFFFF"):
        self.x = 100
        self.y = 0
        self.x_step = 5
        self.y_step = 0
        self.history = []
        self.tail = 0
        self.color = hex2rgb(color)
        self.width = width

    def direction(self, x, y):
        self.x_step = x * self.width
        self.y_step = y * self.width

    def dead(self):
        distances = [calculate_vector_distance((self.x, self.y), vector) for vector in self.history]

        if len(distances) and min(distances) < self.width:
            self.tail = 0
            self.history = []
            return True

        return False
        

    def eat(self, food):
        dist = calculate_vector_distance((self.x, self.y), food)
        if dist < self.width:
            self.tail += 1
            self.history.append(Vector(self.x, self.y))
            return True


    def move(self):

        if self.tail == len(self.history):
            for i in range(self.tail - 1):
                self.history[i] = self.history[i + 1]
        
        if len(self.history):
            self.history[-1] = Vector(self.x, self.y) 
    
        self.x += self.x_step
        self.y += self.y_step

    def show(self, screen):
        self.x = self.x % screen.get_size()[0]
        self.y = self.y % screen.get_size()[1]
        rect = pygame.Rect(self.x, self.y, self.width, self.width)
        pygame.draw.rect(screen, self.color, rect)

        for v in self.history:
            rect = pygame.Rect(v.x, v.y, self.width, self.width)
            pygame.draw.rect(screen, self.color, rect)

