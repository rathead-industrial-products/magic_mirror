import json

f = open("davis")
linenum = 1

jline = f.readline()
while (jline):
    try:
        data = json.loads(jline[:-3])
    except:
        print (linenum, "exception, data = ", len(data), "\n\n\n\r")
        print (jline)
        print (data['data'])
        for key, value in data:
            print(key, value)
        break
    otmp = data["data"]["conditions"][0]["temp"]
    ohum = data["data"]["conditions"][0]["hum"]
    itmp = data["data"]["conditions"][1]["temp_in"]
    ihum = data["data"]["conditions"][1]["hum_in"]
    #print (linenum, otmp, ohum, itmp, ihum)
    jline = f.readline()
    linenum += 1

f.close()


