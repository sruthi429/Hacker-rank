try:
    n = int(input("Enter a number: ").strip())
    
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

except ValueError:
    print("Please enter a valid integer without quotes or symbols.")



