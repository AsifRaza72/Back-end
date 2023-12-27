def calculate_tax(bill,tax_rate):
    # my_global=1
    b=(bill*tax_rate)/100.00
    return b

    # def enclosed():
    #    return (bill*tax_rate)/100.00
    #    print(my_global)
print('Total Tax',calculate_tax(175.00,15))