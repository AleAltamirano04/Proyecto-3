nombre = str
apellido = str
edad = int
parentesco = str
listo = 1
i = int
personas = int
personas = int(input('¿Cuantas personas entraron a la casa?     '))
for i in range(personas):
    while listo == 1:
      print('Escriba el nombre de la persona ')
      nombre = str(input())
      print('Escriba el apellido de la persona ')
      apellido = str(input())
      print('Escriba la edad de la persona ')
      edad = int(input())
      print('Escriba el parentesco de la persona Con la familia')
      parentesco = str(input())
      print('¿Seguimos nombrando personas? Sabiendo que 1 es = Si y No = cualquier numero')
      listo = int(input())
      print('El nombre de la persona que ingreso es',nombre,'y el apellido es',apellido,'Su edad es',edad,'años','Y es el',parentesco,'de la familia')
