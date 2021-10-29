import os
os.system("cls")
inleiding = False
stukje_intro = False
stukje_1 = False
stukje_2 = False
stukje_3 = False
stukje_4 = False
stukje_5 = False
stukje_6 = False
stukje_7 = False
stukje_8 = False
stukje_9 = False
stukje_10 = False
stukje_11 = False
stukje_12 = False
stukje_13 = False
stukje_14 = False
stukje_15 = False
stukje_16 = False
stukje_17 = False
stukje_18 = False
stukje_19 = False
stukje_20 = False
stukje_21 = False
stukje_22 = False
stukje_23 = False
stukje_24 = False
stukje_25 = False
stukje_26 = False
stukje_27 = False
stukje_28 = False
stukje_29 = False
stukje_30 = False
einde_1 = False
einde_2 = False
einde_3 = False
einde_4 = False
einde_5 = False
einde_6 = False
einde_7 = False
spellteje = False


#intro 
print("Welkom bij het keuzeverhaal: Jongen van de bodem.")
print("Je krijgt zodirect stukjes tekst te zien die het verhaal verteld.")
print("Daarna krijg je twee keuzes, A of B. De keuzes die jij maakt hebben invloed op het verhaal.")
print("Laten we beginnen!")
print("(druk op enter om verder te gaan)")
Druk_op_enter_1 = input(">>>")
print("")

inleiding = True
spelletje = True
#inleiding

while spelletje == True:
    os.system("cls")
    
    while inleiding == True:
        print("Inleiding,")
        print("")
        print("Dit verhaal werkt iets anders dan de meeste verhalen, in de zin dat jij hierin de hoofdrol speelt.")
        print("Hoe je door het verhaal heenwerkt valt te vergelijken met een quest op RuneScape.")
        print("(druk op enter om verder te gaan)")
        Druk_op_enter_1 = input(">>>")
        print("")
        stukje_intro = True
        inleiding = False
    

#Stukje_intro
    while stukje_intro == True:
        print("Het is een lange, moeizame dag geweest, je bent uit en staat op het schoolplein")
        print("Je word gebeld door een anonieme nummer,")
        print("Je denkt bij je zelf wie kan dit zijn?")
        print("Je besluit om...")
        print("")
        print("  A. Negeren.")
        print("  B. Opnemen.")
        Antwoord_1 = input(">>>")
    
        if Antwoord_1 == "A":
            stukje_1 = True
            stukje_intro = False
        
        elif Antwoord_1 == "B":
            stukje_2 = True
            stukje_intro = False

        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
    
#Stukje_1
    while stukje_1 == True:
        print("Je besluit om te negeren en naar huis te gaan. ")
    
        Antwoord_1 = input(">>>")
    
        if Antwoord_1 == "A":
            einde_1 = True
            stukje_1 = False
        

        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#Stukje_2
    while stukje_2 == True:
        print("Je neemt op en zegt hallo.")
        print("")
        print("Je hoort een bekende stem het is Spijker")
        print("")
        print("Je moet een kleine bezorging doen voor hem zegt Spijker")
        print("")
        print("Je ...")
        print("  A. Doet het niet.")
        print("  B. Neemt de klus aan")
        Antwoord_2 = input(">>>")
        if Antwoord_2 == "A":
            einde_1 = True
            stukje_2 = False
        
        elif Antwoord_2 == "B":
            stukje_3 = True
            stukje_2 = False

        else:
            
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#Stukje_3
    while stukje_3 == True:
        print("Een paar uur later ")
        print("")
        print("Tzz Tzz..")
        print("")
        print("Je hebt een bericht van Spijker")
        print("Je hebt de locatie gekregen het is in de buurt")
        print("")
        print("Je pakt de scooter en gaat er naar toe")
        print("Je komt aan bij een pleintje, Je ziet in de verte de jongen staan")
        print("")
        print("Je loopt naar ze toe, je herkent ze maar hun jou niet")
        print("")
        print("Je had ruzie met de jongen in blauw")
        print("")
        print("Je ...")
        print("  A. Spreekt de jongen in blauw aan")
        print("  B. Geeft het pakketje en gaat weg")
        Antwoord_3 = input(">>>")
        if Antwoord_3 == "A":
            stukje_4 = True
            stukje_3 = False
        elif Antwoord_3 == "B":
            stukje_5 = True
            stukje_3 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#stukje_4
    while stukje_4 == True:
        print("Je spreekt hem aan")
        print("Ewah je was die boy die biggie deed he vorige keer")
        print("")
        print("De jongen in blauw zegt:")
        print("Waar heb je het over a sah")
        print("")
        print("Je zegt:")
        print("Je deed stoer tegen de concierge van OverY")
        print("De jongen in blauw zegt:")
        print("Ja en dan, hij deed als een flikker")
        print("")
        print("Je zegt")
        print("Die concierge is mijn vader")
        print("Je...")
        print("")
        print("  A. Grijpt hem bij ze kraag en bedrijgt hem en pakt het geld")
        print("  B. Waarschuwd hem")
        Antwoord_4 = input(">>>")
        if Antwoord_4 == "A":
            stukje_7 = True
            stukje_4 = False
        elif Antwoord_4 == "B":
            stukje_8 = True
            stukje_4 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#stukje_5
    while stukje_5 == True:
        print("Je zegt:")
        print("Ewah bro, hier heb die pakje")
        print("Hij pakt het aan en geeft je een envelop")
        print("Je knikt en loopt weg")
        stukje_6 = True
        stukje_5 = False

