import pygame
from pygame import Surface, Vector2, constants
import pygame.display
import pygame.draw
import pygame.time
from src.character import GameCharacter
from src.bricks import Brick
from src.constants import SIZE, BALL_LENGTH, BALL_HEIGTH, BALL_MOVESPEED, BALL_COLOR
from src.game_object import GameObject

class Ball(GameObject):
  def __init__(self, game_character: GameCharacter, bricks: list[Brick]) -> None:
    super().__init__(0, 0, BALL_COLOR)
    self.acceleration = Vector2(BALL_MOVESPEED, BALL_MOVESPEED)
    self.side_a: int = BALL_LENGTH
    self.side_b: int = BALL_HEIGTH
    self.form: tuple[int] = None
    self.moving: bool = False
    self.game_character: GameCharacter = game_character
    self.bricks: list[Brick] = bricks
    self.init()

  def init(self) -> None:
    self.coords.x = (SIZE[0] / 2) - (self.side_a / 2)
    self.coords.y = SIZE[1] - 120

    self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)

  def update(self) -> None:
    self.__move()

  def draw(self, screen: Surface) -> None:
    self.game_object = pygame.draw.ellipse(screen, self.color, self.form)
    self.__check_player_collision()
    self.__check_brick_collision()

  def __move(self) -> None:
    if self.moving:
      self.__correct()
      self.coords += self.acceleration
      self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)

  def position(self) -> None:
    if not self.moving:
      self.coords.x = (self.game_character.coords.x + 
        (self.game_character.side_a / 2) - (self.side_a / 2))
      self.form = (self.coords.x, self.coords.y, self.side_a, self.side_b)

  def __correct(self) -> None:
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

  def __direction_x(self) -> None:
    self.acceleration.x = self.acceleration.x * -1 + 1

  def __direction_y(self) -> None:
    self.acceleration.y = self.acceleration.y * -1 + 1

  def __game_character_hit(self) -> None:
    self.acceleration.y = self.acceleration.y * -1 + 1
    self.acceleration.x = (self.game_character.acceleration.x + 
      self.acceleration.x) / 2

  def __check_player_collision(self) -> None:
    if self.game_object.colliderect(self.game_character.line):
      self.__game_character_hit()

  def __check_brick_collision(self) -> None:
    for brick in self.bricks:
      ball = self.game_object
      hit = False

      if ball.colliderect(brick.lines[0]) or ball.colliderect(brick.lines[2]):
        hit = True
        self.__direction_y()
      elif ball.colliderect(brick.lines[1]) or ball.colliderect(brick.lines[3]):
        hit = True
        self.__direction_x()

      if hit:
        brick.decrease_hitpoints()
  
  def check_bottom_hit(self) -> bool:
    if self.coords.y > self.game_character.coords.y:
      return True
    return False