class day6_2:

   def solve(input: str):
      lines = input.split("\n")
      # lines = [re.split("\s", line) for line in lines]
      lines.pop()
      ops = lines.pop()
      lines = [line for line in lines]
      # print(lines)

      ans = 0
      add = True
      tans = 0
      for i in range(len(ops)):
         char = ops[i]
         if char == "+":
            add = True
            ans += tans
            tans = 0
         elif char == "*":
            add = False
            ans += tans
            tans = 1
         if i+1 < len(ops) and ops[i+1] != " ": continue

         num = ""
         for line in lines:
            num += line[i]
         num = int(num)
         if add: tans += num
         else: tans *= num
      ans += tans
      
      return ans