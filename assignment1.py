"""
Problem Statement: The initial co-ordinate of a fighter plane is given which is
                   supposed to hit a bombing site. The bombing site is moving
                   and its co-ordinates at 1 second interval are given. If the
                   velocity of the plane is __kmph and it is always directed
                   towards the bombing site, determine whether the fighter
                   plane will hit the bombing site successfully or not.
"""
import math

BOMBING_COORDINATES = [(80, 0), (90, -2), (99, -5), (108, -9), (116, -15),
                       (125, -18), (141, -29), (151, -28), (160, -25),
                       (169, -21), (179, -20), (181, -17)]

FIGHTER_INIT = (0, 50)

FIGHTER_VELOCITY = 20

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


def plane_hits():
    """
    The plane will hit the bombing site if at the end its coordinates co-incide
    with the bombing site's
    """
    fighter_coordinate = FIGHTER_INIT  # coordindates of the fighter plane
    for i, c in enumerate(BOMBING_COORDINATES):
        if i >= len(BOMBING_COORDINATES) - 1:
            return(False)
        # Find theta, the direction of vector between fighter-plane --> bombing
        # site and update fighter coordinate
        direction = get_direction(fighter_coordinate, c)
        fighter_x = fighter_coordinate[0] + (FIGHTER_VELOCITY * 1) * math.cos(direction)
        fighter_y = fighter_coordinate[1] + (FIGHTER_VELOCITY * 1) * math.sin(direction)
        fighter_coordinate = (fighter_x, fighter_y)
        if round(fighter_coordinate[0]) == BOMBING_COORDINATES[i + 1][0] and round(fighter_coordinate[1]) == BOMBING_COORDINATES[i + 1][1]:
            return(True)
    return(False)


if __name__ == '__main__':
    if plane_hits():
        print("The Figher plane hits the target")
    else:
        print("The Fighter planes would miss the target")
