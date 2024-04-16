incognita = 155
x = [150,160,170,180,190,200,210]
y = [35.5,37.8,43.6,45.7,47.3,50.1,51.2]
# Algoritmo para determinado la interpolación
# el valor de ingognita es la variable x buscada y la funcion
# interpolacion() recibira el valor buscado y las dos matrices
# x es la matriz en el plano carteciano y buscamos el valor de "y" para el valor de la incognita
def interpolacionY3(valor,vx,vy):
    y1 = ((valor - vx[1])*(valor - vx[2]))/((vx[0] - vx[1])*(vx[0] - vx[2]))
    respuesta_y1 = y1*vy[0]
    y2 = ((valor - vx[0])*(valor - vx[2]))/((vx[1] - vx[0])*(vx[1] - vx[2]))
    respuesta_y2 = y2*vy[1]
    y3 = ((valor - vx[0])*(valor - vx[1]))/((vx[2] - vx[0])*(vx[2] - vx[1]))
    respuesta_y3 = y3*vy[2]
    respuesta = respuesta_y1+respuesta_y2+respuesta_y3
    print(f"Respuesta y3: {respuesta}")


def interpolacionY4(valor,vx,vy):
    y1 = ((valor - vx[1])*(valor - vx[2])*(valor - vx[3]))/((vx[0] - vx[1])*(vx[0] - vx[2])*(vx[0] - vx[3]))
    respuesta_y1 = y1*vy[0]
    y2 = ((valor - vx[0])*(valor - vx[2])*(valor - vx[3]))/((vx[1] - vx[0])*(vx[1] - vx[2])*(vx[1] - vx[3]))
    respuesta_y2 = y2*vy[1]
    y3 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[3]))/((vx[2] - vx[0])*(vx[2] - vx[1])*(vx[2] - vx[3]))
    respuesta_y3 = y3*vy[2]
    y4 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2]))/((vx[3] - vx[0])*(vx[3] - vx[1])*(vx[3] - vx[2]))
    respuesta_y4 = y4*vy[3]
    respuesta = respuesta_y1+respuesta_y2+respuesta_y3+respuesta_y4
    print(f"Respuesta y4: {respuesta}")


def interpolacionY5(valor,vx,vy):
    y1 = ((valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4]))/((vx[0] - vx[1])*(vx[0] - vx[2])*(vx[0] - vx[3])*(vx[0] - vx[4]))
    respuesta_y1 = y1*vy[0]
    y2 = ((valor - vx[0])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4]))/((vx[1] - vx[0])*(vx[1] - vx[2])*(vx[1] - vx[3])*(vx[1] - vx[4]))
    respuesta_y2 = y2*vy[1]
    y3 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[3])*(valor - vx[4]))/((vx[2] - vx[0])*(vx[2] - vx[1])*(vx[2] - vx[3])*(vx[2] - vx[4]))
    respuesta_y3 = y3*vy[2]
    y4 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[4]))/((vx[3] - vx[0])*(vx[3] - vx[1])*(vx[3] - vx[2])*(vx[3] - vx[4]))
    respuesta_y4 = y4*vy[3]
    y5 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3]))/((vx[4] - vx[0])*(vx[4] - vx[1])*(vx[4] - vx[2])*(vx[4] - vx[3]))
    respuesta_y5 = y5*vy[4]
    respuesta = respuesta_y1+respuesta_y2+respuesta_y3+respuesta_y4+respuesta_y5
    print(f"Respuesta y5: {respuesta}")


def interpolacionY6(valor,vx,vy):
    y1 = ((valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5]))/((vx[0] - vx[1])*(vx[0] - vx[2])*(vx[0] - vx[3])*(vx[0] - vx[4])*(vx[0] - vx[5]))
    respuesta_y1 = y1*vy[0]
    y2 = ((valor - vx[0])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5]))/((vx[1] - vx[0])*(vx[1] - vx[2])*(vx[1] - vx[3])*(vx[1] - vx[4])*(vx[1] - vx[5]))
    respuesta_y2 = y2*vy[1]
    y3 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5]))/((vx[2] - vx[0])*(vx[2] - vx[1])*(vx[2] - vx[3])*(vx[2] - vx[4])*(vx[2] - vx[5]))
    respuesta_y3 = y3*vy[2]
    y4 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[4])*(valor - vx[5]))/((vx[3] - vx[0])*(vx[3] - vx[1])*(vx[3] - vx[2])*(vx[3] - vx[4])*(vx[3] - vx[5]))
    respuesta_y4 = y4*vy[3]
    y5 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[5]))/((vx[4] - vx[0])*(vx[4] - vx[1])*(vx[4] - vx[2])*(vx[4] - vx[3])*(vx[4] - vx[5]))
    respuesta_y5 = y5*vy[4]
    y6 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4]))/((vx[5] - vx[0])*(vx[5] - vx[1])*(vx[5] - vx[2])*(vx[5] - vx[3])*(vx[5] - vx[4]))
    respuesta_y6 = y6*vy[5]
    respuesta = respuesta_y1+respuesta_y2+respuesta_y3+respuesta_y4+respuesta_y5+respuesta_y6
    print(f"Respuesta y6: {respuesta}")


