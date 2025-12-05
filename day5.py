import re

class day5:
   def solve(input:str):
      parts = input.split("\n\n")
      rules = parts[0].split("\n")
      instances = parts[1].split("\n")
      try: instances.remove("")
      except: print()
      parsedIns = [int(instance) for instance in instances]
      parsedIns.sort()
      temp = 0
      # gibt keine Dopplungen hat der Code gezeigt:
      # for inst in parsedIns:
      #    if inst == temp: print("Dopplung: ", inst)
      #    temp = inst
      # print(parsedIns)
      print("Sorted")

      rules = [rule.split("-") for rule in rules]
      ans = 0

      # print("Test:", parsedIns[500])
      for rule in rules:
         low = int(rule[0])
         max = int(rule[1])
         minPos = 0
         maxPos = len(parsedIns)
         pos = int((minPos + maxPos)/2)
         
         # print("Ab hier while")
         # findet erste Zahl in der Regel
         while(parsedIns[pos] != low and minPos < maxPos):
            # print("Hier:", pos)
            if parsedIns[pos] < low: minPos = pos
            if parsedIns[pos] > low: maxPos = pos
            tpos = int((minPos + maxPos)/2)
            if tpos == pos: break
            else: pos = tpos

         # print("While vorbei ", max+1-low)
         if parsedIns != low: pos += 1
         nnum = parsedIns[pos]
         while nnum in range(low, max+1):
            parsedIns.pop(pos)
            ans += 1 
            if pos >= len(parsedIns): break
            nnum = parsedIns[pos]

         # alle folgenden Zahlen in einer Regel
         # for i in range(max+1-low):
         #    if parsedIns[pos] == low+i: parsedIns.pop(pos)
         #    elif parsedIns[pos + 1] == low + i: parsedIns.pop(pos+1)
         #    elif parsedIns[pos] > max or parsedIns[pos + 1] > max: break
         #    else: continue
         #    ans += 1
         # print("next numbers checked")
      # print(parsedIns)
      return ans