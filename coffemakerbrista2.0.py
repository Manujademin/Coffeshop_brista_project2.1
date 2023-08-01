#lets make a robot brista to work at a Resturent

print("Heloo coustomer welcome to our coffe shop")
 
name = input("what is you're name \n")

print(name +",we'll bring you a menu soon as posible ")
print("\n")
#print("\n")

print("--------menu-------------")
print("Black Coffe")
print("white coffe")
print("cold coffe")
print("Espresso")

print("\n")
#print("\n")

print("what would you like to order? ")

print("\n")


order = input("May I take youre order? ")

print("\n")
print("Hey "+ name +" youre order will be ready in a moment...")

#so i made a system that can get orders, Now let's make a system that can price items 
#today is 01/08/2023 im Manuja Demin 

if order == "Black coffe" or "black coffe":

    price_per_unit = 5

    if order == "White coffe" or "white coffe":
        price_per_unit = 8

        if order == "Cold coffe" or "cold coffe":

            price_per_unit = 6

            if order == "Espresso" or "espresso":

                price_per_unit = 13

            else:
                price_per_unit = 8

        else:
            price_per_unit = 8
    else:
        price_per_unit = 8
    
else:
    price_per_unit = 8



print("That is about"+ str(price_per_unit))
#lets add Quantity

Quantity = int(input("How much would you like to order: \n"))

price = (Quantity * price_per_unit)

print("That will be :$"+str(price ))

#hope you enjoyed this is manuja demin
