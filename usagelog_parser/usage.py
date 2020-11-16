from datetime import datetime, timedelta
import argparse
import re

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('log', help="path to usage.log")

    args = parser.parse_args()

    surf(*parse(args))

def parse(args):

    f = open(args.log, 'r')

    # list of list of minutes used each hour of each day
    minutes = []
    days = []
    for line in f.readlines():
        match = re.match(
            '(\d{4}-\d{2}-\d{2}_\d{2}:\d{2}) (\d{4}-\d{2}-\d{2}_\d{2}:\d{2})',
            line
        )

        # parse valid lines
        if match and len(match.groups()) == 2:
            datetime_start = datetime.strptime(match.groups()[0], '%Y-%m-%d_%H:%M')
            datetime_end = datetime.strptime(match.groups()[1], '%Y-%m-%d_%H:%M')

            # ignore intervals longer than 12 hours
            if datetime_end - datetime_start > timedelta(hours=12):
                continue

            for datetime_hour, minutes_used in hourrange(datetime_start, datetime_end):
                datetime_day = datetime_hour.replace(hour=0)
                if len(days) == 0 or days[-1] != datetime_day:
                    days.append(datetime_day)
                    minutes.append([0] * 24)

                minutes[-1][datetime_hour.hour] += minutes_used

    return days, minutes

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


def surf(days, minutes):
    "Plot minutes eased each hour of day for each week"

    zerodate = datetime(1970, 1, 1)
    first_date = (days[0] - zerodate).days
    last_date = (days[-1] - zerodate).days

    plt.figure(figsize=(7, 60))
    plt.imshow(minutes, aspect='auto', extent=(0, 23, last_date, first_date))
    plt.yticks()
    plt.gca().yaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))

    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()


if __name__ == '__main__':
    main()
