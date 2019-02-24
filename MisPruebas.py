from HoraMinutoSegundo import HoraMinutoSegundo #Primera prueba

prueba = HoraMinutoSegundo(1,6,7)
prueba.identificarHoraDespues()
print('Tu hora ahora es: ',prueba.getNuevahora(),'hora(s):',prueba.getNuevominuto(),'minuto(s):',prueba.getNuevosegundo(),'segundo(s)')

from HoraMinutoSegundo1 import HoraMinutoSegundo1 #Segunda prueba

prueba1 = HoraMinutoSegundo1(22,59,59)
prueba1.identificarHoraDespues()
print(prueba1.getNuevahora())