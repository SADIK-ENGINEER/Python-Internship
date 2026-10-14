# 1. calculateElectronicsGST(a, b)

def calculateElectronics(a,b):
    amount = a+b
    return amount+(amount*18/100)


# 2. calculateFashionGST(c, d)

def  calculateFashion(c,d):
    amount = c+d
    return amount+(amount*13/100)



# 3.  calculateFoodGST(e)

def calculateFood(e):
 return e+(e*7/100)




# 4.  calculateDiscountedBill(a, b, c, d, e)

def  totalBill(a, b, c, d, e):
 Electronics = calculateElectronics(a,b)
 Fashion = calculateFashion(c,d)
 Food =  calculateFood(e)
 return Electronics+Fashion+Food


# 5.  calculateDiscountedBill(a, b, c, d, e)

def calculateDiscountedBill(a, b, c, d, e):
   Total = totalBill(a, b, c, d, e)
   Discount = Total*20/100
   return Total - Discount

a,b,c,d,e = 100,100,100,100,100

Total =  totalBill(a, b, c, d, e)
Discount = Total*20/100
final_amount = Total - Discount

print("Electronics : ",int(calculateElectronics(a,b)))
print("Fashion : ",int(calculateFashion(c,d)))
print("Food : ",int(calculateFood(e)))
print("Total : ",Total)
print("Discount :",Discount)
print("final_amount:",final_amount)   
