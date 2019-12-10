import sys

edges = list(map(lambda x: x.strip().split(')'), sys.stdin.readlines()))

vertices = {}

root = set(map(lambda x: x[0], edges))

for edge in edges:
   if edge[0] in vertices:
      vertices[edge[0]].append(edge[1])
   else:
      vertices[edge[0]] = [edge[1]]
   if edge[1] in root:
      root.remove(edge[1])

sums = {}
next = vertices[root.pop()]
depth = 0
while next:
   depth += 1
   for _ in range(len(next)):
      node = next.pop()
      if node in vertices:
         next = vertices[node] + next
      sums[node] = depth

print(sum(sums.values()))