import pygame
from pygame import Surface, Vector2, constants
import pygame.display
import pygame.draw
import pygame.time
from src.constants import SIZE, CHAR_LENGTH, CHAR_HEIGTH, CHAR_MOVESPEED, CHAR_COLOR
from src.constants import SCREEN_COLOR
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
    self.collision_line: tuple[int] = (self.coords.x, self.coords.y, 
      self.coords.x + self.side_a, self.coords.y)
    

  def update(self) -> None:
    self.__move()

  def draw(self, screen: Surface) -> None:
    start_pos = (self.collision_line[0], self.collision_line[1])
    end_pos = (self.collision_line[2], self.collision_line[3])
    self.line = pygame.draw.line(screen, SCREEN_COLOR, start_pos, end_pos, 8)
    self.game_object = pygame.draw.rect(screen, self.color, self.form)

  def __move(self):
    self.coords += self.acceleration
    self.__correct()
    self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)
    self.collision_line: tuple[int] = (self.coords.x, self.coords.y, 
      self.coords.x + self.side_a, self.coords.y)

  def __correct(self):
    if self.coords.x < 0:
      self.coords.x = 0
      self.__reset_acceleration()
    elif self.coords.x > SIZE[0] - self.side_a:
      self.__reset_acceleration()
      self.coords.x = SIZE[0] - self.side_a

  def __reset_acceleration(self) -> None:
    self.acceleration.update(0, 0)
  
  def can_accelerate(self) -> bool:
    if self.coords.x <= 0:
      return False
    elif self.coords.x >= SIZE[0] - self.side_a:
      return False
    else:
      return True