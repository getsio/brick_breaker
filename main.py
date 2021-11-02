import pygame
from pygame.constants import K_SPACE, K_a, K_d
import pygame.display
import pygame.draw
import pygame.time
import pygame.event
import pygame.key
from src.constants import BALL_MOVESPEED
from src.constants import CHAR_MOVESPEED
from src.ball import Ball
from src.constants import SIZE
from src.game_object import GameObject
from src.character import GameCharacter

class Game:
  def __init__(self, fps: int, game_character: GameCharacter, ball: Ball, game_objects: list[GameObject], fullscreen: bool = False) -> None:
    """This class represents a pygame window.

    Args:
        fps (int): Frames per second
        size (tuple[int]): Size of the window (width, height)
        fullscreen (bool, optional): Starts the window in Fullscreen if true. Defaults to False.
    """
    pygame.init()
    self.fps: int = fps
    self.game_running: bool = True
    self.size: tuple[int] = SIZE
    self.clock: pygame.time.Clock = pygame.time.Clock()
    self.game_character: GameCharacter = game_character
    self.ball: Ball = ball
    self.game_objects: list[GameObject] = game_objects
    self.__init_screen(fullscreen)

  def run(self) -> None:
    """Starts the game.
    """
    while self.game_running:
      self.__check_game_events()
      self.__check_keys()
      self.update()
      self.draw()
      self.clock.tick(self.fps)

  def __init_screen(self, fullscreen: bool) -> None:
    """Initializes the screen of the game.

    Args:
        fullscreen (bool): Starts the window in Fullscreen if true.
    """
    if fullscreen:
      self.screen: tuple[int] = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
    else:
      self.screen: tuple[int] = pygame.display.set_mode(self.size)

  def __check_game_events(self) -> None:
    """Checks for game events.
    """
    events = pygame.event.get()

    for ev in events:
      if ev.type == pygame.QUIT:
        self.game_running = False

  def __check_keys(self) -> None:
    keys = pygame.key.get_pressed()
    self.game_character.acceleration.update(0, 0)

    if keys[K_a]:
      self.game_character.acceleration.update(-CHAR_MOVESPEED, 0)
    elif keys[K_d]:
      self.game_character.acceleration.update(CHAR_MOVESPEED, 0)

    if keys[K_SPACE] and not self.ball.moving:
      self.ball.moving = True
      move_acceleration = self.game_character.acceleration.x
      self.ball.acceleration.update(move_acceleration, -BALL_MOVESPEED)

  def update(self):
    self.game_character.update()
    self.move_ball()
    self.ball.update()

    for game_object in self.game_objects:
      game_object.update()

  def draw(self):
    self.screen.fill((0, 0, 0))
    self.game_character.draw(self.screen)
    self.ball.draw(self.screen)
    for game_object in self.game_objects:
        game_object.draw(self.screen)
    
    pygame.display.flip()

  def move_ball(self):
    self.ball.position(self.game_character)

if __name__ == '__main__':
  character = GameCharacter()
  ball = Ball()
  game_objects = []
  game = Game(60, character, ball, game_objects)
  game.run()