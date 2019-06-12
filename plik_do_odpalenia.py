from tkinter import *
from tkinter import messagebox
import random
baza1=["Sprawdź to emipirycznie.","Amfetamina jest nieszkodliwa.","Jak kogni to tylko na UAM-ie.","Praca po kogni? Ja umiem wszystko.","Lubię palić marihuanę w nowych wcześniej nie znanych mi miejscach.","Meto to porażka.","Jasion to przemiła kobieta.","Idziesz na wykład do Grega?","Uczyłeś się na Algo? Bo ja będę ściągał chyba.","Niedługo będę was hackował.","Żałuję że nie było mnie na SSAK-U.","Zastanawiam się nad doktoratem z kogni.","Mariusz Urbański to klasa.","Nie zdałem meto.","Zdałem meto, mogę już umierać.","Toyota produkuje najlepsze samochody.","Pierwszy semestr na kogni jest sztosem.","Nie ulegał fałszywym heurystykom.","Tekst Loftus mnie rozwalił.","Opuścić zajęcia z Rasiem, to przypał.","Znam wszystkie rodzaje wnioskowań więc nie mów, że moje rozumowanie jest błędne.","Czy moglibyście wypełnić dla mnie ankietkę?","Nie mam czasu, uczę się na Meto.","Nie ogarniam SPSS-A.","Przeczytałeś teorię podwójnego kodowania Paivo.","Wolisz wcześniejszego czy późniejszego Wittgensteina.","Nie wyspałem się, ale mam dzisiaj wykład z Filo, więc sobie, to odbiję.","W 15 minut na Międzychodzką? Najwyżej się spóźnię.","Ty chodzisz na Algo czy na BPZ?","Dawaj do Zenona na piłeczkę, nie sprawdza nieobecności.","Co za farmazon mówił, że Zenon nie sprawdza nieobecności na w-fie?","Angielski z Kasprem, a komu to potrzebne.","Najwyżej wezmę warunek z PP?","A ten esej z Epi to na kiedy mamy zrobić?","O czym pisałeś esej z Epi?","Jakie jest twoje stanowisko w sporze o uniwersalia?","Pomożesz mi z MPK, bo nie ogarniam.","Ogarnę meto w jeden dzień.","Greg co gada.","Podobno warto iść na programowanie do Jukiego.","Podeślę Ci fajny filmik z Ted-a.","Język niemiecki? A komu to potrzebne.","Naming and grapsing common objects, to najlepszy artykuł jaki czytałem.","Ogarniamy w końcu tą prezentację na WDK? Jutro mamy deadline.","Tylko konceptualizm!","Tylko nominazim!","Lubię czytać Hume'a.","Robimy kogni obóz na Woodstock'u.","Czemu ja zapisałem się na w-f o ósmej to nie wiem.","Dlaczego ja zapisałem się na w-f na Morasko...","Dane neurofizjologiczne oraz neuropsychologiczne wspierają tezę, że w korze mózgowej naczelnych znajdują się dwa pasma projekcji wzrokowych: brzuszny strumień 'percepcyjny' oraz grzbietowy strumień 'działania'.","Najbardziej przekonującym dowodem na rzecz trafności hipotezy wyróżniającej dwa 'mózgi wzrokowe' jest pacjentka DF, która pomimo głębokich zaburzeń percepcji wzrokowej kształtu przedmiotów, potrafi wykorzystywać informacjębo kształcie w trakcie kontroli chwytu przedmiotów.","Iluzje zwodzą oko, a nie rękę.","Dowodem przemawiającym za istnieniem dwóch strumieni brzusznych była pacjentka DF, która cierpiała na agnozję wzrokową.",
"Afordancje to sposobności oddziaływania na obiekty środowiska, związane z ich charakterystykami oraz zdolnościami percepcyjnymi, doświadczeniem i ogólnymi ujmiejętnościami danej jednostki.",
"Pomysłodawcą teorii afrodancji był Gibson.","Słyszałeś o ślepowidzeniu?","Francis Bacon pragnął stworzyć z wiedzy narzędzie do realizowania praktycznych celów.","Zmysły ludzkie są z natury łatwe do pomylenia.","Ludzie próbują doapsować elementy do znanych wzorców.","Wybrałeś już po której stronie stoisz w sporze o uniwersalia?","Według Platona, kondcja człowieka przypomina stan ludzi przebywających w jaskini.","Platon podzielił świat na dwie warstwy - realną i idealną.","Każda idea ma swój odpowiednik realny.","Cienie idei, które dostrzegamy, to świat zjawisk.""Kwantyfikatory umożliwiają zapisanie zdań w krótszej formie.","W matematyce zdanie jest rozumiane jako wyrażenie, o którym można powiedzieć, że jest prawdziwe lub fałszywe.","Związek naszych świadomych wrażeń z tym, co dochodzi do kory wzrokowej z oka, jest strasznie mały.","Solipsyzm jest poglądem głoszącym, że istnieje tylko jednostkowy podmiot poznający, cała zaś rzeczywistość jest jedynie zbiorem jego subiektywnych wrażeń.","Jako podstawowe właściwości percepcji wymienia się recepcję sensoryczną i percepcję umysłową.","Kiedy opisujemy czyjeś spostrzeżenia, zakładamy równocześnie, że dana osoba nabywa przekonanie dotyczące tego, co jest akurat postrzegane.","Celem kognitywistyki jest całościowe spojrzenie na zagadnienie umysłu, tzn. zagadnienia poznania w ogóle (możliwości poznawcze, procesy empiryczn, strukturę myślenia), powstawania umysłu i funkcjonowania jego.","Niektóre informacje, które w danym momencie są poza naszą świadomością, mogą jednak być dostępne świadomości lub przynajmniej procesom poznawczym.","W habituacji, w miarę jak przyzwyczajamy się do danego bodźca, zaczynamy stopniowo coraz mniej zwracać na niego uwagę.","Cztery główne funkcje uwagi to: uwaga selektywna, czujność i detekcja sygnału, poszukiwanie oraz uwaga podzielna.","Miarą tendencji centralnej dla zmiennych nominalnych jest dominanta.","Mirą rozproszenia dla zmiennych porządkowych są kwartyle, odchylenia ćwiartkowe i pozycyjny współczynnik zmienności.","Opis statystyczny nie polega na przepisywaniu właściwych wartości z raportów SPSS.","Badanie zostało przeprowadzone według planu Solomona.","Szukam chętnych do badań! Wyślesz linka?","Aktywizacja pewnych schematów, idei, może mieć znaczący wpływ na zmianę naszego zachowania w sposób widoczny, a jednocześnie zupełnie przez nas nieuświadamiany.","Listy w języku Python to uporządkowane zbiory dowolnych obiektów, włączając w to inne listy.","Python posiada szereg wbudowanych metod do obsługi tekstu. m.in. string.","Człowiek zamknięty w Chińskim Pokoju jest odizolowany od świata zewnętrznego – trzeba więc mu umożliwić kontakt z otoczeniem, by mógł rozumieć i mieć inne stany umysłowe.","Logika to nauka o języku jako systemie znaków słownych.","Każde zdanie jest albo prawdziwe albo fałszywe.","Już Arystoteles...","LEMAAAAT","Istnieje również immaterialna odmiana idealizmu obiektywnego, ale ma ona charakter immanentny; jej autorem jest G. Berkeley.","Przedmioty materialne są dane za pośrednictwem ich reprezentacji (wrażeń) w umyśle, stąd nie możemy mówić o poznaniu źródłowym czy poznaniu wprost.",
"Czy spostrzegamy świat takim, jakim jest naprawdę, czy też, to jak go widzimy zależy od subiektywistycznej specyfiki naszych systemów zmysłowych i konstruktów umysłowych?",
"Problem umysł-ciało jest obecnie uważany za kluczowy w filozofii umysłu.","W eksperymencie Stroopa osoby badane mają określić kolor atramentu, którym napisano słowo i powstrzymać się przed przeczytaniem samego słowa.",
"Następnie badani decydowali, czy litera kontrolna była w prezentowanym zbiorze pokazana.","Percepcja odpowiada za odbieranie informacji z otoczenia.",
"Z badania wynika, że przeszukiwanie wzrokowe różni się od innych zachowań wizualnych.","Czy zdałeś już meto?","Pobrałeś już SPSSa?","Zaliczenie z filozofii jest ustne??!",
"A Pani jak sądzi?","Odczuwam niepokój filozoficzny.", "Sesja się zbliża... Dobrze, że metodologię zdałam w pierwszym terminie!", "Trzeba było iść na algorytmikę, mielibyście luz.", "Miałam już rekurencję na algorytmice! Wszystko jasne.", "Ale i tak nigdy nie zrozumiem o co chodzi Mareczkowi.", "Trzeba znać nazwiska?", "Masz ładne notatki?", "Szukam notatek z BPZ!", "Jak pobrać te prezentacje?", "Czy wy też macie problem z pobraniem tych prezentacji?", "Jakie to są zmienne interwałowe?"]

