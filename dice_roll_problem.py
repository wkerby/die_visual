from random import choice
trial_counter = 0
success_counter = 0
while trial_counter <= 1000000:
    die_event_list = [1,2,3,4,5,6]
    for i in die_event_list:
        roll_value = choice(die_event_list)
        if roll_value == i:
            success_counter += 1
            break
        else:
            pass
    trial_counter += 1

probability = (success_counter/trial_counter)
print(probability)
