import time
import random

# Global variabel för att hålla reda på spelarens framsteg
current_room = None
difficulty = "medium"  # Global variabel för att hålla reda på svårighetsgraden

def choose_difficulty():
    global difficulty
    print("\nVälj svårighetsgrad:")
    print("1. Lätt")
    print("2. Medium")
    print("3. Svår")

    choice = input("Välj ett alternativ (1/2/3): ")

    if choice == "1":
        difficulty = "easy"
    elif choice == "2":
        difficulty = "medium"
    elif choice == "3":
        difficulty = "hard"
    else:
        print("Ogiltigt val. Försök igen.")
        choose_difficulty()

def main_menu():
    print("\n*** Välkommen till 'Fly från fängelsen'! ***\n")
    print("1. Börja spelet")
    print("2. Instruktioner")
    print("3. Avsluta")

    choice = input("Välj ett alternativ (1/2/3): ")

    if choice == "1":
        choose_difficulty()
        start_game()
    elif choice == "2":
        show_instructions()
    elif choice == "3":
        print("\nTack för att du spelade 'Fly från fängelsen'! Hej då!")
    else:
        print("Ogiltigt val. Försök igen.")
        main_menu()

def show_instructions():
    filnamn = "instruktioner.txt"

    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            innehåll = fil.read()
            print(innehåll)
            tryck_på_valfri_tangent()
    except FileNotFoundError:
        print(f"Filen {filnamn} hittades inte.")
        tryck_på_valfri_tangent()
    except Exception as e:
        print(f"Ett fel inträffade: {e}")
        tryck_på_valfri_tangent()

def tryck_på_valfri_tangent():
    input("\nTryck på valfri tangent för att återgå till huvudmenyn...")
    main_menu()

def start_game():
    global current_room
    current_room = cell_room
    print("\n*** Spelet börjar! ***\n")
    print("Du vaknar i en mörk fängelsecell. Du har 24 timmar på dig att fly innan vakterna flyttar dig till ett högsäkerhetsfängelse.")
    time.sleep(2)
    cell_room()

def cell_room():
    global current_room
    current_room = cell_room
    print("\nRum: Fängelsecellen")
    print("Vad vill du göra?")
    print("1. Undersöka sängen")
    print("2. Undersöka väggen")
    print("3. Kalla på vakten")

    choice = input("Välj ett alternativ (1/2/3): ")

    if choice == "1":
        print("\nDu hittar en lös skruv under sängen. Detta kan vara användbart.")
        time.sleep(2)
        corridor_room(tool=True)
    elif choice == "2":
        print("\nDu hittar en svag punkt i väggen, men du behöver ett verktyg för att göra något.")
        time.sleep(2)
        corridor_room(tool=False)
    elif choice == "3":
        print("\nVakten misstänker dig och håller extra koll. Du måste vara snabb!")
        time.sleep(2)
        corridor_room(tool=False)
    else:
        print("Ogiltigt val. Försök igen.")
        cell_room()

def corridor_room(tool):
    global current_room
    current_room = lambda: corridor_room(tool)
    print("\nRum: Korridoren")
    print("Du har lyckats ta dig ut ur cellen och befinner dig nu i en lång korridor.")
    print("Vad vill du göra?")
    print("1. Smyga förbi vakter")
    print("2. Försöka hitta ett förråd")
    print("3. Gå in i vaktrummet")

    choice = input("Välj ett alternativ (1/2/3): ")

    if choice == "1":
        success_chance = {"easy": 0.8, "medium": 0.5, "hard": 0.2}[difficulty]
        if random.random() < success_chance:
            print("\nDu smyger förbi vakterna utan att bli upptäckt.")
            laundry_room(tool)
        else:
            print("\nEn vakt upptäcker dig. Du fångas och förs tillbaka till cellen.")
            restart_from_last_checkpoint()
    elif choice == "2":
        print("\nDu hittar ett förråd med användbara föremål.")
        laundry_room(tool)
    elif choice == "3":
        guard_room(tool)
    else:
        print("Ogiltigt val. Försök igen.")
        corridor_room(tool)

