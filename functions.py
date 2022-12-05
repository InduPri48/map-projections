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

    cos_dsigma = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(delta_long)
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
    
    azimuth = (azimuth * 180) / math.pi # convert to degrees
    
    return azimuth

# Calculate the adjacent arc angle of a spherical right triangle given the hypotenuse arc angle and the vertex angle (all angles in degrees)
def adjacent_arc_angle(hypotenuse_arc_angle, vertex_angle):

    vertex_angle = (vertex_angle * math.pi) / 180 # convert to radians
    hypotenuse_arc_angle = (hypotenuse_arc_angle * math.pi) / 180 # convert to radians

    partial = math.cos(vertex_angle) * math.tan(hypotenuse_arc_angle)
    adjacent_arc_angle = math.atan(partial)
    
    adjacent_arc_angle = (adjacent_arc_angle * 180) / math.pi # convert to degrees

    return adjacent_arc_angle

# Calculate the opposite arc angle of a spherical right triangle given the hypotenuse arc angle and the vertex angle (all angles in degrees)
def opposite_arc_angle(hypotenuse_arc_angle, vertex_angle):

    vertex_angle = (vertex_angle * math.pi) / 180 # convert to radians
    hypotenuse_arc_angle = (hypotenuse_arc_angle * math.pi) / 180 # convert to radians

    partial = math.sin(vertex_angle) * math.sin(hypotenuse_arc_angle)
    opposite_arc_angle_rad = math.asin(partial)
    
    opposite_arc_angle = (opposite_arc_angle * 180) / math.pi # convert to degrees

    return opposite_arc_angle

def generate_lines(lat_spacing, long_spacing, n_divs):

    lines = []

    # Generate the lines of longitude
    for i in range(360 // long_spacing):

        for j in range(n_divs):
    
            # per line
            p1 = [i * long_spacing, -90 + j * (180 / n_divs)]
            p2 = [i * long_spacing, -90 + (j + 1) * (180 / n_divs)]
            line = [p1, p2]
            
            lines = lines + [line]

    # Generate the lines of latitude
    for i in range(180 // lat_spacing):

        for j in range(n_divs):
    
            # per line
            p1 = [-180 + j * (360 / n_divs), -90 + i * lat_spacing]
            p2 = [-180 + (j + 1) * (360 / n_divs), -90 + i * lat_spacing]
            line = [p1, p2]
        
            lines = lines + [line]

    return lines
