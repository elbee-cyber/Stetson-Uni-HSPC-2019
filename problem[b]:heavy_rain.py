# Measure the amount of captured rain
out = 0
fl = int(input())
sl = str(input()) 
heights = list(map(int, sl.split()))
heights.sort()
heights.pop(-1)
wallHeight = heights[-1]
heights.pop(-1)
for i in range(0,len(heights)):
  out += wallHeight - heights[i]
print(out)
