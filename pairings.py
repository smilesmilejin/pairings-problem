def find_pairs(num_string):
  # Split string on the spaces
  nums = num_string.split() 
  # Convert each string into an integer
  nums = [int(num) for num in nums]

  new_nums = set()
  # Nested loop over the integers
  for num1 in nums:
    for num2 in nums:
        # Only add pairing if the first number is less than the second
        if num1 < num2:
          new_nums.add((num1, num2))

  return new_nums


# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")


"""
NOTES FOR INTERVIEWER

--------- Clarifying questions ---------------

Q: How should I handle invalid input?
A: You can assume the input will be valid, containing only integers separated by single spaces with no leading/trailing whitespace.

Q: Can a number be paired with itself?
A: No.

Q: Will there be duplicates in the input?
A: No.

Q: How should I handle an empty string?
A: You can assume there will be at least one integer in the string.

--------- Hints -------------------------------

- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. If they are unsure how to convert this to code, ask them what type of loop(s) best matches the logic described (most likely a nested for loop).

- If your candidate is struggling to split the string, remind them they can look up documentation online.

- If your candidate's code does not work because they forgot to convert the strings to integers, ask them to explain what the type of each variable is at each step.

- If your candidate incorreclty attempts to initalize their set as {}, you can encourage them to look up documentation on how to create an empty set.

"""