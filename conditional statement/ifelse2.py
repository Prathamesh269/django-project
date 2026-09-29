
#Deposit amount:
balance=500
amount=int(input("Enter the amount:"))

# if amount>0:
#     balance+=amount
#     print("balance after deposit:",balance)
# else:
#     print("Invalid balance")

#Withdraw amount:
if amount>0 and amount<=balance:
    balance-=amount
    print("balance after withdraw:",balance)
else:
    print("Invalid balance")
