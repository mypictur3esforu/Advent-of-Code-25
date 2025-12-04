class day4_2:
   def solve(input:str, map_2d, ans):
      if map_2d == None:
         lines = input.split("\n")
         map_2d= [list(line) for line in lines]
         map_2d.pop()
         # print(map_2d)
            
# Example 2D map
      # map_2d = [
      #    ['a', 'b', 'c'],
      #    ['d', 'e', 'f'],
      #    ['g', 'h', 'i']
      # ]

      # Directions for adjacent cells (vertical, horizontal, diagonal)
      directions = [
         (-1, 0),  # Up
         (1, 0),   # Down
         (0, -1),  # Left
         (0, 1),   # Right
         (-1, -1), # Top-left
         (-1, 1),  # Top-right
         (1, -1),  # Bottom-left
         (1, 1)    # Bottom-right
      ]

      tempAns = 0
      # Iterate through the map
      for row in range(len(map_2d)):
         for col in range(len(map_2d[row])):
            count = 0
            current = map_2d[row][col]
            if current != "@": continue
            # print(f"Current character: {current}")

            # Check all adjacent cells
            for dr, dc in directions:
                  adj_row, adj_col = row + dr, col + dc

                  # Ensure the adjacent cell is within bounds
                  if 0 <= adj_row < len(map_2d) and 0 <= adj_col < len(map_2d[0]):
                     # print(adj_row, len(map_2d), adj_row < len(map_2d))
                     adjacent = map_2d[adj_row][adj_col]
                     # print(f"  Adjacent character: {adjacent}")
                     if adjacent == "@": count+=1
            if count < 4:
               tempAns+=1
               map_2d[row][col] = "x"
      # print(map_2d)
      # for tmep in map_2d:
         # print(' '.join(map(str, tmep)))
      
      # print(tempAns)
      if tempAns != 0: return day4_2.solve("", map_2d, ans+tempAns)
      else: return ans
