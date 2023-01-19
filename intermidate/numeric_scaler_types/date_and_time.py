import datetime

d1 = datetime.date(2014, 1, 6)
# you can be explicit with the format
d2 = datetime.date(year=2014, month=1, day=6)

print('Standard Date {}'.format(d1))
print('Explict Date Format yyyy-m-d:  {}'.format(d2))

print('Todays date: {}'.format(datetime.date.today()))
