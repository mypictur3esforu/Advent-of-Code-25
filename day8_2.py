import bisect
class day8_2:
   def solve(input:str):
      lines = input.split("\n")
      lines = [line.split(",") for line in lines]
      try: lines.remove([""])
      except: print("War nix da")
      cords = [[int(num) for num in line]for line in lines]

      distances = []

      for i in range(len(cords)):
         # z = i+1
         for z in range(len(cords)):
            if z <= i: continue
            distance = 0
            for dimension in range(len(cords[z])):
               distance += (cords[i][dimension]-cords[z][dimension])**2
            distances.append([distance, (i, z)])
      distances.sort()

      cuircits =[]
      count = [num for num in range(len(lines))]
      # for i in range(1000): 
      for i in range(len(distances)):
         if distances[i][1] == (10,12) or i == 27:
            print("Hier")
         cuircs = []
         first, second = distances[i][1]
         for c in range(len(cuircits)):
            for k in range(len(cuircits[c])):
               if cuircits[c][k] == first or cuircits[c][k] == second: cuircs.append(c); break
         amount = len(cuircs)
         if amount == 0: cuircits.append([first, second])
         elif amount == 1:
            day8_2.insert_sorted_unique(cuircits[cuircs[0]], first)
            day8_2.insert_sorted_unique(cuircits[cuircs[0]], second)
         else:
            for c in range(1, len(cuircs)):
               for num in cuircits[cuircs[c]]:
                  day8_2.insert_sorted_unique(cuircits[cuircs[0]], num)
               cuircits.pop(cuircs[c])
         if len(cuircits) == 1:
               if day8_2.contains_range(cuircits[0], 0, len(lines)): 
                  return cords[first][0] * cords[second][0]

      # ans = 1
      # print(cuircits)
      # cuircitSize = []
      # for c in range(len(cuircits)):
      #    cuircitSize.append(len(cuircits[c]))
      # cuircitSize.sort(reverse=True)
      # ans*= cuircitSize[0]

      # return ans


   def insert_sorted_unique(arr, value):
    pos = bisect.bisect_left(arr, value)
    if pos == len(arr) or arr[pos] != value:
        arr.insert(pos, value)

   def contains_range(arr, x, y):
    if len(arr) != y-x: return False
    s = set(arr)
    for n in range(x, y):
        if n not in s:
            return False
    return True

