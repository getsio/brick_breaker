from abc import ABCMeta, abstractmethod
from pygame import Surface

class GameObject(metaclass = ABCMeta):
  def __init__(self, x: int, y: int, color: list[int]) -> None:
    self.x = x
    self.y = y
    self.color = color

  @abstractmethod
  def update(self):
    pass

  @abstractmethod
  def draw(self, screen: Surface):
    pass
  