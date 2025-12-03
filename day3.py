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
            if max1 != 9 and num > max1 and i < len(battery)-1: 
               max1 = num
               max2 = 0
            elif num > max2: max2 = num
         print(str(max1)+str(max2))
         ans+= int(str(max1)+str(max2))
      return ans
