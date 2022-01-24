# 1. Increment values by 2 in for loop

for i in  range(0,5,2):
    print(i)


# 2. Infinite for loop
#    For Loop can never be infinite


# 3. Add values to tuples

my_tuple = (0,1,2,3,4,5)
l1=[-3,-2,-1]            #Put all the values to be entered in the tuple in this list
for i in my_tuple:
    l1.append(i)
    t1 = tuple(l1)

print(t1)