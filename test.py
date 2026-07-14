import json

target_list=["Vibrant Runners: Bold Orange & Blue Sneakers","Modern LED Desk Lamp","Apple Phone Case"]

with open("products.json","r") as f:
        product_list = json.load(f)
        print([p for p in product_list if p["name"] in target_list])

