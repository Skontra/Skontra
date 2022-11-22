myList = [[1, 2, 3, 4, 5], [12, 13, 23], [10, 20, 30], [11, 22, 33], [12, 24, 36]]
print("The original list is:")
print(myList)
outputList = [x for l in myList for x in l]
print("The flattened list is:")
print(outputList)