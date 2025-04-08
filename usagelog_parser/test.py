from datetime import datetime, timedelta

datetime_start = datetime(year=2020, month=10, day=1, hour=1, minute=10)
# log_end = datetime(year=2020, month=10, day=1, hour=1, minute=20)
datetime_end = datetime(year=2020, month=10, day=2, hour=2, minute=20)

# iterate every hour between start and end datetimes
def hourrange(start, end):
    hour = timedelta(seconds=3600)
    current_date = start

    while current_date < end:
        current_hour = current_date.replace(minute=0, second=0)
        next_date = min(current_hour + hour, end)
        yield (
            current_hour,
            (next_date - current_date).seconds // 60
        )
        current_date = next_date


days = []
minutes = []
for datetime_hour, minutes_used in hourrange(datetime_start, datetime_end):
    print(minutes_used)
    datetime_day = datetime_hour.replace(hour=0)
    if len(days) == 0 or days[-1] != datetime_day:
        days.append(datetime_day)
        minutes.append([0] * 24)

    minutes[-1][datetime_hour.hour] += minutes_used

print(minutes)
