import functions
import math
import shapefile as shp
import matplotlib.pyplot as plt

def transform_point(obs_lat, obs_long, lat, long):

    gc_arc_angle = functions.great_circle_arc_angle(obs_lat, obs_long, lat, long)
    azimuth = functions.azimuth(obs_lat, obs_long, lat, long)
    
    x = gc_arc_angle / 90 * math.cos(math.radians(azimuth))
    y = gc_arc_angle / 90 * math.sin(math.radians(azimuth))

    return x, y

sf = shp.Reader("world-administrative-boundaries.dbf")
fig, ax = plt.subplots(1)

for shape in sf.shapeRecords():

    transformed_point_xs = []
    transformed_point_ys = []

    for point in shape.shape.points[:]:

        x = point[0]
        y = point[1]

        ty, tx = transform_point(50, 0, y, x)
        
        if tx < -1 or tx > 1 or ty < -1 or ty > 1:
            break
            
        transformed_point_xs = transformed_point_xs + [tx]
        transformed_point_ys = transformed_point_ys + [ty]
        
    ax.plot(transformed_point_xs, transformed_point_ys, color="black", linewidth=0.5)

lines = functions.generate_lines(15, 15, 32)
for line in lines:

    transformed_point_xs = []
    transformed_point_ys = []

    for point in line:

        x = point[0]
        y = point[1]

        ty, tx = transform_point(50, 0, y, x)
        
        if tx < -1 or tx > 1 or ty < -1 or ty > 1:
            break
            
        transformed_point_xs = transformed_point_xs + [tx]
        transformed_point_ys = transformed_point_ys + [ty]
        
    ax.plot(transformed_point_xs, transformed_point_ys, color="red", linewidth=0.5)

plt.show()
