import datetime
import pytz

# store this in the database or something
_now = datetime.datetime.utcnow()

# you can view the timezone which None 
print(_now.tzinfo)

# when displaying the datetime use the pytz module
localized_datetime = pytz.utc.localize(_now)

# right now the tzinfo is UTC
print(localized_datetime.tzinfo)

# then apply the timezone you want
timezone_datetime = localized_datetime.astimezone(pytz.timezone('Africa/Nairobi'))
print(timezone_datetime)
