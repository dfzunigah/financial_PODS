'''
Author: Daniel F. Zuñiga H.
Date: 26/04/18
Place: @Biblioteca Central, National University of Colombia

Description: This module is part of UPODS project. It contains other
             operations not directly related with income/outcome.
'''
import calendar
from collections import Counter
import datetime
import money_in
import money_out
import interpreters

def vector_representation(price, longtail_capacity, focus_capacity, fullhouse_days, staying_time, leaving_time, LJ_hours, Fri_hours, start_date, J24_date, end_date, pods):
    """
@Description: Permite representar de manera vectoral un escenario. Función PRINCIPAL.

@params:
    price [int]: Precio base por hora.
    longtail_capacity [int]: Porcentaje (0 - 100 %) de la capacidad a la que se opera durante el "periodo de longtail".
    focus_capacity [int]: Porcentaje (0 - 100 %) de la capacidad a la que se opera durante la J24.
    fullhouse_days [int]: Número de días por semana que se opera durante la J24.
    staying_time [int]: Tiempo de estadía, en minutos, en el pod por transacción.
    leaving_time [int]: Tiempo de despeje, en minutos, del pod.
    LJ_hours [int]: Número de horas que se trabajan diario de lunes a jueves.
    Fri_hours [int]: Número de horas que se trabajan un viernes.
    start_date [datetime]: Fecha en la que se inicia la operación.
    J24_date [datetime]: Fecha en la que se inicia la J24.
    end_date [datetime]: Fecha en la que termina la operación.
    pods[int]: Número de pods en funcionamieno durante la operación.

@result:
    [list]: De 12 posiciones correspondientes a los parámetros de la función agregados en orden.
    """

    vector = []

    vector.append(price)
    vector.append(longtail_capacity)
    vector.append(focus_capacity)
    vector.append(fullhouse_days)
    vector.append(staying_time)
    vector.append(leaving_time)
    vector.append(LJ_hours)
    vector.append(Fri_hours)
    vector.append(start_date)
    vector.append(J24_date)
    vector.append(end_date)
    vector.append(pods)

    return vector


def operations_counter(vector_representation):
    """
@Description: Realiza los calculos acerca de cuantas operaciones se realizan por POD durante la operación del proyecto.
              Estos valores aumentan conforme aumenta el número de PODS. Función PRINCIPAL.

@params:
    vector_representation [list]: Representación vectorial del escenario de operación. Revisar el método "operations.vector_representation()".

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
    longtail_days = dict(longtail_days)
    try:
        # Número de lunes, martes, miercoles y jueves en los 3 meses.
        mon_thu = longtail_days[day_target(0)] + longtail_days[day_target(1)] + longtail_days[day_target(2)] + longtail_days[day_target(3)]
        # Número de viernes en los 3 meses.
        fri = longtail_days[day_target(4)]
    except:
        print ("Eche monda, revisa las fechas ingresadas (Como mínimo la operación debe ser mayor a una semana.)")

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

    # Adjunto todos los resultados en un vector.
    operations_vector.append(operations_per_day)
    operations_vector.append(friday_operations)
    operations_vector.append(monthly_operations)
    operations_vector.append(focus_operations_per_day)
    operations_vector.append(J24_operations)

    # Ajusta los valores según el porcentaje de uso para el caso de el "periodo longtail" y para el caso de J24.
    for index, value in enumerate(operations_vector):
        if(index <= 3):
            operations_vector[index] = (value * longtail_capacity) / 100
        else:
            operations_vector[index] = (value * focus_capacity) / 100

    # Número de operaciones realizadas en un semestre.
    #total_operations = ((((mon_thu * operations_per_day) + (fri * friday_operations)) * longtail_capacity) / 100) + ((J24_operations * focus_capacity) / 100)
    total_operations = (3 * operations_vector[2]) + operations_vector[4]
    operations_vector.append(total_operations)

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

def day_target(number):
    """
@Description: Este método permite encontrar el nombre de un día de acuerdo a la locación del usuario y comprimirla en un formato. Función auxiliar.

@params:
    number [int]: Número del día, siendo 0 el lunes.

@result:
    [str]: Devuelve los primeros carácteres + un punto del nombre del día.
    """
    string = calendar.day_name[number]
    string = string[:3] + "."

    return string

def liquidation(pods, pod_earnings, implements_cost, washing_cost, own_cost, dotation_cost, web_cost, rent_cost):
    """
@Description: Devuelve un vector que contiene información acerca de la liquidación del proyecto.

@params:

@result:
    [list]: De 2 posiciones con la liquidación semestral y la liquidación anual.
    """
    liquidation_vector = []

    #Calculos semestrales
    semester_earnings = pods * pod_earnings
    semester_costs = implements_cost + washing_cost + own_cost + dotation_cost + web_cost + rent_cost
    semester_liquidation = semester_earnings - semester_costs

    #Calculos anuales
    anual_earnings = 2 * semester_earnings
    anual_costs = (2 * semester_costs) - implements_cost
    anual_liquidation = anual_earnings - anual_costs

    liquidation_vector.append(semester_liquidation)
    liquidation_vector.append(anual_liquidation)

    return liquidation_vector

def tipping_point(pod_earnings, implements_cost, washing_cost, own_cost, dotation_cost, web_cost, rent_cost):
    """
@Description: Para determinado caso, encuentra el "punto de equilibrio", es decir, el número de PODS necesarios por semestre para hacer rentable el negocio.

@params:
    pod_earnings [int]: Ganancias por pod en un semestre.
    implements_cost [int]: Costo semestral de la compra de implementos.
    washing_cost [int]: Costo del lavado de los implementos.
    own_cost [int]: Costo semestral de mi propio salario.
    dotation_cost [int]: Costo semestral de la dotación de marca.
    web_cost [int]: Costo semestral de la página web.
    rent_cost [int]: Costo de la renta de la bodega por semestre.
@result:
    [list]: De 2 posiciones [int] que contiene el número de pods que hacen sostenible el negocio y las utilidades obtenidas.
    """

    tipping_vector = []
    #Variable auxiliar que guardará el valor de la liquidación.
    balance = -1
    #Variable auxiliar que permite contar el número de PODS.
    flag = 1
    #Número máximo de pods que se pueden manejar en una única ubicación.
    place_maxpods = 12
    #Siga probando un número diferente de PODS mientras no tengamos resultados positivos y siempre y cuando no pasemos de la cantidad máxima de pods por lugar.
    while (balance < 0 and flag <= place_maxpods) :
        balance = liquidation(flag, pod_earnings, implements_cost, washing_cost, own_cost, dotation_cost, web_cost, rent_cost)[0]
        flag += 1

    #Agrega el número de PODS y el balance alcanzado con ese número de PODS al vector, luego devuelve el vector.
    tipping_vector.append(flag - 1)
    tipping_vector.append(balance)

    return tipping_vector