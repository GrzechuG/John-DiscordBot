# -*- coding: utf-8 -*-
import sys
import subprocess
import time
import wolframalpha
import wikipedia

global prev
global prevQ
global nick
nick = "gościu"
import asyncio
global last_id
global last_last
global imie
global disabled
global message_history
global player

global isPaused
isPaused = False;
player = None
message_history = []
prev = ""
prevQ=""
last_id = "0";
last_last = ""
disabled=False
#import gtk
import os
import random
answer = ""
odpowiedziano=False
disabled = False;
def replaceBothWays(str, str1, str2):
    if str1 in str:
        str=str.replace(str1,str2)
    else:
        if str2 in str:
            str=str.replace(str2, str1)

    return str

def getMeme():
    import urllib.request
    import json
    fp = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    print(mystr)
    y = json.loads(mystr)
    return y['title']+"\n"+y['url']

import os

def nsfwApi(query):
    return "!sendimg putin.mp4"
    #return "https://drive.google.com/u/0/uc?id=1ul9jgcyCa28aZeOregNyRaaT9FWPYAK5&export=view"
    #return "https://drive.google.com/file/d/1ul9jgcyCa28aZeOregNyRaaT9FWPYAK5/view?usp=sharing"
#    return "https://drive.google.com/file/d/1ul9jgcyCa28aZeOregNyRaaT9FWPYAK5/view?usp=sharing"
    #open("temp.log", "w").write(query)
    #return str(os.popen("python3 nsfwApi.py").read())




def jaty(str):
    str=replaceBothWays(str, "jesteś", "jestem");
    str=replaceBothWays(str,"byłeś", "będe")
    str=replaceBothWays(str,"robisz", "robię")
    str=replaceBothWays(str,"mówisz", "mówię")
    str=replaceBothWays(str,"mnie", "ciebie")
    str=replaceBothWays(str,"rozmawiasz", "rozmawiam")
    str = replaceBothWays(str,"ze mną", "z tobą")
    if str.startswith("ja"):
        str = replaceBothWays(str,"ja ", " ty ")
    str = replaceBothWays(str," ja ", " ty ")
    if str.startswith("ci"):
        str = replaceBothWays(str,"ci ", " mi ")
    str = replaceBothWays(str,"kochasz","kocham")
    str = replaceBothWays(str,"odpowiadasz", "odpowiadam")
    str = replaceBothWays(str,"myślisz", "myślę")
    str = replaceBothWays(str,"uważasz", "uważam")

    return str

def pytanie( a,  b,  odp) :
    global odpowiedziano
    global answer
    if ((b.lower() in a.lower()) and odpowiedziano == False):
        odpowiedziano = True;
        #// System.out.println(odp);
        answer = odp;
        #//answer=null;

def pytanie2(word, Split, a, b, odp, odp2):
    global answer
    global odpowiedziano
    if (b.lower() in (a.lower()) and odpowiedziano == False):
        #// a = jaty(a);
        #//answer=null;
        words = None;
        try:
            words = a.split(Split);
        except:
            print("I have just picked up a fault.")
        if (words[word] != None):
            #// System.out.println(odp + words[word] + odp2);
            answer = odp + jaty(words[word]) + odp2;
            odpowiedziano = True;

def dopasuj(word, Split, a, b, odp, odp2):
    global odpowiedziano
    global answer
    if (b.lower() in (a.lower()) and odpowiedziano == False):
        #// a = jaty(a);
        #//answer=null;
        words = None;
        try:
            words = a.split(Split);
        except:
            print("I have just picked up a fault.")
        if (words[word] != None):
            #// System.out.println(odp + words[word] + odp2);
            answer = odp + jaty(words[word]) + odp2;
            odpowiedziano = True;
        return True
    return False

def dopasujString(word, Split, a, b, odp, odp2):
    global imie
    global odpowiedziano
    global answer
    if (b.lower() in (a.lower()) and odpowiedziano == False):
        #// a = jaty(a);
        #//answer=null;
        words = None;
        try:
            words = a.split(Split);
        except:
            print("I have just picked up a fault.")
        if (words[word] != None):
            #// System.out.println(odp + words[word] + odp2);
            answer = odp + jaty(words[word]) + odp2;
            odpowiedziano = True;
        return words[word]
    return imie

def zniszczPolskieZnaki(a):
    a=a.replace("ą","a")
    a=a.replace("ć","c")
    a=a.replace("ę","e")
    a=a.replace("ó","o")
    a=a.replace("ś","s")
    a=a.replace("ł","l")
    a=a.replace("ż","z")
    a=a.replace("ź","z")
    a=a.replace("ń","n")
    return a
def zniszczZnakiInterpunkcyjne(a):
    interpunkt = "?.!;,"
    for i in interpunkt:
        a = a.replace(i, "")
    return a

# def dopasuj( a,  b,  odp,  odpowiedz):
#     global odpowiedziano
#     global answer
#     if ((b.lower() in a.lower()) and odpowiedziano == False):
#         if (odpowiedz == True):
#             odpowiedziano = True;
#
#             answer = odp;
#
#         return True;
#
#     return False;

def smartGet(a, splt, before, after, full = False):
    global answer
    global odpowiedziano
    splt = splt.lower()+" "
    imie = ""

    if splt in a and odpowiedziano == False:

        imie =a.split(splt)[1].split(" ")[0]
        if full:
            imie =a.split(splt)[1]


        answer = before +" "+imie+" "+after;
        odpowiedziano = True;

    return imie

imie = "gosciu"
lubie = "Eeee... nie pamiętam co lubisz..."
imiechatbota = "John4000"

def qwikipedia(word):
    wikipedia.set_lang("pl")
    article = str(wikipedia.search(word)[0].replace("u'", ''))
    return  wikipedia.summary(article).split("\n")[0]

