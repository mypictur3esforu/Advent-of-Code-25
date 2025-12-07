from functools import lru_cache
class day7_2:
   lines = "" 

   @staticmethod
   def solve(input:str):
      day7_2.lines = input.split("\n")
      day7_2.lines.pop()
      lines = day7_2.lines

      for y in range(len(lines[0])):
         if lines[0][y] == "S": 
            return day7_2.memoization((0, y))
   
   @lru_cache(maxsize=1000)
   @staticmethod
   def memoization(cord):
      x, y = cord
      # print(cord)
      if(cord == (14,0)):
         print("Maaan")
      lines = day7_2.lines

      if lines[x][y] == "^": return 0
      elif x == len(lines)-1: return 1

      ans = 0
      for z in range(x, len(lines)):
         if lines[z][y] != "^": continue

         if y > 0: ans += day7_2.memoization((z, y-1))
         if y < len(lines[z])-1: ans += day7_2.memoization((z, y+1))
         return ans
      return 1
