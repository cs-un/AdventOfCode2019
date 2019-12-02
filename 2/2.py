import sys

codes = list(map(int, ''.join(sys.stdin.readlines()).split(",")))

codes[1] = 12
codes[2] = 2

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

print(codes)