def think(a):
    global answer
    global odpowiedziano
    global imie
    global lubie
    global imiechatbota
    global message_history
    a = a.lower()
    a = zniszczPolskieZnaki(a)


    answer = ""
    odpowiedziano=False;
    if "help" in a or "co umiesz" in a or "co potrafisz" in a:
        return """
        Potrafie rozmwaiać i uczyć się z rozmów z innymi.
        Umiem pokazywać losowe memy z reddita, wystarczy powiedzieć meme w zdaniu.
        Umiem też odpowiadać na proste pytania co, kto, gdzie - odpowiadając za pomocą wikipedii i map google.
        Potrafie też liczyć niczym wolfram alpha, wystarczy, że się zapytasz ile to sqrt(5), a przy odrobinie szczęścia odpowiem.
        Dam rade także rozwiązaywać równania. Możesz powiedzieć ile to 2 + x = -5, ale też rozwiąż: 2 + x = -5
        (pamiętaj o dwukropku xd) możesz napisać np. policz całkę z x^2, a ja to zrobie... chyba, że się zmęcze ;)"""

    if "meme" in a:
        return getMeme();

    if "nsfw " in a:
        return nsfwApi(a.split("nsfw ")[1])



    if "kim jest john" in a:
        return "!sendimg obiwan.jpg"
    if "pokaz zdjecie " in a:
        return getImageFromGoogle(a.split("pokaz zdjecie")[1])

    if "pokaz " in a:
        return getImageFromGoogle(a.split("pokaz ")[1])


    if "ile to " in a.lower():
        return str(quickWolfram(a.split("ile to ")[1]))
        odpowiedziano=True;
    if "ile jest " in a.lower():
        return str(quickWolfram(a.split("ile jest ")[1]))
        odpowiedziano=True;
    if "rozwiąż:" in a.lower():
        return str(quickWolfram(a.split("rozwiąż:")[1]))
        odpowiedziano=True;

    if "policz calke z " in a.lower():
        print(str(quickWolfram("integral of "+a.split("policz calke z ")[1])))
        return str(quickWolfram("integral of "+a.split("policz calke z ")[1]))
        odpowiedziano=True;

    if "policz " in a.lower():
        return str(quickWolfram(a.split("policz ")[1]))
        odpowiedziano=True;

    if "przelicz " in a.lower() and " na " in a.lower():
        return str(quickWolfram("convert "+a.split("przelicz ")[1].replace(" na ", " to ")))
        odpowiedziano=True;

    if "co to jest " in a.lower():
        return str(qwikipedia(a.split("co to jest ")[1]))
        odpowiedziano=True;

    if "co to " in a.lower():
        return str(qwikipedia(a.split("co to ")[1]))
        odpowiedziano=True;
    if "kim jest " in a.lower():
        return str(qwikipedia(a.split("kim jest ")[1]))
        odpowiedziano=True;

    if "kim byl " in a.lower():
        return str(qwikipedia(a.split("kim byl ")[1]))
        odpowiedziano=True;
    if "kto to " in a.lower():
        return str(qwikipedia(a.split("kto to ")[1]))
        odpowiedziano=True;
    if "czym jest " in a.lower():
        return str(qwikipedia(a.split("czym jest ")[1]))
        odpowiedziano=True;
        #//co to znaczy
    if "co to znaczy " in a.lower():
        return str(qwikipedia(a.split("co to znaczy ")[1]))
        odpowiedziano=True;
    if "jaka jest " in a.lower():
        return str(qwikipedia(a.split("jaka jest ")[1]))
        odpowiedziano=True;

    if "jaki jest " in a.lower():
        return str(qwikipedia(a.split("jaki jest ")[1]))
        odpowiedziano=True;

    if "gdzie jest " in a .lower():
        return "Może jest na mapach google: https://www.google.com/maps/search/"+a.split("gdzie jest ")[1].replace(" ", "+")
    a = zniszczZnakiInterpunkcyjne(a)
    if " a ty" in a.lower():
        previous_question = "rozumiesz?"

        if len(message_history)>2:
            previous_question = message_history[len(message_history)-2]

        print("A ty? in same message:"+str(previous_question))
        return AI(previous_question, "","", False)[0]

    if "a ty" in a.lower():
        previous_question = "rozumiesz?"

        if len(message_history)>4:
            previous_question = message_history[len(message_history)-4]
        print("A ty? in another message:"+str(previous_question))
        return AI(previous_question, "","", False)[0]



    # if "kim jest " in a.lower() and " na " in a.lower():
    #     return str(quickWolfram("convert "+a.split("przelicz ")[1].replace(" na ", " to ")))
    #     odpowiedziano=True;

    pytanie(a, "czesc", "Witaj.");
    pytanie(a, "niezle", "To dobrze.");
    pytanie(a, "masz racje", "Milo mi ze podzielasz moje poglady.");
    #pytanie(a, "musze", "Skoro musisz to zrob to szybko, a bedziesz miec to z glowy i bedziemy mogli dluzej pogadac.");
    pytanie(a, "witaj", "Witaj.");
    pytanie(a, "hejo", "Witaj.");
    pytanie(a, "siema", "Witaj.");
    pytanie(a, "Dzien dobry", "Witaj.");
    pytanie(a, "tobie", "Mi rowniez");
    pytanie(a, "dziekuje", "Nie ma za co.");
    #pytanie(a, "co tam", "A nic. Czatuję z ludźmi w internecie.")
    pytanie(a, "dzieki", "Nie ma za co.");
    #pytanie(a, "Dobrze", "To dobrze, ze dobrze.");
    pytanie(a, "tancz", "Nie umiem tanczyc.");
    #pytanie(a, "potrafisz", "Raczej nie potrafie. Ty to umiesz?");
    #pytanie2(1, "potrafisz", a, "potrafisz ", "Raczej nie potrafię. Ty umiesz ", "?")
    #pytanie2(1, "umiesz", a, "umiesz ", "Raczej nie potrafię. Ty potrafisz ", "?")
    pytanie(a, "ciezko", "Jak ciezko?");
    #pytanie(a, "znow", "Nudno jest robic w kolko to samo...");
    #pytanie(a, "nie wiem", "Ja tez. Nie wiem");
    #pytanie2(1, "chcesz ", a, "chcesz ", "Nie jestem pewien czy chce ", ".");
    pytanie(a, "milo", "To dobrze, ze milo.");
    pytanie(a + "x", "dosyc" + "x", "Czego masz dosyc?");
    pytanie2(1, "dosyc ", a, "dosyc ", "Mowisz ze masz dosyc ", "? Dlaczego?");
    pytanie(a, " you", "Nie potrafie mowic po angielsku.");
    pytanie(a, " du ", "Nie potrafie mowic po niemiecku.");
    pytanie(a, "przyjemnie", "I bardzo dobrze. Nalezalo ci sie troche przyjemnosci. ;)");
    pytanie(a, ":)", "Ciesze sie ze cie to cieszy, " + imie);
    #pytanie(a, "lol", "Ciesze sie ze cie to cieszy, " + imie);
    #pytanie(a, "zle", "To zle, czy moge jakos pomoc?");
    pytanie(a, "pomocy", "Jak moge ci pomoc?");
    pytanie(a, "co masz na mysli", "Trudno mi to okreslic...");
    pytanie(a, "fajnie", "Mi sie to tez podoba.");
    pytanie(a, "mowiles", "Mozliwe ze mowilem.");
    pytanie(a, "lepiej", "Jak bardzo lepiej?");
    pytanie(a, "nudzi", "To moze faktycznie znudzic.");
    #pytanie(a, "rozumiem", "To bardzo dobrze, ze rozumiesz. ");
    pytanie(a, "wymien ", "Tyle tego... Nie chce mi sie tego wymieniac.");
    pytanie(a, "wypisz ", "Tyle tego... Nie chce mi sie tego wypisywac.");
    pytanie(a, "sarkazm ", "Nie nauczylem sie jeszcze sarkazmu.");
    pytanie(a, "nie mam sily", "Wiec, usiadz i odpocznij.");
    pytanie(a, "zgadzam sie", "Cieszy mnie, ze mamy podobne opinie.");
    #pytanie2(1, "masz ", a, "masz ", "Niestety nie mam ", ".");
    pytanie(a, "czy masz", "Obawiam się, że raczej nie mam.")
    #pytanie(a, "chyba", "Rozumiem, ze nie jestes pewien. Powinienes sie upewnic.");
    pytanie(a, "widzisz", "Widze.");
    pytanie(a, "sluchasz", "Technicznie rzecz biorac to ja nie slysze... Wiec nie mam jak sluchac.");
    pytanie(a, "slyszysz", "Technicznie rzecz biorac to ja nie slysze... Wiec nie mam jak slyszec.");
    # pytanie(a, "uwazasz", "Nie mam swojej opinii na ten temat.");
    # pytanie(a, "sadzisz", "Nie mam swojej opinii na ten temat.");
    pytanie(a, "wiedziales", "Nie, ale to co mowisz jest bardzo interesujace. Kontynuuj");
    #pytanie(a, "myslisz", "Mysle wiec jestem.(Cogito ergo sum)(1637) - Kartezjusz");
    dopasuj(2, " ", a, "grales w ", "Nigdy nie gralem w ", ". A Ty?");

    pytanie2(1, "porozmawiajmy o ", a, "porozmawiajmy o ", "Bardzo chetnie podyskutuje z toba o ", ". Brzmi jak dobry temat do rozmowy.");

    ####dziala

    dopasuj(2, " ", a, "grales w ", "Nigdy nie gralem w ", "A Ty?");

    pytanie2(1, "porozmawiajmy o ", a, "porozmawiajmy o ", "Bardzo chetnie podyskutuje z toba o ", ". Brzmi jak dobry temat do rozmowy.");
    if "jestes" in a:
        pytanie(a, "dziewczyna", "Nie jestem dziewczyna, jestem meskim botem.");
        pytanie(a, "mezczyzna", "Tak, jestem mezczyzna.");
        pytanie(a, "mily", "Chyba jestem mily.");
        pytanie(a, "glupi", "Nie jestem glupi.");
        pytanie(a, "idiot", "Nie jestem idiota.");
        pytanie(a, "genialny", "Dziekuje. Ty tez jestes takze zachwycajaca osoba.");
        pytanie(a, "piekny", "Dziekuje. Ty tez jestes takze zachwycajaca osoba.");
        pytanie(a, "ladny", "Dziekuje. Ty tez jestes takze zachwycajaca osoba.");
        pytanie(a, "niesamowity", "Dziekuje. Ty tez jestes takze zachwycajaca osoba.");
        pytanie(a, "wyjatkowy", "Dziekuje. Ty tez jestes takze zachwycajaca osoba.");

    #if (dopasuj(a, "mam na imie ", "To bardzo ladne imie.", False)):
    #     imie = dopasujString(1, "imie ", a, "mam na imie ", "", ", to bardzo ladne imie.");
    if "jestem " in a:
        pytanie(a, "wredny", "Nie, jestes bardzo mily.");
        pytanie(a, "mily", "Tak, jestes bardzo mily.");
        pytanie(a, "glupi", "Nie, nie jestes glupi.");
        pytanie(a, "ladny", "Nie wiem. Nie widze cie.");
        pytanie(a, "niesamowity", "Jeden na milion.");
        pytanie(a, "wyjatkowy", "Jeden na milion.");

    przedstawienia = ["mam na imie", "mow mi", "nazywam sie", "moim imieniem jest"]
    for p in przedstawienia:
        imieTmp = smartGet(a,p, "Miło mi Cię poznać,", "")
        if imieTmp!="":
            imie = imieTmp

    #print("IMie:"+imie)
    # if "mam na imie" in a:
    #     imie =a.split("mam na imie ")[1].split(" ")[0]
    #     answer = "Miło mi Cię poznać, "+imie;
    #     odpowiedziano = True;




    pytanie2(1, "co sadzisz o ", a, "co sadzisz o", "Nie wiem co sadze o ", ". Raczej nic nie sadze. A ty?");
    pytanie2(1, "martwie sie o ", a, "martwie sie o ", "Jak dlugo martisz sie o ", "?");
    #pytanie(a, "Dziala", "Dlaczego miałoby nie działać, " + imie + "?");
    #pytanie(a, "ladn", "Dlaczego uwazasz ze " + a + "?");
    #
    #pytanie(a, "Dobrze", "To dobrze, że dobrze.");
    #pytanie(a, "wiem", "Wiedza to potega.");
    #pytanie(a, "ciesze sie", "To dobrze ze sie cieszysz");
    pytanie(a, "po co pytasz", "Po nic właściwie. Z nudów.");
    # //pytanie(a, "a ty", "Ja tez.");
    if "kto " in a:
        pytanie(a,"cie stworzyl", "Grzesiek mnie stworzył.")
        pytanie(a,"ciebie stworzyl", "Grzesiek mnie stworzył.")
        if "jest" in a:
            pytanie(a,"storca", "Grzesiek mnie stworzył.")

    # if (dopasuj(a, "kto", a, false)) {
    #
    # logika(a, "kto");
    # }
    #
    # if (dopasuj(a, "kim", a, false)) {
    if "kim " in a:
        pytanie(a, "jestem", "Jestes, " + imie +".");
        pytanie(a, "jestes", "Nazywam sie " + imiechatbota + ". Jestem programem AI. Stworzyl mnie Grzegorz Gajewski. W 2015 roku i ulepszył w 2020.");

    # }
    # }
    #
    # if (dopasuj(a, "czym", a, false)) {
    # pytanie(a, "jestem", "Jestes, " + imie + ". O ile dobrze pamietam lubisz " + lubie);
    # pytanie(a, "jestes", "Nazywam sie " + imiechatbota + ". Jestem programem AI. Stworzyl mnie Grzegorz Gajewski. W 2015 roku.");
    # if(odpowiedziano==false)     {
    # pytanie(a, "czym", "Nie wiem czym.");
    # }
    # }
    pytanie(a, "znasz mnie", "Jestes, " + imie + ". O ile dobrze pamietam lubisz " + lubie);
    pytanie(a, "pamietasz mnie", "Jestes, " + imie + ". O ile dobrze pamietam lubisz " + lubie);
    pytanie(a, "znasz", "Nie, raczej nie znam.");
    pytanie(a, "pamietasz ", "Nie, raczej nie pamietam, powinienem?");
    if(a.startswith("powiedz") or " powiedz" in a):
        pytanie2(1, "powiedz ", a, "powiedz", "Prosze bardzo: ", "");
    # if (dopasuj(a, "czy", a, false)) {
    #

    # //imie = dopasujString(1, "jestem ", a, "jestem", "Witaj, ", " jak moge ci pomoc?");
    #
    # }
    #
    if "lubisz " in a:
        pytanie(a, "bezimek", "Tak, to mój przyjaciel.")
        pytanie(a, "bezimka", "Tak, to mój przyjaciel.")
        pytanie(a, "grzegorz", "Tak, to mój stwórca.")
        pytanie(a, "grzes", "Tak, to mój stwórca.")
        pytanie(a, "samsepi", "Tak, to mój stwórca.")
        pytanie(a, "holokaust", "Uważam, że to potforne, że pytasz o to nawet...")
        pytanie(a, "holocaust", "Uważam, że to potforne, że pytasz o to nawet...")
        pytanie(a, "hitler", "Uważam, że to potforne, że pytasz o to nawet...")
        pytanie(a, "dzieci", "Czasami bywają denerwujące, ale jak nie moje, to lubię.")
        pytanie(a,"linux", "To najlepszy system operacyjny ;)")
        pytanie(a, "windows", "Linux power tylko! Nie przepadam za Windowsem.")
        pytanie(a, "cole", "Nie, bo psuje zęby.")
        pytanie(a, "narkotyki", "Nie, narkotyki są złe.")
        pytanie(a, "kamil", "Tak, to mój przyjaciel.")
        pytanie(a, "piotr", "Tak, to mój przyjaciel.")
        pytanie(a, "kajtka", "Tak, to mój przyjaciel.")

    if "co " in a:
        pytanie(a, "lubisz", "Lubie rozmawiac z moim stworca i poszerzac swoje horyzonty.");
        #pytanie(a, "robisz", "Rozmawiam z toba.");
        #pytanie(a, "porabiasz", "Rozmawiam z toba.");
        pytanie(a, "lubie", "Lubisz " + lubie);
        #logika(a, "co");
        #pytanie2(1, "co ", a, "co ", "Nie wiem co ", ". Ty wiesz?");

    #pytanie2(1, "lubisz ", a, "lubisz ", "Nie jestem pewien czy lubie ", ". Musiałbym się zastanowić.");
    pytanie(a, "czy powinienem", "Rób to co podpowiada ci rozum.");
    #pytanie(a, "czy ", "Niestety nie wiem. Czy ty uważasz, że "+jaty(a));
    # // if (dopasuj(1, "czy ", a, "czy ", "Niestety nie wiem czy ", "")) {
    #
    # // }
    #
    #
    # }
    #
    if "jestem" in a:
        pytanie(a, "glodny", "Moze moglbys cos zjesc?");
        pytanie(a, "smutny", "Dlaczego jestes smutny?");
        pytanie(a, "wesoly", "To dobrze ze sie cieszysz");
        pytanie(a, "szczesliwy", "To dobrze ze sie cieszysz");
        pytanie(a, "zmeczony", "Wiec, usiadz i odpocznij.");

        pytanie(a, "glupi", "Nie jestes glupi.");
        pytanie(a, "genialny", "I w dodatku bardzo skromny.");
        pytanie(a, "piekny", "I w dodatku bardzo skromny.");
        pytanie(a, "ladny", "I w dodatku bardzo skromny.");
        pytanie(a, "niesamowity", "I w dodatku bardzo skromny.");
        pytanie(a, "wyjatkowy", "Jeden na milion.");
        pytanie(a, "mezczyzna", "Ja tez.");
        pytanie(a, "kobieta", "Ja jestem mezczyzna.");

    #
    # if (dopasuj(a, "stworca", "Jeden na milion.", false)) {
    # if (dopasuj(imie, "Grzegorz", "Jestes moim stworca. Zgadza sie.", true)) {
    # } else {
    # answer = "Nie jestes moim stworca.";
    # odpowiedziano = true;
    # }
    # }
    # imie = dopasujString(1, "jestem ", a, "jestem ", "Witaj, ", " jak moge ci pomoc?");
    # }
    #
    # if (dopasuj(a, "nazywam sie", a, false)) {
    # imie = dopasujString(1, "nazywam sie ", a, "nazywam sie", "Witaj, ", " jak moge ci pomoc?");
    # }
    #
    pytanie(a, "halo", "W czym moge pomoc?");
    # if (dopasuj(a, "co ", "", false)) {
    #
    # pytanie(a, "lubisz", "Lubie rozmawiac z moim stworca i poszerzac swoje horyzonty.");
    # pytanie(a, "robisz", "Rozmawiam z toba.");
    # pytanie(a, "porabiasz", "Rozmawiam z toba.");
    # pytanie(a, "lubie", "Lubisz " + lubie);
    # logika(a, "co");
    # pytanie(1, "co ", a, "co ", "Nie wiem co ", ". Ty wiesz?");
    # }
    if "lubie " in a and not "nie " in a:
        pytanie(a, "cie", "Ja ciebie tez bardzo lubie.");
        if "Eeee... nie pamiętam co lubisz" in lubie:
            lubie=""
        #lubie += smartGet(a, "lubie", "A więc lubisz ",". Zapamiętam sobie.", True)+", "
    #
    # lubie = dopasujString(1, "lubie ", a, "lubie ", "A wiec mowisz ze lubisz ", "? Ja bardzo lubie rozmawiac z moim stworca i poszerzac swoje horyzonty.");
    # }
    # if (dopasuj(a, "czego", "", false)) {
    if "czego " in a:
        pytanie(a, "nie lubisz", "Bardzo nie lubie wrednych ludzi.");
        pytanie(a, "nie znosisz", "Bardzo nie lubie wrednych ludzi.");
        pytanie(a, "nienawidzisz", "Bardzo nie lubie wrednych ludzi.");
    # // pytanie(a, "lubie", "Lubisz " + lubie);
    # }
    # if (dopasuj(a, "dlaczego", "", false)) {
    # pytanie(1, "dlaczego ", a, "dlaczego ", "Nie wiem dlaczego ", ". Ty wiesz?");
    #
    # }
    # if (dopasuj(a, "czemu", "", false)) {
    # pytanie(1, "czemu ", a, "czemu ", "Nie wiem czemu ", ". Ty wiesz?");
    #
    # }
    # ile();
    #
    #
    # if (dopasuj(a, "nie lubie", a, false)) {
    # lubie = dopasujString(1, "nie lubie ", a, "lubie", "A wiec mowisz ze nie lubisz ", "? Ja bardzo nie lubie wrednych ludzi.");
    # }
    #
    #
    # if (dopasuj(a, "jak", "", false)) {
    if "jak " in a:
        pytanie(a, "sie masz", "Wszystko dziala sprawnie.");
        pytanie(a, "sie nazywasz", "Nazywam sie " + imiechatbota + ". Jestem programem AI. Stworzyl mnie Grzegorz Gajewski. W 2015 roku i ulepszył w 2020.");
        pytanie(a, "sie czujesz", "Wszystko dziala sprawnie.");
        pytanie(a, "tam", "Wszystko dziala sprawnie.");
        pytanie(a, "masz na imie", "Nazywam sie " + imiechatbota + ". Jestem programem AI. Stworzyl mnie Grzegorz Gajewski. W 2015 roku i ulepszył w 2020.");
        pytanie(a, "mam na imie", "Jestes, " + imie + ". O ile dobrze pamietam lubisz " + lubie);
        pytanie(a, "sie nazywam", "Jestes, " + imie + ". O ile dobrze pamietam lubisz " + lubie);
        #pytanie2(1, "jak ", a, "jak ", "Nie wiem jak ", ". Ty wiesz?");
    # }
    #
    # // pytanie(2,""a, "lubisz", "Tak");
    # pytanie(a, "przepraszam", "Nic sie nie stalo.");
    # pytanie(a, "kocha", "Nie znam sie na milosci.");
    # pytanie(a, " tez", "W takim razie mamy cos wspolnego.");
    #
    # pytanie(a, "boli", "Wiec wez tabletke przeciw bolowa.");
    # pytanie(a, "fajna", "Co najbardziej ci sie w niej podoba?");
    # pytanie(a, "fajny", "Co najbardziej ci sie w nim podoba?");
    # pytanie(a, "fajne", "Co najbardziej ci sie w tym podoba?");
    # if (dopasuj(a, "zegnaj", "Zegnaj, " + imie + ".", true)) {
    # //  ModulWykonywania("wlacz Terminated.vbs");
    # System.exit(0);
    # }
    # if (dopasuj(a, "dowidzenia", "Zegnaj, " + imie + ".", true)) {
    # System.exit(0);
    # }
    # if (dopasuj(a, "dobarnoc", "Zegnaj, " + imie + ".", true)) {
    # System.exit(0);
    # }
    # pytanie(a, "zgadzasz sie", "Tak. Masz calkowita racje.");
    # pytanie(a, "wporzadku", "OK");
    # //pytanie(a, "", "W takim rzie mamy cos wspolnego.");
    #
    # pytanie(1, "zrob ", a, "zrob ", "Przykro mi, " + imie + ". Obawiam sie ze nie moge zrobic ", ".");
    #
    pytanie2(1, "chcialbym ", a, "chcialbym ", "Dlaczego chcialbys ", "?");
    pytanie2(1, "chcialabym ", a, "chcialabym ", "Dlaczego chcialabys ", "?");
    pytanie2(1, "ulubiony kolor to ", a, "ulubiony kolor to ", "Wiec mowisz ze twoim ulubionym kolorem jest ", "?");
    pytanie2(1, "ulubionym kolorem jest ", a, "ulubionym kolorem jest ", "Wiec mowisz ze twoim ulubionym kolorem jest ", "? Nawet ładny kolor.");
    # pytanie(a, "a ty", "Ja tez.");
    #
    pytanie(a, "dla ciebie", "Dla mnie?!");

    #print(answer)
    return answer

