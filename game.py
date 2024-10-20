

import random
import json  
import datetime


secret = random.randint(1, 20)
attempts = 0    
failed_atempts = [] # Seznam za shranjevanje neuspešnih ugibanj

username = input("Enter your user name: ")

current_time = datetime.datetime.now() 

with open("scorelist.json", "r") as score_file:
    score_list = json.loads(score_file.read()) 
    results_sorted = sorted(score_list, key=lambda x: x["attempts"]) # sortira najboljše rezultate po številu poskusov
    print("Top scores: ")
    for i, result in enumerate(results_sorted[:3], start=1): # izpiše najboljše 3 poskuse
            print(f"{i}. Username: {result["username"]}, Attempts: {result["attempts"]}, Date: {result["date"]} , Secret number: {result["secret_number"]}")


while True:
    guess = int(input("Enter your guess (between 1 and 20): "))
    attempts += 1     

    if guess == secret:
        print("Congrats, you won!")
        print(f"{attempts} attempts needed.")

        score_list.append({"attempts": attempts, "date": current_time.isoformat(), "username": username, "secret_number": secret})

        with open("scorelist.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        # Izpis vseh neuspešnih ugibanj
        if failed_atempts:
            print("Your unsuccessful guesses were:", failed_atempts)
        else:
            print("No unsuccessful guesses.")

        break
    elif guess < secret:
        print("Enter higher number.")
        failed_atempts.append(guess) # Dodamo neuspešno ugibanje v seznam
    elif guess > secret:
        print("Enter lower number.")
        failed_atempts.append(guess)  # Dodamo neuspešno ugibanje v seznam
    else:  
        print("Try again!")