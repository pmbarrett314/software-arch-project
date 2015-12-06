'''
Created on Oct 7, 2014

@author: Paul
'''

from view.curseMenu import menuItem

menuData = {
    'title': "Trade Net brokerage system", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
    'options': [
        {'title': "Trade Net brokerage system", 'type': menuItem.FUNCTIONMENU, 'function': "login", 'subtitle': "Please select an option...",
             'options': [
                 {'title': "List Flights", 'type': menuItem.FUNCTION, 'function': "listFlights"},
                 {'title': "List Reservations", 'type': menuItem.FUNCTION, 'function': 'listReservations'},
             ]
        },
    ]
}




"""
[
        {'title': "Information", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
             'options': [
                 {'title': "List Flights", 'type': menuItem.FUNCTION, 'function': "listFlights"},
                 {'title': "List Reservations", 'type': menuItem.FUNCTION, 'function': 'listReservations'},
             ]
         },
        {'title': "Passengers", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
         'options': [
             {'title': "Reserve Seat", 'type': menuItem.FUNCTION, 'function': 'reserveSeat'},
             {'title': "Change Reservation", 'type': menuItem.FUNCTION, 'function': 'changeReservation'},
             {'title': "Cancel Reservation", 'type': menuItem.FUNCTION, 'function': 'cancelReservation'},
             {'title': "Calculate Round Trip Cost", 'type': menuItem.FUNCTION, 'function': 'calculateCost'},
         ]
         },
        {'title': "Flight Instance Management", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
         'options': [
             {'title': "Add Flight Instance", 'type': menuItem.FUNCTION, 'function': 'addFlightInstance'},
             {'title': "Edit Flight Instance", 'type': menuItem.FUNCTION, 'function': 'editFlightInstance'},
             {'title': "Delete Flight Instance", 'type': menuItem.FUNCTION, 'function': 'deleteFlightInstance'},
         ]
         },
        {'title': "Administration", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
         'options': [
             {'title': "View/Edit Planes", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
                  'options': [
                      {'title': "View Planes", 'type': menuItem.FUNCTION, 'function': 'viewPlanes'},
                      {'title': "Add Plane", 'type': menuItem.FUNCTION, 'function': 'addPlane'},
                      {'title': "Edit Plane", 'type': menuItem.FUNCTION, 'function': 'editPlane'},
                      {'title': "Delete Plane", 'type': menuItem.FUNCTION, 'function': 'deletePlane'},
                  ]
              },
             {'title': "View/Edit Airports", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
              'options': [
                  {'title': "View Airports", 'type': menuItem.FUNCTION, 'function': 'viewAirports'},
                  {'title': "Add Airport", 'type': menuItem.FUNCTION, 'function': 'addAirport'},
                  {'title': "Edit Airport", 'type': menuItem.FUNCTION, 'function': 'editAirport'},
                  {'title': "Delete Airport", 'type': menuItem.FUNCTION, 'function': 'deleteAirport'},
              ]
              },
             {'title': "View/Edit Legs", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
              'options': [
                  {'title': "View Legs", 'type': menuItem.FUNCTION, 'function': 'viewLegs'},
                  {'title': "Add Leg", 'type': menuItem.FUNCTION, 'function': 'addLeg'},
                  {'title': "Edit Leg", 'type': menuItem.FUNCTION, 'function': 'editLeg'},
                  {'title': "Delete Leg", 'type': menuItem.FUNCTION, 'function': 'deleteLeg'},
              ]
              },
             {'title': "View/Edit Flights", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
              'options': [
                  {'title': "View Flights", 'type': menuItem.FUNCTION, 'function': 'viewFlights'},
                  {'title': "Add Flight", 'type': menuItem.FUNCTION, 'function': 'addFlight'},
                  {'title': "Edit Flight", 'type': menuItem.FUNCTION, 'function': 'editFlight'},
                  {'title': "Delete Flight", 'type': menuItem.FUNCTION, 'function': 'deleteFlight'},
              ]
              },
             {'title': "View/Edit Prices", 'type': menuItem.MENU, 'subtitle': "Please select an option...",
              'options': [
                  {'title': "View Price Codes", 'type': menuItem.FUNCTION, 'function': 'viewCodes'},
                  {'title': "Add Price Code", 'type': menuItem.FUNCTION, 'function': 'addCode'},
                  {'title': "Edit Price Code", 'type': menuItem.FUNCTION, 'function': 'editCode'},
                  {'title': "Delete Price Code", 'type': menuItem.FUNCTION, 'function': 'deleteCode'},
              ]
              },
         ]
         },
    ]
"""
