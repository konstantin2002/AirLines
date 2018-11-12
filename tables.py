distances = {'Almaty': {'Kiev': 3500, 'Paris': 5500, 'London': 6000},
             'Kiev': {'Almaty': 3500, 'Paris': 2000, 'London': 2500},
             'Paris': {'Almaty': 5500, 'Kiev': 2000, 'London': 500},
             'London': {'Almaty': 6000, 'Kiev': 2500, 'Paris': 500}}

planeModels = {'Boeing737': {'price': 1300000, 'tank_size': 12, 'cnsmptn': 1.5, 'paidPerKm': 90, 'seats': 150},
               'AirBus325': {'price': 800000, 'tank_size': 10, 'cnsmptn': 1.2, 'paidPerKm': 30, 'seats': 120}}  # cost/tank/cnsmptn/paidPer1000km

fuelPrice = 10000  # price per 1 t of fuel
