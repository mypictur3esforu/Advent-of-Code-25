class day7:
   def solve(input:str):
      lines = input.split("\n")
      beam = [False for char in lines[0]]
      ans = 0
      for line in lines:
         for i in range(len(line)):
            if line[i] == "S": beam[i] = True
            if not beam[i]: continue
            elif line[i] == "^": 
               beam[i] = False
               if i-1 >= 0: beam[i-1] = True
               if i+1 < len(line): beam[i+1] = True
               ans+=1
      return ans