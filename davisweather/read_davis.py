import json
import datetime


WIND_BINS = 31
DIR_BINS  = 8

def bin(value):
    max_bin = WIND_BINS - 1
    return(max_bin if (int(value) >= max_bin) else int(value))

def ordinal(dir):
    SECTOR = (337, 23, 68, 112, 157, 202, 247, 292, 337)
    if dir > SECTOR[0] or dir <= SECTOR[1]: return (0)
    for o in range(1, 8):
        if dir > SECTOR[o] and dir <= SECTOR[o+1]:
            return (o)


f = open("davis")
linenum = 1
start_time = 0

# [hour][wind_speed]
hourly_wind = [[0 for i in range(WIND_BINS)] for j in range(24)]
hourly_dir = [[0 for i in range(DIR_BINS)] for j in range(24)]
hourly_gust = [[0 for i in range(WIND_BINS)] for j in range(24)]
hourly_gust_dir = [[0 for i in range(DIR_BINS)] for j in range(24)]

jline = f.readline()
while (jline):
    try:
        data = json.loads(jline[:-3])
    except:
        print (linenum, "exception, data = ", len(data), "\n\n\n\r")

    ts = data["data"]["ts"]
    if start_time == 0: start_time = ts


    hour = int(datetime.datetime.fromtimestamp(ts).strftime("%H"))

    min = (ts - start_time) / 60
    wind_avg = data["data"]["conditions"][0]["wind_speed_avg_last_10_min"]
    wind_dir = data["data"]["conditions"][0]["wind_dir_scalar_avg_last_10_min"]
    gust = data["data"]["conditions"][0]["wind_speed_hi_last_10_min"]
    gust_dir = data["data"]["conditions"][0]["wind_dir_at_hi_speed_last_10_min"]

    hourly_wind[hour][bin(wind_avg)] += 1
    hourly_dir[hour][ordinal(wind_dir)] += 1
    hourly_gust[hour][bin(gust)] += 1
    hourly_gust_dir[hour][ordinal(gust_dir)] += 1

    jline = f.readline()
    linenum += 1

f.close()

for h in range(24):
    avg = 0
    high = 0
    for i in range(WIND_BINS):
        avg += i * hourly_wind[h][i]
        high = i if (hourly_gust[h][i] and i > high) else high
    print (avg / (WIND_BINS-1), ',', high)