def laundry_room(tool):
    global current_room
    current_room = lambda: laundry_room(tool)
    print("\nRum: Tvätteriet")
    print("Du befinner dig nu i tvätteriet. Här finns det många gömställen.")
    print("Vad vill du göra?")
    print("1. Gömma dig i en tvättkorg")
    print("2. Leta efter något användbart")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        print("\nDu gömmer dig i en tvättkorg och väntar tills vakterna går förbi.")
        kitchen_room(tool)
    elif choice == "2":
        print("\nDu hittar en uniform som kan hjälpa dig att smälta in.")
        kitchen_room(tool)
    else:
        print("Ogiltigt val. Försök igen.")
        laundry_room(tool)

def kitchen_room(tool):
    global current_room
    current_room = lambda: kitchen_room(tool)
    print("\nRum: Köket")
    print("Du går in i ett kök där vakterna brukar äta.")
    print("Vad vill du göra?")
    print("1. Gömma dig i skafferiet")
    print("2. Försöka stjäla nycklar från en vakt")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        print("\nDu gömmer dig och lyckas undvika vakterna.")
        garage_room(tool)
    elif choice == "2":
        success_chance = {"easy": 0.8, "medium": 0.5, "hard": 0.2}[difficulty]
        if random.random() < success_chance:
            print("\nDu lyckas stjäla nycklarna utan att bli upptäckt.")
            garage_room(tool)
        else:
            print("\nVakterna upptäcker dig. Du fångas.")
            caught_by_guard()
    else:
        print("Ogiltigt val. Försök igen.")
        kitchen_room(tool)

def guard_room(tool):
    global current_room
    current_room = lambda: guard_room(tool)
    print("\nRum: Vaktrummet")
    print("Du smyger in i vaktrummet och ser en uniform och ett nyckelkort. För att öppna skåpet med dem, måste du lösa en ekvation.")
    answer = input("Lös: 12 + 8 × 2 = ")
    if answer == "28":
        print("\nRätt! Du tar uniformen och nyckelkortet. Nu kan du röra dig fritt utan att vakterna misstänker dig!")
        laundry_room(tool)
    else:
        print("\nFel svar! Du hinner inte öppna skåpet innan du hör steg utanför. Du lämnar rummet snabbt.")
        restart_from_last_checkpoint()

def garage_room(tool):
    global current_room
    current_room = lambda: garage_room(tool)
    print("\nRum: Garaget")
    print("Du står nu i garaget, där det finns fordon att använda för flykten.")
    print("Vad vill du göra?")
    print("1. Försöka starta en bil")
    print("2. Leta efter en gömd väg ut")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        if tool:
            print("\nDu använder verktygen för att starta bilen och kör iväg. Du är fri!")
            end_game(success=True)
        else:
            print("\nDu kan inte starta bilen utan verktyg. Vakterna hinner ikapp dig.")
            end_game(success=False)
    elif choice == "2":
        print("\nDu hittar en gömd väg som leder ut ur fängelset. Du är fri!")
        end_game(success=True)
    else:
        print("Ogiltigt val. Försök igen.")
        garage_room(tool)

def caught_by_guard():
    print("\nVakten fångar dig och spelet är över.")
    end_game(success=False)

def end_game(success):
    if success:
        print("\n*** Grattis! Du lyckades fly från fängelset! ***\n")
    else:
        print("\n*** Du misslyckades med att fly. Bättre lycka nästa gång! ***\n")
    play_again = input("Vill du spela igen? (ja/nej): ")
    if play_again.lower() == "ja":
        main_menu()
    else:
        print("Tack för att du spelade 'Fly från fängelsen'! Hej då!")

def restart_from_last_checkpoint():
    print("\nDu har förlorat, men du kan återuppta från ditt senaste val.")
    time.sleep(2)
    current_room()

# Starta spelet
main_menu()
