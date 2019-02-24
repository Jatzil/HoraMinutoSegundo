class HoraMinutoSegundo:  #Nombre de la clase
    __hora = int(0)  #Atributos
    __minuto = int(0)
    __segundo = int(0)

    def __init__(self, hora, minuto, segundo):  #Se define el metodo constructor
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo


    def identificarHoraDespues(self):  #Metodo el cual se caracteriza por colocar un verbo al principio
        self.__segundo = self.__segundo + 1  #Procedimiento y operaciones con la regla de los segundos, minutos, y horas, para poder resolver mi codigo
        if (self.__segundo == 60):
            self.__segundo = 0
            self.__minuto = self.__minuto + 1
            if (self.__minuto == 60):
                self.__minuto = 0
                self.__hora = self.__hora + 1
                if (self.__hora == 24):
                    self.__hora = 0

    def getNuevahora(self):  #Método get, para poder retornar los valores, y dar una salida de acuerdo a mi programa
        return self.__hora
    def getNuevominuto(self):
        return self.__minuto
    def getNuevosegundo(self):
        return self.__segundo

