import datetime

Y, M, D = map(int, raw_input().split('/'))
date = datetime.date(Y + 2000, M, D)
while (date.year - 2000) % (date.month * date.day):
    date += datetime.timedelta(1)
print "%04d/%02d/%02d" % (date.year - 2000, date.month, date.day)
