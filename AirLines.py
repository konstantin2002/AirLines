from time import sleep
import planes as pl
import tables as tb


class AirCompany:
    def __init__(self, name):
        self.text_name = name
        self.money_balance = 3000000
        self.planes = {}

    def purchase_plane(self, model):
        if self.money_balance >= tb.planeModels[model]['price']:
            self.planes[model] = pl.Passenger_Aircraft(model)
            self.planes[model].owner = self
            self.money_balance -= tb.planeModels[model]['price']
