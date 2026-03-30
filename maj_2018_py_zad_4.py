from collections import Counter

with open('sygnaly.txt', 'r', encoding='utf-8') as file:
    content = file.read()
lines = content.splitlines()

def zad_4_1():
    print(f'Zapisano zad 4.1{(res:=[l[9] for l in lines if lines.index(l) % 40 == 39], "")[1]}{open("wyniki4.txt", "a", encoding="utf-8").write("".join(res) + chr(10)*3) and ""}')

def zad_4_2():
    print(f'Zapisano zad 4.2{(res:=str(max([(l, len(Counter(l))) for l in lines], key=lambda x: x[1])).replace("(","").replace(")","").replace(",","").replace("\'",""), "")[1]}{open("wyniki4.txt", "a", encoding="utf-8").write(res + chr(10)*3) and ""}')

def zad_4_3():
    print(f'Zapisano zad 4.3{(res:=chr(10).join([l for l in lines if max(ords:=[ord(c) for c in l])-min(ords)<11]), "")[1]}{open("wyniki4.txt", "a", encoding="utf-8").write(res) and ""}')

def zad_4_1_do_4_3():
    zad_4_1()
    zad_4_2()
    zad_4_3()


zad_4_1_do_4_3()
