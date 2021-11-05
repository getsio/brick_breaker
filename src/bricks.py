import pygame
from pygame import Surface, Vector2, constants
import pygame.display
import pygame.draw
import pygame.time
from src.constants import BRICK_HEIGHT, BRICK_LENGTH, BRICK_COLOR_1
from src.game_object import GameObject

class Brick(GameObject):
  def __init__(self, x: int, y: int, color: list[int], hitpoints) -> None:
    super().__init__(x, y, color)
    self.side_a: int = BRICK_LENGTH
    self.side_b: int = BRICK_HEIGHT
    self.form: tuple[int] = (self.coords.x, self.coords.y, self.side_a, self.side_b)
    self.hitpoints: int = hitpoints
    self.collision_line_top: tuple[int] = (x, y, x + self.side_a, y)
    self.collision_line_bottom: tuple[int] = (x, y + self.side_b, 
      x + self.side_a, y + self.side_b)
    self.collision_line_left: tuple[int] = (x, y, x, y + self.side_b)
    self.collision_line_right: tuple[int] = (x + self.side_a, y, 
      x + self.side_a, y + self.side_b)

  def update(self) -> None:
    pass

  def draw(self, screen: Surface) -> None:
    self.game_object = pygame.draw.rect(screen, self.color, self.form)