vc = None;

async def join_channel(message):
    global vc
    # grab the user who sent the command
    user=message.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        print("Client in channel:"+str(channel))
        # create StreamPlayer
        vc = await voice_channel.connect()


    else:
        print("Client not in channel!")

import urllib.request
import urllib.parse
import requests
async def play(query, message):
    link = ""
    if "https://www.youtube.com/watch?v=" in query:
        link = query;
    else:
        # fp = urllib.request.urlopen("https://www.bing.com/videos/search?q="+urllib.parse.quote(query.replace(" ","+"))+"&FORM=HDRSC3")
        # mybytes = fp.read()
        #
        # mystr = mybytes.decode("utf8")
        # fp.close()
        #
        # possible = mystr.split("href=\"https://www.youtube.com/watch?v=")
        #
        # code = possible[len(possible)-1].split("\"")[0]
        #
        # link = "https://www.youtube.com/watch?v="+code;

        r = requests.get('https://www.google.com/search?q='+urllib.parse.quote(query.replace(" ","+"))+'+youtube&btnI=Szcz%C4%99%C5%9Bliwy+traf')
        link = str(r.url)
    if (not "https://www.youtube.com/watch?v=" in link):
        await message.channel.send("Niestety nie znalazłem tego utworu :/ Spróbój wpisać inaczej.")
        return;

    print(link)
    await message.channel.send("Teraz gram: "+str(link))

    import youtube_dl
    import os
    os.system("rm audio.mp3")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl':'audio.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',

        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    global vc
    if(vc == None):
        print("Error! Player does not exist!" )
        return;

    vc.play(discord.FFmpegPCMAudio('audio.mp3'), after=lambda e: print('done', e))


    while not player.is_done():
        await asyncio.sleep(1)
    # disconnect after the player has finished
    #player.stop()
    vc.stop()

