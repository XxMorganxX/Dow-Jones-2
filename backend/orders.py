from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    item: str
    order_id: int 
    timestamp: datetime
    successfully_paid: bool
    price: float
    name: str

    """def __repr__(self):
        rep = "[ \n"
        
        rep += f"Order(item: {self.item}, order_id: {self.id}, timestamp: {self.timestamp.strftime("%H:%M:%S %Y-%m-%d")}, successfully_paid: {self.successfully_paid}, price: {self.price}, name: {self.name})\n"
        rep += "]"
        return rep
    """

    """
    
    
    WRITE A FUNCTION TO COVERT ORDER TO DICT
    
    
    
    """

    @classmethod
    def convert_dict_to_order(cls, order_dict):
        required_keys = {"item", "order_id", "timestamp", "successfully_paid", "price", "name"}
        if set(order_dict.keys()) == required_keys:
            return cls(item=order_dict["item"], order_id=int(order_dict["order_id"]), timestamp=order_dict["timestamp"], successfully_paid=order_dict["successfully_paid"], price=order_dict["price"], name=order_dict["name"])



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

        def __repr__(self):
                return f"OrderRecord(start_time={self.start_time}, end_time={self.end_time}, orders={self.orders})"

        def __iter__(self):
            return iter(self.orders)

