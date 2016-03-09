# Python-Project-Wojna-
Gra karciana - Wojna 
##SPECYFIKACJA PROGRAMU
###Wstęp
"Wojna" to gra karciana, do której powstania posłuży język Python 2.7. Jak wiadomo jest to gra, która od gracza wymaga jedynie 
wykładania kart i opiera się głównie na szczęściu, dlatego zastosowany zostanie system losowania kart. Zasady gry można 
zobaczyć na stronie: https://pl.wikipedia.org/wiki/Wojna_(gra_karciana)
###Opis ogólny
Projekt będzie wykorzystywał bibliotekę Pygame służącą do produkcji gier. Wykorzystam graficzny interfejs. Do zapisu gry używana będzie baza danych SQLite
###Założenia
1. Program będzie wierną kopią gry karcianej "Wojna", czyli będzie się opierał na jej zasadach
2. Graficzny wygląd kart na tle zielonego stołu
3. Grę będzie można przerwać i po ponownym włączeniu gry kontynuować rozgrywkę. Rozpoczęcie nowej gry usunie stary zapis
4. Przed rozgrywką użytkownik będzie musiał podać swoje imię
5. Wynik zostanie zapisany do tabeli wyników (wygrana lub przegrana), w tabeli będzie tez imię gracza, numer rozgrywki oraz data
6. Powstanie Menu główne gry , które bedzie zawierać:"Nowa Gra","Kontynuuj","Wyniki","O Autorze","Wyjście"
7. Gra zostanie udźwiękowiona przy użyciu własnych dźwięków wykonanych w programie "FL Studio 12"
8. Szata graficzna ograniczy się do prostych podstawień grafik, bez zastosowania płynnych animacji

###Opis przypadków użycia
####Ekran Główny:
1. Po włączeniu gry ukaże się ekran główny zawierający menu(zawartość powyżej). Użytkownik będzie mógł wybrać odnośnik poprzez kliknięcie myszą.
2. Na samej górze będzie nazwa aplikacji

####Nowa Gra:
1. Po kliknięciu na nową grę, użytkownikowi pojawi się ekran w którym będzie mógł wpisać swoje imię i zatwierdzić przyciskiem "Ok" lub powrócić , wciskając "Powrót"
2. Po zaakceptowaniu imienia pojawi sie właściwy ekran rozgrywki
3. W lewym dolnym rogu bedzie widoczna talia gracza. Natomiast  w prawym górnym komputera
4. Kliknięcie na talie gracza spowoduje wyłozenie karty na stół (środek ekranu) oraz automatyczne wyłozenie karty komputera
5. Karty zostaną porównane według  zasady starszeństwa kart i wygrywająca karta zostanie podkreślona niebieską linia.
6. Obok tali gracza który wygrał utworzy sie nowa kupka z zebranymi kartami.
7. Gry skoncza sie karty kupka znika i na jej miejsce przechodzi druga kupka i tak w kółko az komuś nie skończą sie karty
8. Zależnie od wyniku na koniec gry pojawi sie komunikat "Wygrałeś" albo "Przegrałeś" pod komunikatem przycisk "Ok"
9. Naciśnięcie przycisku spowoduje przeniesienie do tabeli wyników.

####Tabela Wyników:
1. 