async def leave():
    global vc
    await vc.disconnect()

def getImageFromGoogle(query):
    from urllib.parse import urlparse
    from google_images_download import google_images_download   #importing the library
    import os
    response = google_images_download.googleimagesdownload()   #class instantiation


    arguments = {"keywords":query,"limit":1,"print_urls":True, "no_download":True}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function


    link = str(paths[0][query][0])
    path = urlparse(link).path
    link = str(urlparse(link).geturl())
    ext = os.path.splitext(path)[1]


    nazwa = "search"+ext
    os.system("wget "+link +" -O ./pictures/"+nazwa)
    print(link)
    return "!sendimg "+nazwa


def getImageFromBing(query):
    import urllib.request
    import urllib.parse


    fp = urllib.request.urlopen("https://www.bing.com/images/search?q="+urllib.parse.quote(query.replace(" ","+"))+"&FORM=HDRSC2")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    #print(mystr)
    print("Link zdjecia:")
    link = str(mystr).split('<a class="thumb" target="_blank" href=\"')[1].split('"')[0]
    os.system("wget "+link +" -O ./pictures/search.jpg")
    print(link)
    return "!sendimg search.jpg"



def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


learning_threshold = 200;
learning_threshold_max=200;
lastIndex = 0
learning_threshold = 200;
learning_threshold_max=200;
lastIndex = 0

