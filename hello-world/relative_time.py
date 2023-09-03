

from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=12, weeks=0, hour=20)

print(now)