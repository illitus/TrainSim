from django.shortcuts import render
from django.http import HttpResponse
import csv
from datetime import datetime, timedelta, time,date

# Create your views here.
def station_status(request):
        
    # csv file name
    filename = "statics/csv/churchgate_up.csv"

    # initializing the titles and rows list
    fields_up = []
    rows_up = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields_up = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows_up.append(row)

    # csv file name
    filename = "statics/csv/virar_down.csv"

    # initializing the titles and rows list
    fields_down = []
    rows_down = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields_down = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows_down.append(row)

    filename_d = "statics/csv/distance_up.csv"

    # initializing the titles and rows list
    fields_d_up = []
    rows_d_up = []

    # reading csv file
    with open(filename_d, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields_d_up = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows_d_up.append(row)


    filename_d_down = "statics/csv/distance_down.csv"

    # initializing the titles and rows list
    fields_d_down = []
    rows_d_down = []

    # reading csv file
    with open(filename_d_down, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields_d_down = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows_d_down.append(row)

    # fetching current time
    x = datetime.now()
    x = x.strftime("%H") + ":" + x.strftime("%M")

    # converting x into a time variable again
    x = x.split(":")
    x = timedelta(hours=int(x[0]), minutes=int(x[1]))

    b = request.POST['Station']

    # for up line
    if fields_up.index(b):
        b_i = fields_up.index(b)

    trains = []
    for i in range(0, len(rows_up)):
        details = []
        flag = False
        flag1 = True
        if rows_up[i][b_i]:
            b_t = rows_up[i][b_i]
            b_t = b_t.split(":")
            b_t = timedelta(hours=int(b_t[0]), minutes=int(b_t[1]))
            if b_t <= x:
                for j in range(b_i+1, len(rows_up[i])):
                    if flag1:
                        if rows_up[i][j]:
                            c_i = j
                            c_t = rows_up[i][j]
                            c = fields_up[j]
                            c_t = c_t.split(":")
                            c_t = timedelta(hours=int(c_t[0]), minutes=int(c_t[1]))
                            if b_t <= x <= c_t:
                                flag = True
                                flag1 = False
                            break


                if flag:
                    for p in range(0, len(rows_d_up)):
                        if b == rows_d_up[p][0]:
                            d_b = float(rows_d_up[p][1])
                        if c == rows_d_up[p][0]:
                            d_c = float(rows_d_up[p][1])

                    t_dist = d_c - d_b

                    # calculting total time
                    time = c_t - b_t
                    time = str(time)
                    time = time.split(":")
                    # calculating current time
                    time_c = x - b_t
                    time_c = str(time_c)
                    time_c = time_c.split(":")
                    i_dist = (t_dist / float(time[1])) * float(time_c[1])
                    details.append(rows_up[i][0])
                    details.append(b)
                    details.append(round(i_dist,2 ))
                    details.append(c)
                    # print(i_dist)
                    trains.append(details)

    for i in range(0, len(rows_up)):
        details = []
        flag = False
        flag1 = True
        if rows_up[i][b_i]:
            b_t = rows_up[i][b_i]
            b_t = b_t.split(":")
            b_t = timedelta(hours=int(b_t[0]), minutes=int(b_t[1]))
            if b_t >= x:
                for j in range(b_i-1, 2, -1):
                    if flag1:
                        if rows_up[i][j]:
                            a_i = j
                            a_t = rows_up[i][j]
                            a = fields_up[j]
                            a_t = a_t.split(":")
                            a_t = timedelta(hours=int(a_t[0]), minutes=int(a_t[1]))
                            if a_t <= x <= b_t:
                                flag = True
                                flag1 = False
                            break


                if flag:
                    for p in range(0, len(rows_d_up)):
                        if b == rows_d_up[p][0]:
                            d_b = float(rows_d_up[p][1])
                        if a == rows_d_up[p][0]:
                            d_a = float(rows_d_up[p][1])

                    t_dist = d_b - d_a

                    # calculting total time
                    time = b_t - a_t
                    time = str(time)
                    time = time.split(":")
                    # calculating current time
                    time_c = x - a_t
                    time_c = str(time_c)
                    time_c = time_c.split(":")
                    i_dist = (t_dist / float(time[1])) * float(time_c[1])
                    details.append(rows_up[i][0])
                    details.append(a)
                    details.append(round(i_dist, 2))
                    details.append(b)
                    # print(i_dist)
                    trains.append(details)

    # virar down line

    if fields_down.index(b):
        b_i = fields_down.index(b)

    for i in range(0, len(rows_down)):
        details = []
        flag = False
        flag1 = True
        if rows_down[i][b_i]:
            b_t = rows_down[i][b_i]
            b_t = b_t.split(":")
            b_t = timedelta(hours=int(b_t[0]), minutes=int(b_t[1]))
            if b_t <= x:
                for j in range(b_i+1, len(rows_down[i])):
                    if flag1:
                        if rows_down[i][j]:
                            c_i = j
                            c_t = rows_down[i][j]
                            c = fields_down[j]
                            c_t = c_t.split(":")
                            c_t = timedelta(hours=int(c_t[0]), minutes=int(c_t[1]))
                            if b_t <= x <= c_t:
                                flag = True
                                flag1 = False
                            break


                if flag:
                    for p in range(0, len(rows_d_down)):
                        if b == rows_d_down[p][0]:
                            d_b = float(rows_d_down[p][1])
                        if c == rows_d_down[p][0]:
                            d_c = float(rows_d_down[p][1])

                    t_dist = d_c - d_b

                    # calculting total time
                    time = c_t - b_t
                    time = str(time)
                    time = time.split(":")
                    # calculating current time
                    time_c = x - b_t
                    time_c = str(time_c)
                    time_c = time_c.split(":")
                    i_dist = (t_dist / float(time[1])) * float(time_c[1])
                    details.append(rows_down[i][0])
                    details.append(b)
                    details.append(round(i_dist, 2))
                    details.append(c)
                    # print(i_dist)
                    trains.append(details)

    for i in range(0, len(rows_down)):
        details = []
        flag = False
        flag1 = True
        if rows_down[i][b_i]:
            b_t = rows_down[i][b_i]
            b_t = b_t.split(":")
            b_t = timedelta(hours=int(b_t[0]), minutes=int(b_t[1]))
            if b_t >= x:
                for j in range(b_i-1, 2, -1):
                    if flag1:
                        if rows_down[i][j]:
                            a_i = j
                            a_t = rows_down[i][j]
                            a = fields_down[j]
                            a_t = a_t.split(":")
                            a_t = timedelta(hours=int(a_t[0]), minutes=int(a_t[1]))
                            if a_t <= x <= b_t:
                                flag = True
                                flag1 = False
                            break


                if flag:
                    for p in range(0, len(rows_d_down)):
                        if b == rows_d_down[p][0]:
                            d_b = float(rows_d_down[p][1])
                        if a == rows_d_down[p][0]:
                            d_a = float(rows_d_down[p][1])

                    t_dist = d_b - d_a

                    # calculting total time
                    time = b_t - a_t
                    time = str(time)
                    time = time.split(":")
                    # calculating current time
                    time_c = x - a_t
                    time_c = str(time_c)
                    time_c = time_c.split(":")
                    i_dist = (t_dist / float(time[1])) * float(time_c[1])
                    details.append(rows_down[i][0])
                    details.append(a)
                    details.append(round(i_dist, 2))
                    details.append(b)
                    # print(i_dist)
                    trains.append(details)
    
    statfields=[]
    statlist=[]
    with open('statics/csv/distance_up.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    statlist1=[]
    for i in statlist:
        statlist1.append(i[0:3].upper())

    return render(request,'dashboard/station_status.html',{'station':b,'timenow':datetime.now(),'trains':trains, 'statlist':statlist, 'statlist1':statlist1})
    

def dist_up(schedule,stations,x):
    filename_d = "statics/csv/distance_up.csv"

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
                t_dist = d_b - d_a
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
                i_dist = (t_dist / float(time[1])) * float(time_c[1])
                i_dist = round(i_dist,2)
                
                flag = False
                break
    return i_dist

def dist_down(schedule,stations,x):
    filename_d = "statics/csv/distance_down.csv"

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
    if flag:
        for k in range(0, len(schedule)):
            if schedule[k] > x:
                # s = False
                a = stations[k - 1]
                b = stations[k]
                for i in range(0, len(rows_d)):
                    if a.lower() == rows_d[i][0].lower():
                        d_a = float(rows_d[i][1])
                    if b == rows_d[i][0]:
                        d_b = float(rows_d[i][1])
                t_dist = d_b - d_a
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
                i_dist = (t_dist / float(time[1])) * float(time_c[1])
                i_dist = round(i_dist,2)
                flag = False
                break
    return i_dist

def dashboard(request):

    if(request.POST['Line']=='WR : Virar to Churchgate'):
        return dashboard_vircg(request)
    if(request.POST['Line']=='WR : Churchgate to Virar'):
        return dashboard_cgvir(request)

def dashboard_vircg(request):
    
    cg_up = "statics/csv/churchgate_up.csv"
    stat="statics/csv/distance_up.csv"
    # initializing the titles and rows list
    transit=[]
    new_schedule=[]
    fields = []
    rows = []
    #print(os.getcwd())
    # reading csv file
    with open(cg_up, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        # print("Total no. of rows: %d" % csvreader.line_num)
    statfields=[]
    statlist=[]
    with open(stat, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    # fetching current time
    x = datetime.now()
    #x=time(10,3,0)
    x = x.strftime("%H") + ":" + x.strftime("%M")

    # converting x into a time variable again
    x = x.split(":")
    x = timedelta(hours=int(x[0]), minutes=int(x[1]))

    # checking running trains
    new_schedule=[]
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
            details.append(rows[i][0])
            flag = True

            # for trains in stations
            for k in range(0, len(schedule)):
                if schedule[k] == x:
                    s = dist_up(schedule,stations,x)
                    
                    details.append(stations[k].upper())
                    details.append(10+statlist.index(stations[k])*37.5)
                    details.append(s)
                    flag = False
                    break

            # for trains not in stations
            if flag:
                for k in range(0, len(schedule)):
                    if schedule[k] > x:
                        s = dist_up(schedule,stations,x)
                        details.append(stations[k - 1].upper())
                        details.append(10+statlist.index(stations[k-1])*37.5)                    
                        details.append(s)
                        flag = False
                        break
            # print(details)
            transit.append(details)            
        

    for i in range(0, len(rows)):
        schedule = []
        details = []
        stations = []
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])

        if schedule[0] < x < schedule[-1]:
            flag = True
            for k in range(3, len(rows[i])):
                if rows[i][k]:
                    details.append(rows[i][k])
                else:
                    details.append('----:----')

            new_schedule.append(details)
    ziplist=zip(transit,new_schedule)
    return render(request,"dashboard/vircg.html",{'timenow':x,'ziplist':ziplist})

def dashboard_cgvir(request):
    cg_up = "statics/csv/virar_down.csv"
    stat="statics/csv/distance_down.csv"
    # initializing the titles and rows list
    transit=[]
    new_schedule=[]
    fields = []
    rows = []
    #print(os.getcwd())
    # reading csv file
    with open(cg_up, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        # print("Total no. of rows: %d" % csvreader.line_num)
    statfields=[]
    statlist=[]
    with open(stat, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    # fetching current time
    x = datetime.now()
    #x=time(10,3,0)
    x = x.strftime("%H") + ":" + x.strftime("%M")

    # converting x into a time variable again
    x = x.split(":")
    x = timedelta(hours=int(x[0]), minutes=int(x[1]))

    # checking running trains
    new_schedule=[]
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
            details.append(rows[i][0])
            flag = True

            # for trains in stations
            for k in range(0, len(schedule)):
                if schedule[k] == x:
                    s = dist_down(schedule,stations,x)
                    details.append(stations[k].upper())
                    details.append(10+statlist.index(stations[k])*37.5)
                    details.append(s)
                    flag = False
                    break

            # for trains not in stations
            if flag:
                for k in range(0, len(schedule)):
                    if schedule[k] > x:
                        s = dist_down(schedule,stations,x)
                        details.append(stations[k - 1].upper())
                        details.append(10+statlist.index(stations[k-1])*37.5)                    
                        details.append(s)
                        flag = False
                        break
            # print(details)
            transit.append(details)            
        

    for i in range(0, len(rows)):
        schedule = []
        details = []
        stations = []
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])

        if schedule[0] < x < schedule[-1]:
            flag = True
            for k in range(3, len(rows[i])):
                if rows[i][k]:
                    details.append(rows[i][k])
                else:
                    details.append('----:----')

            new_schedule.append(details)
    ziplist=zip(transit,new_schedule)
    return render(request,"dashboard/cgvir.html",{'timenow':x,'ziplist':ziplist})



def vircg_route(request,routecode):
    cg_up = "statics/csv/churchgate_up.csv"
    stat="statics/csv/distance_up.csv"

    # initializing the titles and rows list
    transit=[]
    new_schedule=[]
    fields = []
    rows = []
    statfields=[]
    statlist=[]
    with open(stat, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    #print(os.getcwd())
    # reading csv file
    with open(cg_up, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    x = datetime.now()
    #x=time(10,3,0)
    x = x.strftime("%H") + ":" + x.strftime("%M")

    # converting x into a time variable again
    x = x.split(":")
    x = timedelta(hours=int(x[0]), minutes=int(x[1]))

    # checking running trains
    new_schedule=[]
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
            details.append(rows[i][0])
            flag = True

            # for trains in stations
            for k in range(0, len(schedule)):
                if schedule[k] == x:
                    s = dist_up(schedule,stations,x)
                    details.append(stations[k].upper())
                    details.append(10+statlist.index(stations[k])*37.5)
                    details.append(s)
                    flag = False
                    break

            # for trains not in stations
            if flag:
                for k in range(0, len(schedule)):
                    if schedule[k] > x:
                        s = dist_up(schedule,stations,x)
                        details.append(stations[k - 1].upper())
                        details.append(10+statlist.index(stations[k-1])*37.5)                    
                        details.append(s)
                        flag = False
                        break
            # print(details)
            transit.append(details)            
        

    for i in range(0, len(rows)):
        schedule = []
        details = []
        stations = []
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])
            

        if schedule[0] < x < schedule[-1]:
            flag = True
            for k in range(3, len(rows[i])):
                if rows[i][k]:
                    details.append(rows[i][k])
                    
                else:
                    details.append('----:----')
                    

            new_schedule.append(details)
    ind=0
    for each in transit:
        if (each[0]==routecode):
            break
        ind=ind+1
    res=""
    return render(request, "dashboard/route_vircg.html",{"each":transit[ind],"tr":new_schedule[ind],'timenow':x,"statlist":statlist,"res":res})

def cgvir_route(request,routecode):
    cg_up = "statics/csv/virar_down.csv"
    stat="statics/csv/distance_down.csv"

    # initializing the titles and rows list
    transit=[]
    new_schedule=[]
    fields = []
    rows = []
    statfields=[]
    statlist=[]
    with open(stat, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    #print(os.getcwd())
    # reading csv file
    with open(cg_up, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    x = datetime.now()
    #x=time(10,3,0)
    x = x.strftime("%H") + ":" + x.strftime("%M")

    # converting x into a time variable again
    x = x.split(":")
    x = timedelta(hours=int(x[0]), minutes=int(x[1]))

    # checking running trains
    new_schedule=[]
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
            details.append(rows[i][0])
            flag = True

            # for trains in stations
            for k in range(0, len(schedule)):
                if schedule[k] == x:
                    s = dist_up(schedule,stations,x)
                    details.append(stations[k].upper())
                    details.append(10+statlist.index(stations[k])*37.5)
                    details.append(s)
                    flag = False
                    break

            # for trains not in stations
            if flag:
                for k in range(0, len(schedule)):
                    if schedule[k] > x:
                        s = dist_up(schedule,stations,x)
                        details.append(stations[k - 1].upper())
                        details.append(10+statlist.index(stations[k-1])*37.5)                    
                        details.append(s)
                        flag = False
                        break
            # print(details)
            transit.append(details)            
        

    for i in range(0, len(rows)):
        schedule = []
        details = []
        stations = []
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])
            

        if schedule[0] < x < schedule[-1]:
            flag = True
            for k in range(3, len(rows[i])):
                if rows[i][k]:
                    details.append(rows[i][k])
                    
                else:
                    details.append('----:----')
                    

            new_schedule.append(details)
    ind=0
    for each in transit:
        if (each[0]==routecode):
            break
        ind=ind+1
    res=""
    return render(request, "dashboard/route_cgvir.html",{"each":transit[ind],"tr":new_schedule[ind],'timenow':x,"statlist":statlist,"res":res})


def vircg_delay(request,routecode):
    cg_up = "statics/csv/churchgate_up.csv"
    stat="statics/csv/distance_up.csv"

    # initializing the titles and rows list
    transit=[]
    new_schedule=[]
    fields = []
    rows = []
    statfields=[]
    statlist=[]
    with open(stat, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    #print(os.getcwd())
    # reading csv file
    with open(cg_up, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    x = datetime.now()
    #x=time(10,3,0)
    x = x.strftime("%H") + ":" + x.strftime("%M")

    # converting x into a time variable again
    x = x.split(":")
    x = timedelta(hours=int(x[0]), minutes=int(x[1]))

    # checking running trains
    new_schedule=[]
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
            details.append(rows[i][0])
            flag = True

            # for trains in stations
            for k in range(0, len(schedule)):
                if schedule[k] == x:
                    s = dist_down(schedule,stations,x)
                    details.append(stations[k].upper())
                    details.append(10+statlist.index(stations[k])*37.5)
                    details.append(s)
                    flag = False
                    break

            # for trains not in stations
            if flag:
                for k in range(0, len(schedule)):
                    if schedule[k] > x:
                        s = dist_down(schedule,stations,x)
                        details.append(stations[k - 1].upper())
                        details.append(10+statlist.index(stations[k-1])*37.5)                    
                        details.append(s)
                        flag = False
                        break
            # print(details)
            transit.append(details)            
        

    for i in range(0, len(rows)):
        schedule = []
        details = []
        stations = []
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])
            

        if schedule[0] < x < schedule[-1]:
            flag = True
            for k in range(3, len(rows[i])):
                if rows[i][k]:
                    details.append(rows[i][k])
                    
                else:
                    details.append('----:----')
                    

            new_schedule.append(details)
    ind=0
    for each in transit:
        if (each[0]==routecode):
            break
        ind=ind+1
    res=mitigation_up(request,routecode)
    return render(request, "dashboard/route_vircg.html",{"each":transit[ind],"tr":new_schedule[ind],'timenow':x,"statlist":statlist,"res":res})

def cgvir_delay(request,routecode):
    cg_up = "statics/csv/virar_down.csv"
    stat="statics/csv/distance_down.csv"

    # initializing the titles and rows list
    transit=[]
    new_schedule=[]
    fields = []
    rows = []
    statfields=[]
    statlist=[]
    with open(stat, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    #print(os.getcwd())
    # reading csv file
    with open(cg_up, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    x = datetime.now()
    #x=time(10,3,0)
    x = x.strftime("%H") + ":" + x.strftime("%M")

    # converting x into a time variable again
    x = x.split(":")
    x = timedelta(hours=int(x[0]), minutes=int(x[1]))

    # checking running trains
    new_schedule=[]
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
            details.append(rows[i][0])
            flag = True

            # for trains in stations
            for k in range(0, len(schedule)):
                if schedule[k] == x:
                    s = dist_down(schedule,stations,x)
                    details.append(stations[k].upper())
                    details.append(10+statlist.index(stations[k])*37.5)
                    details.append(s)
                    flag = False
                    break

            # for trains not in stations
            if flag:
                for k in range(0, len(schedule)):
                    if schedule[k] > x:
                        s = dist_down(schedule,stations,x)
                        details.append(stations[k - 1].upper())
                        details.append(10+statlist.index(stations[k-1])*37.5)                    
                        details.append(s)
                        flag = False
                        break
            # print(details)
            transit.append(details)            
        

    for i in range(0, len(rows)):
        schedule = []
        details = []
        stations = []
        for j in range(3, len(rows[i])):
            if rows[i][j]:
                t = rows[i][j]
                t = t.split(":")
                t = timedelta(hours=int(t[0]), minutes=int(t[1]))
                schedule.append(t)
                stations.append(fields[j])
            

        if schedule[0] < x < schedule[-1]:
            flag = True
            for k in range(3, len(rows[i])):
                if rows[i][k]:
                    details.append(rows[i][k])
                    
                else:
                    details.append('----:----')
                    

            new_schedule.append(details)
    ind=0
    for each in transit:
        if (each[0]==routecode):
            break
        ind=ind+1
    res=mitigation_up(request,routecode)
    return render(request, "dashboard/route_cgvir.html",{"each":transit[ind],"tr":new_schedule[ind],'timenow':x,"statlist":statlist,"res":res})



def mitigation_up(request,route):
    # csv file name
    filename = "statics/csv/churchgate_up.csv"

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
            transit.append(rows[i][0])


    # current status data
    print(transit)

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

    print(stations)
    # distance data


    # csv file name
    filename_d = "statics/csv/distance_up.csv"

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
    # for k in range(0, len(schedule)):
    #     if schedule[k] == x:
    #         # s = True
    #         a = stations[k]
    #         b = stations[k+1]
    #         print("Currently Running from {} to {} ".format(a, b))
    #         a_t = schedule[k]
    #         b_t = schedule[k+1]
    #         i_dist = 0
    #         print(i_dist)
    #         flag = False
    #         break

    # for trains not in stations
    i_dist=0
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
                t_dist = d_b - d_a
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
                i_dist = (t_dist / float(time[1])) * float(time_c[1])
                print(i_dist)
                flag = False
                break

    loc = request.POST['Station']
    for i in range(0, len(rows_d)):
        if loc == rows_d[i][0]:
            d_loc = float(rows_d[i][1])
            break

    c_dist = float(request.POST['Distance'])

    covered_distance = c_dist + d_loc
    ideal_distance = i_dist + d_a

    if ideal_distance==covered_distance:
        res=("Train {} is on time".format(route))

    else:
        delay = round(ideal_distance - covered_distance, 2)
        res=("Train {} is {} kms behind scheduled position".format(route, delay))
        # perform mitigation
        time_r = b_t - x
        time_r = str(time_r)
        time_r = time_r.split(":")

        r_dist = d_b - covered_distance

        m_speed = (r_dist * 60) / float(time_r[1])

        str1 = "There is a major delay in the route."
        str2 = "The delay cannot be mitigated."
        str3 = "The train must maintain an average speed of"
        str4 = " kmph to minimize the delay."

        if m_speed > 90:
            m_speed = 90
            res=("There is a major delay in the route.\n"
                "The delay cannot be mitigated completely.\n"
                "The train must maintain an average speed above " +str(m_speed)+ " to minimize the delay.")
            report = "There is a major delay in the route. The delay cannot be mitigated completely. The train must maintain an average speed above " +str(m_speed)+ " kmph to minimize the delay."
            with open('delay.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date.today(), x, 'Churchgate_Up', route, delay, loc, "No", report])


        else:
            res=("There is a minor delay in the route.\n"
                "For the delay to be mitigated the train must maintain an average speed of {} kmph for the remaining distance.".format(round(m_speed, 2)))
            report = "There is a minor delay in the route. For the delay to be mitigated the train must maintain an average speed of" +str(round(m_speed, 2))+ "kmph"
            with open('delay.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date.today(), x, 'Churchgate_Up', route, delay, loc, "Yes", report])
    return(res)

def mitigation_down(request,route):
    # csv file name
    filename = "statics/csv/virar_down.csv"

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
            transit.append(rows[i][0])


    # current status data
    print(transit)

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

    print(stations)
    # distance data


    # csv file name
    filename_d = "statics/csv/distance_down.csv"

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
    # for k in range(0, len(schedule)):
    #     if schedule[k] == x:
    #         # s = True
    #         a = stations[k]
    #         b = stations[k+1]
    #         print("Currently Running from {} to {} ".format(a, b))
    #         a_t = schedule[k]
    #         b_t = schedule[k+1]
    #         i_dist = 0
    #         print(i_dist)
    #         flag = False
    #         break

    # for trains not in stations
    i_dist=0
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
                t_dist = d_b - d_a
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
                i_dist = (t_dist / float(time[1])) * float(time_c[1])
                print(i_dist)
                flag = False
                break

    loc = request.POST['Station']
    for i in range(0, len(rows_d)):
        if loc == rows_d[i][0]:
            d_loc = float(rows_d[i][1])
            break

    c_dist = float(request.POST['Distance'])

    covered_distance = c_dist + d_loc
    ideal_distance = i_dist + d_a

    if ideal_distance==covered_distance:
        res=("Train {} is on time".format(route))

    else:
        delay = round(ideal_distance - covered_distance, 2)
        res=("Train {} is {} kms behind scheduled position".format(route, delay))
        # perform mitigation
        time_r = b_t - x
        time_r = str(time_r)
        time_r = time_r.split(":")

        r_dist = d_b - covered_distance

        m_speed = (r_dist * 60) / float(time_r[1])

        str1 = "There is a major delay in the route."
        str2 = "The delay cannot be mitigated."
        str3 = "The train must maintain an average speed of"
        str4 = " kmph to minimize the delay."

        if m_speed > 90:
            m_speed = 90
            res=("There is a major delay in the route.\n"
                "The delay cannot be mitigated completely.\n"
                "The train must maintain an average speed above " +str(m_speed)+ " to minimize the delay.")
            report = "There is a major delay in the route. The delay cannot be mitigated completely. The train must maintain an average speed above " +str(m_speed)+ " kmph to minimize the delay."
            with open('delay.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date.today(), x, 'Churchgate_Up', route, delay, loc, "No", report])


        else:
            res=("There is a minor delay in the route.\n"
                "For the delay to be mitigated the train must maintain an average speed of {} kmph for the remaining distance.".format(round(m_speed, 2)))
            report = "There is a minor delay in the route. For the delay to be mitigated the train must maintain an average speed of" +str(round(m_speed, 2))+ "kmph"
            with open('delay.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date.today(), x, 'Virar_Down', route, delay, loc, "Yes", report])
    return(res)


def delay_log(request):
    # csv file name
    filename = "statics/csv/delay.csv"

    # initializing the titles and rows list
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    
    return render(request,'dashboard/delay_log.html',{'rows':rows})

