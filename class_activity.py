# Write a function `happyNewYear` that takes in a single parameter, `year`. 
# If it is a new **millennium**, the function should print `“Happy New Millenium!”`. If it is a new **decade**, the function should print `“Happy New Decade!”`, otherwise it should print `“Happy New Year!”`. 

def happyNewYear(year):
  # Add code here
  if year % 1000 == 0:
    return print("Happy New Millenium!")
  elif year % 10 == 0:
    return print("Happy New Decade!")
  else:
    return print("Happy New Year!")


# These lines of code are used to test our function.
# Test Case #1: should print Happy New Millenium!


happyNewYear(2000)

# Test Case #2: should print Happy New Decade!
happyNewYear(2010)

#Test Case #3: should print Happy New Year!
happyNewYear (2001)

#Add your own testcase below!