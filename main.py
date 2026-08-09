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
flur_osten = Raum("Flur", "Der östliche Flur ist eng und schlecht beleuchtet. Die Tapeten hängen lose von den Wänden, und der Boden knarrt bei jedem Schritt.", "Du siehst eine Tür nach Norden zum Badezimmer, eine Tür nach Süden zum Eingang und eine offene Verbindung nach Osten zum Dachboden. Spinnweben hängen in den Ecken und der Duft von Staub liegt in der Luft.")
badezimmer = Raum("Badezimmer", "Das Badezimmer ist feucht und schimmelig, mit einer kaputten Lampe über dem Waschbecken.", "Der Spiegel ist zerbrochen und auf dem Boden liegen Scherben. Eine rostige Badewanne steht in der Ecke, der Abfluss ist verstopft und Wasserflecken ziehen sich die Fliesen hinauf.")
eingang = Raum("Eingang", "Der Eingangsbereich ist kalt und zugig, die halb geöffnete Haustür schlägt leise im Wind.", "In einer Ecke steht ein umgestürzter Schirmständer, die Garderobe ist leer. Vor der Tür liegt nasser Matsch, und der Weg führt weiter in Richtung Norden in den Flur.")
dachboden = Raum("Dachboden", "Der Dachboden ist voll mit alten Kisten und verstaubten Möbeln. Das einzige Licht fällt durch ein kleines Dachfenster.", "Überall liegen Spinnweben, und die Luft ist trocken und abgestanden. Du hörst das leise Knarren der Holzbalken, wenn du dich bewegst. Eine Leiter führt zurück in den Flur.")
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

flur_osten.verbindungen["osten"] = dachboden
dachboden.verbindungen["westen"] = flur_osten

flur_westen.verbindungen["westen"] = keller
keller.verbindungen["osten"] = flur_westen




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
#System bauen, dass erkennt wo du schon warst und dann im umschautext sagt wo welcher Weg hinführt