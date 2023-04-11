#we would need two pointers
#one left pointer that starts from the index 0
#right pointer starts from 1
#the right pointer will traverse the array and compare it with the left pointer
#if right pointer is same as left pointer -> right pointer keeps on moving
#if right pointer is not equal to left pointer -> move left pointer to one index and assign that index value to the value where right pointer is pointing
#we need to return the length of unique items in the nums array
#the left pointer will be pointing at the index of last unique item
#so return i+1
def removeDuplicates(nums):
  i = 0

  for j in range(1,len(nums)):
    if nums[i] != nums[j]:
      i += 1
      nums[i] = nums[j]
  
  return i + 1


      
      



print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))