def calculate_price(base_price, demand, availability):
    price = base_price

    # Demand-based adjustment
    if demand == "high":
        price *= 1.3
    elif demand == "medium":
        price *= 1.1

    # Availability-based adjustment
    if availability == "low":
        price *= 1.2
    elif availability == "high":
        price *= 0.9

    return round(price, 2)
