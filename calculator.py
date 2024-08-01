name =input("Enter your name : ")
balance = int(input ("Enter your balance : "))
print ("  ")
print ("Hello",name,"What do you like to buy ?") 
print ("Your current balance is",balance,"..")
print ("We have following vegetables..")

cart = []
def add_to_cart(item):
    cart.append(item)
    
def view_cart():
    if cart :
        print ("Items in cart : ")
        for item in cart:
            print (item)
    else :
        print ("Your cart is empty.")

def vegetables_list ():
    print ("1.Capsicum")
    print ("2.Tomatto")
    print ("3.Potato")
    print ("4.Cabbage")
    print ("5.Onion")
    print ("6.To view cart")

    choice = int(input("=>"))
    if choice == 1:
        capsicum ()
    elif choice ==2:
        tomatto ()
    elif choice ==3:
        potatto ()
    elif choice ==4:
        cabbage ()
    elif choice ==5:
        onion ()
    elif choice ==6:
        view_cart ()
             
def capsicum ( ):
    quantity = int(input("Enter quantity as kg : "))
    cost= quantity*100
    print ("  ")
    print ("The price of",quantity,"Kg is",cost,"rs")
    print ("1.Purchage")
    print ("2.Too high price")
    choice =int(input("=>"))
    if choice ==1 :
                if balance>=cost:
                    add_to_cart ("=> Capsicum")
                    print ("Capsicum added to cart successfully")
                else:
                    print ("Unsufficent balance")
                print ("  ")
                print ("Any other vegetables sir ?")
                vegetables_list ()
    elif choice == 2:
                print ("Sorry sir, do you like to buy anything else ?")
                vegetables_list ()

def tomatto ():
    quantity = int(input("Enter quantity as kg : "))
    cost = quantity*70
    print ("  ")
    print ("The price of", quantity,"Kg is",cost,"rs" )
    print ("1.Purchage")
    print ("2.Too high price")
    choice = int(input("=>"))
    if choice == 1:
        if balance>=cost:
            add_to_cart ("=> Tomatto")
            print ("Tomatto added to cart successfully")
        else:
            print ("Unsufficient balance")
        print ("  ")
        print ("Any other vegetables sir ?")
        vegetables_list ()
    elif choice == 2:
        print ("Sorry sir, do you like to buy anything else ?")
        vegetables_list ()

def potatto ():
    quantity = int(input("Enter quantity as kg : "))
    cost = quantity*50
    print ("  ")
    print ("The price of",quantity,"Kg is",cost,"rs")
    print ("1.Purchage")
    print ("2.Too high price")
    choice = int(input("=>"))
    if choice == 1:
        if balance>=cost:
            add_to_cart ("=> Potatto")
            print ("Potatto added to cart successfully")
        else:
            print ("Unsufficient balance")
        print ("  ")
        print ("Any other vegetables sir ?")
        vegetables_list ()
    elif choice == 2:
        print ("Sorry sir, do you like to buy anything else ?")
        vegetables_list ()

def cabbage ():
    quantity = int(input("Enter quantity as kg : "))
    cost = quantity*60
    print ("  ")
    print ("The price of",quantity,"Kg is",cost,"rs")
    print ("1.Purchage")
    print ("2.Too high price")
    choice = int(input("=>"))
    if choice == 1:
        if balance>=cost:
            add_to_cart ("=> Cabbage")
            print ("Cabbage added to cart successfully")
        else:
            print ("Unsufficient balance")
        print ("  ")
        print ("Any other vegetables sir ?")
        vegetables_list ()
    elif choice == 2:
        print ("Sorry sir, do you like to buy anything else ?")
        vegetables_list ()

def onion ():
    quantity = int(input("Enter quantity as kg : "))
    cost = quantity*40
    print ("  ")
    print ("The price of",quantity,"Kg is",cost,"rs")
    print ("1.Purchage")
    print ("2.Too high price")
    choice = int(input("=>"))
    if choice == 1:
        if balance>=cost:
            add_to_cart ("=> Onion")
            print ("Onion added to cart successfully")
        else:
            print ("Unsufficient balance")
        print ("  ")
        print ("Any other vegetables sir ?")
        vegetables_list ()
    elif choice == 2:
        print ("Sorry sir, do you like to buy anything else ?")
        vegetables_list ()

def cart_quantity ():
    print ("You have following in your cart",view_cart)

vegetables_list ()
