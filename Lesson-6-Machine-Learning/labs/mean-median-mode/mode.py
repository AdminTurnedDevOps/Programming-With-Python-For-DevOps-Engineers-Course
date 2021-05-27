import numpy

# Speeds
# 1. School zones: 25
# 2. Residential: 35
# 3. major roads: 45 or 50
# 4. highways: 65
# 5. Smaller highways: 55

lst = [25, 35, 45, 50, 65, 55]

speed = numpy.mean(lst)

print(speed)