# (Big) data engineering micro-tasks.
This project has a goal to provide utility functions I found useful in working with (Big) data engineering tasks.<br/>
And the task should be generic enough to have this code in a public repository.

## Utility "Date interval hole(s) printer".
Problem: there is a list of data partitions and there is a need to identify 'holes' in this internal.<br/>
Example:  Given list of partitions between "2018-01-01" and "2018-12-31", find missing ones.

### Find holes in a month's partitions
#### Method definition
```python
def date_hole_printer(dates_list, period_start=None, period_end=None, dt_format='%Y-%m-%d', units='days',
                      is_sorted=True):
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
    :returns sorted list of 'holes' (strings)
    """
```

#### An example
```python
f_input = [
  '2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06',
  '2020-12-08', '2020-12-09', '2020-12-10', '2020-12-11', '2020-12-12', '2020-12-13', 
  '2020-12-14', '2020-12-15', '2020-12-16', '2020-12-17', '2020-12-18', '2020-12-19',
  '2020-12-20', '2020-12-22', '2020-12-23', '2020-12-24', '2020-12-25', '2020-12-26',
  '2020-12-27', '2020-12-28', '2020-12-29', '2020-12-30'
]
f_output = date_hole_printer(dates_list=f_input)
>f_output ['2020-12-07', '2020-12-21']
```
