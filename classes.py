import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name, color, screen_width, screen_height):
        super().__init__()
        self.name = name
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)

    def update(self, screen_width, screen_height):
        i = 5
        self.rect.x += i
        if self.rect.x < screen_width:
            i *= -1