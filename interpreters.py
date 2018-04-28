'''
Author: Daniel F. Zuñiga H.
Date: 25/04/18
Place: @CyT, National University of Colombia

Description: This module is part of the UPODS project. It contains
             the methods providing an user-friendly explanation of
             results and data obtaining in the rest of the modules.
'''

import locale
import money_in
import money_out
import operations
from termcolor import colored

def operation_printer(answer, vector_representation, operations_vector, earnings_vector, implements_vector,
                      washing_vector, own_vector, dotation_vector, web_vector, rent_vector, liquidation_vector):
    """
@Description: De acuerdo a la respuesta del usuario, muestra la interpretación de toda la operación durante el semestre.

@params:
    answer [str]: La respuesta del usuario acerca de la profundidad de la información. Refierase al método "UI.difficulty_chooser()".
    vector_representation [list]: Representa el escenario. Refierase al método "operations.vector_representation()".
    operations_vector [list]: Contiene los calculos respecto al número de operaciones/clientes. Refierase al método "operations.operations_counter()".
    earnings_vector [list]: Contiene los calculos respecto a las ganancias. Refierase al método "money_in.earnings()".
    implements_vector [list]: Contiene los calculos respecto al costo de los implementos. Refierase al método "money_out.implements_cost()".
    washing_vector [list]: Contiene los calculos respecto a los costos de lavado. Refierase al método "money_out.washing_cost()".
    own_vector [list]: Contiene los calculos respecto a mi propio salario. Refierase al método "money_out.own_salary()".
    dotation_vector [list]: Contiene los calculos respecto a la dotación. Refierase al método "money_out.dotation_cost()".
    web_vector [list]: Contiene los calculos respecto a la página web. Refierase al método "money_out.web_cost()".
    rent_vector [list]: Contiene los calculos respecto a la renta de la bodega. Refierase al método money_out.rent_cost()".

@result: Text.

@TODO: Añadir a los parámetros los costos y ganancias aún no desarrolladas.
    """

    scenario = vector_representation
    operations_array = operations_vector
    earnings_array = earnings_vector
    implements_array = implements_vector
    washing_array = washing_vector
    own_array = own_vector
    dotation_array = dotation_vector
    web_array = web_vector
    rent_array = rent_vector
    liquidation_array = liquidation_vector

    #Mostrará sólo los balances.
    if (answer == 'N'):
        print("\n\tRESUMEN SEMESTRAL POR POD\n")
        scenario_full(scenario)
        clients_balance(operations_array,1)
        earnings_balance(earnings_array,1)
        implements_balance(implements_array,1)
        washing_balance(washing_array,1)
        own_balance(own_array,1)
        dotation_balance(dotation_array,1)
        web_balance(web_array,1)
        rent_balance(rent_array,1)
        print("\n\t\tDefinitiva\n")
        liquidation_balance(liquidation_array,1)
        print()

    #Mostrará todos los resultados.
    else:
        print("\n\t\t\tINFORME SEMESTRAL POR POD\n")
        scenario_full(scenario)
        clients_full(operations_array)
        print("\nGANANCIAS\n")
        earnings_full(earnings_array)
        print("\nCOSTOS\n")
        implements_full(implements_array)
        washing_full(washing_array)
        own_full(own_array)
        dotation_full(dotation_array)
        web_full(web_array)
        rent_full(rent_array)
        print("\n\t\tDefinitiva\n")
        liquidation_balance(liquidation_array, 1)
        print()


#INTERPRETES DE GANANCIAS

    #COMPLETOS

def earnings_full(earnings_vector):
    """
@Description: Interpretación del vector de ganancias.

@params:
    earnings_vector [list]: Contiene la información relacionada con las ganancias. Referenciese al método "money_in.earnings()"

@result: Text.
    """
    interpreted_vector = []

    # Da formato a cada valor del vector de ganancia y lo coloca en otro vector.
    for earning in earnings_vector:
        interpreted_vector.append(locale.currency(earning, grouping=True))

    print("Dinero ganado por pod un día normal (L - J): " + interpreted_vector[0])
    print("Dinero ganado por pod un viernes: " + interpreted_vector[1])
    print("Dinero ganado por un pod en un mes normal. (En uno de los tres primeros meses): " + interpreted_vector[2])
    print("Dinero ganado por un pod en los tres primeros meses: " + interpreted_vector[3])
    print("Dinero ganado por un pod en un día de la J24: " + interpreted_vector[4])
    print("Dinero ganado por un pod en el mes de la J24: " + interpreted_vector[5])
    print("Ganancias totales en el semestre por pod: " + interpreted_vector[6])

    #SOLO-BALANCE

