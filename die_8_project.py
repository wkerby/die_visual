from random import *

class Die():
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
    def dice_roll(self):
        return randint(1,self.num_sides)

def count_num(mylist, number):
    count = 0
    for i in mylist:
        if i == number:
            count += 1
        else:
            continue
    return count

die3 = Die()
die4 = Die()
die5 = Die()

triple_die_count_list = []
triple_die_roll_list = [die3.dice_roll() + die4.dice_roll() + die5.dice_roll() for i in list(range(0,1000))]
for i in list(range(3,19)):
    triple_die_count_list.append(count_num(triple_die_roll_list,i))
#continue at the bottom of the page

die1 = Die(8)
die2 = Die(8)

die_8_count_list = []
die_8_roll_list = [die1.dice_roll() + die2.dice_roll() for i in list(range(0,1000000))]


for i in list(range(2,17)):
    die_8_count_list.append(count_num(die_8_roll_list,i))


import pygal
histogram = pygal.Bar()
histogram.title = "Result of D8 + D8 dice roll"
histogram.x_labels = ["2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
histogram.x_title = "Result"
histogram.y_title = "Result frequency"
histogram.add("D8 + D8", die_8_count_list)
histogram.render_to_file('die_8_visual.svg')


histogram1 = pygal.Bar()
histogram1.title = "Result of D6 + D6 + D6 dice roll"
histogram1.x_labels = ["3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
histogram1.x_title = "Result"
histogram1.y_title = "Result frequency"
histogram1.add("D6 + D6 + D6",triple_die_count_list)
histogram1.render_to_file('triple_die_visual.svg')
