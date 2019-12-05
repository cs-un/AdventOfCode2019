def validnumber(num):
   s = str(num)
   prevc = s[0]
   adj = {}
   increasing = True
   for c in s[1:]:
      if c == prevc:
         if c in adj:
            adj[c] = False
         else:
            adj[c] = True
      if c < prevc:
         increasing = False
         break
      prevc = c
   return True in adj.values() and increasing


low, high = 240920, 789857

tot = 0

for num in range(low, high):
   if validnumber(num):
      tot+=1
print(tot)
