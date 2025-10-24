"""Insurance Model A - Age Based Pricing"""

from datetime import date
import random


class ModelA:
    """Simple insurance pricing model"""

    def __init__(self):
        self.name = "Model A - Age Based Pricing"

    def calculate_price(
            self,
            birthdate: date,
            driver_license_date: date,
            car_model: str,
            car_brand: str,
            postal_code: str
    ) -> dict:
        """
        Calculate insurance price based on input parameters
        Assumes all inputs are already validated for simplicity.

        Returns:
            dict with price, breakdown, and metadata
        """
        # Calculate driver age
        today = date.today()
        age = today.year - birthdate.year - (
                (today.month, today.day) < (birthdate.month, birthdate.day)
        )

        # Pricing logic
        if age < 25:
            base_price = random.uniform(800, 1200)
            age_factor = 1.5
        elif age < 30:
            base_price = random.uniform(600, 900)
            age_factor = 1.2
        elif age < 50:
            base_price = random.uniform(400, 700)
            age_factor = 1.0
        elif age < 65:
            base_price = random.uniform(500, 800)
            age_factor = 1.1
        else:
            base_price = random.uniform(600, 1000)
            age_factor = 1.3

        variation = random.uniform(0.95, 1.05)
        final_price = round(base_price * age_factor * variation, 2)

        return {
            "model_name": self.name,
            "price": final_price,
            "currency": "EUR",
            "breakdown": {
                "base_price": round(base_price, 2),
                "age_factor": age_factor,
                "variation_factor": round(variation, 2)
            },
            "metadata": {
                "driver_age": age,
                "car": f"{car_brand} {car_model}",
                "postal_code": postal_code
            }
        }

    def health_check(self) -> dict:
        """Simple health check"""
        return {"status": "healthy", "model": self.name}