class Budget:
    
    def __init__ (self):
        self.budget = 100

    def withdraw(self,amount):
        self.budget = self.budget - amount    

    def deposit(self,amount):
        self.budget = self.budget + amount

    def transfer(self,catagory,amount):
        self.budget = self.budget - amount
        if catagory == 'food':
            food.budget = food.budget + amount
        if catagory == 'clothing':
            clothing.budget = clothing.budget + amount
        if catagory == 'entertainment':
            entertainment.budget = entertainment.budget + amount

food = Budget()
clothing = Budget()
entertainment = Budget()

print (food.budget)
print (clothing.budget)
print (entertainment.budget)

clothing.withdraw(20)
entertainment.deposit(5)

print (food.budget)
print (clothing.budget)
print (entertainment.budget)

clothing.transfer('food',50)

print (food.budget)
print (clothing.budget)
print (entertainment.budget)