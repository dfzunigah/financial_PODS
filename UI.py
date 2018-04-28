'''
Author: Daniel F. Zuñiga H.
Date: 25/04/18
Place: @Apt, Bogotá.

Description: This module is part of UPODS project. It's
             the module where text-UI is defined

'''

import operations
import datetime
import interpreters
import money_out
import money_in

def input_scenario():
    """
@Description: Pide al usuario todos los datos necesarios para definir un escenario. Función PRINCIPAL.

@params: None

@result:
    [list]: Genera la representación vectorial del escenario. Refierase al método "operations.vector_representation()".
    """

    #Entrada de los datos
    print("\nPor favor, describe el escenario:\n")
    #Opciones: $3000, $2500, $2000
    try:
        price = int(input("Introduzca el precio por hora ($3k,$2.5k,$2k): $"))
        longtail_capacity = int(input("Introduzca el porcentaje de capacidad de uso durante los 3 primeros meses (0 - 100%): "))
        focus_capacity = int(input("Introduzca el porcentaje de capacidad de uso durante J24 (0 - 100%): "))
        fullhouse_days = int(input("Introduzca número de días de operación durante la jornada de biblioteca 24H (5,6,7): "))
        staying_time = int(input("Introduzca el tiempo de permanencia en minutos (60,45,30): "))
        leaving_time = int(input("Introduzca el tiempo de desalojo en minutos (0,5,10): "))
        LJ_hours = int(input("Introduzca el número de horas trabajadas de lunes a viernes: "))
        Fri_hours = int(input("Introduzca el número de horas trabajadas un viernes: "))
        start_date = date_parser("inicio de operación")
        J24_date = date_parser("inicio J24")
        end_date = date_parser("fin de operación")
        pods = int(input("Número de pods operando: "))
    except:
        print("Nea, sea serio. Revise bien si lo que colocó es lógico.")

    #Creación del vector de representación del escenario.
    vector_array = operations.vector_representation(price, longtail_capacity, focus_capacity, fullhouse_days, staying_time, leaving_time, LJ_hours, Fri_hours, start_date, J24_date, end_date, pods)
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
@Description: Pide al usuario qué tipo de información le gustaría ver: Completa o sólo resultados. Función auxiliar.

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

def main_menu():
    """
@Description: La lógica con la que se maneja la interfaz del usuario. Función PRINCIPAL.

@params: None.

@result: Texto, llamadas a funciones auxiliares.
    """

    answer = ""
    #Imprime el menú principal
    print("Bienvenid@, ¿Qué te gustaría hacer?\n")
    print("1. Simular un escenario.")
    print("2. Salir")
    #Respuesta inclusiva. Hasta que no sea correcta no avanza.
    while not (answer == "1" or answer =="2"):
        answer = input("¿Tu respuesta? (1 o 2): ")

    #De acuerdo a la respuesta del usuario se lleva a cabo determinada acción.
    if (answer == "2"):
        exit(0)
    else:
        #El usuario crea el escenario.
        scenario = input_scenario()

        # Realización de todas las operaciones.
        operations_array = operations.operations_counter(scenario)
        earnings_array = money_in.pod_earnings(scenario)
        implements_array = money_out.implements_cost(operations_array)
        washing_array = money_out.washing_cost(operations_array[-1])
        own_array = money_out.own_salary()
        dotation_array = money_out.dotation_cost()
        web_array = money_out.web_cost()
        rent_array = money_out.rent_cost()

        pod_earnings = interpreters.earnings_balance(earnings_array, 0)
        implements_cost = interpreters.implements_balance(implements_array, 0)
        washing_cost = interpreters.washing_balance(washing_array, 0)
        own_cost = interpreters.own_balance(own_array, 0)
        dotation_cost = interpreters.dotation_balance(dotation_array, 0)
        web_cost = interpreters.web_balance(web_array, 0)
        rent_cost = interpreters.rent_balance(rent_array, 0)

        liquidation_array = operations.liquidation(scenario[-1], pod_earnings, implements_cost, washing_cost, own_cost,
                                                   dotation_cost, web_cost, rent_cost)


        #El usuario decide qué quiere realizar.
        setup = action_chooser()
        if (len(setup) == 2):
            #El usuario quiere un informe sobre el desempeño del negocio.
            if (setup[0] == "1"):
                interpreters.operation_printer(setup[1], scenario, operations_array, earnings_array, implements_array,
                                               washing_array, own_array, dotation_array, web_array, rent_array,
                                               liquidation_array)
            #El usuario quiere consultar un tópico en especifico.
            elif (setup[0] == "2"):
                #Nos devuelve cúal fue el tópico sobre el que quiere consultar el usuario.
                topic = topic_menu()
                #Según el tópico y su respuesta de dificultad, se llama al método indicado.
                if(topic == "1"):
                    if(setup[1] == "Y"):
                        interpreters.clients_full(operations_array)
                    else:
                        interpreters.clients_balance(operations_array,1)
                elif(topic == "2"):
                    interpreters.liquidation_balance(liquidation_array,1)
                elif (topic == "3"):
                    if (setup[1] == "Y"):
                        interpreters.earnings_full(earnings_array)
                    else:
                        interpreters.earnings_balance(earnings_array,1)
                elif (topic == "4"):
                    if (setup[1] == "Y"):
                        interpreters.implements_full(implements_array)
                    else:
                        interpreters.implements_balance(implements_array,1)
                elif (topic == "5"):
                    if (setup[1] == "Y"):
                        interpreters.washing_full(washing_array)
                    else:
                        interpreters.washing_balance(washing_array,1)
                elif (topic == "6"):
                    if (setup[1] == "Y"):
                        interpreters.own_full(own_array)
                    else:
                        interpreters.own_balance(own_array,1)
                elif (topic == "7"):
                    if (setup[1] == "Y"):
                        interpreters.dotation_full(dotation_array)
                    else:
                        interpreters.dotation_balance(dotation_array,1)
                elif (topic == "8"):
                    if (setup[1] == "Y"):
                        interpreters.rent_full(rent_array)
                    else:
                        interpreters.rent_balance(rent_array,1)
                else:
                    if (setup[1] == "Y"):
                        interpreters.web_full(web_array)
                    else:
                        interpreters.web_balance(web_array,1)
        else:
            #Calculo del vector de punto de equilibrio.
            tipping_vector = operations.tipping_point(pod_earnings, implements_cost, washing_cost, own_cost, dotation_cost,
                                          web_cost, rent_cost)
            #Interpretación del punto de equilibrio.
            interpreters.tipping_balance(tipping_vector,1)



