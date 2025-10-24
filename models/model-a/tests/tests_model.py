from ..model_a import ModelA
from datetime import date


def test_model_initialization():
    model = ModelA()
    assert model.name == "Model A - Age Based Pricing"


def test_calculate_price():
    model = ModelA()
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
    assert result["model_name"] == "Model A - Age Based Pricing"


def test_health_check():
    model = ModelA()
    health = model.health_check()
    assert health["status"] == "healthy"
    assert health["model"] == "Model A - Age Based Pricing"