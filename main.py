import pygame
import pygame.display
import pygame.draw
import pygame.time
import pygame.event
from src.constants import SIZE
from src.game_object import GameObject
from src.character import GameCharacter

class Game:
  def __init__(self, fps: int, game_character: GameCharacter, game_objects: list[GameObject], fullscreen: bool = False) -> None:
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
    self.game_objects: list[GameObject] = game_objects
    self.__init_screen(fullscreen)

  def run(self) -> None:
    """Starts the game.
    """
    while self.game_running:
      self.__check_game_events(pygame.event.get())
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

  def __check_game_events(self, events: list[pygame.event.Event]) -> None:
    """Checks the type of Pygame Events.

    Args:
        events (list[pygame.event.Event]): List of Pygame events
    """
    for ev in events:
      if ev.type == pygame.QUIT:
        self.game_running = False
      elif ev.type == pygame.KEYDOWN:
        self.__check_keydown_events(ev)
      elif ev.type == pygame.KEYUP:
        self.__check_keyup_events(ev)

  def __check_keydown_events(self, ev: pygame.event.Event) -> None:
    """Checks what Key was pressed.

    Args:
        ev (pygame.event.Event): Pygame event
    """
    if ev.key == pygame.K_ESCAPE:
      self.game_running = False
    elif ev.key == pygame.K_f:
      if self.screen.get_flags() & pygame.FULLSCREEN:
        pygame.display.set_mode(self.size)
      else:
        pygame.display.set_mode(self.size, pygame.FULLSCREEN)
    elif ev.key == pygame.K_a:
      self.game_character.direction[0] = True
    elif ev.key == pygame.K_d:
      self.game_character.direction[1] = True

  def __check_keyup_events(self, ev: pygame.event.Event) -> None:
    """Checks what Key was released.

    Args:
        ev (pygame.event.Event): Pygame event
    """
    if ev.key == pygame.K_a:
      self.game_character.direction[0] = False
    elif ev.key == pygame.K_d:
      self.game_character.direction[1] = False

  def update(self):
    self.game_character.update()

    for game_object in self.game_objects:
      game_object.update()

  def draw(self):
    self.screen.fill((0, 0, 0))
    self.game_character.draw(self.screen)
    for game_object in self.game_objects:
        game_object.draw(self.screen)
    
    pygame.display.flip()

if __name__ == '__main__':
  character = GameCharacter([255, 255, 255])
  game_objects = []
  game = Game(60, character, game_objects)
  game.run()