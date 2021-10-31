import pygame
from pygame import Surface, constants
import pygame.display
import pygame.draw
import pygame.time
from src.character import GameCharacter
from src.constants import SIZE, BALL_LENGTH, BALL_HEIGTH, BALL_MOVESPEED, BALL_COLOR
from src.game_object import GameObject

class Ball(GameObject):
  def __init__(self) -> None:
    super().__init__(0, 0, BALL_COLOR)
    # Clockwise: 0 = up, 1 = right, 2 = down, 3 = left
    self.direction: list[bool] = [False, False, False, False]
    self.movement_speed: int = BALL_MOVESPEED
    self.side_a: int = BALL_LENGTH
    self.side_b: int = BALL_HEIGTH
    self.form: tuple[int] = 0
    self.moving: bool = False
    self.init()

  def init(self):
    self.x = (SIZE[0] / 2) - (self.side_a / 2)
    self.y = SIZE[1] - 120

    self.form = (self.x, self.y, self.side_a, self.side_b)

  def update(self):
    self.__move()

  def draw(self, screen: Surface):
    pygame.draw.ellipse(screen, self.color, self.form)

  def __move(self):
    pass

  def position(self, char: GameCharacter):
    self.x = char.x + (char.side_a / 2) - (self.side_a / 2)
    self.form = (self.x, self.y, self.side_a, self.side_b)
