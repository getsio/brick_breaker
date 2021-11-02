from typing import Sized
import pygame
from pygame import Surface, Vector2, constants
import pygame.display
import pygame.draw
import pygame.time
from src.character import GameCharacter
from src.constants import SIZE, BALL_LENGTH, BALL_HEIGTH, BALL_MOVESPEED, BALL_COLOR
from src.game_object import GameObject

class Ball(GameObject):
  def __init__(self) -> None:
    super().__init__(0, 0, BALL_COLOR)
    self.acceleration = Vector2(BALL_MOVESPEED, BALL_MOVESPEED)
    self.side_a: int = BALL_LENGTH
    self.side_b: int = BALL_HEIGTH
    self.form: tuple[int] = None
    self.moving: bool = False
    self.init()

  def init(self):
    self.coords.x = (SIZE[0] / 2) - (self.side_a / 2)
    self.coords.y = SIZE[1] - 120

    self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)

  def update(self):
    self.__move()

  def draw(self, screen: Surface):
    pygame.draw.ellipse(screen, self.color, self.form)

  def __move(self):
    if self.moving:
      self.coords += self.acceleration
      self.__correct()
      self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)

  def position(self, char: GameCharacter):
    if not self.moving:
      self.coords.x = char.coords.x + (char.side_a / 2) - (self.side_a / 2)
      self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)

  def __correct(self):
    if self.coords.x < 0:
      self.coords.x = 0
      self.__direction_x()
    elif self.coords.x > SIZE[0] - self.side_a:
      self.coords.x = SIZE[0] - self.side_a
      self.__direction_x()

    if self.coords.y < 0:
      self.coords.y = 0
      self.__direction_y()
    elif self.coords.y > SIZE[1] - self.side_b:
      self.coords.y = SIZE[1] - self.side_b
      self.__direction_y()

  def __direction_x(self):
    self.acceleration.x = self.acceleration.x * -1 + 1

  def __direction_y(self):
    self.acceleration.y = self.acceleration.y * -1 + 1