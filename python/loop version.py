#list comprehension
#loop version
result=[]
for i in range(11):
    result.append(i)
    print(result)
#list comprehension version
    print([i for i in range(11)])
#for loop version-->odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
        print(result)
        print([i for i in range(11)if i%2!=0])

#continue
        result=[]
        for i in range(11):
            if i%2!=0:
                result.append(i)
            else:
                result.append(i**2)
        print(result)
        print([i if i%2!=0 else i**2 for i in range(11)])
        mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop--odd-->square it
#even -->cube it
        result=[]
        result1=[]
        mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        for i in mat:
            for j in i:
                if j%2==0:
                    result.append(j**3)
                else:
                    result1.append(j**2)
        print(result)
        print(result1)
#merge
result=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in mat:
    for j in i:
        if j%2==0:
            result.append(j**2)
        else:
            result1.append(j**3)
        print(result)                               
#list comprehesion
        print([ele** if ele%2!=0 else ele**3 for row in mat for i in row])
        print([ele** if ele%2!=0 else ele**3 for ele in row for row in mat])
        
#paired
        mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
        list_b = [6, 4, 6, 1, 2, 2]
        [(i, mylist.index(i)) for i in list_b]
          
