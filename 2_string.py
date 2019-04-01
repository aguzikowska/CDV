tekst = "Anna, pawel, julIA"

lista = tekst.spli(", ")
print(tekst)
print(lista)
print(type(lista)) #list

imie1 = lista[0]
print(imie1) #Anna


imieDuze = imie1.upper()
print(imieDuze) #ANNA

imieMale = imie1.lower()
print(imieMale) #anna

#sprawdzenie zawartosci
print("/nPodaj swoje nazwisko:" , end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #True or False


nazwisko = ""
print(nazwisko.isalpha())  #False

tekst1 = "\nJulia\n"
tekst2 = "Nowak"
print(tekst1 + tekst2)

tekst1 = tekst1.rstrip() #usuwanie czegos tam
print(tekst1 + tekst2)
print (tekst1 + " " +tekst2)

#wyswietlenie lancucha znakow

#wszystkie wersje Phytona
text = "%s, Java i %s" % ("PHP" , "Phyton")
print(text)


#nowsze wersje Phytona >2.6
text = "{1}, Java i {0}".format("PHP" , "Phyton")
print(text)

#help(text.replace)

new = text.replace("PHP" , "C#")
print(new)

#wypisanie danych
rok = 2019
miesiac = "kwiecien"
dzien = 1

print("\nData:",end "")
print(dzien, miesac, rok)

print("\nData:",end "")
print(dzien, miesac, rok, sep="-")

print()


