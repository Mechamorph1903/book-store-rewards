"""
Author: Daniel Anorue
Program Title: Book Store Rewards. 
File Description: Helps the user calculate the total cost of books
purchased in a book store. The program outputs their receipt with Sub Total,
Tax, Total (Subtotal + Tax), and Points Earned values"
"""


books_purchased = int(input("How many books did you purchase this month? "))

books_purchased += 1
subTotal = 0
counter = 1

while (counter < books_purchased):
    book_price = float(input(f"What was the price of Book {counter}? "))
    subTotal += book_price
    counter += 1


tax = 0.07 * subTotal
finalPrice =  tax + subTotal

if (subTotal >= 20 and subTotal < 40):
    points = 5
elif (subTotal >= 40 and subTotal < 60):
    points = 15
elif (subTotal >= 60 and subTotal < 80):
    points = 30
elif (subTotal >= 80 and subTotal < 100):
    points = 60
elif (subTotal > 100):
    points = 120
else:
    points = 0

 
print('*'*40)
print(f"{'Receipt':^40}")
print('*'*40)
print(f"{f'    Sub Total: $ {subTotal:.2f}':^40}")
print(f"{f'   Taxes Owed: $ {tax:.2f}':^40}")
print('*'*40)
print(f"{f'        Total: $ {finalPrice:.2f}':^40}")
print(f"{f'Points Earned:   {points:.2f}':^40}")
print('*'*40)
