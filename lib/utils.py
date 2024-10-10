import tempfile
import os 
import json

def read_drink_options(menu_items_path):
        menu = []

        with open(menu_items_path, 'r') as f:
                for line in f:
                        stripped_line = ''.join(line.split())
                        drink_name, price_range = stripped_line.split(":")
                        menu_entry = (drink_name, price_range)
                        menu.append(menu_entry)
        
        return menu



def write_json_safely(file_path, data):
    # Write to a temporary file first
    with tempfile.NamedTemporaryFile('w', delete=False, dir=os.path.dirname(file_path)) as temp_file:
        json.dump(data, temp_file, indent=4)
        temp_file.flush()
        os.fsync(temp_file.fileno())
        temp_filename = temp_file.name
    
    # Replace the original file with the temporary file
    os.replace(temp_filename, file_path)