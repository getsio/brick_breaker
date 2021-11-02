from abc import ABCMeta, abstractmethod
from pygame import Surface, Vector2

class GameObject(metaclass = ABCMeta):
  def __init__(self, x: int, y: int, color: list[int]) -> None:
    self.coords: Vector2 = Vector2(x, y)
    self.color: list[int] = color

  @abstractmethod
  def update(self):
    pass

  @abstractmethod
  def draw(self, screen: Surface):
    pass
  