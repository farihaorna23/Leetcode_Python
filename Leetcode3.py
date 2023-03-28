#time complexity -> O(n)
#space complexity -> O(n)

# str: abcabcbb
# abc -> bca -> cab -> abc -> cb -> b
def lengthOfLongestSubstring(str):
  maximum = 0
  left = 0
  new_set = set()
  #for loop that traverse over the string, add any unique value to the object
  for indx in range(len(str)):
    #an set that contains all the substring with no duplicates
    #if a current value is in the set, than we remove items from the left side until the duplicate value is removed
    while str[indx] in new_set:
      new_set.remove(str[left]) #The time complexity of removing from a set is O(1)
      left += 1 #move the pointer
    # add the current charcater value to the set
    new_set.add(str[indx])
    #get the maximum value for each iteration 
    maximum = max(maximum,len(new_set))
  #return the substring
  return maximum



      

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
