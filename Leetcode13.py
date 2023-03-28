# Roman numerals are usually written largest to smallest from left to right.
def romanToInt(str) -> int:
  #just have a hashmap that takes up 7 values
  check_value = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
  }

  #traverse through the string
  #check if the current character's integer value is greater or smaller than the next character's integer value
  #if current's integer is greater, then add them up
  #if smaller, subtract the integer value of the current charater from the next character and add them up


  #Time complexity -> o(n)
  #space complexity -> o(1)
  total = 0
  length = len(str)
  i=0
  while i < length:
    if str[i] not in check_value:
      return -1
    elif i == length-1:
      total += check_value[str[i]]
      break
    elif i != length-1:
      if check_value[str[i]] >= check_value[str[i+1]]:
        total += check_value[str[i]]
        i+=1
      elif check_value[str[i]] < check_value[str[i+1]]:
        total += check_value[str[i+1]] - check_value[str[i]]
        i = i+2
    
  
  return total



#cleaner version

def romanToInt1(str):
  check_value = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
  }
  total = 0
  for i in range(len(str)):
    if i+1 < len(str) and check_value[str[i]] < check_value[str[i+1]]:
      total -= check_value[str[i]]
    else:
      total += check_value[str[i]]
  
  return total




print(romanToInt1("MCMXCIV")) #1994
print(romanToInt1("LVIII")) #58
print(romanToInt1("III")) # 3