def earnings_balance(earnings_vector, type):
    """
@Description: Muestra las ganancias por pod en un semestre.

@params:
    earnings_vector [list]: Contiene la información relacionada con las ganancias. Referenciese al método "money_in.earnings()"
    type [int]: Indica si el resultado a volver es el valor o la interpretación.

@result: Text.
    """

    returning_value = locale.currency(earnings_vector[6], grouping=True)

    if (type == 0):
        return earnings_vector[6]
    else:
        #Imprime el valor con formato.
        print("Ganancias:",colored(returning_value,'green'))



#INTERPRETES DE COSTOS

    #COMPLETOS

def implements_full(implements_vector):
    """
@Description: Interpretación del vector de costo de los implementos.

@params:
    implements_vector[list]: Contiene la información relacionada con los costos de los implementos. Referenciese al método "money_out.implements_cost()"

@result: Text
    """
    print("Costo de",implements_vector[1][0],"almohadas al semestre: ", locale.currency(implements_vector[0][0], grouping = True))
    print("Costo de",implements_vector[1][1],"cobijas al semestre: ", locale.currency(implements_vector[0][1], grouping = True))
    print("Costo de",implements_vector[1][2],"sabanas al semestre: ", locale.currency(implements_vector[0][2], grouping = True))
    print("Costo de",implements_vector[1][3],"fundas al semestre: ", locale.currency(implements_vector[0][3], grouping = True))
    print("Costo total de los implementos al semestre: ", locale.currency(implements_vector[0][4], grouping = True))
    print()


def washing_full(washing_vector):
    """
@Description: Interpretación del vector de costo de lavado.

@params:
    washing_vector[list]: Contiene la información relacionada con los costos de lavado. Referenciese al método "money_out.washing_cost()"

@result: Text
    """
    print("El costo por lavar",washing_vector[2],"libras de implementos a ",locale.currency(washing_vector[1], grouping=True)," cada libra durante el semestre es de:",locale.currency(washing_vector[0], grouping=True))
    print()


def own_full(salary_vector):
    """
@Description: Interpretación del vector de mi propio salario.

@params:
    salary_vector[list]: Contiene la información relacionada con mi propio salario. Referenciese al método "money_out.own_salary()"

@result: Text
    """
    if(salary_vector[0] == 1):
        print("Mi salario fue fijado en base a poder pagar la matricula semestral equivalente a",locale.currency(salary_vector[1], grouping=True))
        print("Lo cual equivaldría mensualmente a", locale.currency(salary_vector[2], grouping=True))
        print()
    elif(salary_vector[0] == 2):
        print("Mi salario fue fijado en base a poder pagar mis cuentas personales mensuales, es decir, mensualmente",locale.currency(salary_vector[2], grouping=True))
        print("Lo que en el semestre es equivalente a",locale.currency(salary_vector[1], grouping=True))
        print("Estos valores provienen de:\n")
        print("Arriendo de la casa:",locale.currency(salary_vector[3], grouping=True))
        print("Servicios de la casa:", locale.currency(salary_vector[4], grouping=True))
        print("Comida al mes (2 comidas de $4700 20 días al mes):", locale.currency(salary_vector[5], grouping=True))
        print()


def dotation_full(dotation_vector):
    """
@Description: Interpretación del vector de costo de la dotación.

@params:
    dotation_vector[list]: Contiene la información relacionada con los costos de dotación. Referenciese al método "money_out.dotation_cost()"

@result: Text
    """
    print("La dotación se realiza cada 4 meses, nuestra dotación comprende: Camiseta estampada de la marca y guantes de higiene.")
    print("Una caja de guantes cuesta:",locale.currency(dotation_vector[3], grouping=True))
    print("Una camiseta estampada cuesta",locale.currency(dotation_vector[2], grouping=True),". Son",locale.currency(dotation_vector[1], grouping=True),"empleados.")
    print("El costo total de la dotación por semestre es de:",locale.currency(dotation_vector[0], grouping=True))
    print()


