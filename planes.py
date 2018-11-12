import parts as pr
import tables as tb
from random import randint
from math import floor
class AirCraft:
    def __init__(self, model):
        self.text_name = model
        self.current_point = 'Almaty'
        self.owner = None
        self.tank_size = tb.planeModels[model]['tank_size']
        self.fuel_left = 0
        self.fuel_consumption_rate = tb.planeModels[model]['cnsmptn']  # consumption of fuel per 1000 km
        self.paidPerKm = tb.planeModels[model]['paidPerKm']

    def is_enough(self, depart_point, arrive_point, fuel, consumption):
        dist_to_fly = tb.distances[depart_point][arrive_point]
        dist_can_be_flied = fuel * 1000 / consumption
        if dist_can_be_flied - dist_to_fly > 100:  # we leave fuel for extra 100 km
            return True
        else:
            return False

    def calculate_sum_of_sold_tickets(self, destination):
        ticket_price = tb.distances[self.current_point][destination] * self.paidPerKm/self.seats
        sales_rate = randint(80, 100)
        sold_tickets = floor(self.seats*sales_rate/100)
        print('price for the ticket '+str(ticket_price))
        print('total sold tickets '+str(sold_tickets))
        print('sum for sold tickets ' + str(sold_tickets*ticket_price))
        return sold_tickets*ticket_price


    def make_flight(self, destination):
        if self.is_enough(self.current_point, destination, self.fuel_left, self.fuel_consumption_rate):
            print(self.text_name + ' is flying to ' + destination)
            self.fuel_left -= tb.distances[self.current_point][destination] / 1000 * self.fuel_consumption_rate
            self.owner.money_balance += self.calculate_sum_of_sold_tickets(destination)
            self.current_point = destination

        else:
            answer = input('There is not enough fuel to fly to ' + destination+'. Would you like to fill the tank? y/n ')
            if answer.lower() == 'y':
                self.fill_tank()
                self.make_flight(destination)
            else:
                print('The flight has been canceled.')

    def fill_tank(self):
        fuel_to_buy = self.tank_size - self.fuel_left
        print('We pay for the fuel '+str(tb.fuelPrice * fuel_to_buy))
        self.owner.money_balance -= tb.fuelPrice * fuel_to_buy
        self.fuel_left = self.tank_size
        print('We are filling fuel...')


class Passenger_Aircraft(AirCraft):
    def __init__(self, model):
        self.seats = tb.planeModels[model]['seats']
        self.cargo_space = pr.CargoModule()
        super().__init__(model)
