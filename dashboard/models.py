from django.db import models

# Create your models here.



class Line(models.Model):
    line_code=models.CharField(max_length=5)
    line_name=models.CharField(max_length=20)
    beg_station=models.CharField(max_length=20)
    end_station=models.CharField(max_length=20)
    def __str__(self):
        return (self.line_name)
    
class Station(models.Model):
    st_code=models.CharField(max_length=5)
    st_name=models.CharField(max_length=20)
    line_code=models.ManyToManyField(Line)
    def __str__(self):
        return (self.station_name)

class Route(models.Model):
    route_id=models.IntegerField()
    route_start=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='source_station')
    route_end=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='dest_station')
    start_time=models.TimeField()
    end_time=models.TimeField()
    stops=models.ManyToManyField(Station)
    route_line=models.ForeignKey(Line,on_delete=models.CASCADE)
    no_of_car=models.IntegerField()
    speed=models.CharField(max_length=5)
    category=models.CharField(max_length=5)
    days=models.CharField(max_length=5)
    def __str__(self):
        return (self.route_id+' : '+self.route_start+' to '+self.route_end)
