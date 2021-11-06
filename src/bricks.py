import pygame
from pygame import Rect, Surface, Vector2, constants
import pygame.display
import pygame.draw
import pygame.time
from src.constants import SCREEN_COLOR
from src.constants import BRICK_HEIGHT, BRICK_LENGTH, BRICK_COLOR_1
from src.game_object import GameObject

class Brick(GameObject):
  def __init__(self, x: int, y: int, color: list[int], hitpoints) -> None:
    super().__init__(x, y, color)
    self.side_a: int = BRICK_LENGTH
    self.side_b: int = BRICK_HEIGHT
    self.form: tuple[int] = (self.coords.x, self.coords.y, self.side_a, self.side_b)
    self.hitpoints: int = hitpoints
    self.lines: tuple[int] = None
    self.collision_line_top: tuple[int] = (x, y, x + self.side_a, y)
    self.collision_line_bottom: tuple[int] = (x, y + self.side_b, 
      x + self.side_a, y + self.side_b)
    self.collision_line_left: tuple[int] = (x, y, x, y + self.side_b)
    self.collision_line_right: tuple[int] = (x + self.side_a, y, 
      x + self.side_a, y + self.side_b)

  def update(self) -> None:
    pass

  def draw(self, screen: Surface) -> None:
    self.lines = tuple(self.__get_line(screen, self.collision_line_top, 
      self.collision_line_right, self.collision_line_bottom, self.collision_line_left))

    self.game_object = pygame.draw.rect(screen, self.color, self.form, 1)

  def living(self) -> bool:
    return self.hitpoints > 0

  def decrease_hitpoints(self) -> None:
    self.hitpoints -= 1

  def __get_line(self, screen: Surface, *coll_lines: list[tuple]) -> Rect:
    lines = []
    for coll_line in coll_lines:
      start_pos = (coll_line[0], coll_line[1])
      end_pos = (coll_line[2], coll_line [3])
      lines.append(pygame.draw.line(screen, SCREEN_COLOR, start_pos, end_pos, 3))
    return lines
