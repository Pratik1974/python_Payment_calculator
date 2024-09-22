## input we need from the user
# total rent
# total food ordered for snacking
# electricity units spend
# charge per unit
# person living in flat

##Output
# Total amount you've to pay is

rent = int(input("Enter your flat rent= "))
food = int(input("Enter your the amount of food ordered= "))
electricity_spend = int(input("Enter the total of electricity spend"))
charge_per_unit = int(input("Enter the charge per unit= "))
person = int(input("Enter the number of persons living in flat: "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // person

print(f"Each person will pay = {output}")