# Pizza ordering System

def welcome():
    print("Welcome to ABC pizza spot")
    print("How can we help you ??")
    
def info():
    fname = input("Enter the your First Name Please: ")
    lname =  input("Enter the your Last Name Please: ")
   
    return fname,lname


class person:
    def __init__(self):      
        self.fname =""
        self.lname = ""   
        self.kindOfPerson = ""
        self.customerOrderProfile = {}
        
        
        
    def getInfo(self):# information of person.
        self.fname,self.lname = info()
        
    def decidingPerson(self): # deciding who is who
        self.kindOfPerson =  input("Enter the kind of person Please ['customer' 'cashier' 'cashier','chef']: ")
        if (self.kindOfPerson.lower() == "customer"):  
            print("you are a customer!!!") # identify customer
            pizza = input("What kind of pizza  would you like: ?")
            side = input ("What Kind of side would you like: ? ")
            drink = input ("What Kind of drink would you like: ? ")
            self.customerOrderProfile["mPizza"] = pizza
            self.customerOrderProfile["mSide"] = side
            self.customerOrderProfile["mdrink"] = drink
            self.customerOrderProfile["cdrink"] = 5
            self.customerOrderProfile["cPizza"] = 10
            self.customerOrderProfile["cSide"] = 5
            #print (f"{self.customerOrderProfile}")
            
        elif (self.kindOfPerson == "cashier"):
            #identify cashier process.
            print(f"Order Received and processing")
            print(f"Your order item Listed  below will be delivered momentarily ")
            print (f"Order sent to Chef  for Preparation")
            print(f"Items received: {self.customerOrderProfile['mPizza']}, {self.customerOrderProfile['mSide']}, and {self.customerOrderProfile['mdrink']} ")
            
        elif (self.kindOfPerson == "chef"):
            print("Order received")
            print(f"{self.customerOrderProfile['mPizza']} successfully prepared ")
            print(f"{self.customerOrderProfile['mSide']} successfully prepared")
            print(f"{self.customerOrderProfile['mdrink']} successfully prepared")
            print(f"{'*' * 30}")
            print(f"{'*' * 30}")
            
    def deliverCustomer(self):
        print(f"{'*' * 30}")
        print(f"{'*' * 30}")
        print("Order Complete")
        print("Thank you for your order")
        print ("Come back soon")
    
    def __repr__(self):
       # if (self.kindOfPerson.lower() == "customer"):
        return f" Customer First name: {self.fname} \n"\
                           f" Customer Last name: {self.lname}\n"\
                            f" Pizza ordered : {self.customerOrderProfile['mPizza']} cost: ${self.customerOrderProfile['cPizza']}\n"\
                            f" Side ordered : {self.customerOrderProfile['mSide']} cost: ${self.customerOrderProfile['cSide']}\n"\
                            f" Drink ordered : {self.customerOrderProfile['mdrink']} cost: ${self.customerOrderProfile['cdrink']}\n"\
                            f" Total cost of Pizza is  {self.customerOrderProfile['cPizza'] + self.customerOrderProfile['cSide'] + self.customerOrderProfile['cdrink']}"
        #else:
            #return f" Update for chef and cashier"
                        
    

welcome()
input("Enter any key to continue/")
kappa = person()
kappa.getInfo()
print(f"{'*' * 30}")
print("Enter 'customer' first to place order  (Demo test)")
input("Enter any key to continue/")
kappa.decidingPerson()
print(f"{'*' * 60}")
print(f"{'*' * 60}")
print ("Enter 'cashier' --(Demo Test)")
input("Enter any key to continue/")
kappa.decidingPerson()
print(f"{'*' * 60}")
print(f"{'*' * 60}")
print("Enter 'chef' (Demo Test)")
input("Enter any key to continue/")
kappa.decidingPerson()
print(kappa)
kappa.deliverCustomer()




