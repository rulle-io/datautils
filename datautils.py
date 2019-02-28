from datetime import datetime, timedelta


def hole_filter_str(period_start, period_end, data_input, dt_format ='%Y-%m-%d', units='days'):
    """
    Finds 'holes' in interval [period_start .. period_end) given a list of existing dates as strings.
    Return a list of dates as strings in the same format, which are the "holes" in the interval.
    Strings are converted to datetime objects using 'dt_format' pattern.
    :param period_start: start of period, inclusive
    :param period_end: end of period, exclusive
    :param data_input: a list of input strings
    :param dt_format: a pattern used in datetime.strptime()
    :param units: timedelta units. One of following [days, hours]
    :returns sorted list of 'holes' as string(s)
    """
    dates_as_dt = map(lambda x: datetime.strptime(x, dt_format), data_input)
    period_start_dt = datetime.strptime(period_start, dt_format)
    period_end_dt = datetime.strptime(period_end, dt_format)
    data_filtered = hole_filter_dt(period_start_dt, period_end_dt, dates_as_dt, units)
    return list(map(lambda x: x.strftime(dt_format), data_filtered))


def get_period_length_in_units(period_start, period_end, units):
    period_delta = period_end - period_start
    if units == "days":
        int_units = 'days'
        int_divisor = 1
    elif units == "hours":
        int_units = 'seconds'
        int_divisor = 60 * 60  # seconds --> hours
        # due to no attribute 'hours' on timedelta
    else:
        raise ValueError("Unsupported unit")
    # due to no attribute 'hours' on timedelta
    units_delta = int(getattr(period_delta, int_units) / int_divisor)
    return units_delta


def hole_filter_dt(period_start, period_end, input_dates, units='days'):
    """
    Takes a list of datetime instances and return a list of datetimes, which are the "holes" in this sequence.
    :param period_start: start of period, inclusive (datetime)
    :param period_end: end of period, exclusive (datetime)
    :param input_dates: a list of input (as datetime)
    :param units: timedelta units. One of following [days, hours]
    :returns: a sorted list of found "holes" (as datetime)
    """

    full_list = generate_dt_list(period_start, period_end, units)
    full_set = set(full_list)
    actual_set = set(input_dates)
    found_holes = sorted(list(full_set - actual_set))
    return found_holes


def generate_dt_list(period_start_dt, period_end_dt, units):
    """
    Generates a list of datetime objects using given interval [period_start_dt .. period_end_dt)
    :param period_start_dt: start of period, inclusive
    :param period_end_dt: end of period, exclusive
    :param units:
    :returns: a generated list
    """
    units_number = get_period_length_in_units(period_start_dt, period_end_dt, units)
    full_list = [period_start_dt + timedelta(**{units: i}) for i in range(0, units_number)]
    return full_list
