class day4:
   def solve(input:str):
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

      ans = 0
      # Iterate through the map
      for row in range(len(map_2d)):
         for col in range(len(map_2d[row])):
            count = 0
            current = map_2d[row][col]
            if current == ".": continue
            # print(f"Current character: {current}")

            # Check all adjacent cells
            for dr, dc in directions:
                  adj_row, adj_col = row + dr, col + dc

                  # Ensure the adjacent cell is within bounds
                  if 0 <= adj_row < len(map_2d) and 0 <= adj_col < len(map_2d[0]):
                     # print(adj_row, len(map_2d), adj_row < len(map_2d))
                     adjacent = map_2d[adj_row][adj_col]
                     # print(f"  Adjacent character: {adjacent}")
                     if adjacent == "@" or adjacent=="x": count+=1
            if count < 4:
               ans+=1
               map_2d[row][col] = "x"
      # print(map_2d)
      for tmep in map_2d:
         print(' '.join(map(str, tmep)))
      return ans