def action_chooser():
    """
@Description: Muestra un menú auxiliar para elegir qué hacer con el escenario descrito. Función auxiliar.

@params: None.

@Result: Texto.
    [list]: De 2 posiciones indicando qué acción quiere realizar y qué dificultad eligió para ello.
    Nota: En caso de haber elegido la tercera acción sólo devuelve este valor, no un vector.
    """

    answer = ""
    #Imprime el menú de acciones.
    print("\n¿Qué deseas averiguar?\n")
    print("1. Un informe sobre el desempeño del negocio.")
    print("2. Me gustaría consultar un tópico en especifico.")
    print("3. Quiero saber cuál es el punto de inflexión para mi escenario.")

    #Respuesta inclusiva. Hasta que no sea correcta no avanza.
    while not (answer == "1" or answer == "2" or answer == "3"):
        answer = input("¿Tu respuesta? (1,2 o 3): ")

    #De acuerdo a la elección del usuario devuelve un vector sobre qué tipo de acción quiere hacer y su dificultad.
    if(answer == "1"):
        choise1 = difficulty_chooser()
        return answer, choise1
    elif(answer == "2"):
        choise2 = difficulty_chooser()
        return answer, choise2
    else:
        return answer


def topic_menu():
    """
@Description: Permite elegir al usuario un tópico especifico para consultar. Realiza la intepretación.
@params: None.
@result:
    [str]: Retorna cual fue la elección que hizo el usuario.
    """
    print("\n¿Sobre qué te gustaría aprender?\n")
    print("1. Acerca del número de clientes.")
    print("2. Sobre el balance del proyecto.")
    print("3. Ganancias semestrales.")
    print("4. Costos de implementos.")
    print("5. Costos de lavado.")
    print("6. Costos propios.")
    print("7. Costos de dotación.")
    print("8. Costos de renta.")
    print("9. Costos de la plataforma web.")

    topic = ""
    while not (topic == "1" or topic == "2" or topic == "3" or topic == "4" or topic == "5" or topic == "6" or topic == "7" or
               topic == "8" or topic == "9"):
        topic = input("\n¿Tu respuesta? (1 - 9):")

    return topic

def goback_menu():
    """
@Description: Un simple menú preguntando si quiere volver al menú principal. Función auxiliar.

@params: None.
@result: Exit(0) ó un booleano True, indicando que sí quiere volver al menú principal.

    """
    print("")
    goback = input("¿Te gustaría volver al menú inicial? (Y/N):")
    goback = goback.upper()
    if (goback == "N"):
        exit(0)
    else:
        return True