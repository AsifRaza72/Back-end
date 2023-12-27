# file=open('bb.txt','r')
# data=file.readlines()
# print(data)
# file.close()
with open ('bb.txt','a') as file:
    file.writelines([" This is a new file created!2","\nThis is another line to be added."])