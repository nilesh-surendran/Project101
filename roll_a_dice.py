import random

response=input('Do you want to roll a dice? y for yes:')
print(response)

while response=="y":
    number = random.randint(1,6)
    print(number)
    if number == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]")

    elif number == 2: 
        print("[-----]") 
        print("[     ]") 
        print("[0   0]") 
        print("[     ]") 
        print("[-----]")

    elif number == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]")

    elif number == 4: 
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]")

    elif number == 5: 
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]")

    elif number == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]")

    response=input("Press y to roll again and n to exit:")