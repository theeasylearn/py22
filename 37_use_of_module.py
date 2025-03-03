# example of how to use module
import currency
rupee = float(input("Enter rupees"))
dollar = currency.toDollar(rupee)
euro = currency.toEuro(rupee)
pound = currency.toPound(rupee)
print(f" dollar = {dollar} euro = {euro} pound = {pound}")

