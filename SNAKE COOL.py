import turtle 
import time
import random

posponer=0.1     

#marcador del juego.
score=0
high_score=0

#Configuración de la ventana de juego o app.
wn=turtle.Screen()
wn.title("SNAKE COOL")
wn.bgcolor("red")
wn.setup(width=800,height=600)
wn.tracer(0)

#Barrera del marcador
barra=turtle.Turtle()
barra.goto(-450,250)
barra.pencolor("white")
barra.speed(0)
barra.goto(450,250)

#Cuerpo principal
head= turtle.Turtle()
head.speed=(0)
head.shape("square")
head.color("cyan","black")
head.penup()
head.goto(0,0)
head.direction="stop"

#Objetos
comida= turtle.Turtle()
comida.speed=(0)
comida.shape("circle")
comida.color("yellow")
comida.penup()
comida.goto(0,120)
comida.direction="stop"

segment_list=[]

#Marcador de puntaje:
marcador= turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,260)
marcador.write("Score: 0    High Score: 0", 
align="center", font=("Courier",20,"normal"))

#decignación de funciones:
def arriba():
    head.direction = "up"
def abajo():
    head.direction = "down"
def izq():
    head.direction = "left"
def derecha():
    head.direction = "right"

#movimientos
def movimiento():
    if head.direction == "up": 
        y= head.ycor()
        head.sety(y+20)

    if head.direction == "down": 
        y= head.ycor()
        head.sety(y-20)

    if head.direction == "left": 
        x= head.xcor()
        head.setx(x-20)

    if head.direction == "right": 
        x= head.xcor()
        head.setx(x+20)
    
#Control por Teclado.
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izq,"Left")
wn.onkeypress(derecha,"Right")

#cerrar ventana 
def salir():
    global correr
    correr = False
wn.listen()
wn.onkeypress(salir,"s")

#Bucle de la ventana.
correr= True
while correr:
    wn.update()
#colisiones en pantalla:
    if head.xcor()> 380 or head.xcor()<-380 or head.ycor()>230 or head.ycor()<-280:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for segmento in segment_list:
            segmento.goto(1000,1000)
    #Eliminar segmentos:
        segment_list.clear()
        score=0
        marcador.clear()   
        marcador.write("Score:{}    High Score:{}".format(score,high_score), 
                align="center", font=("Courier",25,"normal"))

    #Posición del objeto.
    if head.distance(comida)<20:
        x = random.randint(-370,370)
        y = random.randint(-270,220)
        comida.goto(x,y)
        #Segmentos de la cabeza principal
        new_segment= turtle.Turtle()
        new_segment.speed=(1)
        new_segment.shape("square")
        new_segment.color("green","cyan")
        new_segment.penup()
        segment_list.append(new_segment)

    #Conteo del Marcador:
        score +=1
        
        if score>high_score:
            high_score=score
        marcador.clear()
        marcador.write("Score:{}    High Score:{}".format(score,high_score), 
                align="center", font=("Courier",25,"normal"))
        score=total_seg+1

    #movimiento total del cuerpo:
    total_seg=len(segment_list)
    
    for index in range(total_seg -1, 0, -1):
        x= segment_list[index - 1].xcor()
        y= segment_list[index - 1].ycor()
        segment_list[index].goto(x,y)
    if total_seg>0:
        x= head.xcor()
        y= head.ycor()
        segment_list[0].goto(x,y)
    
    movimiento()
    #colisines con el cuerpo
    for segmento in segment_list:
        if segmento.distance(head)< 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"   

            for segmento in segment_list:
                segmento.goto(1000,1000)

            segment_list.clear()
            score=0
            marcador.clear()
            marcador.write("Score:{}    High Score:{}".format(score,high_score), 
                align="center", font=("Courier",25,"normal"))
    
    time.sleep(posponer)
    
wn.bye()