#stukje_6
    while stukje_6 == True:
        print("Je belt Spijker op en zegt dat je het pakketje hebt")
        print("")
        print("Spijker zegt:")
        print("Aii goed bezig ik stuur je locatie waar je het moet brengen")
        print("")
        print("Je zegt: oke")
        print("")
        print("SPijker: Als je er bent heb ik nog een klus voor je ben je daarvoor in?")
        print("")
        print("Je zegt...")
        print("")
        print("  A. Ja toch")
        print("  B. No man heb het druk")
        Antwoord_6 = input(">>>")
        if Antwoord_6 == "A":
            stukje_9 = True
            stukje_6 = False
        elif Antwoord_6 == "B":
            stukje_10 = True
            stukje_6 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
# Stukje_7
    while stukje_7 == True:
        print("Je pakt hem bij ze kraag")
        print("Je zegt:")
        print("Luister a sukkel je gaat respect tonen tegen me vader he")
        print("Geef me die dokoe nuu NUU")
        print("")
        print("Jongen in blauw zegt:")
        print("Is goed sorry sorry")
        stukje_11 = True
        stukje_7 = False

# Stukje_8
    while stukje_8 == True:
        print("Kijk doe nog 1x keer zo tegen me pa")
        print("Jongen in Blauw zegt: Wat dan")
        print("Wat dan? Dan gaan we matten")
        print("Hier pak het")
        print("Je geeft het pakje")
        print("Hij geeft je geld")
        print("")
        print("  A. Je kiest ervoor om jezelf eerst te laten smokkelen en daarna je moeder en zusjes")
        print("  B. Je kiest er niet voor om gesmokkeld te worden en jullie gaan te voet naar de grens")
        stukje_6 = True
        stukje_8 = False
#--------------------------------------------------------



#stukje_10
    while stukje_10 == True:
        print("Je krijgt locatie van Spijker.")
        print("Na een uur in de bus te zitten kom je aan")
        print("Je bedenkt je in de bus dat je weg kan met het geld ")
        print("Je twijfelt")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je geeft hem het geld.")
        print("  B. Je houd het geld.")
        Antwoord_10 = input(">>>")
        if Antwoord_10 == "A":
            stukje_12 = True
            stukje_10 = False
        elif Antwoord_10 == "B":
            stukje_13 = True
            stukje_10 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
# stukje_11
    while stukje_11 == True:
        print("Spijker belt je")
        print("Tzz Tzzz")
        print("Je neemt op je zegt:")
        print("Yo")
        print("Spijker zegt:")
        print("Heb je dat pakketje geleverd?")
        print("Je zegt ja")
        print("Spijker: Goed bezig")
        print("Spijker: Ik stuur je locatie kom daar naartoen over 10 min")
        einde_2 = True
        stukje_11 = False

