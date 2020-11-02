"""
Solução primeiro exercicio da certificação python basico hackerrank.
"""

class Car:
  def __init__(self, max_speed, speed_unit):
    self.max_speed = max_speed
    self.speed_unit = speed_unit
  def __str__(self):
    my_string = "Car with the maximum speed of {} {}"
    return my_string.format(self.max_speed, self.speed_unit)

class Boat:
  def __init__(self, max_speed):
    self.max_speed = max_speed

  def __str__(self):
    my_string = "Boat with the maximum speed of {} knots"
    return my_string.format(self.max_speed)
