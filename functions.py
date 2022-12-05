import math

# Calculate the arc length given the angle (in degrees) it subtends at the sphere's center and the radius of the sphere
def arc_length(radius, arc_angle):

    arc_angle = (arc_angle * math.pi) / 180 # convert to radians

    arc_length = radius * arc_angle

    return arc_length

# Calculate the arc angle (in degrees) given the arc length and the radius of the sphere
def arc_angle(radius, arc_length):

    arc_angle_rad = arc_length / radius

    arc_angle = (arc_angle_rad * 180) / math.pi # convert to radians

    return arc_angle

# Calculate the great circle arc angle (in degrees) between two points on the surface of the sphere
def great_circle_arc_angle(lat1, long1, lat2, long2):

    delta_long = ((long2 - long1) * math.pi) / 180 # difference in longitudes and then convert to radians
    lat1 = (lat1 * math.pi) / 180 # convert to radians
    lat2 = (lat2 * math.pi) / 180 # convert to radians

    cos_dsigma = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2_rad) * math.cos(delta_long)
    dsigma = math.acos(cos_dsigma)
    
    dsigma = (dsigma * 180) / math.pi # convert to degrees
    
    return dsigma

# Calculate the azimuth angle (in degrees) around from North going clockwise from point 1 to point 2
def azimuth(lat1, long1, lat2, long2):

    delta_long = ((long2 - long1) * math.pi) / 180 # difference in longitudes and then convert to radians
    lat1 = (lat1 * math.pi) / 180 # convert to radians
    lat2 = (lat2 * math.pi) / 180 # convert to radians
    
    top = math.sin(delta_long)
    bottom = math.cos(lat1) * math.tan(lat2) - math.sin(lat1) * math.cos(delta_long)
    azimuth = math.atan2(top, bottom)
    
    azimuth = (azimuth_rad * 180) / math.pi # convert to degrees
    
    return azimuth
