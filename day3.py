class day3:
   def solve(input:str):
      banks = input.split("\n")
      ans = 0
      for bank in banks:
         battery = list(bank)
         max1= 0
         max2= 0
         for i in range(len(battery)):
            if max1 == 9 & max2 == 9: continue
            num = int(battery[i])
            if max1 != 9 & num > max1 & i < len(battery)-2: max1 = num
            elif num > max2: max2 = num

         ans+= int(str(max1)+str(max2))
      return ans
