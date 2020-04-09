# importing csv module
import csv
from datetime import datetime, timedelta

# csv file name
filename = "churchgate_up.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)


# fetching current time
x = datetime.now()
x = x.strftime("%H") + ":" + x.strftime("%M")

# converting x into a time variable again
x = x.split(":")
x = timedelta(hours=int(x[0]), minutes=int(x[1]))

# checking running trains
transit = []

for i in range(0, len(rows)):
    schedule = []
    details = []
    stations = []
    for j in range(3, len(rows[i])):
        if rows[i][j]:
            # schedule.append(rows[i][j])
            t = rows[i][j]
            t = t.split(":")
            t = timedelta(hours=int(t[0]), minutes=int(t[1]))
            schedule.append(t)
            stations.append(fields[j])

    # print(schedule)

    if schedule[0] < x < schedule[-1]:
        # print("running: ", rows[i][0])
        transit.append(int(rows[i][0]))


# current status data
print(transit)

route = str(input("Enter Route Code: "))

schedule = []
stations = []

for i in range(0, len(rows)):
    if route == rows[i][0]:
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])

# distance data


# csv file name
filename_d = "distance_up.csv"

# initializing the titles and rows list
fields_d = []
rows_d = []

# reading csv file
with open(filename_d, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields_d = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows_d.append(row)


flag = True

# for trains in stations
for k in range(0, len(schedule)):
    if schedule[k] == x:
        # s = True
        a = stations[k]
        b = stations[k+1]
        print("Currently Running from {} to {} ".format(a, b))
        a_t = schedule[k]
        b_t = schedule[k+1]
        i_dist = 0
        print(i_dist)
        flag = False
        break

    # for trains not in stations
if flag:
    for k in range(0, len(schedule)):
        if schedule[k] > x:
            # s = False
            a = stations[k - 1]
            b = stations[k]
            for i in range(0, len(rows_d)):
                if a == rows_d[i][0]:
                    d_a = float(rows_d[i][1])
                if b == rows_d[i][0]:
                    d_b = float(rows_d[i][1])
            t_dist = d_a - d_b
            print("Currently Running from {} to {} ".format(a, b))
            a_t = schedule[k-1]
            b_t = schedule[k]
            # calculting total time
            time = b_t - a_t
            time = str(time)
            time = time.split(":")
            # calculating current time
            time_c = x - a_t
            time_c = str(time_c)
            time_c = time_c.split(":")
            i_dist = t_dist / float(time[1]) * float(time_c[1])
            print(i_dist)
            # print(t_dist / float(time[1]))
            flag = False
            break

# loc = str(input("Enter Departing Station: "))
dist_rl = float(input("Enter Distance Covered: "))

if i_dist > dist_rl:
    print("Train Delayed")

else:
    print("Train on time")




