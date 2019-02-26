from datetime import datetime, timedelta
from functools import reduce


def hole_filter_str(data_input, dt_format ='%Y-%m-%d', is_sorted=True, units='days'):
    """
    Takes a list of dates as strings and return a list of dates as strings in the same format, which are the "holes".
    Strings are converted to datetime objects using dt_format pattern.
    :param data_input: a list of input strings
    :param dt_format: a pattern used in datetime.strptime()
    :param is_sorted: boolean, will trigger sort of the list if set to False
    :param units: timedelta units. One of following [days, hours]
    """
    dates_as_dt = list(map(lambda x: datetime.strptime(x, dt_format), data_input))
    data_filtered = hole_filter_dt(dates_as_dt, is_sorted, units)
    return list(map(lambda x: x.strftime(dt_format), data_filtered))


def reduce_f(x, y):
    """
    Function used in reduce method.
    :param x: pair of (list of "hole" datetime
    :param y: last processed "non-hole" datetime
    :return: reduced pair (x, y)
    """
    dt_delta = y - x[1]
    ext_units = x[2]  # inconvenient way to supply a parameter for a reduce function
    # it starts to look not concise :)
    if ext_units == "days":
        int_units = 'days'
        int_divisor = 1
    else:  # hours
        int_units = 'seconds'
        int_divisor = 60*60  # seconds --> hours
    # due to no attribute 'hours' on timedelta
    units_delta = int(getattr(dt_delta, int_units) / int_divisor)
    if units_delta < 0:
        raise ValueError("Looks like this list is not sorted")

    if units_delta == 1:
        return x[0], y, x[2]
    else:
        for i in range(1, units_delta):
            x[0].append(x[1] + timedelta(**{ext_units: i}))  # mutated x[0]
    return x[0], y, x[2]


def hole_filter_dt(input_dates, is_sorted=True, units='days'):
    """
    Takes a list of datetime instances and return a list of datetimes, which are the "holes" in this sequence.
    :param input_dates: a list of input datetimes
    :param is_sorted: boolean, will trigger sort of the list if set to False
    :param units: timedelta units. One of following [days, seconds, microseconds, milliseconds, minutes, hours, weeks]
    :return: a list of found "hole" datetimes
    """
    found_holes = []  # can be mutated in reduce_f
    if len(input_dates) > 1:
        if not is_sorted:
            input_dates = sorted(input_dates)
        reduce(reduce_f, input_dates[1:], (found_holes, input_dates[0], units))
    return found_holes
