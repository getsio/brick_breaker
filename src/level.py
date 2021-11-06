from pygame import Surface
import pygame.draw
from src.bricks import Brick
from src.constants import SIZE, BRICK_COLOR_1

class Level:
  def __init__(self, bricks_per_row: int, bricks_per_col: int) -> None:
    self.bricks_per_row: int = bricks_per_row
    self.bricks_per_col: int = bricks_per_col

    self.brick_width: int = SIZE[0] / bricks_per_row
    self.brick_height: int = (2 * SIZE[1] / 3) / bricks_per_col

    self.start_points_x: list[int] = []
    self.start_points_y: list[int] = []

    for brick in range(bricks_per_row):
      self.start_points_x.append(brick * self.brick_width)

    for brick in range(bricks_per_col):
      self.start_points_y.append(brick * self.brick_height)

    self.bricks: list[Brick] = []
    self.draw_bricks()

  def draw_bricks(self) -> None:
    for point_y in self.start_points_y:
      for point_x in self.start_points_x:
        self.bricks.append(Brick(point_x, point_y, BRICK_COLOR_1, 1))

  def get_bricks(self) -> list[Brick]:
    return self.bricks