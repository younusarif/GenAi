attempts = 0
while attempts < 3:
    answer01 = input("Do you agree ?yes/no:")   # ← Add ()
    if answer01 == "yes":
        print("Glad")
        break
    attempts += 1
print("Thank You")