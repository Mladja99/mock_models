# Insurance Model C - Brand Based Pricing

Brand-focused car insurance pricing model.

## Installation
```bash
# Via pip from GitHub
pip install git+https://github.com/username/mock-models-repo.git#subdirectory=packages/model-c

# Via poetry from GitHub
poetry add git+https://github.com/username/mock-models-repo.git#subdirectory=packages/model-c

# Specific version/branch/tag
pip install git+https://github.com/username/mock-models-repo.git@v0.1.0#subdirectory=packages/model-c
poetry add git+https://github.com/username/mock-models-repo.git#branch=main&subdirectory=packages/model-c
```

## Usage
```python
from model_c import ModelC
from datetime import date

model = ModelC()

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
- Luxury Brand: Higher premiums
- Premium Brand: Slightly increased premiums
- Economy Brand: Standard premiums

## Author:

Mladen