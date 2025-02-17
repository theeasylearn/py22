'''
    write a program to calculate tax amount, gross income and net income from given monthly income as per new income tax rule.
    Income Slab (Rs.)
	Income                  Tax Rate (%)
    0 - 4,00,000	        NIL
    4,00,001 - 8,00,000	    5
    8,00,001 - 12,00,000	10
    12,00,001 - 16,00,000	15
    16,00,001 - 20,00,000	20
    20,00,001 - 24,00,000	25
    Above 24,00,000	        30

    steps 
    1) take monthly income from user 
    2) calculate annual income(gross income) 
        multiply monthly income with 12
    3) calculate tax amount as per rule 
    4) after tax amount is calculated, calculate net income 
        netincome = gross income - tax 
    display gross income, tax and net income 
'''
monthly_income = int(input("Enter your monthly income"))
gross_income = monthly_income * 12
tax_amount = None
if gross_income>2400000:
    tax_amount = gross_income * 0.30
elif gross_income>2000000:
    tax_amount = gross_income * 0.25
elif gross_income>1600000:
    tax_amount = gross_income * 0.20
elif gross_income>1200000:
    tax_amount = gross_income * 0.15
elif gross_income>800000:
    tax_amount = gross_income * 0.10
elif gross_income>400000:
    tax_amount = gross_income * 0.05
else: 
    tax_amount = 0

net_income = gross_income - tax_amount
print(f"gross income = {gross_income} tax amount = {tax_amount} net income = {net_income}")
