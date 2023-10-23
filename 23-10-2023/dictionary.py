file={"jpg":10,"txt":14,"csv":23,"py":20}
for extension in file:
    print(extension)
for ext ,amount in file.items():
    print("There are {} files with the .{}".format(amount,ext))
print("value =",file["jpg"])