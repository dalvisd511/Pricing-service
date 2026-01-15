class PricingRequest:
    def __init__(self, base_price, demand, availability):
        self.base_price = base_price
        self.demand = demand
        self.availability = availability

    def validate(self):
        if not isinstance(self.base_price, (int, float)):
            raise ValueError("Base price must be a number")

        if self.base_price <= 0:
            raise ValueError("Base price must be greater than zero")

        if self.demand not in ["low", "medium", "high"]:
            raise ValueError("Demand must be low, medium, or high")

        if self.availability not in ["low", "medium", "high"]:
            raise ValueError("Availability must be low, medium, or high")
