#Time complexity -> o(n) ->  where n is the length of the longer input string
#Space complexity -> o(n) -> because we we are storing the result string.
def addBinary(a,b):
  i = len(a)-1
  j = len(b)-1
  carry = 0
  result = ""
  while i>=0 or j>=0 or carry:
    total = carry
    if i>=0:
      total += int(a[i])
      i -= 1
    
    if j >= 0:
      total += int(a[j])
      j -= 1
    
    result = str(total%2) + result
    carry = total // 2
  
  return result


print(addBinary("11", "1"))