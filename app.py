import os
import time
import math
from lib.rawinputreader import rawinputreader
from config import WIDTH, HEIGHT, GRACE_FACTOR, CALCULATION_DELTA
import json
import pprint

RAW_INPUT = rawinputreader()


def get_mouse_movement_from_raw_input(raw_input):
    if len(raw_input) > 0:
        LEFT = raw_input[0][6]
        DOWN = raw_input[0][7]
        return (LEFT, DOWN)
    else:
        return (0, 0)


def print_directions(raw_input):
    if len(raw_input) > 0:
        LEFT = raw_input[0][6]
        DOWN = raw_input[0][7]
        if DOWN > 0:
            print('moving mouse upwards')
        elif DOWN < 0:
            print('moving mouse downwards')
        if LEFT > 0:
            print('moving mouse right')
        elif LEFT < 0:
            print('moving mouse left')


def track_mouse_movement():
    events = RAW_INPUT.pollEvents()
    # time.sleep(.04)
    MOUSE_MOVEMENT = get_mouse_movement_from_raw_input(events)
    time.sleep(CALCULATION_DELTA)  # DO IN NEED THIS ANYMORE?
    origin = (WIDTH / 2, HEIGHT / 2)
    dx         = MOUSE_MOVEMENT[0]
    dy         = MOUSE_MOVEMENT[1]

    if dx == 0 and dy == 0:
        return {
            'displacement_vector': (0, 0),
            'new_point': (WIDTH / 2, HEIGHT / 2),
            'no_movement': True
        }

    else:
        return {
            'displacement_vector': (dx, dy),
            'new_point': ((((GRACE_FACTOR * dx)) + WIDTH / 2),
                          (((GRACE_FACTOR * dy)) + HEIGHT / 2)),
            'no_movement': False
        }


if __name__=='__main__':
    while True:
        print(
        track_mouse_movement()
        )