import pygame
from pygame import Surface, constants
import pygame.display
import pygame.draw
import pygame.time
from src.constants import SIZE, CHAR_LENGTH, CHAR_HEIGTH, CHAR_MOVESPEED, CHAR_COLOR
from src.game_object import GameObject

class GameCharacter(GameObject):
  def __init__(self):
    super().__init__(0, 0, CHAR_COLOR)
    # Clockwise: 0 = left, 1 = right
    self.direction: list[bool] = [False, False]
    self.movement_speed: int = CHAR_MOVESPEED
    self.side_a: int = CHAR_LENGTH
    self.side_b: int = CHAR_HEIGTH
    self.init()

  def init(self):
    self.x = (SIZE[0] / 2) - (self.side_a / 2)
    self.y = SIZE[1] - 100

    self.form = (self.x, self.y, self.side_a, self.side_b)

  def update(self) -> None:
    self.__move()

  def draw(self, screen: Surface) -> None:
    pygame.draw.rect(screen, self.color, self.form)

  def __move(self):
    if self.direction[0] and self.x >= 0:
      self.x -= self.movement_speed
    elif self.direction[1] and self.x <= (SIZE[0] - self.side_a):
      self.x += self.movement_speed

    self.__correct_x()
    self.form = (self.x, self.y, self.side_a, self.side_b)

  def __correct_x(self):
    if self.x < 0:
        self.x = 0
    elif self.x > SIZE[0] - self.side_a:
        self.x = SIZE[0] - self.side_a