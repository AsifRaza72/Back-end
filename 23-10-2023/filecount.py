# a=5
# b=0
# print(a/b)    
def divide_by(a,b):
#     return a/b
# try:
#     ans=divide_by(40,0)
# except Exception as e:
#     print("Something went wrong",e)
#     print(e.__class__)
# # print(divide_by(40,0))
  try:
    ans=divide_by(40,0)
  except ZeroDivisionError as e:
    print(e,"We cannot divide by 0")