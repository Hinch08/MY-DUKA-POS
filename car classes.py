# Task 1.Create a Car Class Have the following attributes:
#  brand - model - year -fuel_capcity - fuel_level -is_running(boolen value) 
# Have the following methods as behaviour for your class: start() stop() refuel() drive() display_car_info()

# 2.Create child classes from parent class Car namely: Toyota & Audi and have them override the methods above

from typing import Self


class Car:
    def __init__(self,brand,model,year,fuel_capacity,fuel_level,is_running):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.is_running = is_running
    def start(self):
        if self.is_running:
            print(f"{self.brand} {self.model} is already running")   
        else:
            self.is_running = True
            print(f"{self.brand} {self.model} has started")
    def stop(self):
        if not self.is_running:
            print(f"{self.brand} {self.model} is already stopped") 
        else:
            self.is_running = False
            print(f"{self.brand} {self.model} has stopped")
    def refuel(self):
        if self.fuel_level < self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
            print(f"{self.brand} {self.model} has been refueled to full capacity")
        else:
            print(f"{self.brand} {self.model} fuel level is already full")
    def drive(self):
        if self.is_running:
            if self.fuel_level > 0:
                self.fuel_level -= 1
                print(f"{self.brand} {self.model} is driving. Fuel level: {self.fuel_level}")
            else:
                print(f"{self.brand} {self.model} has no fuel. Please refuel.")
        else:
            print(f"{self.brand} {self.model} is not running. Please start the car first.")
    def display_car_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel Capacity: {self.fuel_capacity}")
        print(f"Fuel Level: {self.fuel_level}")
        print(f"Is Running: {self.is_running}")
class Toyota(Car):
    def start(self):
        if self.is_running:
            print(f"{self.brand} {self.model} is already running")   
        else:
            self.is_running = True
            print(f"{self.brand} {self.model} has started with a smooth engine sound")
    def stop(self):
        if not self.is_running:
            print(f"{self.brand} {self.model} is already stopped") 
        else:
            self.is_running = False
            print(f"{self.brand} {self.model} has stopped with a gentle brake")
    def refuel(self):
        if self.fuel_level < self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
            print(f"{self.brand} {self.model} has been refueled to full capacity with high-quality fuel")
        else:
            print(f"{self.brand} {self.model} fuel level is already full")
    def drive(self):
        if self.is_running:
            if self.fuel_level > 0:
                self.fuel_level -= 1
                print(f"{self.brand} {self.model} is driving smoothly. Fuel level: {self.fuel_level}")
            else:
                print(f"{self.brand} {self.model} has no fuel. Please refuel.")
        else:
            print(f"{self.brand} {self.model} is not running. Please start the car first.")
    def display_car_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel Capacity: {self.fuel_capacity}")
        print(f"Fuel Level: {self.fuel_level}")
        print(f"Is Running: {self.is_running}")                                                