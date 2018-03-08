
from datetime import datetime,timedelta

valid_start = datetime(2017, 8, 21, 10)
valid_end   = datetime(2017, 8, 21, 11)

invalid_start = valid_start - timedelta(1)
invalid_end   = valid_end   + timedelta(1)
