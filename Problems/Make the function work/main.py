def closest_higher_mod_5(x):
    reminder = x % 5
    if reminder == 0:
        return x
    return x + 5 - reminder
