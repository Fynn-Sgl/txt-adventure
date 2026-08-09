class Raum:
    def __init__(self, name, beschreibung, umschauen):
        self.name = name
        self.beschreibung = beschreibung
        self.verbindungen = {}
        self.umschauen = umschauen

#ungenützte Räume
zelle = Raum("Zelle", "Du befindest dich in einer kleinen, dunklen Zelle. Es gibt nur eine Tür, die nach Norden führt.", "Die Wände sind aus grobem Stein und mit Moos bedeckt. Es gibt ein kleines Fenster hoch oben, durch das du den Mond sehen kannst. Es ist kalt und feucht hier.")
keller = Raum("Keller", "Der Keller ist dunkel und feucht, die Wände sind mit Schimmel bedeckt.", "Der Keller ist dunkel und Lang. Außer einer Tür nach Norden und eine nach einer alten Holztreppe befindlichen Tür im Süden gibt es noch eine Tür im Westen, die aber verschlossen ist.")

#Räume im Haus
kueche = Raum("Küche", "Es riecht etwas verdorben, in der Spüle liegt ein Teller mit Essensresten.", "Im Norden steht eine Tür offen, rechts ist eine Küchenzeile mit einem Herd und einem Kühlschrank, links ist eine Arbeitsfläche mit einem Messerblock. Es riecht sehr mies und es ist sehr unordentlich hier.")
flur_westen = Raum("Flur", "Der Flur ist dunkel und feucht, die Wände sind mit Schimmel bedeckt.", "Der Flur ist dunkel und Lang. Außer einer Tür nach Norden und ein im Süden gibt es noch eine Tür im Westen, die aber verschlossen ist.")
wohnzimmer = Raum("Wohnzimmer", "Das Wohnzimmer ist mit alten Möbeln vollgestellt, die Fenster sind mit dicken Vorhängen verdeckt.", "Es gibt eine Tür im Osten und im Süden. Durch die Fenster scheint leicht der Mond durch, aber es ist zu dunkel um etwas zu erkennen.")
flur_osten = Raum("Flur","","")
badezimmer = Raum("Badezimmer","","")
eingang = Raum("Eingang","","")
treppe_dachboden = Raum("Treppe zum Dachboden","","" ) 
treppe_keller = Raum("Treppe zum Keller","","" )
#endregion



#region Verbindungen
kueche.verbindungen["norden"] = flur_westen
flur_westen.verbindungen["süden"] = kueche

flur_westen.verbindungen["norden"] = wohnzimmer
wohnzimmer.verbindungen["süden"] = flur_westen 

flur_westen.verbindungen["osten"] = flur_osten
flur_osten.verbindungen["westen"] = flur_westen

flur_osten.verbindungen["norden"] = badezimmer
badezimmer.verbindungen["süden"] = flur_osten

flur_osten.verbindungen["süden"] = eingang
eingang.verbindungen["norden"] = flur_osten

# Initialzustand
aktueller_raum = kueche 

print("Du wachst in einem dunklen Raum auf. Es ist kalt und feucht, und du kannst kaum etwas sehen und dein Kopf dröhnt." \
"Es riecht nach Moder und Verfall, und du spürst eine unheimliche Präsenz in der Luft. Du weißt nicht, wie du hierher gekommen bist oder was dich erwartet, aber du weißt, dass du einen Weg finden musst, um zu entkommen.")

while True:
    # 1. OUTPUT
    print(f"\nOrt: {aktueller_raum.name}")#Gibt den aktuellen Raumnamen aus
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
    

#zum starten des Spieles in die Komandozeile eingeben: python main.py

#inventarmechanik hinzufügen
#zähler der aktionen trackt, am ende sagt wie lange du gebraucht hast und dir nach einer bestimmten zeit neue storry sachen einfallen.