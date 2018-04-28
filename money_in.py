"""
Author: Daniel F. Zuñiga H.
Date: 25/04/18
Place: @Biblioteca Central, National University of Colombia

Description: This module is part of UPODS project. It
             contains all income operations.
"""

import operations

def price_vector(price):
    """
@Description: De acuerdo al precio base por hora, fijará los precios para media hora (30 min.) y 45 minutos. Función auxiliar.

@params:
    price [int]: Precio por hora.

@result:
    [list]: Con tres (3) precios (por hora [pos_0], por 45 min. [pos_1] y por 30 min. [pos_2])
    """

    price_vector = []
    
    if(price == 3000):
        price_vector.append(3000)
        price_vector.append(2300)
        price_vector.append(1500)
        return price_vector
    
    elif(price == 2500):
        price_vector.append(2500)
        price_vector.append(2000)
        price_vector.append(1500)
        return price_vector
    
    elif(price == 2000):
        price_vector.append(2000)
        price_vector.append(1500)
        price_vector.append(1000)
        return price_vector

    else:
        print("Hay un error en algún lado.")


def price_per_time(staying_time, price_vector):
    """
@Description: Devuelve el costo de la estadía según el tiempo de estadía. Función auxiliar.

@params:
    staying_time [int]: Tiempo en minutos de estadía.
    price_vector [list]: Vector de 3 posiciones con los precios de 60, 45 y 30 minutos. Revisar el método "money_in.price_vector()"

@result:
    [int]: El precio del tiempo de estadía.
    """

    if(staying_time == 60):
        return price_vector[0]
    
    elif(staying_time == 45):
        return price_vector[1]
    
    elif(staying_time == 30):
        return price_vector[2]
    
    else:
        print("Hay un error en algún lado.")


def focus_days(fullhouse_days, date_from, date_to):
    """
@Description: Devuelve el número de días al mes que se operará en base al número de días operados por semana. Función auxiliar.

@params:
    fullhouse_days [int]: Número de días operados por semana.
    date_from [datetime]: Fecha en la que inicia la J24.
    date_to [datetime]: Fecha en la que termina la J24.

@result:
    [int]: Número de días que se operará al mes.
    """

    #Calcula el número de días totales y la frecuencia de cada día.
    days_vector = operations.days_counter(date_from, date_to)
    #Número total de días entre las dos fechas.
    total_days = days_vector[0]
    #Diccionario que contiene la relación "Día de la semana : Número de días".
    weekdays = days_vector[1]
    weekdays = dict(weekdays)
    try:
        if(fullhouse_days == 7):
            return total_days

        elif(fullhouse_days == 6):
            mon_sat = weekdays[operations.day_target(0)] + weekdays[operations.day_target(1)] + weekdays[operations.day_target(2)] + weekdays[operations.day_target(3)] + weekdays[operations.day_target(4)] + weekdays[operations.day_target(5)]
            return mon_sat

        elif(fullhouse_days == 5):
            mon_fri = weekdays[operations.day_target(0)] + weekdays[operations.day_target(1)] + weekdays[operations.day_target(2)] + weekdays[operations.day_target(3)] + weekdays[operations.day_target(4)]
            return mon_fri

        else:
            print("Hay un error en algún lado.")
    except:
        print ("Eche monda, revisa las fechas ingresadas (Como mínimo la operación debe ser mayor a una semana.)")

