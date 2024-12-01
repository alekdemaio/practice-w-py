def longest_common_subsequence(string_1, string_2):
  print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))

  grid = [[0 for col in range(len(string_1) + 1)] for row in range(len(string_2) + 1)]

  # Fill the DP table
  for row in range(1, len(string_2) + 1):
    print("Comparing: {0}".format(string_2[row - 1]))
    for col in range(1, len(string_1) + 1):
      print("Against: {0}".format(string_1[col - 1]))
      if string_1[col - 1] == string_2[row - 1]:  # Correct comparison of characters
        grid[row][col] = grid[row - 1][col - 1] + 1
      else:
        grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])

  #for row_line in grid:
    #print(row_line)
  #return grid[-1][-1]
  ans = []
  while row>0 and col>0:
    if string_1[col - 1] == string_2[row - 1]:
      ans += string_1[col - 1]
      col-=1
      row-=1
    elif grid[row][col - 1] > grid[row - 1][col]:
      col-=1
    else:
      row-=1
  return ans[::-1]

# Test the function
dna_1 = "ACCGTT"
dna_2 = "CCAGCA"
print(longest_common_subsequence(dna_1, dna_2))  # Expected Output: 3
