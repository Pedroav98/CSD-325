
# Pedro Avila
# CSD-325 - Module 1
# Assignment: On the Wall + Flowchart(s)

# Function to count down the bottles
def countdown(bottles):
    while bottles > 0:
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        bottles -= 1

        print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.")
        print()


# Main program
bottles = int(input("Enter number of bottles: "))

countdown(bottles)

print("Time to buy more bottles of beer.")
