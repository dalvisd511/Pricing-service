from app.pricing import calculate_price

def test_high_demand_low_availability():
    price = calculate_price(100, "high", "low")
    assert price == 156.0

def test_medium_demand_medium_availability():
    price = calculate_price(100, "medium", "medium")
    assert price == 110.0

def test_low_demand_high_availability():
    price = calculate_price(100, "low", "high")
    assert price == 90.0
