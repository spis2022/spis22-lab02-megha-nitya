import math 
# The goal of this program is to practice Python constructs
def getNumber():
   x=0 
   finalNum=""
   
   while x==0:  
     symbols = input("Enter a digit: ")
     number = int(symbols)
     if number>=0:
       finalNum=finalNum+symbols
     if number<0:
       x+=1
   
   return finalNum

#print(getNumber())

def sumDigits(x):
  #store length of x in a variable
  numLength = len(str(x))
  sum = 0
  #for loop
  for i in range(numLength-1):
    #print("entering loop")
    rightdigit = x % 10
    #print("rightdigit", rightdigit)
    sum+=rightdigit
    x = x // 10
    print("x = ", x)
    
    if x < 10:
      sum += x
    #print("exiting loop")
   # You will need to complete this function

  return sum

#print("sum:", sumDigits(23))
'''
converts men's wage to women's wage taking into account country
parameters: mens wage and country
return: womens wage
'''
def convertWageMtoW(mWage, country):
  if country == "Norway":
    wageGap = 0.046

  elif country == "France":
    wageGap = 0.118

  elif country == "Canada":
    wageGap = 0.167

  else:
    wageGap = 0.182
  
  ratio = 1 - wageGap

  return mWage * ratio

print("wage", convertWageMtoW(100, "Greece"))
