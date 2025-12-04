class day3_2:
   def solve(input:str):
      banks = input.split("\n")
      ans = 0
      for bank in banks:
         battery = list(bank)
         max = [0]*12
         for i in range(len(battery)):
            num = int(battery[i])
            for z in range(12):
               if max[z] >= num or i > len(battery)-12+z: continue
               max[z] = num
               max[z+1:] = [0] * (len(max)- z-1)
               break
         maxNumb = "".join(map(str, max))
         print(maxNumb)
         ans+= int(maxNumb)
      return ans
