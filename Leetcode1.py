#input: list and integers
#output: integers -> index of the numbers in the list that adds up to the target

#important notes:
# assume that each input would have exactly one solution, and you may not use the same element twice.

#brute force approach
#time complexity -> Quadratic o(n^2) due to nested loops
def twosum(array,target):
  for x in range(len(array)):
    for y in range(x+1,len(array)):
      if array[x] + array[y] == target:
        return [x,y]
  #return -1 if no indexes add up to the target
  return -1
  
#time complexity -> o(n)
#space complexity -> o(n)
def twosum1(array,target):

  #using hashmap to remember if we have seen the value before and remember its index
  remember = {}

  #iterate through the numbers in the list
  #for each of the number, get the value the current number needs in order to reach the target
  #check if we have seen the current number's complement number before in the obj, if so, get the index

  for x in range(len(array)):
    complement_value = target - array[x]

    if complement_value in remember:
      return [x,remember[complement_value]]
    else:
      remember[array[x]] = x
  #return -1 if no indexes add up to the target
  return -1


print(twosum1([2,7,11,15],9))