#stukje_12
    while stukje_12 == True:
        print("Je komt aan bij de locatie")
        print("Je loopt naar binnen")
        print("Je ziet Spijker")
        print("Spijker: Ewah je bent er goed")
        print("Je geeft hem het geld")
        print("Spijker: Lekker bezig broertje")
        print("Je hoort een auto's met sirene  die richting jullie komen")
        print("Spijker: Jallah kom kom weg hier")
        print("Spijker: Kom je mee of niet?")
        print("Je...")
        print("")
        print("  A. gaat met Spijker mee")
        print("  B. gaat in je eentje weg")
        Antwoord_12 = input(">>>")
        if Antwoord_12 == "A":
            stukje_14 = True
            stukje_12 = False
        elif Antwoord_12 == "B":
            stukje_15 = True
            stukje_12 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
#stukje_13
    
    while stukje_13 == True:
        print("Je blijft zitten in de bus")
        print("Je belt de politie ")
        print("Je geeft ze locatie en je zegt dat ze rustig naar binnen moeten")
        print("")
        print("Paar uur later")
        print("")
        print("Je ziet op het nieuws dat er mensen zijn opgepakt")
        print("")
        print("Je word gebeld door een onbekend nummer")
        print("Je neemt op")
        print("Spijker: Je bent dood")
        print("Hij hangt op")
        print("Je...")
        print("")
        print("  A. blijft in je stad")
        print("  B. vlucht naar België")
        Antwoord_13 = input(">>>")
        if Antwoord_13 == "A":
            stukje_16 = True
            stukje_13 = False
        elif Antwoord_13 == "B":
            stukje_17 = True
            stukje_13 = False 
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#Stukje_14
    while stukje_14 == True:
        print("Je rent met Spijker mee")
        print("Spijker: snel snel stap in")
        print("Spijker: rij rij! we gaan ze kwijt raken ")
        print("Er zitten 4 auto's achter ons aan zeg je")
        print("Spijker: Geen probleem")
        print("Jullie worden geklapt van de zijkant er was nog een auto aan het wachten")
        print("Jullie crashen tegen een paal aan")
        print("Je word wakker in een cel")
        print("De deur gaat open een politie man zegt mee komen")
        print("Paar uur later zitten jullie in een rechtzaal")
        print("Er word gepraat maar je lette niet op")
        print("Je zag Spijker naast je zitten")
        print("De rechter vraagt wat jullie daar deden")
        print("Je...")
        print("")
        print("  A. verteld de waarheid")
        print("  B. zwijgt")
        Antwoord_14 = input(">>>")
        if Antwoord_14 == "A":
            stukje_18 = True
            stukje_14 = False
        elif Antwoord_14 == "B":
            einde_5 = True
            stukje_14 = False 
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#stukje_15
    while stukje_15 == True:
        print("Je gaat in je eentje weg ")
        print("Politie gingen een achtervolging aan met de auto waar Spijker in zat")
        print("")
        print("Paar uur later")
        print("")
        print("Je ziet op het nieuwe dat er mensen zijn opgepakt bij een auto crash tijdens een achtervolging")
        print("Je zegt tegen je zelf dat je gelukkig niet met hun bent mee gegaan")
        stukje_18 = True
        stukje_15 = False

    #stukje_16
    while stukje_16 == True:
        print("Je blijft in je stad")
        print("")
        print("Paar weken later")
        print("")
        print("Je loopt door je wijk er stopt een busje naast je")
        print("Er springen mannen er uit die gemaskerd zijn en je word ontvoerd")
            einde_3 = True
            stukje_16 = False


    #stukje_17
    while stukje_17 == True:
        print("Je vlucht naar België")
        einde_4 = True
        stukje_17 = False

    #stukje_18
    while stukje_18 == True:
        print("Je word gebeld door een onbekende nummer")
        print("Je hoort Spijker")
        print("Spijker: Ewah broertje, je moet me helpen man ")
        print("Spijker: Kan je oogje houden op me buit bij driehoek? ")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je hangt op en negeert")
        print("  B. Je gaat een oogje houden.")
        Antwoord_18 = input(">>>")
        if Antwoord_18 == "A":
            einde_1 = True
            stukje_18 = False
        elif Antwoord_18 == "B":
            stukje_19 = True
            stukje_18 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    #stukje_19
    while stukje_19 == True:
        print("Je besluit een oogje op driehoek te houden")
        print("")
        print("Volgende dag")
        print("")
        print("Je komt aan bij driehoek")
        print("Je loopt naar binnen en gaat naar achter in een kamertje")
        print("Je loopt naar beneden")
        print("Je ziet een wietplantge")
        print("")
        print("Je...")
        print("  A. checkt alles en gaat weg")
        print("  B. blijft en gaat de planten onderhouden.")
        Antwoord_19 = input(">>>")
        if Antwoord_19 == "A":
            stukje_20 = True
            stukje_18 = False
        elif Antwoord_19 == "B":
            stukje_21 = True
            stukje_18 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
     
    # stukje_20
    while stukje_20 == True:
        print("Je checkt alles ")
        print("Tempratuur is goed ")
        print("Je geeft de planten beetje water ")
        print("Je vertrekt")
        einde_7 = True
        stukje_20 = False



    #stukje 21
    while stukje_21 == True:
        print("Je bent gebleven")
        print("Je hoort sirene's")
        print("Shit skotoe")
        print("Je wilt naar buiten gaan maar ze zijn al binnen")
        print("Je word aangehouden bij de wietplantage")
        print("")
            einde_6 = True
            stukje_21 = False


    #einde1
    while einde_1 == True:
        print("Je besluit om naar huis te gaan")
        print("")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E1 = input(">>>")
        if Antwoord_E1 == "A":
            inleiding = True
            einde_1 = False
        elif Antwoord_E1 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_1 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    while einde_2 == True:
        print("Je komt aan op de locatie.")
        print("Je ziet Spijker en die jongen in blauw")
        print("Ewah goed dat je er bent zegt Spijker")
        print("Weet je wie dit is?")
        print("Je zegt nee")
        print("Spijker: dit is me broertje")
        print("Spijker: Je hebt hem geript toch of niet?")
        print("Je zegt: Ja, omdat hij me pa vorige keer had uitscholden voor homo")
        print("Spijker: Jou vader boeit mij niet oke")
        print("Spijker: loopt weg")
        print("Je zegt nee nee eyy!")
        print("2 mannen lopen op je af met een pistool")
        print("Hij schreeuwd op je knieën")
        print("Je gaat op je knieën")
        print("BAM")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E2 = input(">>>")
        if Antwoord_E2 == "A":
            inleiding = True
            einde_2 = False
        elif Antwoord_E2 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_2 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    while einde_3 == True:
        print("De zak over je hoofd word er afgehaald")
        print("Je ziet Spijker.")
        print("Spijker: je hebt me genaaid he")
        print("Spijker: weet je wat we met naaiers doen?")
        print("Spijker: pakt een pistool er bij")
        print("DIT DOEN WE! BAM")
        print("")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E3 = input(">>>")
        if Antwoord_E3 == "A":
            inleiding = True
            einde_3 = False
        elif Antwoord_E3 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_3 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
        
    while einde_4 == True:
        print("Je komt aan bij je familie in België")
        print("Je gaat daar blijven slapen")
        print("")
        print("paar weken later")
        print("")
        print("Je vraagt als je er mag blijven wonen")
        print("Dat mag en je zegt dat je ook een baan gaat zoeken")
        print("")
        print("paar jaar later")
        print("")
        print("Je word prof boxer en koopt een eigen huis")
        print("Happy end")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E4 = input(">>>")
        if Antwoord_E4 == "A":
            inleiding = True
            einde_4 = False
        elif Antwoord_E4 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_4 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
    
    while einde_5 == True:
        print("Je besluit te zwijgen")
        print("Je krijgt 5 jaar celstraf")

        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E4 = input(">>>")
        if Antwoord_E4 == "A":
            inleiding = True
            einde_5 = False
        elif Antwoord_E4 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_5 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

        while einde_6 == True:
        print("Je bent in de rechtzaal")
        print("Je ziet Spijker vrij in de tribune hij lacht naar je")
        print("Rechter: Je word veroordeeld tot illigaale drugs verkoop")
        print("Rechter: Je krijgt 5 jaar celstraf")

        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E4 = input(">>>")
        if Antwoord_E4 == "A":
            inleiding = True
            einde_5 = False
        elif Antwoord_E4 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_6 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

        while einde_7 == True:
        print("Je besluit om een nieuwe start te nemen")
        print("Je stapt uit de onderwereld")
        print("Je begint met boxen")
        print("En je word prof boxer")
        print("Einde!")

        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E4 = input(">>>")
        if Antwoord_E4 == "A":
            inleiding = True
            einde_7 = False
        elif Antwoord_E4 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_7 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue