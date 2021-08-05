out = 0
fl = int(input("Number of blocks: "))
sl = str(input("Height values seperated by space: ")) 
heights = list(map(int, sl.split()))
heights.sort()
heights.pop(-1)
wallHeight = heights[-1]
heights.pop(-1)
for i in range(0,len(heights)):
  out += wallHeight - heights[i]
print(out)