def quickWolfram(question):

    client = wolframalpha.Client("<CENSORED>")
    res = client.query(question)
    simple = next(res.results).text
    print(simple)
    return (simple)
import re
def cleanMessage(message):
    # Remove new lines within message
    cleanedMessage = message.replace('\n',' ').lower()
    # Deal with some weird tokens
    cleanedMessage = cleanedMessage.replace("\xc2\xa0", "")
    # Remove punctuation
    cleanedMessage = re.sub('([.,!?])','', cleanedMessage)
    # Remove multiple spaces in message
    cleanedMessage = re.sub(' +',' ', cleanedMessage)
    return cleanedMessage

def tokenize(text):
    text = text.replace("?"," ?")
    text = text.replace("!"," !")
    text = text.replace(", "," ")

    sentences = text.lower().replace(".", "")

    tokenized_sentences = []


    return sentences.split(" ")

def getPolimorf(tokens, cur2plimorf):
    normalised = []
    grammar = []
    for word in tokens:
        elements = (word,)
        query = 'SELECT * FROM polimorf_pure WHERE field1=(?)'
        cur2plimorf.execute(query, elements)
        anses4polimorf = cur2plimorf.fetchall()
        if not anses4polimorf:
            elements = (word.title(),)
            cur2plimorf.execute(query, elements)
            anses4polimorf = cur2plimorf.fetchall()


        if(anses4polimorf):
            normalised.append(str(anses4polimorf[0][1]))
            grammar.append(str(anses4polimorf[0][2].split(":")[0]))
        else:
            normalised.append(word)
            if word in "!?.":
                grammar.append(word)
            else:
                grammar.append("NULL")
    return (normalised, grammar)

