class day7_2:
   def solve(input:str):
      lines = input.split("\n")
      beam = [not False for char in lines[0]]
      for line in lines:
         for i in range(len(line)):
            if line[i] == "S": beam[i] = True
      return day7_2.backtracking(lines[1:], beam, "")
   
   def backtracking(lines, beam, check):
      for b in beam:
         if b: check += "|"
         else: check += "."
      check+= "\n"
      if len(check.split("\n")) == 8: print(check)
      ans = 0
      # Suchen, ob es einen betrachbaren Strahl gibt und wo der ist (betrachtbar erst wenn er sich splitted, ansonsten geht er einfach weiter)
      for line in lines:
         i = -1
         for z in range(len(line)):
            if line[z] == "^" and beam[z] == True: i = z
         if i != -1: break
         lines=lines[1:]
      else: 
         return 1

      # wird nur bei Strahl der sich splitted ausgeführt
      beam[i] = False
      if i-1 >= 0:
         beam[i-1] = True
         ans += day7_2.backtracking(lines[1:], beam, check)
      if i+1 < len(line):
         beam[i] = False
         beam[i-1] = False
         beam[i+1] = True
         ans+= day7_2.backtracking(lines[1:], beam, check)

      return ans      
