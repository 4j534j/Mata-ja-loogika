

print("nimi kodanik!")
nimi = input(" ")

print("noh ", nimi, " palju se lubatud kiirus siis ka oli?")
lubatudkiirus = input( )

print("ahahh ja kui kiiresti sa siis sõitsid")
ulekiiirus = input()
trahv = (float(ulekiiirus) - float(lubatudkiirus)) * 3


if trahv > 190:
    trahv = 190

if trahv < 0:
    trahv = 0

if trahv == 0:
    print(nimi, "järgmine kord saan su kätte")
else:
    print(nimi, "kiiruse ületamise eest on teie trahv", trahv)