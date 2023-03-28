# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
def isValid1(str):
  if len(str) % 2 != 0:
    return False
  
  #hashmap
  closed_complement_bracket = {
    ")" : "(",
    "]" : "[",
    "}" : "{"
  }
  
  #()
  #([{}])
  stack = []
  
  #iterate through the string and add it to the stack when open bracket is encountered
  #when closed bracket is encountered, check if the top of the stack has it opening bracket
  #if yes, then pop the opening bracket off the stack
  #if no, return false cause the bracket opening and closing are not right
  for s in str:
    if s in closed_complement_bracket:
      if stack and stack[-1] == closed_complement_bracket[s]:
        stack.pop()
      else:
        return False
    else:
      stack.append(s)
    
  print(stack)

  #if the stack is empty, it means all the brackets had both their opening and closing brackets in the right order
  if not stack:
    return True
  else:
    return False



print(isValid1("([{}])"))
