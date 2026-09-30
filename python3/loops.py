nums =[20,33,54,6,87,12,45]

#linear search
x=45
idx =0

for val in nums:
    if(val ==x):
        print(idx)
        break
    idx +=1