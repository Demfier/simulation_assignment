"""
Problem Statement: The initial co-ordinate of a fighter plane is given which is
                   supposed to hit a bombing site. The bombing site is moving
                   and its co-ordinates at 1 second interval are given. If the
                   velocity of the bomb is 20 kmph and it is always directed
                   towards the bombing site, determine whether the bomb
                   will hit the bombing site successfully or not.

Note: The bomb would be said to successfully hit the target if it is within
      10km proximity of the target at point of time.
"""
import math

BOMBING_COORDINATES = [(80, 0), (90, -2), (99, -5), (108, -9), (116, -15),
                       (125, -18), (141, -29), (151, -28), (160, -25),
                       (169, -21), (179, -20), (181, -17)]

FIGHTER_INIT = (0, 50)

BOMB_VELOCITY = 20  # in kmph

INFINITY = math.atan(math.tan(math.pi / 2))


def get_direction(c1, c2):
    """
    Take two coordinates c1 and c2 and returns the angle between them (theta).
    """
    try:
        slope = (c2[1] - c1[1]) / float(c2[0] - c1[0])
        slope = math.atan(slope)
    except ZeroDivisionError:
        # This means that theta is 90
        slope = INFINITY
    return(slope)


def eucledian_distance(c1, c2):
    """
    Returns eucledian distance between two points with coordinates c1 and c2
    """
    return(math.sqrt((c2[1] - c1[1])**2 + (c2[0] - c1[0])**2))


def plane_hits():
    """
    The bomb will hit the bombing site if at the end its coordinates are in
    a 10km proximity range from the target.
    """
    bomb_coordinate = FIGHTER_INIT  # coordindates of the bomb
    for i, c in enumerate(BOMBING_COORDINATES):
        if i >= len(BOMBING_COORDINATES) - 1:
            print("The bomb misses the target")
            return(False)
        # Find theta, the direction of vector between bomb --> bombing
        # site and update bomb's coordinate
        direction = get_direction(bomb_coordinate, c)
        bomb_x = bomb_coordinate[0] + (BOMB_VELOCITY * 1) * math.cos(direction)
        bomb_y = bomb_coordinate[1] + (BOMB_VELOCITY * 1) * math.sin(direction)
        bomb_coordinate = (bomb_x, bomb_y)

        # Check if the bomb hits the target
        if eucledian_distance(bomb_coordinate,
                              BOMBING_COORDINATES[i + 1]) < 10:
            print("The fighter plane destroys the bombing site at t=%ds from "
                  "initialization" % (i+1))
            return(True)
    print("The plane misses the target")
    return(False)


if __name__ == '__main__':
    plane_hits()
