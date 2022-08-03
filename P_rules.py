"""
Pravi igrač i n kompjutera igraju poker (svaki od njih je player). Špil ima 52 karte, različitih karata je 13, a različitih boja 4 (H, D, S,
C). Najjača karta je ona najveća u ruci (pod rukom se smatraju dvije vlastite karte i karte na stolu. As može vrijediti i kao najmanja i kao
najveća karta, ali ne u jednoj ruci. Par su dvije iste karte. Dva para su dvaput po dvije iste karte. Tris su tri iste karte. Skala je pet
karti po redu. Fleš je pet karti iste boje. Full house su par i tris, a njegova jačina se određuje prema jačini trisa. Poker su četiri iste
karte. Skala u flešu je skala u istoj boji. Royal fleš je skala od 10 do asa u istoj boji.

Listu karti u ruci složiti iz liste vrsta karti i boja, tako da je jedna karta jedna lista u listi karti.

Svatko ima prije određeni broj coinova.

Kod dijeljenja svatko dobiva dvije karte (hole cards).

Prvi dealer se određuje random, a zatim je svaki sljedeći onaj lijevo od njega. Lijevo od dealera (D) je small blind (SB, 1 coin - najmanji
mogući ulog), a lijevo od small blinda big blind (BB, 2 coina).

Pre-flop runda: igrač lijevo od big blindea može pratiti (call) prošlog igrača, dizati ulog (raise) barem za iznos prošlog raiseanja (za
prvi put je to BB) pa sve do ulaganja svega (all-in, ako igrač mora pratiti, a nema dovoljno, all-in se vrijedi kao da je pratio, a ako
netko all-ina, a drugi ima dovoljno, onda stavlja onoliko koliko je stavio onaj koji je najmanje all-inao, nakon što netko all-ina, svatko
ima opciju staviti dovoljno, all-inati ako nema dovoljno ili foldati, nakon toga oni koji nisu all-inali igraju normalno, a oni koji jesu
se preskaču jer oni čekaju (ako su ostala samo dva igrača i jedan je all-inao, a drugi odradio potez, onda se nema što dalje igrati) ili
spustiti karte (foldati). Kad prođe krug, a da nitko nije raiseao ili all-inao (vrati se red na onoga koji je zadnji raiseao ili all-inao),
kreće sljedeća runda. Na kraju runde, prije određivanja tko je pobijedio, svatko mora pokazati svoje karte. Kod foldanja treba složiti da
je random hoće li kompjuter kod foldanja pokazati karte ili ne. Foldati može bilo tko i bilo kad, bez obzira je li D, SB, BB ili prvi na
redu. Kad se all-ina, onda se pot fiktivno razlaže u main pot, kojeg čini ulog svakog igrača jednak ulogu onog koji je uložio najmanje
(njega mogu dobiti svi igrači), te prvi side pot, kojeg čini onaj višak do uloga jednakog drugom najmanjem ulogu (njema mogu osvojiti svi
koji imaju ulog jednak ili veći od toga) itd.; na kraju main pot i možda neki/neke side pot/potove dobije jedan igrač, sljedeći side pot
(ako ga ima) dobiva onaj igrač koji ima najbolje karte od onih koji su sudjelovali u tom side potu i tako dalje, sve dok ima side potova.
Ako netko na početku runde ima manje od BB-a (tj. standardno ne može pratiti), onda jedino može all-inati ili foldati. Ako su samo dva
igrača i jedan all-ina, a drugi ima dovoljno, onda nema smisla da on uloži više od onog koji je all-inao, što treba posložiti. SB-u i BB-u
se automatski uzima ulog prije prve runde.

Flop runda: tri karte se stavljaju na stol, koje svaki igrač može koristiti u ruci. U ovoj i svakoj sljedećoj rundi igrači mogu proslijediti
(checkati) umjesto calla ako još nitko nije ulagao toj rundi te betati umjesto raisea ako još nitko nije ulagao u toj rundi.

Turn runda: četvrta karta se stavlja na stol, a sve ostalo je isto kao i u prošloj rundi.

River runda: peta karta se stavlja na stol, a sve ostalo je isto kao i u prošloj rundi.

U zadnjoj rundi (round) je na stolu pet karti (community cards).

Na kraju svi pokažu karte i netko pobijedi, uzimajući sve uloženo (pot). Kreće nova partija (game; bez pitanja hoće li igrač novu partiju) s
preostalim coinovima.

Pita se hoće li se igrati novi meč (match)."""