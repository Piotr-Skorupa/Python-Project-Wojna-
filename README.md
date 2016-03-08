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
