import sys

grid = {}
intersections = []
intersectiondDists = []

wires = sys.stdin.readlines()

for w in range(len(wires)):
   wire = wires[w].split(',')
   curX = 0
   curY = 0
   idx = 0
   for point in wire:
      steps = int(point[1:])
      idx += 1
      if point[0] == 'R':
         for i in range(curX + 1, curX + steps):
            if w == 0:
               if not (i, curY) in grid:
                  grid[(i, curY)] = idx
            elif (i, curY) in grid:
               intersections.append((i, curY))
               intersectiondDists.append(idx + grid[(i, curY)])
            idx += 1
         curX += steps
      elif point[0] == 'L':
         for i in range(curX - 1, curX - steps, -1):
            if w == 0:
               if not (i, curY) in grid:
                  grid[(i, curY)] = idx
            elif (i, curY) in grid:
               intersections.append((i, curY))
               intersectiondDists.append(idx + grid[(i, curY)])
            idx += 1
         curX -= steps
      elif point[0] == 'U':
         for i in range(curY + 1, curY + steps,):
            if w == 0:
               if not (curX, i) in grid:
                  grid[(curX, i)] = idx
            elif (curX, i) in grid:
               intersections.append((curX, i))
               intersectiondDists.append(idx + grid[(curX, i)])
            idx += 1
         curY += steps
      else:
         for i in range(curY - 1, curY - steps, -1):
            if w == 0:
               if not (curX, i) in grid:
                  grid[(curX, i)] = idx
            elif (curX, i) in grid:
               intersections.append((curX, i))
               intersectiondDists.append(idx + grid[(curX, i)])
            idx += 1
         curY -= steps

print(intersections)
mindist = 999999

for intersection in intersections:
   dist = abs(intersection[0]) + abs(intersection[1])
   mindist = min(mindist, dist)

print(mindist)
print(min(intersectiondDists))