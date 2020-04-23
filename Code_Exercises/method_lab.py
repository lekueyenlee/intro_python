# method code example
#

# Definition of methods
# method 1 - returns a value
def calculate_commission(in_sales_amount):
    commission_rate = .3
    commission_amount = in_sales_amount * commission_rate

    return commission_amount

#method 2 - only executes and doesn't return a value
def print_total_earned(in_sales_amount, in_commission_amount):
    total = in_sales_amount + in_commission_amount
    print("$ " + str(total))

sales_amount = 500

# this is what it means to call (invoke) methods
commission_earned = calculate_commission(sales_amount)

print_total_earned(sales_amount, commission_earned)
