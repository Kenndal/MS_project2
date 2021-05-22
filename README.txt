Projekt 2 MS - legacy stations

Topologia z labu 7 dla stacji xc
Dodane zostały legacy stations, tak że można zmieniać ich liczbę w zależności od liczby klastrów (będzie dodowane po jednej na klaster)
Max liczba legacy stations to liczba klastrów, np. jak są 3 layery to AP ax jest 19, wiec max liczba legacy station to 19, jak dasz więcej to nic się nie stanie (return 0 jest)


Ogólnie to wersja pierwsza działa. Stacje ax i legacy działają na w tym samym kanale, wiec wpływają na siebie.
Kanał i wpływ potwierdziłem pcapami, widać w ramkach że jest ta sama częstotliwość dla obu standardów.
Na ten moment 802.11ax działa na szerokości 80MHz, najniższy MCS (przy większych coś się psuło, nie spradzałem jeszcze).
Legacy staions działają na 802.11n, na szerokści 40 MHz, najniższy MCS.


Przykladowe wyniki i widoczny wpływ obu standarjdów jest widoczny na osiąganą przepustowość.


UWAGA: "aggregate area throughput" jest zbierany dla 802.11ax i dla 802.11n, to może być mylące


TODO: 
Spradzić jak zrobić to żeby RTS/CTS nie odpalał się na legacy stations
Spradzić jak ustawiać szerokość na legacy stations
Spradzić jak to działa przy rożnej liczbie "layerów, stacje 802.11ax i stacji legacy
Spradzić jak zbiera się csv
Spradzić dalej czy wyniki mają jakiś sens.
Ustalić dokładny scenariusz
Przygotować skrypty do odpalania automaycznie na labsimie
Przeparsować wyniki przed wtorkiem

Alternatywnie na wtorek można zebrać porównanie RTS/CTS = enable/disable