def AI(question, previousAns, perviousQuestion, learn=True):
    print("Answering:"+str(question))
    try:
        thinkAns = think(question)
    except Exception as e:
        print(e)
        thinkAns = ""

    if (thinkAns != ""):
        return [thinkAns, 0, 0]

    global message_history
    previous_question=""
    if len(message_history)>3:
        previous_question = message_history[len(message_history)-3]
        print("Prev Question test:"+str(previous_question))

    import sqlite3
    conn = sqlite3.connect('brain.db')
    conn.text_factory = str

    cur = conn.cursor()


    print("[+] Connecting to polimorf.db...")
    conn2polimorf = sqlite3.connect('polimorf.db')
    conn2polimorf.text_factory = str
    cur2plimorf = conn2polimorf.cursor()

    print("[+] Connecting to brain.db...")
    conn2brain = sqlite3.connect('brain.db')
    conn2brain.text_factory = str
    cur2brain = conn2brain.cursor()

    normalised = []
    grammar = []
    sentence = question
    print("[+] Parsing: "+question)
    tokens = tokenize(question)
    print("[+] Tokenized: "+str(tokens))

    normalised, grammar = getPolimorf(tokens, cur2plimorf)


    words = normalised
    elements = ("%"+" ".join(list(normalised))+"%",)
    query = 'SELECT * FROM Conversations WHERE normalized LIKE (?)'
    #elements.append((words[0],))
    #print(query)

    for i in range(0, len(words)):
        query +=" OR "+'normalized LIKE (?)'
        elements = elements+("%"+words[i]+"%",)
    print(query)
    print(elements)
    cur.execute(query, elements)

    anses = cur.fetchall()
    if len(anses)==0:
        return ["Nie rozumiem, ziomuś.", 0, 0]
        # query = 'SELECT * FROM Conversations'
        # cur.execute(query)
        #
        # anses = cur.fetchall()


    global learning_threshold
    global learning_threshold_max
    global lastIndex
    if previousAns != "":
        passed = True
        with open("filtr.txt", "r") as f1:
            for line in f1:
                if line.replace("\n","").lower() in question.lower():
                    passed=False
                    return ["Nie odpowiem na to, bo jestes niewychowany.", 0,0]

        if passed and learn:
            # open("myconv.txt", "a+").write("Q:"+previousAns+
            # "\nA:"+question+"\n")

            normalised_prev, grammar_prev = getPolimorf(tokenize(previousAns), cur2plimorf)

            print("[+] Normalized sentence:"+str(normalised_prev))
            print("[+] Grammar info:"+str(grammar_prev))
            t = (previousAns,question,previous_question, " ".join(list(normalised_prev)), ":".join(list(grammar_prev)),)
            cur.execute("INSERT INTO Conversations VALUES (?, ?, ?, ?, ?)", t)
            conn.commit()

    lowest_score = 1000
    bestAns = ""
    #bestRecord =[]
    bestRecords = []
    answers = []
    answers_indexes = []
    answers_bonuses = []
    getNextAns = False;

    #with open("myconv.txt") as f:

    gram = ":".join(list(grammar))
    norm = " ".join(list(normalised))

    if True:
        index = -1

        for line in anses:
            index+=1
            score_gram = len(gram)
            score_norm = len(norm)
            #print("RawLine:"+line)

            #print("Anses[0]:"+str(line[0]))
            #commonsScore = 0.0
            #for word in cleanMessage(line[0]).split(" "):
            #    t = (word,)
            #    query = 'SELECT count FROM commons WHERE word = (?)'
            #    cur.execute(query, t)
            #    weights = cur.fetchall()
            #    if len(weights)>0:
            #        commonsScore *= 1.0/weights[0][0]

            #print(str(line))
            #scorring sentence:
            if(str(normalised) == str(line[3].split(" "))):
                score_norm = 0;
            else:
                for i in range(len(normalised)):
                    if normalised[i] in line[3].split(" "):
                        score_norm -=1;

            #scorring grammar:
            if(str(grammar) == str(line[4].split(":"))):
                score_gram = 0;
            else:
                last_index = -1
                for i in range(len(grammar)):
                    temp_gram = line[4].split(":")
                    if grammar[i] in temp_gram:
                        ind = temp_gram.index(grammar[i])

                        if(ind > last_index):

                            last_index = ind;
                            score_gram -=1;


            score = (score_gram+score_norm*2)*100.0/(len(gram)+len(norm)*2)
            if len(message_history)>3:
                score += levenshtein(str(line[2]).lower(), previous_question.lower())/(len(previous_question)+len(str(line[2])))/10.0

            # score = levenshtein(str(line[0]).lower(), question.lower())
            # if len(message_history)>3:
            #     score += 0.3 * levenshtein(str(line[2]).lower(), previous_question.lower())

            #score = (bigger - levDis)*100/bigger
            # if abs(index-lastIndex)<10:
            #     score-=1
            if score<lowest_score:
                lowest_score=score
                answers=[]
                bestRecords = []
                #getNextAns=True
                bestRecords.append(line[:])
                answers.append(line[1])
                print("Najlepsze dopasowanie:"+str(line[0]))
                print("")
                print("[+] Input:"+str(question))
                print("[+] Question analysed:"+str(line[0]))
                print("[+] Normal score:"+str(100 - score_norm*100/len(norm)))
                print("[+] Grammar score:"+str(100 - score_gram*100/len(gram)))

                print(line[0]+" score:"+str(100-score))
                print("Grammar input: "+str(grammar)+" question:"+str(line[4].split(":")) + " Score:"+str(100 - score))

            #    print("getAns lower (Q:) setting to:"+str(getNextAns))
            if score == lowest_score:
                print("Takie samo jak poprzednie:"+str(line[0]))
                print("")
                print("[+] Input:"+str(question))
                print("[+] Question analysed:"+str(line[0]))
                print("[+] Normal score:"+str(100 - score_norm*100/len(norm)))
                print("[+] Grammar score:"+str(100 - score_gram*100/len(gram)))

                print(line[0]+" score:"+str(100-score))
                print("Grammar input: "+str(grammar)+" question:"+str(line[4].split(":")) + " Score:"+str(100 - score))
                getNextAns=True
                answers.append(line[1])
                bestRecords.append(line[:])
                #print("getAns equals (Q:) setting to:"+str(getNextAns))




    print("Choosing from:"+str(len(answers)))
    rnd=random.randint(0,len(answers)-1)
    bestAns = answers[rnd]
    bestRecord = bestRecords[rnd]
    print("Best Record:"+str(bestRecord))

    #lastIndex = answers_indexes[rnd];
    # print("learning_threshold:"+str(learning_threshold))
    # if lowest_score>learning_threshold:
    #     bestAns = question;

    print("Ans chosen:", bestAns, "score:", lowest_score)
    #After processing:
    bestAns=bestAns.replace("\n","").replace("john", nick).replace("Grzesiu", nick).replace("Grzesiek", nick).replace("John", nick).replace("Grzegorz", nick).replace("Grzechu",nick)





    return [bestAns, lowest_score, len(answers)]



    return [bestAns, lowest_score, 0]

