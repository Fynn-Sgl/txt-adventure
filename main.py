class Raum:
    def __init__(self, name, beschreibung, umschauen):
        self.name = name
        self.beschreibung = beschreibung
        self.verbindungen = {}
        self.umschauen = umschauen

kueche = Raum("Küche", "Es riecht etwas verdorben, in der Spüle liegt ein Teller mit Essensresten.", "Im Norden steht eine Tür offen, rechts ist eine Küchenzeile mit einem Herd und einem Kühlschrank, links ist eine Arbeitsfläche mit einem Messerblock. Es riecht sehr mies und es ist sehr unordentlich hier.")
flur_unten = Raum("Flur", "Der Flur ist dunkel und feucht, die Wände sind mit Schimmel bedeckt.", "Der Flur ist dunkel und Lang. Außer einer Tür nach Norden und ein im Süden gibt es noch eine Tür im Westen, die aber verschlossen ist.")
wohnzimmer = Raum("Wohnzimmer", "Das Wohnzimmer ist mit alten Möbeln vollgestellt, die Fenster sind mit dicken Vorhängen verdeckt.", "Es gibt eine Tür im Osten und im Süden. Durch die Fenster scheint leicht der Mond durch, aber es ist zu dunkel um etwas zu erkennen.")

kueche.verbindungen["norden"] = flur_unten
flur_unten.verbindungen["süden"] = kueche
flur_unten.verbindungen["norden"] = wohnzimmer
wohnzimmer.verbindungen["süden"] = flur_unten
#wohnzimmer.verbindungen["osten","o"] 

# Initialzustand
aktueller_raum = kueche 

while True:
    # 1. OUTPUT
    print(f"\nOrt: {aktueller_raum.name}")
    print(aktueller_raum.beschreibung)
    
    # 2. INPUT
    alias_map = {"n": "norden", "s": "süden", "o": "osten", "w": "westen", "north": "norden", "south": "süden", "east": "osten", "west": "westen"}
    user_input = input("> ").lower() # Kleinschreibung zur Fehlervermeidung
    befehl = alias_map.get(user_input, user_input) # Aliase auflösen, falls vorhanden

    # 3. UPDATE / TRANSITION
    if befehl == "quit" or befehl == "exit" or befehl == "q" or befehl == "ende" or befehl == "beenden":
        break

    if befehl == "help" or befehl == "?" or befehl == "h" or befehl == "hilfe":
        print("Mögliche Befehle: Norden(n), Süden(s), Osten(o), Westen(w), beenden(q), Hilfe(h), umschauen(l)")
        continue
        
    if befehl == "umschauen" or befehl == "look" or befehl == "l":
        print(aktueller_raum.umschauen)
        continue

    if befehl in aktueller_raum.verbindungen:
        aktueller_raum = aktueller_raum.verbindungen[befehl]
    else:
        print("Dort kannst du nicht hin gehen.")
    