def interpolacionY7(valor,vx,vy):
    y1 = ((valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6]))/((vx[0] - vx[1])*(vx[0] - vx[2])*(vx[0] - vx[3])*(vx[0] - vx[4])*(vx[0] - vx[5])*(vx[0] - vx[6]))
    respuesta_y1 = y1*vy[0]
    y2 = ((valor - vx[0])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6]))/((vx[1] - vx[0])*(vx[1] - vx[2])*(vx[1] - vx[3])*(vx[1] - vx[4])*(vx[1] - vx[5])*(vx[1] - vx[6]))
    respuesta_y2 = y2*vy[1]
    y3 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6]))/((vx[2] - vx[0])*(vx[2] - vx[1])*(vx[2] - vx[3])*(vx[2] - vx[4])*(vx[2] - vx[5])*(vx[2] - vx[6]))
    respuesta_y3 = y3*vy[2]
    y4 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6]))/((vx[3] - vx[0])*(vx[3] - vx[1])*(vx[3] - vx[2])*(vx[3] - vx[4])*(vx[3] - vx[5])*(vx[3] - vx[6]))
    respuesta_y4 = y4*vy[3]
    y5 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[5])*(valor - vx[6]))/((vx[4] - vx[0])*(vx[4] - vx[1])*(vx[4] - vx[2])*(vx[4] - vx[3])*(vx[4] - vx[5])*(vx[4] - vx[6]))
    respuesta_y5 = y5*vy[4]
    y6 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[6]))/((vx[5] - vx[0])*(vx[5] - vx[1])*(vx[5] - vx[2])*(vx[5] - vx[3])*(vx[5] - vx[4])*(vx[5] - vx[6]))
    respuesta_y6 = y6*vy[5]
    y7 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5]))/((vx[6] - vx[0])*(vx[6] - vx[1])*(vx[6] - vx[2])*(vx[6] - vx[3])*(vx[6] - vx[4])*(vx[6] - vx[5]))
    respuesta_y7 = y7*vy[6]
    respuesta = respuesta_y1+respuesta_y2+respuesta_y3+respuesta_y4+respuesta_y5+respuesta_y6+respuesta_y7
    print(f"Respuesta y7: {respuesta}")


def interpolacionY8(valor,vx,vy):
    y1 = ((valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6])*(valor - vx[7]))/((vx[0] - vx[1])*(vx[0] - vx[2])*(vx[0] - vx[3])*(vx[0] - vx[4])*(vx[0] - vx[5])*(vx[0] - vx[6])*(vx[0] - vx[7]))
    respuesta_y1 = y1*vy[0]
    y2 = ((valor - vx[0])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6])*(valor - vx[7]))/((vx[1] - vx[0])*(vx[1] - vx[2])*(vx[1] - vx[3])*(vx[1] - vx[4])*(vx[1] - vx[5])*(vx[1] - vx[6])*(vx[1] - vx[7]))
    respuesta_y2 = y2*vy[1]
    y3 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6])*(valor - vx[7]))/((vx[2] - vx[0])*(vx[2] - vx[1])*(vx[2] - vx[3])*(vx[2] - vx[4])*(vx[2] - vx[5])*(vx[2] - vx[6])*(vx[2] - vx[7]))
    respuesta_y3 = y3*vy[2]
    y4 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6])*(valor - vx[7]))/((vx[3] - vx[0])*(vx[3] - vx[1])*(vx[3] - vx[2])*(vx[3] - vx[4])*(vx[3] - vx[5])*(vx[3] - vx[6])*(vx[3] - vx[7]))
    respuesta_y4 = y4*vy[3]
    y5 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[5])*(valor - vx[6])*(valor - vx[7]))/((vx[4] - vx[0])*(vx[4] - vx[1])*(vx[4] - vx[2])*(vx[4] - vx[3])*(vx[4] - vx[5])*(vx[4] - vx[6])*(vx[4] - vx[7]))
    respuesta_y5 = y5*vy[4]
    y6 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[6])*(valor - vx[7]))/((vx[5] - vx[0])*(vx[5] - vx[1])*(vx[5] - vx[2])*(vx[5] - vx[3])*(vx[5] - vx[4])*(vx[5] - vx[6])*(vx[5] - vx[7]))
    respuesta_y6 = y6*vy[5]
    y7 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5])*(valor - vx[7]))/((vx[6] - vx[0])*(vx[6] - vx[1])*(vx[6] - vx[2])*(vx[6] - vx[3])*(vx[6] - vx[4])*(vx[6] - vx[5])*(vx[6] - vx[7]))
    respuesta_y7 = y7*vy[6]
    y8 = ((valor - vx[0])*(valor - vx[1])*(valor - vx[2])*(valor - vx[3])*(valor - vx[4])*(valor - vx[5])*(valor - vx[6]))/((vx[7] - vx[0])*(vx[7] - vx[1])*(vx[7] - vx[2])*(vx[7] - vx[3])*(vx[7] - vx[4])*(vx[7] - vx[5])*(vx[7] - vx[6]))
    respuesta_y8 = y8*vy[7]
    respuesta = respuesta_y1+respuesta_y2+respuesta_y3+respuesta_y4+respuesta_y5+respuesta_y6+respuesta_y7+respuesta_y8
    print(f"Respuesta y8: {respuesta}")


if len(x)==3:
    interpolacionY3(incognita,x,y)
elif len(x)==4:
    interpolacionY4(incognita,x,y)
elif len(x)==5:
    interpolacionY5(incognita,x,y)
elif len(x)==6:
    interpolacionY6(incognita,x,y)
elif len(x)==7:
    interpolacionY7(incognita,x,y)
elif len(x)==8:
    interpolacionY8(incognita,x,y)