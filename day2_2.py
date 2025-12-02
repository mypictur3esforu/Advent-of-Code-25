class day2_2:

   @staticmethod
   def getDividors(id:str):
      dividors = []
      chars = len(id)
      for num in range(1, chars):
         if chars % num == 0: dividors.append(num)
      return dividors
   
   
   @staticmethod
   def checkID(id:str, dividors):
      # if dividors == []: return False
      for dividor in dividors:
         parts = [id[i:i+dividor] for i in range(0, len(id), dividor)]
         # print(parts)
         for part in parts:
            if part != parts[0]:
               break
         else: return True
      return False


   @staticmethod
   def solve(input: str):
      # input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
      # input = "333-334"
      ids = []
      for borders in input.split(","):
         ids.append(borders.split("-"))
      # print(ids)

      ans = 0
      for id in ids:
         invalidID = False
         for num in range(int(id[0]), int(id[1])+1):
            numb = str(num)
            addible = day2_2.checkID(numb, day2_2.getDividors(numb))
            if addible:
               # print(num)
               ans += num
      # print(ans)
      return ans