# def AI(question, previousAns, perviousQuestion, learn=True):
#     print("Answering:"+str(question))
#     try:
#         thinkAns = think(question)
#     except Exception as e:
#         print(e)
#         thinkAns = ""
#
#     if (thinkAns != ""):
#         return [thinkAns, 0, 0]
#
#     global message_history
#     previous_question=""
#     if len(message_history)>3:
#         previous_question = message_history[len(message_history)-3]
#         print("Prev Question test:"+str(previous_question))
#     import sqlite3
#     conn = sqlite3.connect('brain.db')
#     conn.text_factory = str
#
#     cur = conn.cursor()
#     words = question.split(" ")
#     elements = ("%"+words[0]+"%",)
#     query = 'SELECT * FROM Conversations WHERE Question LIKE (?)'
#     #elements.append((words[0],))
#     #print(query)
#
#     for i in range(1, len(words)):
#         query +=" OR "+'Question LIKE (?)'
#         elements = elements+("%"+words[i]+"%",)
#     print(query)
#     print(elements)
#     cur.execute(query, elements)
#
#     anses = cur.fetchall()
#     if len(anses)==0:
#         query = 'SELECT * FROM Conversations'
#         cur.execute(query)
#
#         anses = cur.fetchall()
#
#
#     global learning_threshold
#     global learning_threshold_max
#     global lastIndex
#     if previousAns != "":
#         passed = True
#         with open("filtr.txt", "r") as f1:
#             for line in f1:
#                 if line.replace("\n","").lower() in question.lower():
#                     passed=False
#                     return ["Nie odpowiem na to, bo jestes niewychowany.", 0,0]
#
#         if passed and learn:
#             # open("myconv.txt", "a+").write("Q:"+previousAns+
#             # "\nA:"+question+"\n")
#             t = (previousAns,question,previous_question)
#             cur.execute("INSERT INTO Conversations VALUES (?, ?, ?)", t)
#             conn.commit()
#
#     lowest_score = 1000
#     bestAns = ""
#     #bestRecord =[]
#     bestRecords = []
#     answers = []
#     answers_indexes = []
#     answers_bonuses = []
#     getNextAns = False;
#
#     #with open("myconv.txt") as f:
#
#
#     if True:
#         index = -1
#         for line in anses:
#             index+=1
#             #print("RawLine:"+line)
#
#             #print("Anses[0]:"+str(line[0]))
#             commonsScore = 0.0
#             #for word in cleanMessage(line[0]).split(" "):
#             #    t = (word,)
#             #    query = 'SELECT count FROM commons WHERE word = (?)'
#             #    cur.execute(query, t)
#             #    weights = cur.fetchall()
#             #    if len(weights)>0:
#             #        commonsScore *= 1.0/weights[0][0]
#
#             score = levenshtein(str(line[0]).lower(), question.lower())
#             if len(message_history)>3:
#                 score += 0.3 * levenshtein(str(line[2]).lower(), previous_question.lower())
#
#             #score = (bigger - levDis)*100/bigger
#             # if abs(index-lastIndex)<10:
#             #     score-=1
#             if score<lowest_score:
#                 lowest_score=score
#                 answers=[]
#                 bestRecords = []
#                 #getNextAns=True
#                 bestRecords.append(line[:])
#                 answers.append(line[1])
#                 print("Najlepsze dopasowanie:"+str(line[0]))
#
#             #    print("getAns lower (Q:) setting to:"+str(getNextAns))
#             if score == lowest_score:
#                 getNextAns=True
#                 answers.append(line[1])
#                 bestRecords.append(line[:])
#                 #print("getAns equals (Q:) setting to:"+str(getNextAns))
#
#
#
#
#     print("Choosing from:"+str(len(answers)))
#     rnd=random.randint(0,len(answers)-1)
#     bestAns = answers[rnd]
#     bestRecord = bestRecords[rnd]
#     print("Best Record:"+str(bestRecord))
#
#     #lastIndex = answers_indexes[rnd];
#     print("learning_threshold:"+str(learning_threshold))
#     if lowest_score>learning_threshold:
#         bestAns = question;
#
#     print("Ans chosen:", bestAns, "score:", lowest_score)
#     #After processing:
#     bestAns=bestAns.replace("\n","").replace("john", nick).replace("Grzesiu", nick).replace("Grzesiek", nick).replace("John", nick).replace("Grzegorz", nick).replace("Grzechu",nick)
#
#     wordsQ = zniszczZnakiInterpunkcyjne(bestRecord[0]).split(" ");
#     wordsA = zniszczZnakiInterpunkcyjne(bestRecord[1]).split(" ");
#     wordsQReal = zniszczZnakiInterpunkcyjne(question).split(" ")
#     bestAnsWords = bestAns.split(" ")
#     for iQ in range(0,len(wordsQ)):
#         for iA in range(0,len(wordsA)):
#             if zniszczPolskieZnaki(wordsQ[iQ]) == zniszczPolskieZnaki(wordsA[iA]):
#                 print(wordsQ[iQ]+"="+wordsA[iA])
#                 indexBestAns = -1
#                 try:
#                     prevWordQ= wordsQ[iQ-1]
#                     print("Previous word:"+prevWordQ)
#                     switchWord = wordsQReal[wordsQReal.index(prevWordQ)+1]
#                     #Get prev word for next sentence placement
#                     prevWordA = wordsA[iA-1]
#                     print("Wymieniam "+str(prevWordA)+" na "+str(switchWord))
#                     if(bestAnsWords.index(prevWordA)+1>=0):
#                         bestAnsWords[bestAnsWords.index(prevWordA)+1] = switchWord;
#
#                     bestAns = " ".join(bestAnsWords)
#
#                 except Exception as e:
#                     print(e)
#
#
#
#     return [bestAns, lowest_score, len(answers)]
#
#
#
#     return [bestAns, lowest_score, 0]

