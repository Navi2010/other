# Function to get odd numbers under a given limit
def get_odd_numbers(limit):
    odd_numbers = []
    for num in range(limit):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

# Get user input
user_input = int(input("enter a number: "))

odd_numbers = get_odd_numbers(user_input)


fruits = ['apple', 'banana', 'cherry', 'grape']

capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize())

print("odd numbers under", user_input, ":", odd_numbers)
print("capitalized fruits:", capitalized_fruits)
