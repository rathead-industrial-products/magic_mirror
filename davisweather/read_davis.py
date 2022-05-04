import json
import datetime

f = open("davis")
linenum = 1
start_time = 0

hourly_wind = [0] * 24

jline = f.readline()
while (jline):
    try:
        data = json.loads(jline[:-3])
    except:
        print (linenum, "exception, data = ", len(data), "\n\n\n\r")

    ts = data["data"]["ts"]
    if start_time == 0: start_time = ts


    hour = datetime.datetime.fromtimestamp(ts).strftime("%H")

    min = (ts - start_time) / 60
    wind_avg = data["data"]["conditions"][0]["wind_speed_avg_last_10_min"]
    wind_dir = data["data"]["conditions"][0]["wind_dir_scalar_avg_last_10_min"]
    gust = data["data"]["conditions"][0]["wind_speed_hi_last_10_min"]
    gust_dir = data["data"]["conditions"][0]["wind_dir_at_hi_speed_last_10_min"]
    print ("%d, %s, %s, %s, %s" % (min, wind_avg, wind_dir, gust, gust_dir))
    jline = f.readline()
    linenum += 1

f.close()
hour = datetime.datetime.fromtimestamp(start_time).strftime("%H")
print(hour, datetime.datetime.fromtimestamp(start_time))


