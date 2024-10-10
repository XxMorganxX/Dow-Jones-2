import sys
import os
from datetime import datetime, timedelta
from random import choice, randint, uniform


# Order in form: name, order_id, timestamp, successfully_paid, price, item


# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.utils import read_drink_options, write_json_safely

# Generates a text file with test orders 
# Provide a quantity of orders, median time that the orders will occur at and an amount of time that the orders will deviate from the median time
# deviation time in num of seconds
def generate_test_orders_func(quant_orders, median_time, deviation_time):

        print(f"Generating {quant_orders} test orders")
        print(f"start time: {dt.strftime("%H:%M:%S %Y-%m-%d")}")




        menu_items_path = "../sample_data/menu_items.txt"
        menu_info = read_drink_options(menu_items_path)

        order_keys = ["item","order_id", "timestamp", "successfully_paid", "price", "name"]
        generated_orders = {}
        order_count = 1


        time_step = deviation_time / (quant_orders - 1)

        order_ids = []

        names = ["Morgan", "Will", "Spencer"]
        

        for test_order in range(quant_orders):
                new_order = {}
                rand_drink = choice(menu_info)
                new_order[order_keys[0]] = rand_drink[0] 
                
                
                random_id = randint(10000, 99999)
                while(random_id in order_ids):
                        if random_id in order_ids:
                                random_id = randint(1, 99999)
                order_ids.append(random_id) 

                new_order[order_keys[1]] = str(random_id) 

                timestamp = median_time + timedelta(seconds= (time_step * (test_order - (quant_orders-1)/2)))

                new_order[order_keys[2]] = timestamp.strftime("%H:%M:%S %Y-%m-%d") 

                new_order[order_keys[3]] = str(True)

                prices = [float(x) for x in rand_drink[1].split(",")]

                new_order[order_keys[4]] = str(uniform(prices[0], prices[1])) 

                new_order[order_keys[5]] = choice(names) 

                generated_orders[order_count] = new_order
                order_count += 1

        write_json_safely("../sample_data/test_orders.json", generated_orders)


        
        
        











dt = datetime.now()
generate_test_orders_func(21, datetime.now(), 180)

