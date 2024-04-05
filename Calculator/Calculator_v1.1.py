import math

# Műveletek definiálása
operations = {
    "1": lambda a, b: a + b,
    "2": lambda a, b: a - b,
    "3": lambda a, b: a * b,
    "4": lambda a, b: a / b if b != 0 else "Hiba: nullával való osztás nem lehetséges",
    "5": lambda a: math.sqrt(a),
    "6": lambda a: a ** 2,
    "7": lambda a: a ** 3,
    "8": lambda a: math.sin(math.radians(a)),
    "9": lambda a: math.cos(math.radians(a)),
    "10": lambda a: math.tan(math.radians(a)),
    "11": lambda a: math.factorial(int(a)),
    "12": lambda a: sum(range(int(a)+1)),
    "13": lambda a: math.pi * a,
    "14": lambda a: math.e * a,
    "15": lambda a: math.log(a),
    "16": lambda a: math.exp(a),
    "17": lambda a: math.ceil(a),
    "18": lambda a: round(a),
    "19": lambda a: math.floor(a),
    "20": lambda a: math.sinh(a),
    "21": lambda a: math.cosh(a),
    "22": lambda a: math.tanh(a),
    "23": lambda a: math.degrees(a),
    "24": lambda a: math.radians(a),
    "25": lambda a: math.acos(a),
    "26": lambda a: math.asin(a),
    "27": lambda a: math.atan(a),
    "28": lambda a: math.acosh(a),
    "29": lambda a: math.asinh(a),
    "30": lambda a: math.atanh(a)
}

# Fő program
while True:
    print("Válassz egy műveletet:")
    print("1 - Összeadás")
    print("2 - Összeadás")
    print("3 - Kivonás")
    print("4 - Szorzás")
    print("5 - Osztás")
    print("6 - Gyökvonás")
    print("7 - Négyzetre emelés")
    print("8 - Köbre emelés")
    print("9 - Szinusz")
    print("10 - Koszinusz")
    print("11 - Tangens")
    print("12 - Faktoriális")
    print("13 - Számok összege 0-tól")
    print("14 - Pi-szoros")
    print("15 - e-szoros")
    print("16 - Logaritmus")
    print("17 - Exponenciális")
    print("18 - Felfelé kerekítés")
    print("19 - Kerekítés")
    print("20 - Lefelé kerekítés")
    print("21 - Sinus hiperbolikusz")
    print("22 - Koszinus hiperbolikusz")
    print("23 - Tangens hiperbolikusz")
    print("24 - Radiánból fokba váltás")
    print("25 - Fokból radiánba váltás")
    print("26 - Arccoszinusz")
    print("26 - Arcszinusz")
    print("27 - Arctangens")
    print("28 - Arccoszinusz hiperbolikus")
    print("29 - Arcsinusz hiperbolikus")
    print("30 - Arctangens hiperbolikus")
    print("0 - Kilépés")
    
    choice = input("Válassz egy műveletet (0-30): ")
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
