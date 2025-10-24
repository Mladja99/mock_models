from datetime import date
import random


class ModelB:
    """Experience-based pricing model"""

    def __init__(self):
        self.name = "Model B - Experience Based Pricing"

    def calculate_price(
            self,
            birthdate: date,
            driver_license_date: date,
            car_model: str,
            car_brand: str,
            postal_code: str
    ) -> dict:
        """Calculate price based on driving experience"""

        today = date.today()
        experience_years = today.year - driver_license_date.year - (
                (today.month, today.day) < (driver_license_date.month, driver_license_date.day)
        )

        if experience_years < 2:
            base_price = random.uniform(900, 1300)
            experience_factor = 1.6
        elif experience_years < 5:
            base_price = random.uniform(650, 950)
            experience_factor = 1.3
        elif experience_years < 10:
            base_price = random.uniform(500, 750)
            experience_factor = 1.0
        else:
            base_price = random.uniform(400, 650)
            experience_factor = 0.85

        postal_hash = sum(ord(c) for c in postal_code)
        location_factor = 0.9 + (postal_hash % 20) / 100

        variation = random.uniform(0.95, 1.05)
        final_price = round(base_price * experience_factor * location_factor * variation, 2)

        return {
            "model_name": self.name,
            "price": final_price,
            "currency": "EUR",
            "breakdown": {
                "base_price": round(base_price, 2),
                "experience_factor": experience_factor,
                "location_factor": round(location_factor, 2),
                "variation_factor": round(variation, 2)
            },
            "metadata": {
                "driving_experience_years": experience_years,
                "car": f"{car_brand} {car_model}",
                "postal_code": postal_code
            }
        }

    def health_check(self) -> dict:
        return {"status": "healthy", "model": self.name}