#write a program to calculate profit/loss from given purchase & sale price
'''
    accept purchase & sale price from user 
    calculate difference between sale price and purchase price 
    if difference is positive it is profit
    if difference is negative it is loss 
'''
purchase_cost = int(input("Enter purchase price"))
sales_price = int(input("Enter sale price"))
difference = sales_price - purchase_cost

if difference>0: # == != < > <= >=
    print("profit = " + str(difference))

if difference<0:
    print("loss = " + str(difference))


if difference==0:
    print("no profit no loss")

 