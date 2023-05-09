def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2 - time_1

def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    return seconds_difference(time_1, time_2) / 3600
"""
I read the instructions and understood what you meant by the prompt. I read the snippet
and assumed this was done through division, and didn't notice I needed to convert as well.
"""

#Function Complete

def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    return hours + (minutes / 60) + (seconds / 60 / 60)

#Function Complete

def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0
    Military Time

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(25)
    1

    """
    return hours % 24
#Function Complete


### Write your get_hours function definition here:
def get_hours(seconds):
        """ (number) -> number
        Return the number of hours equivelant to seconds.

        It takes 3600 seconds to make an hour.
        >>> get_hours(3600)
        1
        It takes 7200 seconds to make an hour.
        >>> get_hours(7200)
        2
        """
        return to_24_hour_clock(seconds // 3600)
#Function Complete

### Write your get_minutes function definition here:
def get_minutes(seconds):
        """ (number) -> number
        Return the remainder of seconds remaining and convert to minutes.
        
        >>> get_minutes(60)
        1
        >>> get_minutes(120)
        2
        >>> get_minutes(3600)
        0
        """
        return (seconds % 3600) // 60
#Function Complete

### Write your get_seconds function definition here:
def get_seconds(seconds):
        """ (number) -> number
        Return the remainder of seconds remaining and convert to minutes.
        
        >>> get_seconds(3600)
        20
        >>> get_seconds(7200)
        40
        """
        return (seconds % 3600) % 60
#Function Complete


def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    return to_24_hour_clock(time - utc_offset)
#Function Complete

def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    return to_24_hour_clock(time + (utc_offset))
#Function Complete