def przycisk1():
    lista=[]
    for i in range(int(pole_zdania.get())):
        baza=baza1[:]
        cytat=random.choice(baza)
        baza.remove(cytat)
        lista.append(cytat)
    rozwiazanie=''.join(lista)
    messagebox.showinfo("Wygenerowane zdania", rozwiazanie)

def przycisk2():
    lista=[]
    for i in range(int(pole_akapity.get())+1):
        for j in range(0,random.randint(3,15)):
            baza=baza1[:]
            cytat=random.choice(baza)
            baza.remove(cytat)
            lista.append(cytat+ " ")
    rozwiazanie=''.join(lista)
    messagebox.showinfo("Wygenerowane zdania", rozwiazanie)
def przycisk1():
    try:
        lista=[]
        baza=baza1[:]
        if len(baza1)<int(pole_zdania.get()):
            messagebox.showinfo("Wygenerowane zdania", "Nie mogę wygenerować takiej ilości zdań")
            pole_zdania.delete(0, 'end')
        else:
            for i in range(int(pole_zdania.get())):

                cytat=random.choice(baza)
                baza.remove(cytat)
                lista.append(cytat)
            rozwiazanie=''.join(lista)
            messagebox.showinfo("Wygenerowane zdania", rozwiazanie)
            pole_zdania.delete(0, 'end')
    except ValueError:
        pole_zdania.delete(0, 'end')
    except IndexError:
        pole_zdania.delete(0, 'end')
