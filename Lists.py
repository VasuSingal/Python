#1. 
li = ["Apple", 34, "Mango", "Tree", "Start"]
l = ["EXTENDED"]

li.append("Append") #Append adds element to the last index
# li.clear() Clear function clears all the elements if the list
a = li.copy() #Returns a true copy of the list li in a
li.count(34) #Counts the number of specified elements in a fgiven list
li.extend(l) #Adds another iterable to the end of the given list
li.index("Apple") #Returns the index of the element given
li.insert(3, "INSERTED") # inserts given object at the given index
li.pop(2) # Removes the element at specified index
li.remove("Apple") #Remove the element with the given value
li.sort(reverse=True) #Sorts in Descending order
li.sort(reverse=False) #sorts in Ascending Order
print(li)

#2.
# Negative indexes are useful to slice an element from the end. Last element of a given object is indexed as -1 in negative indexes.