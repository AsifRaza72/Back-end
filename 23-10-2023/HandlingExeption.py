items=[1,2,3,4,5]
try:
    item=items[6]
except Exception as e:
    print("something went wrong",e)
    print(e.__class__)
# print(item)