def przycisk2():
    try:
        lista=[]
        baza=baza1[:]
        if int(pole_akapity.get())>8 or int(pole_akapity.get())<1:
            messagebox.showinfo("Wygenerowane akapity", "Nie mogę wygenerować takiej ilości akapitów")
            pole_akapity.delete(0, 'end')
        else:
            for i in range(int(pole_akapity.get())+1):
                for j in range(0,random.randint(3,15)):
                    cytat=random.choice(baza)
                    baza.remove(cytat)
                    lista.append(cytat+ " ")
                if i==1:
                    None
                else:
                    lista.append('\n\n')
            rozwiazanie=''.join(lista)
            messagebox.showinfo("Wygenerowane akapity", rozwiazanie)
            pole_akapity.delete(0, 'end')
    except ValueError:
        pole_akapity.delete(0, 'end')
    except IndexError:
        pole_akapity.delete(0, 'end')
def akcjaZrob ():
    messagebox.showinfo("Kontakt","Biuro Kogni-ipsum \n Mickiewicza 4/12 \n 61-233 Poznań \n adres e-mail:kogniipsum@poczta.pl")
def akcjaAutor ():
    messagebox.showinfo("Twórcy","Autorzy: \n Kzysztof Dziedzina \n Alicja Kowalczyk \n Natalia Skreczko \n Amelia Szostak")
def akcja_O_nas ():
    messagebox.showinfo("Nasza firma","Jesteśmy nowoczesną firmą tworzącą zaawansowane projekty w szybkim czasie. Używamy sprzętu najlepszej jakości i dbamy o dobro naszego klienta. W naszym biurze zawsze panuje przyjemna atmosfera.")


okno=Tk()
okno.title("Kogni-ipsum")
okno.geometry("600x300")
pasekMenu=Menu(okno)


opcjeMenu=Menu(pasekMenu,tearoff=0)
pasekMenu.add_cascade(label="Opcje",menu=opcjeMenu)
opcjeMenu.add_command(label="Wyjdź",command=okno.quit)
pomocMenu=Menu(pasekMenu,tearoff=0)
pasekMenu.add_cascade(label="Pomoc",menu=pomocMenu)
pomocMenu.add_command(label="Kontakt z nami",command=akcjaZrob)
kontaktMenu=Menu(pasekMenu,tearoff=0)
pasekMenu.add_cascade(label="Autorzy",menu=kontaktMenu)
kontaktMenu.add_command(label="O Autorach",command=akcjaAutor)
kontaktMenu.add_command(label="Więcej o nas...",command=akcja_O_nas)


####
zdania = Label(okno, text="Wprowadź ilość zdań")
zdania.grid(row=2,column=0)
przycisk_zdania=Button(okno, text = "Generuj zdania", command = przycisk1, bg="DarkSlateBlue", fg="gold")
przycisk_zdania.grid(row=2,column=2)
pole_zdania= Entry(okno)
pole_zdania.grid(row=2,column=1)
####
akapity = Label(okno, text="Wprowadź ilość akapitow")
akapity.grid(row=3, column=0)
pole_akapity= Entry(okno)
pole_akapity.grid(row=3,column=1)
przycisk_akapity=Button(okno, text = "Generuj akapity", command = przycisk2, bg="DarkSlateGray", fg="gold")
przycisk_akapity.grid(row=3, column=2)
okno.config(menu=pasekMenu)
okno.mainloop()
