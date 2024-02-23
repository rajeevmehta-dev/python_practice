def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(location="Rajeev", name ="mehta")



def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")
    
prime_checker(number=13)
print(bool(1))
