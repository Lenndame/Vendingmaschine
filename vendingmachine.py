import random
# ---------------------------------------------------------
# Vending maschine
# ---------------------------------------------------------

drinks = {
    "Cola": 150,
    "Pepsi": 200,
    "Sprite": 200,
}

money = [200, 100, 50]
coins = []
paid = []
stolen = 0
running = True
coin_count = 0

log = {
    "Total Coins": 0,
    "Total Paid": 0,
    "Choice Count": {drink: 0 for drink in drinks},
    "Amount Stolen": 0,
    "Swallowed Coins": 0,
    "You chose violence": 0,
    "Peaceful": 0,
}

while running:
    print("*" * 50)
    print("Ihre Auswahlmöglichkeiten sind: ")
    for drink, price in drinks.items():
        print(f"{drink}, Preis: {price / 100}€")
    print("*" * 50)
    choice = input("Bitte wählen Sie Ihr Getränk (q für Abbruch, Log für Log): ")

    if choice in drinks:
        print(f"{choice} wurde gewählt! Der Preis beträgt {drinks[choice] / 100}€")
        log["Choice Count"][choice] += 1
        paid.clear()

        while sum(paid) < drinks[choice]:
            if sum(paid) != 0:
                print(f"Es fehlen noch: {(drinks[choice] - sum(paid)) / 100} €")
            coins = input("Bitte werfen Sie Ihre Münzen ein: ").split(",")
            sad = random.randint(0, 10)
            for coin in coins:
                log["Total Coins"] += 1
                coin = int(coin)
                coin_count += 1                   
                if coin not in money:
                    stolen += coin
                    log["Swallowed Coins"] += 1
                    continue
                elif coin == 100:
                    if sad >= 5:
                        stolen += coin
                        log["Swallowed Coins"] += 1
                elif coin_count > 3:
                    stolen += coin
                    log["Swallowed Coins"] += 3
                    print("ERROR! Zu viele Münzen!")
                    coin_count = 0
                    paid.clear()
                    break
                else:
                    paid.append(coin)
                    log["Total Paid"] += sum(paid)
        else:
            if sum(paid) >= drinks[choice]:
                print(f"Ihr Wechselgeld beträgt: {(sum(paid) - drinks[choice]) / 100}€")
                print(f"KLONK! Bitte Ihre {choice} ")
                coin_count = 0
                unlucky = random.randint(0, 10)
                if unlucky >= 8:
                    print(f"Verdammt, es scheint als ob die {choice} im Schacht stecken geblieben ist!")
                    stuck = input("Treten, anrempeln oder weg gehen? ")
                    if stuck in ["treten", "anrempeln"]:
                        log["You chose violence"] += 1
                        broken = random.randint(0, 10)
                        if broken >= 6:
                            print("BRRZZTTT!!! Die Maschine ist Schrott!")
                        else:
                            print("Glück gehabt! Das Getränk ist herausgefallen!")
                    elif stuck == "weg gehen":
                        log["Peaceful"] += 1
                        lucky = random.randint(0, 10)
                        if lucky >= 2:
                            print("Glück gehabt! Das Getränk ist herausgefallen!")
                        else:
                            print("Dann bleibst du wohl durstig")
                           
    elif choice == "q":
        print("Kein Durst")
        running = False
    elif choice == "Log":
        log["Amount Stolen"] = stolen
        print(log)
    else:
        print("Computer sagt nein!")
