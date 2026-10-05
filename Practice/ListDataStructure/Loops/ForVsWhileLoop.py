# While Loop
var01 =1 
while var01 <=6:
   print(var01)
   var01 +=1

# Use Input with while Loop
answer = ""
while answer != "Yes":
    answer = input("Do you agree ?(yes/no):")
    print("Thank You") 

# Condition 3 attempt to accept and output"Glad we are on same page"
# Otherwise "You are Out"

attempts = 0
while attempts < 3:
    answer01 = input("Do you agree ?yes/no:")   # ← Add ()
    if answer01 == "yes":
        print("Glad")
        break
    attempts += 1
print("Thank You")

