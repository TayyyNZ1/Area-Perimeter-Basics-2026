# Author: Talia Poole
# Used past programs to help me when stumped
# Date: 03.06.2026

# Entering a number that is a positive integer
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:
        
        try:
            # Ask the user for a number
            response = float(input(question))

            # Check that the number is more than zero
            if response > 0:
                    return response
            else:
                print(error)
        except ValueError:
            print(error)

# Main program
# Ask user for width and length
keep_going = ""
while keep_going == "":
     
    for item in range(0, 1): 
        width = num_check("Width (metres): ")
        print(width)

    for item in range(0, 1):
        length = num_check("Length (metres): ")
        print(length)

    for item in range(0, 1):
        fence_cost_per_metre = num_check("Fence cost / metre: ")
        print(fence_cost_per_metre)

# Calculate fencing cost
    perimeter = 2 * (width + length)
    total_cost = perimeter * fence_cost_per_metre

    print()
    print(f"The total fence length is {perimeter}.")
    print(f"The total fence cost is ${total_cost}")

# Ask the user if they wish to go again
    keep_going = input("To use again, press enter. To end program, press any other key. \n")
print(f"Thank you for using the fence cost calculator. Have a nice day:) \n")
