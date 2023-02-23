#!/usr/bin/env python3
"""Default to Python3"""

import random
import time
import sys

Outdoor = ['adrenaline forest','Skateboarding','a Bush Walk',
            'Hiking','Mountain Biking','The Beach', 'The River', 'The Pool','Gyming']
Indoor = ['Bouldering','Doctor Who', 'Drawing','Painting', 'Meditation', 'Music']
activity_type = {"Outdoor" : Outdoor, "Indoor" : Indoor}

def main():
    """ Determines what activity to do. """
    print('Pick your poison: ' + '1.',list(activity_type.keys())[0], ' 2.',list(activity_type.keys())[1])
    specified_type, num_results = choose_activity()
    activity_results = activity_selector(specified_type, num_results)
    print('Dayum! '+ activity_results + ', now that\'s one hell of a line up')
    sys.exit()


def choose_activity():    
    """ Prompt user to choose activity type. """
    print("A number, any number", end=" ")
    dot_timer = 0
    time.sleep(1)
    while dot_timer < 3:
        dot_timer = dot_timer + 1
        print('.', end=" ")
        sys.stdout.flush()
        time.sleep(0.75)
    specified_type = list(activity_type.keys())[int(input("as long as it's in the list): "))-1]
    print("You entered " + "\"" + specified_type + "\"" + " activities, good choice!")
    return  specified_type, int(input('On a scale of 1 to 5, how much fun do you want to have? '))


def activity_selector(specified_type, recommend_num):
    """ Randoly selects based on activity type. """
    line_up = ', '.join(random.sample( activity_type[specified_type], recommend_num))
    if recommend_num > 1:
        line_up = line_up[:line_up.rfind(',')+1] + ' and' + line_up[line_up.rfind(',')+1:]
    return line_up

    
if __name__ == '__main__':
    main()
    