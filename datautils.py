from datetime import datetime, timedelta
from functools import reduce


def hole_filter_str(data_input, dt_format ='%Y%m%d'):
    """Takes a list of dates as strings and return a list of dates, which are the "holes".
    """
    dates_as_dt = list(map(lambda x: datetime.strptime(x, dt_format), data_input))
    # TODO test invalid format
    data_filtered = hole_filter_dt(dates_as_dt)
    return list(map(lambda x: x.strftime(dt_format), data_filtered))


def reduce_f(x, y):
    d_delta = timedelta(days=1)
    delta = (y - x[1]).days
    #  if (y - x[1] == d_delta):
    if (delta == 1):
        return (x[0], y)
    else:
        for i in range(1, delta):
            x[0].append(x[1] + timedelta(days=i))  # mutated x[0]
    return (x[0], y)


def hole_filter_dt(input_dates, is_sorted=True):
    found_holes = [] # can be mutated in reduce_f
    if len(input_dates) > 1:
        reduce(reduce_f, input_dates[1:], (found_holes, input_dates[0]))
    return found_holes
