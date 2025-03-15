def print_triangle(height, char='*'):
    for i in range(1, height + 1):
        
        chars = 2 * i - 1

        print(char * chars)

try:
    height = int(input("Enter the height of the triangle: "))
    if height <= 0:
        print("Please enter a positive number.")
    else:
        print_triangle(height)
except ValueError:
    print("Invalid input. Please enter a number.")