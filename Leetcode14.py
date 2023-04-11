# The time complexity of this code is O(m*n), where m is the length of the shortest string in the input array and n is the number of strings in the input array. This is because in the worst case, we need to compare every character of every string in the input array to find the longest common prefix. The outer loop iterates over the characters of the first string, which has length m. The inner loop iterates over the remaining n-1 strings in the input array.

#The space complexity of this code is O(1), since we are only using a constant amount of extra space to store the prefix string and a few loop counters. No additional data structures are used.

def longestCommonPrefix(arr):
  #if array is empty return empty string
  if not arr:
    return ""
  
  prefix = ""
  #have to make sure that all the items have the same charcaters in the begining
  #we can start by comparing if each of the charcater in the first item is present in all the other items
  #if no, stop and break out -> that's the end
  #if yes, collect the common string in a saved variable
  #make sure the if length of any string is exceeded -> should stop
  for i in range(len(arr[0])):
    for j in range(1,len(arr)):
      if i >= len(arr[j]) or arr[j][i] != arr[0][i]:
        return prefix
    prefix += arr[0][i] 
  
  return prefix



print(longestCommonPrefix(["flower","flow","flight"]))