def rent_full(rent_vector):
    """
@Description: Interpretación del vector de costo de arrendamiento de la bodega.

@params:
    rent_vector[list]: Contiene la información relacionada con los costos de arrendamiento de la bodega implementos.
    Referenciese al método "money_out.rent_cost()"

@result: Text
    """
    print("El arriendo mensual de un lugar para guardar las cosas es de:",locale.currency(rent_vector[1], grouping=True))
    print("El arriendo semestral estaría en:",locale.currency(rent_vector[0], grouping=True))
    print()

#Interpretación completa del coste de la página web.
def web_full(web_vector):
    """
@Description: Interpretación del vector de costo de la página web.

@params:
    web_vector[list]: Contiene la información relacionada con los costos de la página web. Referenciese al método "money_out.web_cost()"

@result: Text
    """
    print("El costo aproximado por el dominio y el hosting de la página web es de:",locale.currency(web_vector[0], grouping=True))
    print()

    #SOLO-BALANCE

def implements_balance(implements_vector, type):
    """
@Description: Muestra los costos de compra de implementos.

@params:
    implements_vector [list]: Contiene la información relacionada con los costos de compra de implements.
    Referenciese al método "money_out.implements_cost()"
    type [int]: Indica si el resultado a volver es el valor (0) o la interpretación.

@result: Text.
    """
    if (type == 0):
        return implements_vector[0][4]
    else:
        print("Costo implementos:", colored(locale.currency(implements_vector[0][4], grouping=True), 'red'))


def washing_balance(washing_vector, type):
    """
@Description: Muestra los costos de lavado de implementos.

@params:
    washing_vector [list]: Contiene la información relacionada con los costos de lavado. Referenciese al método "money_out.washing_cost()"
    type [int]: Indica si el resultado a volver es el valor (0) o la interpretación.

@result: Text.
    """
    if (type == 0):
        return washing_vector[0]
    else:
        print("Costo de lavado:", colored(locale.currency(washing_vector[0], grouping = True), 'red'))


def own_balance(salary_vector, type):
    """
@Description: Muestra los costos de mi propio salario.

@params:
    salary_vector [list]: Contiene la información relacionada con mi propio salario. Referenciese al método "money_out.own_salary()"
    type [int]: Indica si el resultado a volver (0) es el valor o la interpretación.

@result: Text.
    """
    if (type == 0):
        return salary_vector[1]
    else:
        print("Salario propio:", colored(locale.currency(salary_vector[1], grouping = True), 'red'))


def dotation_balance(dotation_vector, type):
    """
@Description: Muestra los costos de dotación.

@params:
    dotation_vector [list]: Contiene la información relacionada con los costos de dotación. Referenciese al método "money_out.dotation_cost()"
    type [int]: Indica si el resultado a volver (0) es el valor o la interpretación.

@result: Text.
    """
    if (type == 0):
        return dotation_vector[0]
    else:
        print("Costo de dotación:", colored(locale.currency(dotation_vector[0], grouping=True),'red'))


def rent_balance(rent_vector, type):
    """
@Description: Muestra los costos de renta de la bodega.

@params:
    rent_vector [list]: Contiene la información relacionada con los costos de la renta de la bodega. Referenciese al método "money_out.rent_cost()"
    type [int]: Indica si el resultado a volver (0) es el valor o la interpretación.

@result: Text.
    """
    if (type == 0):
        return rent_vector[0]
    else:
        print("Costo de arriendo:",colored(locale.currency(rent_vector[0], grouping=True),'red'))


def web_balance(web_vector, type):
    """
@Description: Muestra los costos de operación/mantenimient de la página web.

@params:
    web_vector [list]: Contiene la información relacionada con los costos de la página web. Referenciese al método "money_out.web_cost()"
    type [int]: Indica si el resultado a volver (0) es el valor o la interpretación.

@result: Text.
    """
    if (type == 0):
        return web_vector[0]
    else:
        print("Costo web:",colored(locale.currency(web_vector[0], grouping=True),'red'))



