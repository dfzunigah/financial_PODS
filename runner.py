'''
Author: Daniel F. Zuñiga H.
Date: 25/04/18
Place: @Apt, Bogotá.

Description: This module is part of UPODS project. It's the main module.

'''

import interpreters
import money_in
import money_out
import operations
import UI
import locale
import datetime

s = datetime.date(2018,2,5)
J24 = datetime.date(2018,5,8)
e = datetime.date(2018,6,7)

locale.setlocale(locale.LC_ALL, '')
#Datos ingresados por el usuario
#scenario = UI.input_scenario()
scenario = operations.vector_representation(2500,100,7,45,5,12,10,s,J24,e)
answer = UI.difficulty_chooser()

#Realización de todas las operaciones.
operations_array = operations.operations_counter(scenario)
earnings_array = money_in.pod_earnings(scenario)
implements_array = money_out.implements_cost(operations_array)
washing_array = money_out.washing_cost(operations_array[-1])
own_array = money_out.own_salary()
dotation_array = money_out.dotation_cost()
web_array = money_out.web_cost()
rent_array = money_out.rent_cost()

interpreters.operation_printer(answer,scenario,operations_array,earnings_array,implements_array,washing_array,own_array,dotation_array,web_array,rent_array)

#interpreters.clients_balance(operations_array,2)
