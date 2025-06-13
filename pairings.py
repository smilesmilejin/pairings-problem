def find_pairs(num_string):
  # Write your solution here!
  # pass
  # duplicate? no duplicate
  # match with itselt?

  # split each num in the numstring into a list
  # convert the list into list of integers

  # create a empty set
  # find all possible pairs in num_string
  # add (min, max) to empty set

  # return result

  num_string_split = num_string.split()

  nums = [int(num)for num in num_string_split]
  # print(nums)

  result = set()

  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      num1 = nums[i]
      num2 = nums[j]

      if num1 < num2:
        pair = (num1, num2)
      elif num1 > num2:
        pair = (num2, num1)

      result.add(pair)

  # print(result)
  return result
      




# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")