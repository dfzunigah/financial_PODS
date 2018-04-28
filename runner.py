'''
Author: Daniel F. Zuñiga H.
Date: 28/04/18
Place: @Apt, Bogotá.

Description: This module is part of UPODS project. It's the main module.

'''

import UI
import locale

#Fija el formato según la ubicación y configuración del equipo.
locale.setlocale(locale.LC_ALL, '')

#Ciclo de menu principal.
goback = True
while (goback == True):
    UI.main_menu()
    UI.goback_menu()