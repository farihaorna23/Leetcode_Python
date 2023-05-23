def removeElement(nums,val):
  i = 0

  for j in range(len(nums)):
    if nums[j] != val:
      nums[i] = nums[j]
      i+=1
  
  return i
  



print(removeElement([0,1,2,2,3,0,4,2],2)) #Output: 5, nums = [0,1,4,0,3,_,_,_]
