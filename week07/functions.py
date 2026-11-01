# Self-Assessment Questins
# 1. The first bug I noticed was on line 10. The for loop is created but there is no ":" at the end of the line. I noticed this error just by looking at the code. I'd say that
# my current debugging isn't incredible but I can spot obvious mistakes. 
# 2. The apply_discount takes in two inputs (price and tier) and it determines what discount percentage you get based on your tier.
# The code will adjust the price to the applied discount. It will then return the adjusted discounted price. I believe a colleague could use it without
# reading the body because as long as you understand you need 2 inputs, you can make it work.
# 3. I used AI to help fix the issues on the broken_sales file. The AI assisted me in finding out what was wrong with the initial code, it was really useful.
# The AI for sure helped my understanding because I honestly overlooked the "total = sales" issue. 

# Exercise 1

def calculate_tax(price, rate):
    return price * rate 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, .08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# Exercise 2 

def apply_discount(price, tier): 
    if tier == "gold":
        return price * 0.85
    elif tier == "silver": 
        return price * .9
    elif tier == "bronze":
        return price * .95
    else:
        return price

price = 200 
tiers = ["gold", "silver", "bronze", "none"]
for tier in tiers: 
        print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3 

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: {discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
     discounted = apply_discount(price, tier)
     tax = calculate_tax(discounted, tax_rate)
     return discounted + tax

print(f"Final price: ${final_price(200, "gold", 0.07):.2f}")

# Exercise 4 

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
     total = final_price(price, tier, 0.07)
     print(f"Price: ${price:.2f} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 5 
# sales = [120, 80, 250, 175, 90]

# total = 0
# for sale in sales:
#     total += sale
# print(f"Total: ${total}")

# count = 0
# for sale in sales:
#     count += 1
# print(f"Count: {count}")

# i = 0
# while i < len(sales):
#     print(sales[i])
#     i += 1


# Exercise 6

x = 100
def double_it():
    x = 999
    return x * 2

print(x) # Prints out 100
print(double_it()) # Prints out 1998
print(x) # Prints out 100