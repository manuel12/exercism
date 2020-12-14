# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:	
  def __init__(self, direction=NORTH, x=0, y=0):
    self.direction = direction
    self.x = x
    self.y = y
    self.coordinates = (self.x, self.y)

  def move(self, commands):
    for command in commands:
      if command == "R":
        if self.direction == "NORTH":
         self.direction = "EAST"
        elif self.direction == "EAST":
         self.direction = "SOUTH"
        elif self.direction == "SOUTH":
          self.direction = "WEST"
        elif self.direction == "WEST":
          self.direction = "NORTH"
      
      elif command == "L":       
        if self.direction == "NORTH":
          self.direction = "WEST"
        elif self.direction == "WEST":
          self.direction = "SOUTH"
        elif self.direction == "SOUTH":
          self.direction = "EAST"
        elif self.direction == "EAST":
          self.direction = "NORTH"
      
      else:
        if self.direction == "NORTH":
          self.y += 1
        if self.direction == "WEST":
          self.x -= 1
        if self.direction == "SOUTH":
          self.y -= 1
        if self.direction == "EAST":
          self.x += 1
    
    self.coordinates = (self.x, self.y)

