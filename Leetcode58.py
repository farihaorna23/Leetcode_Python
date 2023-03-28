#brute force approach
#Time complexity -> o(n)
#space complexity -> o(n)
def lengthOfLastWord(str):
  new_sentence = str.strip() #o(n)
  new_arr = new_sentence.split(" ") #o(n)
  return len(new_arr[-1])



#optomized approach
#start iterating from the end since we only the length of the last word
def lengthOfLastWord1(str):
  length = 0
  i = len(str)-1

  #cut off white spaces from the end by moving the pointer
  while str[i] == " ":
    i -= 1
  
  #the loop will end after it encounters its first
  while i >= 0:
    if str[i] == " ":
      break
    length += 1
    i -=1
  
  return length

print(lengthOfLastWord1("   fly me   to   the moon  "))
print(lengthOfLastWord1("Hello World"))
print(lengthOfLastWord1("luffy is still joyboy"))



