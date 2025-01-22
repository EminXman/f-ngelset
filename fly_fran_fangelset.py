import time
import random

def main_menu():
    print("\n*** Välkommen till 'Fly från fängelsen'! ***\n")
    print("1. Börja spelet")
    print("2. Instruktioner")
    print("3. Avsluta")

    choice = input("Välj ett alternativ (1/2/3): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        show_instructions()
    elif choice == "3":
        print("\nTack för att du spelade 'Fly från fängelsen'! Hej då!")
    else:
        print("Ogiltigt val. Försök igen.")
        main_menu()

def show_instructions():
    print("\n*** Instruktioner ***\n")
    print("'Fly från fängelsen' är ett textbaserat äventyrsspel. Utforska rum, lös gåtor och ta kloka beslut för att lyckas fly.")
    print("Du kommer att möta utmaningar och hinder. Tänk strategiskt för att vinna!")
    input("\nTryck på Enter för att återgå till huvudmenyn.")
    main_menu()

def start_game():
    print("\n*** Spelet börjar! ***\n")
    print("Du vaknar i en mörk fängelsecell. Du har 24 timmar på dig att fly innan vakterna flyttar dig till ett högsäkerhetsfängelse.")
    time.sleep(2)
    cell_room()

def cell_room():
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
    print("\nRum: Korridoren")
    print("Du har lyckats ta dig ut ur cellen och befinner dig nu i en lång korridor.")
    print("Vad vill du göra?")
    print("1. Smyga förbi vakter")
    print("2. Försöka hitta ett förråd")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        if random.choice([True, False]):
            print("\nDu smyger förbi vakterna utan att bli upptäckt.")
            armory_room(tool)
        else:
            print("\nEn vakt upptäcker dig. Du fångas och förs tillbaka till cellen.")
            caught_by_guard()
    elif choice == "2":
        print("\nDu hittar ett förråd med användbara föremål.")
        armory_room(tool)
    else:
        print("Ogiltigt val. Försök igen.")
        corridor_room(tool)

def armory_room(tool):
    print("\nRum: Förrådsrummet")
    print("Du ser flera verktyg och en dörr som leder vidare.")
    print("Vad vill du göra?")
    print("1. Ta ett rep och en kofot")
    print("2. Gå vidare utan att ta något")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        print("\nDu tar med dig verktygen. Dessa kan komma till nytta senare.")
        kitchen_room(has_tools=True)
    elif choice == "2":
        print("\nDu lämnar förrådet utan att ta något.")
        kitchen_room(has_tools=False)
    else:
        print("Ogiltigt val. Försök igen.")
        armory_room(tool)

def kitchen_room(has_tools):
    print("\nRum: Köket")
    print("Du går in i ett kök där vakterna brukar äta.")
    print("Vad vill du göra?")
    print("1. Gömma dig i skafferiet")
    print("2. Försöka stjäla nycklar från en vakt")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        print("\nDu gömmer dig och lyckas undvika vakterna.")
        garage_room(has_tools)
    elif choice == "2":
        if random.choice([True, False]):
            print("\nDu lyckas stjäla nycklarna utan att bli upptäckt.")
            garage_room(has_tools)
        else:
            print("\nVakterna upptäcker dig. Du fångas.")
            caught_by_guard()
    else:
        print("Ogiltigt val. Försök igen.")
        kitchen_room(has_tools)

def garage_room(has_tools):
    print("\nRum: Garaget")
    print("Du står nu i garaget, där det finns fordon att använda för flykten.")
    print("Vad vill du göra?")
    print("1. Försöka starta en bil")
    print("2. Leta efter en gömd väg ut")

    choice = input("Välj ett alternativ (1/2): ")

    if choice == "1":
        if has_tools:
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
        garage_room(has_tools)

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

# Starta spelet
main_menu()

