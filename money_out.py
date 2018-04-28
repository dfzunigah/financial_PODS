'''
Author: Daniel F. Zuñiga H.
Date: 25/04/18
Place: @Biblioteca Central, National University of Colombia

Description: This module is part of UPODS project. It provides all expenses
             operations. The results are returned in a easy-to-process vector.
'''

import math

def implements_cost(operations_vector):
    """
@Description: Calcula los costes y la cantidad de implementos utilizados (Almohadas, cobijas, fundas, sabanas).
              Importancia: Función PRINCIPAL.
              Relationship: Este rubro es por pod. Aumenta conforme aumenten las operaciones.
              Cadencia: Se calcula cada año.

@params:
    operations_vector [list]: Vector de 6 posiciones, todos de tipo [int]. Referirse al método "operations.operations_counter"

@result:
    [list]: De 2 posiciones, cada una conteniendo una lista.
        [pos_0]: [list] De 5 posiciones, posee información acerca de los costos de los implementos. Todos sus elementos son [int].
            [pos_0]: Coste de todas las almohadas.
            [pos_1]: Coste de todas las cobijas.
            [pos_2]: Coste de todas las sabanas.
            [pos_3]: Coste de todas las fundas.
            [pos_4]: Coste total de todos los implementos.
        [pos_1]: [list] de 4 posiciones, posee información acerca de la cantidad de implementos. Todos sus elementos son [int].
            [pos_0]: Número total de almohadas.
            [pos_1]: Número total de cobijas.
            [pos_2]: Número total de sabanas.
            [pos_3]: Número total de fundas.

@TODO: Mejorar el calculo del costo de implementos, tener en cuenta el tiempo de uso afuera y más de un ciclo de vida.
    """
    implements_cost = []
    implements_stock = []
    
    #Número máximo de usos por almohada: 3 meses = (365 / 12) * 3 = 91.25 usos.
    pillow_maxuses = 91
    #Número máximo de usos por cobija. (2 semanas)
    blanket_maxuses = 14
    #Número máximo de usos por sabana. (2 semanas)
    sheet_maxuses = 14
    #Número máximo de usos por fundas. (3 días)
    cover_maxuses = 3
    
    #Precio al detal de una sola almohada.
    retail_pillow = 10000
    #Precio al detal de una cobija.
    retail_blanket = 5000
    #Precio al detal de una sabana.
    retail_sheet = 14500
    #Precio al detal de una funda.
    retail_cover = 1000
    
    #Porcentaje de descuento obtenido por comprar al por mayor.
    discount = 20
    #Precio de cada implemento con descuento.
    stock_pillow = retail_pillow - ((retail_pillow * discount) / 100)
    stock_blanket = retail_blanket - ((retail_blanket * discount) / 100)
    stock_sheet = retail_sheet - ((retail_sheet * discount) / 100)
    stock_cover = retail_cover - ((retail_cover * discount) / 100)

    #Operaciones totales realizadas en el semestre.
    total_operations = operations_vector[5]

    #Número de almohadas, sabanas, cobijas y fundas necesarias: Número de operaciones / Máximos usos aproximada por arriba.
    total_pillows = math.ceil(total_operations / pillow_maxuses)
    total_blankets = math.ceil(total_operations / blanket_maxuses)
    total_sheets = math.ceil(total_operations / sheet_maxuses)
    total_covers = math.ceil(total_operations / cover_maxuses)
    
    #Costo total de las almohadas, cobijas, sabanas y fundas por independiente en el semestre.
    pillows_cost = total_pillows * stock_pillow
    blankets_cost = total_blankets * stock_blanket
    sheets_cost = total_sheets * stock_sheet
    covers_cost = total_covers * stock_cover
    #Costo total de los implementos en conjunto
    total_cost = pillows_cost + blankets_cost + sheets_cost + covers_cost

    #Se añaden todos los costos a un vector de costos.
    implements_cost.append(pillows_cost)
    implements_cost.append(blankets_cost)
    implements_cost.append(sheets_cost)
    implements_cost.append(covers_cost)
    implements_cost.append(total_cost)
    #Se añade el número de implementos a un vector.
    implements_stock.append(total_pillows)
    implements_stock.append(total_blankets)
    implements_stock.append(total_sheets)
    implements_stock.append(total_covers)

    return implements_cost, implements_stock


def washing_cost(total_operations):
    """
@Description: Calcula los costes de lavado de los implementos utilizados (Almohadas, cobijas, fundas, sabanas).
              Importancia: Función PRINCIPAL.
              Relationship: Este rubro es por pod. Aumenta conforme aumenten las operaciones.
              Cadencia: Se calcula cada semestre.

@params:
    total_operations [int]: Número total de operaciones/clientes al semestre.

@result:
    [list]: De 3 posiciones, todas de tipo [int], describiendo la información de lavado.
        [pos_0]: Costo total del lavado.
        [pos_1]: Costo de lavar una (1) libra de implementos, independiente de qué sean.
        [pos_2]: Número de libras a lavar.
    """

    washing_vector = []

    #Peso en gramos de cada implemento.
    pillow_weight = 150
    blanket_weight = 500
    sheet_weight = 100
    cover_weight = 25

    #Número máximo de usos por almohada: 3 meses = (365 / 12) * 3 = 91.25 usos.
    pillow_maxuses = 91
    #Número máximo de usos por cobija. (2 semanas)
    blanket_maxuses = 14
    #Número máximo de usos por sabana. (2 semana)
    sheet_maxuses = 14
    #Número máximo de usos por fundas. (3 días)
    cover_maxuses = 3

    semester_operations = total_operations
    
    #Por cada tipo de implemento, calcula el peso total de todas las lavadas. (Usos / máximo uso) * Peso
    pillow_agregatte = pillow_weight * math.ceil(semester_operations / pillow_maxuses)
    blanket_agregatte = blanket_weight * math.ceil(semester_operations / blanket_maxuses)
    sheet_agregatte = sheet_weight * math.ceil(semester_operations / sheet_maxuses)
    cover_agregatte = cover_weight * math.ceil(semester_operations / cover_maxuses)

    #Suma del agregado de peso de todos los implementos y obtención del número de libras.
    total_agregatte = pillow_agregatte + blanket_agregatte + sheet_agregatte + cover_agregatte
    total_agregatte /= 500

    #Cada libra lavada cuesta $3500.
    cost = 3500
    washing_cost = cost * total_agregatte

    washing_vector.append(washing_cost)
    washing_vector.append(cost)
    washing_vector.append(total_agregatte)

    return washing_vector


