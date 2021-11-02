import pygame
from pygame import Surface, Vector2, constants
import pygame.display
import pygame.draw
import pygame.time
from src.constants import SIZE, CHAR_LENGTH, CHAR_HEIGTH, CHAR_MOVESPEED, CHAR_COLOR
from src.game_object import GameObject

class GameCharacter(GameObject):
  def __init__(self):
    super().__init__(0, 0, CHAR_COLOR)
    self.acceleration: Vector2 = Vector2(CHAR_MOVESPEED, 0)
    self.side_a: int = CHAR_LENGTH
    self.side_b: int = CHAR_HEIGTH
    self.init()

  def init(self):
    self.coords.x = (SIZE[0] / 2) - (self.side_a / 2)
    self.coords.y = SIZE[1] - 100

    self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)

  def update(self) -> None:
    self.__move()

  def draw(self, screen: Surface) -> None:
    pygame.draw.rect(screen, self.color, self.form)

  def __move(self):
    self.coords += self.acceleration
    self.__correct()
    self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)

  def __correct(self):
    if self.coords.x < 0:
        self.coords.x = 0
    elif self.coords.x > SIZE[0] - self.side_a:
        self.coords.x = SIZE[0] - self.side_a