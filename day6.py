import re
class day6:

   def solve(input: str):
      lines = input.split("\n")
      # lines = [re.split("\s", line) for line in lines]
      lines.pop()
      ops = lines.pop().split()
      try: lines = [[int(num) for num in line.split()] for line in lines]
      except: print("Input konnte nicht parsed werden")
      # print(lines)

      ans = 0
      for i in range(len(ops)):
         tans = 1
         for line in lines:
            if(ops[i] == "+"): ans += line[i]
            elif(ops[i] == "*"):
               tans *= line[i]
         if ops[i] == "*": ans += tans
      
      return ans