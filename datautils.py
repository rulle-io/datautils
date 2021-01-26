from datetime import datetime, timedelta


def date_hole_printer(dates_list, period_start=None, period_end=None, dt_format='%Y-%m-%d', units='days', is_sorted=True):
    """
    Finds 'holes' in interval [period_start .. period_end) given a list of existing dates as strings.
    Return a list of dates as strings in the same format, which are the "holes" in the interval.
    Strings are converted to datetime objects using 'dt_format' pattern.
    :param period_start: start of period, inclusive. If None, first element of date_list is used as period_end.
    :param period_end: end of period, exclusive. If None, last element of date_list is used as period_end.
    :param dates_list: a list of input strings
    :param dt_format: a pattern used in datetime.strptime()
    :param units: timedelta units. One of following [days, hours]
    :param is_sorted: Whether dates_list is sorted.
    :returns sorted list of 'holes' as string(s)
    """
    # input parameters validation
    if dates_list is None:
        raise ValueError("Invalid dates list")
    if len(dates_list) == 0:
        raise ValueError("Empty dates list")

    if not is_sorted:
        dates_list = sorted(dates_list)
        
    if period_start is None:
        period_start = dates_list[0]
    if period_end is None:
        end_delta = 1
        period_end = dates_list[-1] # Inclusive date TODO
    else:
        end_delta = 0
    if period_start > period_end:
        raise ValueError("Invalid interval")
    if period_start == period_end:
        raise ValueError("Empty interval")

    dates_as_dt = map(lambda x: datetime.strptime(x, dt_format), dates_list)
    
    period_start_dt = datetime.strptime(period_start, dt_format)
    period_end_dt = datetime.strptime(period_end, dt_format) # Inclusive -> Exclusive 
    data_filtered = hole_filter_dt(period_start_dt, period_end_dt, dates_as_dt, units, end_delta)
    return list(map(lambda x: x.strftime(dt_format), data_filtered))


def get_period_length_in_units(period_start, period_end, units, end_delta=0):
    period_delta = period_end - period_start
    if units == "days":
        int_units = 'days'
        int_divisor = 1
        extra_delta = timedelta(days=end_delta)
    elif units == "hours":
        int_units = 'seconds'
        int_divisor = 60 * 60  # seconds --> hours
        # due to no attribute 'hours' on timedelta
        extra_delta = timedelta(hours=end_delta)
    else:
        raise ValueError("Unsupported unit")
    # due to no attribute 'hours' on timedelta
    units_delta = int(getattr(period_delta + extra_delta, int_units) / int_divisor)
    return units_delta


def hole_filter_dt(period_start, period_end, input_dates, units='days', end_delta=0):
    """
    Takes a list of datetime instances and return a list of datetimes, which are the "holes" in this sequence.
    :param period_start: start of period, inclusive (datetime)
    :param period_end: end of period, exclusive (datetime)
    :param input_dates: a list of input (as datetime)
    :param units: timedelta units. One of following [days, hours]
    :returns: a sorted list of found "holes" (as datetime)
    """

    full_list = generate_dt_list(period_start, period_end, units, end_delta)
    full_set = set(full_list)
    actual_set = set(input_dates)
    found_holes = sorted(list(full_set - actual_set))
    return found_holes


def generate_dt_list(period_start_dt, period_end_dt, units, end_delta=0):
    """
    Generates a list of datetime objects using given interval [period_start_dt .. period_end_dt)
    :param period_start_dt: start of period, inclusive
    :param period_end_dt: end of period, exclusive
    :param units:
    :returns: a generated list
    """
    units_number = get_period_length_in_units(period_start_dt, period_end_dt, units, end_delta)
    full_list = [period_start_dt + timedelta(**{units: i}) for i in range(0, units_number)]
    return full_list
