import pygame
from pygame import Surface, constants
import pygame.display
import pygame.draw
import pygame.time
from src.game_object import GameObject

class GameCharacter(GameObject):
  def __init__(self, x: int, y: int, color: list[int], side_a: int, side_b: int):
    super().__init__(x, y, color)
    # Clockwise: 0 = left, 1 = right
    self.direction = [False, False]
    self.movementSpeed = 4
    self.side_a = side_a
    self.side_b = side_b
    self.form = (self.x, self.y, self.side_a, self.side_b)

  def update(self) -> None:
    pass

  def move(self) -> None:
    pass

  def draw(self, screen: Surface) -> None:
    pygame.draw.rect(screen, self.color, self.form)