from datetime import date
import random


class ModelC:
    """Brand-based pricing model"""

    def __init__(self):
        self.name = "Model C - Brand Based Pricing"
        self.luxury_brands = {'bmw', 'mercedes', 'audi', 'porsche', 'lexus', 'tesla', 'jaguar'}
        self.premium_brands = {'volvo', 'volkswagen', 'mazda', 'subaru', 'honda', 'toyota'}

    def calculate_price(
            self,
            birthdate: date,
            driver_license_date: date,
            car_model: str,
            car_brand: str,
            postal_code: str
    ) -> dict:
        """Calculate price based on car brand"""

        brand_lower = car_brand.lower()

        if brand_lower in self.luxury_brands:
            base_price = random.uniform(750, 1100)
            brand_factor = 1.4
            category = "luxury"
        elif brand_lower in self.premium_brands:
            base_price = random.uniform(500, 800)
            brand_factor = 1.1
            category = "premium"
        else:
            base_price = random.uniform(400, 650)
            brand_factor = 1.0
            category = "economy"

        today = date.today()
        age = today.year - birthdate.year - (
                (today.month, today.day) < (birthdate.month, birthdate.day)
        )

        age_adjustment = 1.15 if age < 25 else 1.05 if age >= 50 else 1.0

        variation = random.uniform(0.95, 1.05)
        final_price = round(base_price * brand_factor * age_adjustment * variation, 2)

        return {
            "model_name": self.name,
            "price": final_price,
            "currency": "EUR",
            "breakdown": {
                "base_price": round(base_price, 2),
                "brand_category": category,
                "brand_factor": brand_factor,
                "age_adjustment": age_adjustment,
                "variation_factor": round(variation, 2)
            },
            "metadata": {
                "driver_age": age,
                "car_brand": car_brand,
                "car_model": car_model,
                "postal_code": postal_code
            }
        }

    def health_check(self) -> dict:
        return {"status": "healthy", "model": self.name}
