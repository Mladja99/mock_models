# Insurance Model B - Experience Based Pricing

Experience-focused car insurance pricing model.

## Installation
```bash
# Via pip from GitHub
pip install git+https://github.com/username/mock-models-repo.git#subdirectory=packages/model-b

# Via poetry from GitHub
poetry add git+https://github.com/username/mock-models-repo.git#subdirectory=packages/model-b

# Specific version/branch/tag
pip install git+https://github.com/username/mock-models-repo.git@v0.1.0#subdirectory=packages/model-b
poetry add git+https://github.com/username/mock-models-repo.git#branch=main&subdirectory=packages/model-b
```

## Usage
```python
from model_b import ModelB
from datetime import date

model = ModelB()

result = model.calculate_price(
    birthdate=date(1995, 6, 15),
    driver_license_date=date(2015, 8, 20),
    car_model="Golf",
    car_brand="Volkswagen",
    postal_code="3014 NM"
)

print(f"Price: {result['price']} {result['currency']}")
```

## API

### `ModelB.calculate_price()`

**Parameters:**
- `birthdate` (date): Driver's birth date
- `driver_license_date` (date): License issue date
- `car_model` (str): Car model name
- `car_brand` (str): Car brand/manufacturer
- `postal_code` (str): Postal code of residence

**Returns:** dictionary with:
- `model_name` (str): Model identifier
- `price` (float): Annual insurance price
- `currency` (str): Currency code (EUR)
- `breakdown` (dict): Price calculation details
- `metadata` (dict): Additional information

## Pricing Logic

This model focuses on driver age:
- Experience < 2: Higher premiums (young driver risk)
- Experience 2-5: Slightly increased premiums
- Experience 5-10: Standard premiums
- Experience 10+: Low premiums

## Author:

Mladen