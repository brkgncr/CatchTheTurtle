import turtle
import random
import time


#turtle icin ekran olusturma
turtle_ekran = turtle.Screen()
turtle_ekran.title("Catch The Turtle")
turtle_ekran.bgcolor("light blue")
turtle_ekran.setup(750,750)


#zamanlayici olusturma
sayac_ekran = turtle.Turtle()
sayac_ekran.speed(0)
sayac_ekran.color("black")
sayac_ekran.penup()
sayac_ekran.hideturtle()
sayac_ekran.goto(0, 290)
sayac_ekran.write("Başlangıç", align="center", font=("Courier", 24, "normal"))

#score icin yazi
score = 0
score_ekran = turtle.Turtle()
score_ekran.speed(0)
score_ekran.color("blue")
score_ekran.penup()
score_ekran.hideturtle()
score_ekran.goto(0, 320)
score_ekran.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

#kaplunabaga olusturur
turtles = []
def turtle_olsutur():
    turtle_yakalama = turtle.Turtle()
    turtle_yakalama.shapesize(stretch_wid=3, stretch_len=2)
    turtle_yakalama.shape("turtle")
    turtle_yakalama.color("green")
    turtle_yakalama.speed(0)
    turtle_yakalama.penup()
    x = random.randint(-340, 340)
    y = random.randint(-340, 260)
    turtle_yakalama.goto(x, y)
    turtles.append(turtle_yakalama)

#kaplmabaga olsuturma
for _ in range(1):
    turtle_olsutur()

#baslatma icin geri sayim
def baslat_sayac():
    for i in range(5, 0, -1):
        sayac_ekran.clear()
        sayac_ekran.write("Başlangıç: {}".format(i), align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
    sayac_ekran.clear()

#sayaci guncelleme
def sayac_guncelleme():
    global gerisayim_suresi
    sayac_ekran.clear()
    sayac_ekran.goto(0, 290)
    sayac_ekran.write("Süre: {} saniye".format(gerisayim_suresi), align="center", font=("Courier", 24, "normal"))

def tiklama(x, y):
    global score
    for turtle_ in turtles:
        if turtle_.distance(x, y) < 20:
            turtle_.goto(random.randint(-290, 290), random.randint(-290, 290))
            score += 1
            score_ekran.clear()
            score_ekran.write("Skor: {}".format(score), align="center", font=("Courier", 24, "normal"))




#sayaci baslatma
baslat_sayac()

#score icin tiklama islemleri
turtle_ekran.listen()
turtle_ekran.onclick(tiklama)

#geri sayim suresi
gerisayim_suresi = 15

#ana oyun dongusu
while gerisayim_suresi > 0:
    turtle_ekran.update()
    time.sleep(1)
    gerisayim_suresi -= 1
    sayac_guncelleme()

#oyun sonu mesaji
sayac_ekran.clear()
sayac_ekran.goto(0, 260)
sayac_ekran.write("Oyun Bitti!", align="center", font=("Courier", 24, "normal"))
time.sleep(5)

#oyunu kapatma
turtle_ekran.bye()