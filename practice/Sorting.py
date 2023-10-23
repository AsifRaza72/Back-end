list=[2,5,7,9,3,1,6,8]
method=input("Enter the method ?")
def sort_list(numbers,method):
    new_list=[]
    if method=='asc':
        for i in numbers:
            if i>i+1:
                i=i+1
            new_list.append(numbers[i])
        i +=1
    return new_list

print("sorted list :",sort_list(list,method) )