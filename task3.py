#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

i1 = input("Enter your first item's price :")
i2 = input("Enter your second item's price :")
i3 = input("Enter your third item's price :")
i4 = input("Enter your fourth item's price :")
i5 = input("Enter your fift item's price :")

i1 = float(i1)
i2 = float(i2)
i3 = float(i3)
i4 = float(i4)
i5 = float(i5)

subt = i1 + i2 + i3 + i4 + i5
tax = subt/100 * 12
tax = round(tax,2)
t = subt + tax
t = round(t,2)

subt = str(subt)
tax = str(tax)
t = str(t)


print("Your subtotal is $"+subt,"and your taxes total $"+tax,"for a total of $"+t,)






