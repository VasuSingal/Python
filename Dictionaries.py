#1.

dic = {"one":1, "two":2, "three":3}

dic.values() #Returns all the values in this case 1,2,3
dic.keys() #Returns all the keys in this case one, two, three

# dic.clear() Clears all the elements in the dictionary
dic.get("one") # Returns the value of given key
dic.items() #Returns all the key and value pairs a tuples
dic.pop("three") #Deletes the element with the given key
dic.popitem() #Deletes the last key and value pair
dic.update({"four":4}) #Updates the given dictionary with the provided key and value pairs

print(dic)

#2.
myset = {"hello", "this", "is", "a", "set"}
print(myset)

