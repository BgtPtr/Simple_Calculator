import math

# Műveletek definiálása
operations = {
    "1": lambda a, b: a + b,
    "2": lambda a, b: a - b,
    "3": lambda a, b: a * b,
    "4": lambda a, b: a / b if b != 0 else "Hiba: nullával való osztás nem lehetséges",
    "5": lambda a: math.sqrt(a),
    "6": lambda a: a ** 2,
    "7": lambda a: a ** 3
}

# Fő program
while True:
    print("Válassz egy műveletet:")
    print("1 - Összeadás")
    print("2 - Kivonás")
    print("3 - Szorzás")
    print("4 - Osztás")
    print("5 - Gyökvonás")
    print("6 - Négyzetre emelés")
    print("7 - Köbre emelés")
    print("0 - Kilépés")
    
    choice = input("Válassz egy műveletet (0-7): ")
    if choice not in operations.keys() and choice != "0":
        print("Hibás választás, válassz újra!")
        continue
    
    if choice == "0":
        break

    num1 = float(input("Add meg az első számot: "))
    
    if choice in ["1", "2", "3", "4"]:
        num2 = float(input("Add meg a második számot: "))
        result = operations[choice](num1, num2)
    else:
        result = operations[choice](num1)
    
    print(f"Az eredmény: {result}")
