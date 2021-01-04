import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key in kwargs.keys():
      for n in range(kwargs[key]):
        self.contents.append(key)
  
  def draw(self, num_balls):
    if num_balls >= len(self.contents):
      return self.contents

    else:
      drawn_balls = []
      for n in range(num_balls):
        index = random.randrange(len(self.contents))
        drawn_balls.append(self.contents[index])
        self.contents = self.contents[0:index] + self.contents[index + 1:]

      return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_correct = 0
  for i in range(num_experiments):
    temp_hat = copy.copy(hat)
    drawn = temp_hat.draw(num_balls_drawn)
    is_correct = True
    for key in expected_balls.keys():
      if drawn.count(key) < expected_balls[key]:
        is_correct = False
        break
    if is_correct:
      num_correct += 1

  return num_correct / num_experiments
