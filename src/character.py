import pygame
from pygame import constants
import pygame.display
import pygame.draw
import pygame.time
from abc import ABCMeta, abstractmethod

class GameCharacter:
  def __init__(self):
    self.x = 0
    self.y = 0
    # Clockwise: 0 = left, 1 = right
    self.direction = [False, False]
    self.color = [255, 255, 255]
    self.movementSpeed = 4