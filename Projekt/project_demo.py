import random


### TEXT ADVENTURE GAME DEMO

# 🏕️ Intro
def intro():
    print("🌲 Willkommen im geheimnisvollen Wald!")
    player_name = input("Wie heißt du, Abenteurer:in? ")
    print(f"Hallo {player_name}, dein Abenteuer beginnt jetzt...\n")
    return player_name

# 🌲 Erste Entscheidung mit Zufallsereignis
def first_path():
    print("Du wachst auf einer Lichtung auf. Zwei Pfade führen in den dunklen Wald.")
    choice = input("Gehst du nach links oder rechts? (links/rechts): ").lower()

    if choice == "links":
        event = random.choice(["fox", "trap"])
        if event == "fox":
            print("\n🦊 Ein sprechender Fuchs taucht auf und bietet dir seine Hilfe an.")
            return "fox"
        else:
            print("\n💥 Eine Falle schnappt zu! Du verlierst etwas Energie.")
            return "trap"
    elif choice == "rechts":
        print("\n🌫️ Du betrittst einen nebligen Sumpf. Es ist schwer, etwas zu erkennen.")
        return "swamp"
    else:
        print("\n⚠️ Ungültige Eingabe. Versuch es nochmal.")
        return first_path()

# 🦊 Szene mit dem Fuchs
def fox_scene():
    print("Der Fuchs sagt: 'Ich kenne einen geheimen Pfad aus dem Wald heraus.'")
    answer = input("Vertraust du dem Fuchs? (ja/nein): ").lower()

    if answer == "ja":
        print("\n🎉 Der Fuchs führt dich sicher aus dem Wald. Du hast gewonnen!")
    elif answer == "nein":
        print("\n🙈 Du gehst alleine weiter und verirrst dich erneut.")
        return first_path()
    else:
        print("\n🦊 Der Fuchs schaut dich verwirrt an und verschwindet.")
        return first_path()

# 💀 Falle
def trap_scene():
    print("Du kämpfst dich aus der Falle und kehrst zur Lichtung zurück.")
    return first_path()

# 🛶 Szene im Sumpf
def swamp_scene():
    print("Du findest ein altes Boot am Ufer eines dunklen Sees.")
    choice = input("Willst du das Boot nehmen oder zurückgehen? (boot/zurück): ").lower()

    if choice == "boot":
        outcome = random.choice(["island", "storm"])
        if outcome == "island":
            print("\n🏝️ Das Boot bringt dich zu einer geheimnisvollen Insel. Fortsetzung folgt...")
        else:
            print("\n🌩️ Ein Sturm kommt auf und kentert das Boot. Game over.")
    elif choice == "zurück":
        print("\n🔁 Du kehrst zur Lichtung zurück.")
        return first_path()
    else:
        print("\n⚠️ Du zögerst zu lange. Die Sonne geht unter.")
        return swamp_scene()

# 🧭 Hauptfunktion
def start_game():
    player_name = intro()
    path = first_path()

    if path == "fox":
        fox_scene()
    elif path == "trap":
        trap_scene()
    elif path == "swamp":
        swamp_scene()

# ▶️ Spiel starten
start_game()