def own_salary():
    """
@Description: Calculo de mi propio salario. Hay varias opciones, descomente la que quiera probar, comente las demás.
              Importancia: Función PRINCIPAL.
              Relationship: Este rubro es independiente de los pods. Aumenta conforme aumenten las utilidades y la complejidad del negocio.
              Cadencia: Se calcula cada semestre.

@params: None.

@result:
    [list]: Un vector de minímo 3 posiciones. El tamaño depende de la opción elegida. Todas las posiciones son de tipo [int].
        [pos_0]: Número de la opción.
        [pos_1]: Salario semestral.
        [pos_2]: Salario mensual.
        [pos_3+]: Conceptos con los que se calcula el salario.

    """

    salary_vector = []

    #Opción 1 - Matricula semestral

    #Conceptos del salario
    semester_fee = 1650000
    monthly_pay = semester_fee / 4
    #Se agrega el número de opción, el pago semestral y el pago mensual.
    salary_vector.append(1)
    salary_vector.append(semester_fee)
    salary_vector.append(monthly_pay)

    '''
    #Opción 2 - Minimo para mí
    
    #Conceptos del salario
    house_lease = 275000
    services = 76035
    feeding = 4700 * 2 * 20
    monthly_pay = house_lease + services + feeding
    semester_pay = monthly_pay * 4
    #Se agrega el número de opción, el pago semestral y el pago mensual.
    salary_vector.append(2)
    salary_vector.append(semester_pay)
    salary_vector.append(monthly_pay)
    #Se agregan los conceptos del salario.
    salary_vector.append(house_lease)
    salary_vector.append(services)
    salary_vector.append(feeding)
    '''

    return salary_vector


def dotation_cost():
    """
@Description: Calculo del valor de la dotación.
              Importancia: Función PRINCIPAL.
              Relationship: Este rubro es independiente de los pods. Aumenta según aumente el número de trabajadores.
              Cadencia: Se calcula cada semestre.

@params: None.

@result:
    [list]: De 4 posiciones, todas [int], indicando la información de la dotación.
        [pos_0]: Costo total de la dotación.
        [pos_1]: Número de empleados.
        [pos_2]: Costo de cada camisa.
        [pos_3]: Costo de una caja de guantes desechables.
    """

    dotation_vector = []

    #Número de empleados (sin incluirme)
    employees = 6
    #Precio de una camiseta estampada que identifique la marca.
    shirt_cost = 50000
    #Precio de una caja de guantes desechables.
    glove_cost = 50000
    total_cost = (employees * shirt_cost) + glove_cost

    dotation_vector.append(total_cost)
    dotation_vector.append(employees)
    dotation_vector.append(shirt_cost)
    dotation_vector.append(glove_cost)

    return dotation_vector


def rent_cost():
    """
@Description: Calculo del costo de rentar un lugar para guardar las cosas del proyecto.
              Importancia: Función PRINCIPAL.
              Relationship: Este rubro es dependiente de los pods. Aumenta según aumente el número de implementos.
              Cadencia: Se calcula cada semestre.

@params: None.

@result:
    [list]: De 2 posiciones [int] describiendo el arriendo del lugar.
        [pos_0]: Costo semestral del arriendo.
        [pos_1]: Costo mensual del arriendo.
    """

    rent_vector = []

    #Arriendo mensual del lugar.
    place_cost = 250000
    #Costo al semestre del lugar.
    semester_cost = place_cost * 4

    rent_vector.append(semester_cost)
    rent_vector.append(place_cost)

    return rent_vector


def web_cost():
    """
@Description: Calculo del costo del mantenimiento de la página web.
              Importancia: Función PRINCIPAL.
              Relationship: Este rubro sólo aumenta por la inflación y en caso de hacer mejoras. Depende de la complejidad del proyecto.
              Cadencia: Se calcula cada año.

@params: None.

@result:
    [list]: De una posición, contiene el coste aproximada de mantener el dominio y el hosting.
    """

    web_vector = []

    #Valor del dominio y el hosting anual.
    anual_web = 100000
    semester_cost = anual_web / 2

    web_vector.append(semester_cost)

    return  web_vector


def manufacturing_cost():
    """
@Description: Calculo de los costos de manufactura y mantenimiento de un POD.
              Importancia: Función PRINCIPAL.
              Relationship: Este rubro depende de los insumos de creación. Aumenta según aumente el número de pods.
              Cadencia: Se calcula cada ciclo de vida de un POD, se espera como mínimo un año.

@params: TODO

@result: TODO
    """

    manufacturing_vector = []

    return manufacturing_vector


def longtail_employees():
    """
@Description: TODO

@params: TODO

@result: TODO
    """

    longtail_vector = []
    return longtail_vector


def focus_employees():
    """
@Description: TODO

@params: TODO

@result: TODO
    """

    focus_vector = []
    return focus_vector