#INTERPRETES DE OPERACIÓN

    #COMPLETOS

def scenario_full(vector_representation):
    """
@Description: Interpretación del vector de representación del escenario. No existe "scenario_balance", no es necesario.

@params:
    vector_representation [list]: Contiene la información relacionada el escenario. Referenciese al método "operations.vector_representation()"

@result: Text.
    """
    precio = money_in.price_per_time(vector_representation[4], money_in.price_vector(vector_representation[0]))
    print("Operación comenzando el",vector_representation[8],"con el inicio de la J24 el",vector_representation[9],"y terminando el", vector_representation[10])
    print("Trabajando",vector_representation[6],"horas de lunes a jueves y",vector_representation[7],"horas los viernes. Y",vector_representation[3],"días a la semana durante la J24.")
    print("Cobrando $", precio,"por un tiempo de estadía de",vector_representation[4],"minutos.")
    print("Teniendo en cuenta que el tiempo de desalojo/preparación es de", vector_representation[5],"minutos.")
    print("Operando al", vector_representation[1],"% de la capacidad durante los tres primeros meses y al", vector_representation[2],"% de la capacidad en la J24.\n")


def clients_full(operations_vector):
    """
@Description: Interpretación del vector de operaciones.

@params:
    operations_vector [list]: Contiene la información relacionada con el número de operaciones. Referenciese al método "operations.operations_counter()"

@result: Text.
    """
    print("OPERACIONES\n")
    print("Número de operaciones/clientes un día normal (L-J):", operations_vector[0])
    print("Número de operaciones/clientes un viernes:", operations_vector[1])
    print("Número de operaciones/clientes cada mes (En los primeros tres (3) meses):", operations_vector[2])
    print("Número de operaciones/clientes un día de la J24:", operations_vector[3])
    print("Número de operaciones/clientes en la J24:", operations_vector[4])
    print("Número de operaciones/clientes en el semestre:", operations_vector[5])
    print()

    #SOLO-BALANCE

def clients_balance(operations_vector, type):
    """
@Description: Muestra el número de operaciones al semestre.

@params:
    operations_vector [list]: Contiene la información relacionada con las operaciones . Referenciese al método "operations.operations_counter()"
    type [int]: Indica si el resultado a volver es el valor (0) o la interpretación.

@result: Text.
    """
    if(type == 0):
        return operations_vector[5]
    else:
        print("Número de operaciones/clientes:", operations_vector[5])


def liquidation_balance(liquidation_vector, type):
    """
@Description: Devuelve la interpretación/resumen de la liquidación de un escenario. No existe "liquidation_full", no es necesario.

@params:
    liquidation_vector [list]: Contiene la información relacionada con la liquidación de un escenario.
    type [int]: Indica si el resultado a volver es el valor (0) o la interpretación.

@result:
    Dependiendo de el tipo que haya elegido el usuario, devuelve el valor [int] o una interpretación textual.
    """

    if(type == 0):
        return liquidation_vector[0]
    else:
        if (liquidation_vector[0] < 0):
            semester = colored(locale.currency(liquidation_vector[0], grouping=True), 'red')
        else:
            semester = colored(locale.currency(liquidation_vector[0], grouping=True),'green')

        if (liquidation_vector[1] < 0):
            anual = colored(locale.currency(liquidation_vector[1], grouping=True), 'red')
        else:
            anual = colored(locale.currency(liquidation_vector[1], grouping=True),'green')

        print("Liquidación semestral:", semester)
        print("Liquidación anual:", anual)

def tipping_balance(tipping_vector, type):
    """
@Description: Devuelve la interpretación/resumen del punto de equilibrio de un escenario. No existe "tripping_full", no es necesario.

@params:
    tipping_vector [list]: Contiene la información relacionada con el punto de equilibrio de un escenario.
    type [int]: Indica si el resultado a volver es el valor (0) o la interpretación.

@result:
    Dependiendo de el tipo que haya elegido el usuario, devuelve el valor [int] o una interpretación textual.
    """
    if (type == 0):
        return tipping_vector[0]
    else:
        print("Se requieren de",tipping_vector[0],"pods para poder general utilidades en este escenario.")
        print("Usando este número de PODS generarías",tipping_vector[1], "en utilidades.")
