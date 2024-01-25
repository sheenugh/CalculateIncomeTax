# This py file is trying on my own first, wherein I am testing myself if I can solve the exercise on my own like creating my own algorithm without
# searching it to the internet or chatgpt.

# Note: I watch the tutorial first in YT about how to use the specific function and apply it here in my task

# Given 
# Taxable Income = First: $10,000, Next: $10,000, Third: ??
# Rate = First Rate: 0, Second Rate: 10%, Third Rate: 20%

first_income = 10000
second_or_income = 10000
income = 45000
payable_tax = 0 
print("The given income is ", income)

if income <= 10000:
    payable_tax = 0
elif income <= 20000:
    x = income - 10000
    payable_tax = x * 0.1
else:
    payable_tax = 0
    payable_tax = 10000 * 0.1
    payable_tax += (income - 20000) * 0.2

print("The first income tax is ", first_income, " dollars, having 0% rate.")
print("The next income tax is ", second_or_income, " dollars, having 10% rate.")
print("The third or remaining income tax is", payable_tax, " dollars, having 20% rate.")