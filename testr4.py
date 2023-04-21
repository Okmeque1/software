a = [23,12,4,1231,414,124141,42,12,-1,43,-34,5]
maximum = a[0]
index = 0
indexmax = 0
for b in a:
    if maximum < b:
        maximum = b
        indexmax = index
    index += 1
print("Finished with " + str(maximum) + " as maximum result and " + str(indexmax) + " as index in list.")