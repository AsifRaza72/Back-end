# 1. Under the num_list create a new for loop and print out each value on the list in sequential order.
num_list=[93,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for i in num_list:
    print(i)
print()
# 2. Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition.   
for i in num_list:
    if (i>45):
        print(i)
print()
# 3. Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”
for i in num_list:
    if(i>45):
        print("OVER 45",i)
    else:
        print("UNDER 45",i)
print()
# 4. Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number.
# 5. Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
# 6. Inside the for loop increment the counter by 1.
# 7. Add a print statement outside the for loop to print the value of the count variable.
# 8. Finally, add a break statement directly after the print statement inside the if condition for finding the number.
count=0
for index , number in enumerate(num_list):
    if (number == 36):
        count +=1
        print("Value found at position:",index)
        break
print(count)