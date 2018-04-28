'''
Author: Daniel F. Zuñiga H.
Date: 25/04/18
Place: @Apt, Bogotá.

Description: This module is part of UPODS project. It's
             the module where text-UI is defined

'''

import operations
import datetime

def input_scenario():
    """
@Description: Pide al usuario todos los datos necesarios para definir un escenario. Función PRINCIPAL.

@params: None

@result:
    [list]: Genera la representación vectorial del escenario. Refierase al método "operations.vector_representation()".
    """

    #Entrada de los datos
    #Opciones: $3000, $2500, $2000
    price = int(input("Introduzca el precio ($3k,$2.5k,$2k): $"))
    capacity = int(input("Introduzca el porcentaje de capacidad de uso (0 - 100%): "))
    fullhouse_days = int(input("Introduzca número de días de operación durante la jornada de biblioteca 24H (5,6,7): "))
    staying_time = int(input("Introduzca el tiempo de permanencia en minutos (60,45,30): "))
    leaving_time = int(input("Introduzca el tiempo de desalojo en minutos (0,5,10): "))
    LJ_hours = int(input("Introduzca el número de horas trabajadas de lunes a viernes: "))
    Fri_hours = int(input("Introduzca el número de horas trabajadas un viernes: "))
    start_date = date_parser("inicio de operación")
    J24_date = date_parser("inicio J24")
    end_date = date_parser("fin de operación")

    #Creación del vector de representación del escenario.
    vector_array = operations.vector_representation(price, capacity, fullhouse_days, staying_time, leaving_time, LJ_hours, Fri_hours, start_date, J24_date, end_date)
    return vector_array


def date_parser(date_event):
    """
@Description: Pide al usuario el día, mes y año de un evento. Función auxiliar.

@params:
    date_event [str]: Es el texto que identifica el evento.

@result:
    [date]: Una fecha con los parámetros ingresados.
    """
    d_string = 'Día de ' + date_event + ': '
    m_string = 'Mes de ' + date_event + ': '
    y_string = 'Año de ' + date_event + ': '
    #Entrada de los datos
    day = int(input(d_string))
    month = int(input(m_string))
    year = int(input(y_string))

    #Conformación de la fecha y retorno.
    date = datetime.date(year, month, day)
    return  date


def difficulty_chooser():
    """
@Description: Pide al usuario qué tipo de información le gustaría ver: Completa o sólo resultados. Función PRINCIPAL.

@params: None

@result:
    [str]: Un carácter indicando la respuesta.
    """
    answer = ''
    print("\n¿Deseas ver todos los detalles de las operaciones? (Y/N)")
    print("Si seleccionas 'Y' verás UN INFORME.")
    print("Si seleccionas 'N' verás UN RESUMEN.")

    #Operación inclusiva: Es necesario que la respuesta concuerde con alguno de los casos para continuar.
    while not(answer == 'Y' or answer == 'N'):
        answer = input("Tu respuesta: ")
        answer = answer.upper()

    return answer