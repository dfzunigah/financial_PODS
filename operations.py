'''
Author: Daniel F. Zuñiga H.
Date: 25/04/18
Place: @Biblioteca Central, National University of Colombia

Description: This module is part of UPODS project. It contains other
             operations not directly related with income/outcome.
'''

from collections import Counter
import datetime
import money_in

def vector_representation(price, capacity, fullhouse_days, staying_time, leaving_time, LJ_hours, Fri_hours, start_date, J24_date, end_date):
    """
@Description: Permite representar de manera vectoral un escenario. Función PRINCIPAL.

@params:
    price [int]: Precio base por hora.
    capacity [int]: Porcentaje (0 - 100 %) de la capacidad a la que se opera.
    fullhouse_days [int]: Número de días por semana que se opera durante la J24.
    staying_time [int]: Tiempo de estadía, en minutos, en el pod por transacción.
    leaving_time [int]: Tiempo de despeje, en minutos, del pod.
    LJ_hours [int]: Número de horas que se trabajan diario de lunes a jueves.
    Fri_hours [int]: Número de horas que se trabajan un viernes.
    start_date [datetime]: Fecha en la que se inicia la operación.
    J24_date [datetime]: Fecha en la que se inicia la J24.
    end_date [datetime]: Fecha en la que termina la operación.

@result:
    [list]: De 10 posiciones correspondientes a los parámetros de la función agregados en orden.
    """

    vector = []

    vector.append(price)
    vector.append(capacity)
    vector.append(fullhouse_days)
    vector.append(staying_time)
    vector.append(leaving_time)
    vector.append(LJ_hours)
    vector.append(Fri_hours)
    vector.append(start_date)
    vector.append(J24_date)
    vector.append(end_date)

    return vector


def operations_counter(vector_representation):
    """
@Description: Realiza los calculos acerca de cuantas operaciones se realizan por POD durante la operación del proyecto.
              Estos valores aumentan conforme aumenta el número de PODS. Función PRINCIPAL.

@params:
    vector_representation [list]: Representación vectorial del escenario de operación. Revisar el método "math.vector_representation()".

@result:
    [list]: de 6 posiciones con la información del número de clientes. Cada posición contiene un [int].
        [pos_0]: Operaciones/clientes diarias en un día normal (L-J)
        [pos_1]: Operaciones/clientes diarias un viernes.
        [pos_2]: Operaciones/clientes mensuales en uno de los 3 primeros mes o "periodo longtail".
        [pos_3]: Operaciones/clientes en los 3 primeros meses o en el "periodo longtail".
        [pos_4]: Operaciones/clientes en la J24.
        [pos_5]: Operaciones/clientes durante el semestre.
    """

    operations_vector = []

    # Separa cada variable del vector en variables individuales para mejor manejo.
    capacity = vector_representation[1]
    fullhouse_days = vector_representation[2]
    staying_time = vector_representation[3]
    leaving_time = vector_representation[4]
    LJ_hours = vector_representation[5]
    Fri_hours = vector_representation[6]
    start_date = vector_representation[7]
    J24_date = vector_representation[8]
    end_date = vector_representation[9]

    # El tiempo que dura cada operación será el tiempo de estadía sumado al tiempo que demore en arreglarse el POD.
    operation_time = staying_time + leaving_time
    # Número de minutos que hay en un día normal de operación (L - J).
    daily_minutes = 60 * LJ_hours
    # Número de minutos que hay en un viernes.
    friday_minutes = 60 * Fri_hours

    # Número de operaciones realizadas a diario en un día normal de operación (L - J) aproximada por abajo.
    operations_per_day = daily_minutes // operation_time
    # Número de operaciones realizadas en un día viernes.
    friday_operations = friday_minutes // operation_time

    # Calculamos el número total de días y la frecuencia de cada día de la semana durante todos los 3 primeros meses.
    # No se tiene en cuenta el día en que inicia la J24. Tomamos el segundo elemento, el diccionario de frecuencias de cada día.
    longtail_days = days_counter(start_date, J24_date)[1]
    # Número de lunes, martes, miercoles y jueves en los 3 meses.
    mon_thu = longtail_days['lun'] + longtail_days['mar'] + longtail_days['mié'] + longtail_days['jue']
    # Número de viernes en los 3 meses.
    fri = longtail_days['vie']

    # Número de operaciones realizadas en un mes normal (UNO DE LOS 3 PRIMEROS MESES).
    monthly_operations = ((mon_thu / 3) * operations_per_day) + ((fri / 3) * friday_operations)

    # Número de días de operación en el último mes (Jornada 24 horas) según el número de días que se opere a la semana.
    J24_days = money_in.focus_days(fullhouse_days, J24_date, end_date)
    # Número de minutos en un día completo de 24 horas.
    daily_focus_minutes = 60 * 24
    # Número de operaciones posibles en un día en la J24 aproximado por debajo.
    focus_operations_per_day = daily_focus_minutes // operation_time
    # Número de operaciones realizadas en la J24.
    J24_operations = focus_operations_per_day * J24_days

    # Número de operaciones realizadas en un semestre.
    total_operations = (mon_thu * operations_per_day) + (fri * friday_operations) + J24_operations

    # Adjunto todos los resultados en un vector.
    operations_vector.append(operations_per_day)
    operations_vector.append(friday_operations)
    operations_vector.append(monthly_operations)
    operations_vector.append(focus_operations_per_day)
    operations_vector.append(J24_operations)
    operations_vector.append(total_operations)

    # Ajusta los valores según el porcentaje de uso.
    for index, value in enumerate(operations_vector):
        operations_vector[index] = (value * capacity) / 100

    return operations_vector


def days_counter(date_from, date_to):
    """
@Description: Realiza operaciones entre dos fechas. No se tiene en cuenta un día (De lunes a martes hay un día, no dos). Función PRINCIPAL.

@params:
    date_from [datetime]: Fecha en la que inicia un evento.
    date_to [datetime]: Fecha en la que termina un evento.

@result:
    [list]: de 2 posiciones.
        [pos_0]: [int] Devuelve el número de días que hay entre dos fechas sin contar uno de los días provistos (Mirar descripción).
        [pos_1]: [dict] Con la frecuencia de cada día de la semana. Las llaves son las 3 primeras letras del día en ingles (Mon, Tue, ...)
    """

    #Número de días entre dos fechas sin contar un día. (Por ejemplo, de lunes a martes hay un día, no dos)
    total_days = (date_to - date_from)
    total_days = total_days.days

    #Contador en forma de diccionario.
    weekdays = Counter()
    #Agrega cada día del rango provisto (CONTANDO TODOS LOS DÍAS, por eso el +1), según el día de la semana.
    for i in range((date_to - date_from).days+1):
        weekdays[(date_from + datetime.timedelta(i)).strftime('%a')] += 1

    #Devolvemos un vector de 2 posiciones. (return total_days, weekdays == return [total_days, weekdays])
    return total_days, weekdays

