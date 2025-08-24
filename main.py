from datetime import datetime
import pytz

# Example: Philippines (Asia/Manila)
tz = pytz.timezone("Asia/Manila")
local_time = datetime.now(tz)

print("Local Time:", local_time.strftime("%Y-%m-%d %H:%M"))
