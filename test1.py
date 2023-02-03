
#code
wallet = 5000
computer_price = 1000

#le prix de l'ordinateur est inferieur à 1000$
if computer_price <= wallet:
    print("L'achat est possible")
    wallet -= computer_price
else:
    print("L'achat est impossible, vous navez que {}$".format(wallet))
print(wallet)



