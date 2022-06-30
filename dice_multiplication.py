from random import *

class Die():
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
    def dice_roll(self):
        return randint(1,self.num_sides) #randint arguments don't need to add a '+1' ending element as in the range function
def num_count(mylist, number):
    count = 0
    for i in mylist:
        if i == number:
            count += 1
        else:
            continue
    return count 

die1 = Die()
die2 = Die()
multiply_die_count_list = []
multiply_die_roll_list = [die1.dice_roll()*die2.dice_roll() for i in list(range(0,1000))]

for i in list(range(1,37)):
    multiply_die_count_list.append(num_count(multiply_die_roll_list,i))


import pygal
histogram = pygal.Bar()
histogram.title = "Results of a D6*D6 dice roll"
histogram.x_labels = [str(i) for i in list(range(1,37))]
histogram.x_title = "Result"
histogram.y_title = "Result frequency"
histogram.add("D6*D6",multiply_die_count_list)
histogram.render_to_file('multiply_die_visual.svg')
