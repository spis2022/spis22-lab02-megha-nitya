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

print(getNumber())

