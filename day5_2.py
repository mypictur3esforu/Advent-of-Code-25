import re

class day5_2:
   def solve(input:str):
      parts = input.split("\n\n")
      rules = parts[0].split("\n")
      rules = [rule.split("-") for rule in rules]
      rules = [[int(num) for num in rule] for rule in rules]
      rules.sort()
      rules.append([0, 0])

      ans = 0

      lastMax= rules[0][1]
      min = rules[0][0]
      for rule in rules:
         if rule[0] <= lastMax:
            if rule[1] > lastMax: lastMax = rule[1]
            if rule != rules[len(rules)-1]: continue
         # wenn Reihe net weiter geht bisherige Zahlen addieren und nächste Reiher starten
         ans += lastMax - min + 1
         min = rule[0]
         lastMax = rule[1]

      return ans