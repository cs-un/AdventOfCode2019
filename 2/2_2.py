import sys

def solve(incodes):
   for x in range(0, 100):
      for y in range(0, 100):
         codes = incodes[:]
         codes[1] = x
         codes[2] = y
         for i in range(0, len(codes) - 1, 4):
            inp1 = codes[i+1]
            inp2 = codes[i+2]
            outpos = codes[i+3]
            if codes[i] == 1:
               codes[outpos] = codes[inp1] + codes[inp2]
            elif codes[i] == 2:
               codes[outpos] = codes[inp1] * codes[inp2]
            elif codes[i] == 99:
               break
         if codes[0] == 19690720:
            return x, y


incodes = list(map(int, ''.join(sys.stdin.readlines()).split(",")))

x, y = solve(incodes)

print(100 * x + y)