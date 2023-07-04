import random
# ---------------------------------------------------------
# Vending maschine
# Log: "drink:1 - input_value: 200 - change: 50 - coins: 3 - OK"
# ---------------------------------------------------------

drinks = {"Coca Cola": 150,
        "Pepsi Cola": 200,
        "Sprite":200,
}

money = [200, 100, 50]
coins = []
paid = []
log = []
choice = []
collected = 0
coin_count = 0
running = 1

while running:
    print("*"*50)
    for drink in drinks:
        print(f"Auswahlmöglichkeiten{drink,drinks[drink]/100}")
    print("*"*50)
    choice = input("Bitte wählen sie ihr Getränk (q für Abbruch, Log für log): ")
    if choice in drinks:
        print(f"{choice} wurde gewählt! Der Preis ist {drinks[drink]/100}€")
        log.append(choice)
        coins = input("Bitte die münzen einzeln einwerfen! ").split(",")
        for coin in coins:
            coin_count += 1
            log.append(coin_count)
            if int(coin) not in money:
                collected += int(coin)
                log.append(choice)
            elif coin_count > 3:
                collected += int(coin)
                log.append(choice)
                coin_count - 3
                break
            else:
                paid.append(int(coin))
        while sum(paid) != drinks[choice]:
            if sum(paid) > drinks[choice]:
                print(f"Ihr Wechselgeld beträgt: {(drinks[choice] - sum(paid)) /100}€")
                log.append(paid)
                break
            elif sum(paid) < drinks[choice]:
                print(f"Es fehlt noch: {(drinks[choice] - sum(paid)) /100} €")
                log.append(paid)
                coins = input("Bitte nachwerfen! ").split(",")
                for coin in coins:
                    coin_count += 1
                    log.append(coin_count)
                    if coin_count > 3:
                        collected += int(coin)
                        log.append(choice)
                        coin_count - 3
                        break
                    elif int(coin) not in money:
                        collected += int(coin)
                        log.append(choice)
                    #elif int(coin) == 100:
                    #    random.choice
                    else:
                        paid.append(int(coin))
                        log.append(paid)
        else:
            if sum(paid) == drinks[choice]:
                print(f"KLONK! bitte Ihre {choice}")
                log.append(paid)
                paid.clear
    elif choice == ("q", "exit", "close"):
        running - 1
    elif choice == "Log":
        print(log)
    # else:
    #     print("Computer sagt nein!")
