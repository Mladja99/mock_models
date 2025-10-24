from models.model_c.src.model_c import ModelC
from datetime import date


def test_model_initialization():
    model = ModelC()
    assert model.name == "Model C - Brand Based Pricing"


def test_calculate_price():
    model = ModelC()
    result = model.calculate_price(
        birthdate=date(1995, 6, 15),
        driver_license_date=date(2015, 8, 20),
        car_model="Golf",
        car_brand="Volkswagen",
        postal_code="3014 NM"
    )

    assert "price" in result
    assert "currency" in result
    assert "breakdown" in result
    assert "metadata" in result
    assert result["currency"] == "EUR"
    assert result["price"] > 0
    assert result["model_name"] == "Model C - Brand Based Pricing"


def test_health_check():
    model = ModelC()
    health = model.health_check()
    assert health["status"] == "healthy"
    assert health["model"] == "Model C - Brand Based Pricing"