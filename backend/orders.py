from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    item: str
    id: int 
    timestamp: datetime
    successfully_paid: bool
    price: float
    name: str


"""
OrderRecord class starts all necessary information about the orders within a given time frame


"""
class OrderRecord:
        def __init__(self, start_time, end_time):
                self.start_time = start_time
                self.end_time = end_time
                self.orders = []

        
        def create_order(self, item, order_id, timestamp, successfully_paid, price, name):
                if self.start_time <= timestamp <= self.end_time:
                        new_order = Order(item, order_id, timestamp, successfully_paid, price, name)
                        self.orders.append(new_order)
                else:
                        print(f"Order Id {order_id} not within time window.")
        
        def __str__(self):
                rep = "All Orders: [ \n"
                for order in self.orders:
                        rep += f"       item: {order.item}, order_id: {order.id}, timestamp: {order.timestamp.strftime("%H:%M:%S %Y-%m-%d")}, successfully_paid: {order.successfully_paid}, price: {order.price}, name: {order.name},\n"
                rep += "]"
                return rep