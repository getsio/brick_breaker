from src.bricks import Brick
from src.constants import SIZE

class Level:
  def __init__(self, bricks_per_row: int, bricks_per_col: int) -> None:
    self.bricks_per_row: int = bricks_per_row
    self.bricks_per_col: int = bricks_per_col

    self.brick_width: int = SIZE[0] / bricks_per_row
    self.brick_height: int = (2 * SIZE[1] / 3) / bricks_per_col

    print(self.brick_width, self.brick_height)