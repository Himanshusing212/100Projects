import random
print("Welcome to the PyPassword Generator!")
n = int(input("How many letters would you like in your password?\n"))
s = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', '<', '>', ',', '.', '/','', '~', '`',]
pwd =""
for i in range(n+1):
    pwd += random.choice(letters)
for j in range(s+1):
    pwd += random.choice(symbols)
for q in range(num+1):
    pwd += random.choice(numbers)

print("Here is your password: ",pwd)