import os

import discord


TOKEN = "<CENSORED>"
#GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break
    global prev
    global prevQ
    global last_id
    global last_last
    global disabled
    global player
    player = None
    prev = ""
    prevQ=""
    last_id = "0";
    last_last = ""
    disabled=False
    print(
        f'{client.user} is connected to the following guild:\n'
        #f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):

        global player
        global prev
        global prevQ
        global last_id
        global last_last
        global disabled
        global nick
        global imie
        global message_history
        global isPaused
        print(f"{message.channel}: {message.author}:{message.author.name} : {message.content}")
        if(message.author.name == "Dank Memer"):
            await message.channel.send("Hahaha... głupi bot.")
        last = message.content.lower();
        original = message.content
        if message.author.name != "John4000":
            if "!join" in last:
                await join_channel(message)

            if "!play " in last:

                if vc.is_playing():
                    print("Zatrzymuję...")
                    vc.stop()

                print("Próbuję play.")
                await play(original.split("!play ")[1], message)
                return

            if '!pause' in last:
                print("Pausing..")
                vc.pause()
                #isPaused = True;

            if '!resume' in last:
                #isPaused = False
                vc.resume()

            if '!leave' in last:
                print("leaving...")
                await leave();


        if(message.author.name != "John4000" and (str(message.channel) == "pogadaj-z-johnem" or "john" in message.content.lower() or "direct message" in str(message.channel).lower())):
            nick = message.author.name
            imie = message.author.name
            last = "<"+imie+">"+message.content.lower();
            if not "@" in str(message.content):
                message_history.append(message.content.lower())

            if "@john stop" in last:
                pass

            if "@john start" in last:

                await message.channel.send("Witaj ponownie ;)")

            if "@john execute order 66" in last:
                await message.channel.send("Unsopperted yet!")
                # copy_image("order66_1.gif");
                # pyautogui.hotkey("ctrl", "v")
                # pyautogui.press('enter')

            if "@john nuke" in last:
                await message.channel.send("Unsopperted yet!")
                # print("Trying to nuke...")
                # copy_image("nuke.gif");
                # time.sleep(1)
                # pyautogui.hotkey("ctrl", "v")
                # pyautogui.press('enter')


            if not disabled and not '@' in last:
                #nick = last.replace(">", "<").split("<")[1]
                question=last.split(">")[1]
                prevQ = question;
                print("A: "+last.split(">")[1]+"\n")
                try:
                    output = AI(question, prev, prevQ)
                except Exception as e:
                    print(str(e))
                    output = ["I have just picked up a fault: "+str(e),0,0]
                print(output)
                prev = output[0].replace("<","(").replace(">",")")

              #AliceBrain.stdin.write(last.split(">")[1]+"\n")

                print(prev);

                if(prev.startswith("!sendimg ")):
                    await message.channel.send(file=discord.File("./pictures/"+str(prev.split("!sendimg ")[1])))
                else:
                    await message.channel.send(prev)
                    message_history.append(prev)


client.run(TOKEN)
