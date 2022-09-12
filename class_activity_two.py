# Write a function called `isAFactor` that when given two integer parameters , `num1` and `num2`, returns `True` if `num1` is a factor of `num2` and `False` otherwise.

# Try writing the function from scratch. Use the naming conventions as specified in the problem description above!

#ADD CODE HERE!

def isAFactor(num1, num2):
  if num2%num1 == 0:
    return True
  else:
    return False




# These lines of code are used to test our function.
# Test Case #1: should return True
print(isAFactor(10,70))

# Test Case #2: should return False
print(isAFactor(3,70))

#Test Case #3: should return True
print(isAFactor(1,7))

#Add your own testcase below!