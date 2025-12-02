class day2:
   def solve(input: str):
      # input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
      # print(input.split(","))
      ids = []
      for borders in input.split(","):
         ids.append(borders.split("-"))
      # print(ids)

      ans = 0
      for id in ids:
         invalidID = False
         for num in range(int(id[0]), int(id[1])+1):
            # print(num)
            numb = str(num)
            chars = len(numb)
            if chars % 2 != 0:
               continue
               # special case alle Zahlen gleich
               # for char in numb:
                  # if()
            first = numb[:chars // 2]
            second = numb[chars // 2:]
            # second = second[::-1]
            for i in range(len(first)):
               if first[i] != second[i]:
                  break 
            else: 
               # if (invalidID):
               print(num)
               ans += num
      print(ans)
      return ans

      