def pod_earnings(vector_representation):
    """
@Description: Devuelve las ganancias brutas de un POD por transacciones.
              Importancia: Función PRINCIPAL.
              Relationship: Este rubro aumenta conforme aumenta el número de PODS.
              Cadencia: Se calcula cada semestre.
@params:
    vector_representation [list]: Representación vectorial del escenario de operación. Revisar el método "operations.vector_representation()".

@result:
    [list]: De 7 posiciones con la información de las ganancias brutas obtenidas por transacciones. Cada posición contiene un [int].
        [pos_0]: Ganancias diarias en un día normal (L-J).
        [pos_1]: Ganancias diarias en un día viernes.
        [pos_2]: Ganancias en un mes normal (Uno de los tres primeros meses)
        [pos_3]: Ganancias durante los tres primeros meses o "periodo Longtail"
        [pos_4]: Ganancias en un día de la J24.
        [pos_5]: Ganancias durante toda la jornada J24.
        [pos_6]: Ganancias durante el semestre.
    """

    earnings_vector = []

    #Separa cada variable del vector que representa el escenario en variables individuales para un mejor manejo.
    price_array = price_vector(vector_representation[0]) #Crea un vector de precios según el precio base  por hora.
    longtail_capacity = vector_representation[1]
    focus_capacity = vector_representation[2]
    fullhouse_days = vector_representation[3]
    staying_time = vector_representation[4]
    leaving_time = vector_representation[5]
    LJ_hours = vector_representation[6]
    Fri_hours = vector_representation[7]
    start_date = vector_representation[8]
    J24_date = vector_representation[9]
    end_date = vector_representation[10]

    #El tiempo que dura cada operación sera el tiempo de estadía sumado al tiempo que demore en arreglarse el POD.
    operation_time = staying_time + leaving_time
    #Número de minutos que hay en un día normal de operación(L - J).
    daily_minutes = 60 * LJ_hours
    #Número de minutos que hay en un viernes.
    friday_minutes = 60 * Fri_hours

    #Número de operaciones realizadas a diario en un día normal de operación (L - J) aproximada por abajo.
    operations_per_day = daily_minutes // operation_time
    #Número de operaciones realizadas en un día viernes.
    friday_operations = friday_minutes // operation_time
    
    #Se obtiene el precio de cada operación.
    operation_price = price_per_time(staying_time, price_array)

    #Calculamos el número total de días y la frecuencia de cada día de la semana durante todos los 3 primeros meses.
    #No se tiene en cuenta el día en que inicia la J24. Tomamos el segundo elemento, el diccionario de frecuencias de cada día.
    longtail_days = operations.days_counter(start_date, J24_date)[1]
    longtail_days = dict(longtail_days)
    #Número de lunes, martes, miercoles y jueves en los 3 meses.
    mon_thu = longtail_days[operations.day_target(0)] + longtail_days[operations.day_target(1)] + longtail_days[operations.day_target(2)] + longtail_days[operations.day_target(3)]
    #Número de viernes en los 3 meses.
    fri = longtail_days[operations.day_target(4)]

    #Dinero ganado por pod un día normal (L - J)
    LJ_money = operation_price * operations_per_day
    #Dinero ganado por pod un viernes.
    friday_money = operation_price * friday_operations
    #Dinero ganado por un pod en un mes normal. (En UNO DE LOS TRES primeros meses)
    monthly_money = ((mon_thu / 3) * LJ_money) + ((fri / 3) * friday_money)
    #Dinero ganado por un pod en los tres primeros meses.
    #La parte a la derecha del "-"(negativo) representa la semana de descanso al semestre.
    #Pero si se saben el número de días festivos se pueden añadir a la expresión.
    longtail_money = ((mon_thu * LJ_money) + (fri * friday_money)) - ((4 * LJ_money) + friday_money)

    #Número de días de operación en el último mes (Jornada 24 horas o J24) según el número de días que se opere a la semana.
    #Las fechas colocadas corresponden al inicio de la J24 (J24_date) y al final del semestre (end_date)
    J24_days = focus_days(fullhouse_days, J24_date, end_date)
    #Número de minutos en un día completo de 24 horas.
    daily_focus_minutes = 60 * 24

    #Número de operaciones posibles en un día en la J24 aproximado por debajo.
    focus_operations_per_day = daily_focus_minutes // operation_time

    #Dinero ganado por un pod en un día de la J24.
    daily_focus_money = operation_price * focus_operations_per_day
    #Dinero ganado por un pod en el mes de la J24.
    focus_monthly_money = daily_focus_money * J24_days

    #Añade todos los valores de ganancia en un vector.
    earnings_vector.append(LJ_money)
    earnings_vector.append(friday_money)
    earnings_vector.append(monthly_money)
    earnings_vector.append(longtail_money)
    earnings_vector.append(daily_focus_money)
    earnings_vector.append(focus_monthly_money)

    #Ajusta los valores según el porcentaje de uso.
    for index,value in enumerate(earnings_vector):
        if (index <= 3):
            earnings_vector[index] = (value * longtail_capacity) / 100
        else:
            earnings_vector[index] = (value * focus_capacity) / 100

    #Ganancias totales en el semestre por pod.
    earnings = earnings_vector[3] + earnings_vector[5]
    earnings_vector.append(earnings)

    return earnings_vector