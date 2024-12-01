from time import time


####### TEST INPUTS HERE
small = [0, 1, 0]
medium = [4, 2, 1, 3, 0, 1, 2]
edge_case = [0, 2, 0]

####### NAIVE SOLUTION HERE
def rain_water(histogram):
  total_water = 0
  for i in range(1, len(histogram)-1):
    left_values = histogram[:i]
    left_max = max(left_values)
    #print("Left max is: {0}".format(left_max))
    right_values = histogram[i:]
    right_max = max(right_values)
    #print("Right max is: {0}".format(right_max))
    curr = fill_mark = min(left_max, right_max)-histogram[i]
    if curr > 0:
      fill_mark = curr
      total_water += fill_mark
  return total_water

####### OPTIMIZED SOLUTION HERE
def optimized_rain_water(histogram):
  length = len(histogram)
  left_maxes = [0] * length
  right_maxes = [0] * length
  total = 0

  # Calculate maxes
  left_max = histogram[0]
  right_max = histogram[-1]
  for i in range(length):
    left_max = max(left_max, histogram[i])
    left_maxes[i] = left_max
    #right_max = max(right_max, histogram[length-1-i])
    #right_maxes[length-1-i] = right_max
  for i in range(length-1, -1, -1):
    right_max = max(right_max, histogram[i])
    total += min(left_maxes[i], right_max) - histogram[i]
  return total

####### BENCHMARKING HERE

#NAIVE
start = time()
print(rain_water(small))
print(time()-start)

start = time()
print(rain_water(medium))
print(time()-start)

start = time()
print(rain_water(edge_case))
print(time()-start)

#OPTIMIZED
start = time()
print(optimized_rain_water(small))
print(time()-start)

start = time()
print(optimized_rain_water(medium))
print(time()-start)

start = time()
print(optimized_rain_water(edge_case))
print(time()-start)
