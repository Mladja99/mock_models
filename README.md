# Insurance Pricing Models

Collection of car insurance pricing models packaged as independent Python packages for the Ominimo Pricing Engine project.

## Overview

This repository contains three pricing models:
- **Model A**: Age-based pricing (focuses on driver age)
- **Model B**: Experience-based pricing (focuses on driving experience)
- **Model C**: Brand-based pricing (focuses on car brand/category)

Each model is a standalone Python package that can be installed independently.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip or poetry

### Install from GitHub

You can install models directly from this GitHub repository:

#### Using pip

```bash
# Install Model A
pip install git+https://github.com/yourusername/your-repo-name.git#subdirectory=packages/model_a

# Install Model B
pip install git+https://github.com/yourusername/your-repo-name.git#subdirectory=packages/model_b

# Install Model C
pip install git+https://github.com/yourusername/your-repo-name.git#subdirectory=packages/model_c

# Or install all at once
pip install \
  git+https://github.com/yourusername/your-repo-name.git#subdirectory=packages/model_a \
  git+https://github.com/yourusername/your-repo-name.git#subdirectory=packages/model_b \
  git+https://github.com/yourusername/your-repo-name.git#subdirectory=packages/model_c
```

#### Using Poetry

Add to your `pyproject.toml`:

```toml
[tool.poetry.dependencies]
insurance-model-a = {git = "https://github.com/yourusername/your-repo-name.git", subdirectory = "packages/model-a"}
insurance-model-b = {git = "https://github.com/yourusername/your-repo-name.git", subdirectory = "packages/model-b"}
insurance-model-c = {git = "https://github.com/yourusername/your-repo-name.git", subdirectory = "packages/model-c"}
```

Then run:
```bash
poetry install
```

#### Specific Version/Branch/Tag

```bash
# Install from specific branch
pip install git+https://github.com/yourusername/your-repo-name.git@main#subdirectory=packages/model_a

# Install from specific tag
pip install git+https://github.com/yourusername/your-repo-name.git@v0.1.0#subdirectory=packages/model_a

# Install from specific commit
pip install git+https://github.com/yourusername/your-repo-name.git@abc123#subdirectory=packages/model_a
```

### Local Installation (Development)

For local development, clone the repository and install in editable mode:

```bash
# Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

# Install a model in editable mode
cd packages/model_a
pip install -e .

# Or with poetry
poetry install
```

## Usage

### Basic Example

```python
from model_a import ModelA
from model_b import ModelB
from model_c import ModelC
from datetime import date

# Initialize models
model_a = ModelA()
model_b = ModelB()
model_c = ModelC()

# Prepare input data
input_data = {
    "birthdate": date(1995, 6, 15),
    "driver_license_date": date(2015, 8, 20),
    "car_model": "Golf",
    "car_brand": "Volkswagen",
    "postal_code": "1234AC"
}

# Get prices from each model
price_a = model_a.calculate_price(**input_data)
price_b = model_b.calculate_price(**input_data)
price_c = model_c.calculate_price(**input_data)

# Display results
print(f"Model A: €{price_a['price']}")
print(f"Model B: €{price_b['price']}")
print(f"Model C: €{price_c['price']}")
```

### Model Interface

All models follow the same interface:

#### `calculate_price(**kwargs) -> dict`

**Parameters:**
- `birthdate` (date): Driver's birth date
- `driver_license_date` (date): Driver's license issue date
- `car_model` (str): Car model name
- `car_brand` (str): Car brand/manufacturer
- `postal_code` (str): Postal code of residence

**Returns:**
```python
{
    "model_name": str,      # Model identifier
    "price": float,         # Annual insurance price in EUR
    "currency": str,        # Currency code (always "EUR")
    "breakdown": dict,      # Price calculation breakdown
    "metadata": dict        # Additional information
}
```

#### `health_check() -> dict`

Returns the model's health status.

**Returns:**
```python
{
    "status": str,    # "healthy"
    "model": str      # Model name
}
```

## Model Descriptions

### Model A - Age Based Pricing

Focuses primarily on driver age as the main pricing factor.

**Pricing Logic:**
- Drivers under 25: Higher premiums (young driver risk)
- Drivers 25-50: Standard premiums
- Drivers 50-65: Slightly increased premiums
- Drivers 65+: Higher premiums (senior driver risk)

**Example:**
```python
from model_a import ModelA
from datetime import date

model = ModelA()
result = model.calculate_price(
    birthdate=date(2003, 3, 10),  # Young driver
    driver_license_date=date(2021, 4, 15),
    car_model="Corolla",
    car_brand="Toyota",
    postal_code="1234AC"
)
print(result['price'])  # Higher price due to age
```

### Model B - Experience Based Pricing

Focuses primarily on driving experience (years since license obtained).

**Pricing Logic:**
- Less than 2 years: Highest premiums (inexperienced)
- 2-5 years: High premiums
- 5-10 years: Standard premiums
- 10+ years: Lower premiums (experienced driver discount)

**Example:**
```python
from model_b import ModelB
from datetime import date

model = ModelB()
result = model.calculate_price(
    birthdate=date(1990, 5, 20),
    driver_license_date=date(2023, 1, 15),  # New license
    car_model="Golf",
    car_brand="Volkswagen",
    postal_code="5678BD"
)
print(result['price'])  # Higher price due to lack of experience
```

### Model C - Brand Based Pricing

Focuses primarily on car brand and category (luxury/premium/economy).

**Pricing Logic:**
- Luxury brands (BMW, Mercedes, Audi, etc.): Highest premiums
- Premium brands (Volvo, Volkswagen, Mazda, etc.): Medium premiums
- Economy brands (all others): Standard premiums

**Example:**
```python
from model_c import ModelC
from datetime import date

model = ModelC()
result = model.calculate_price(
    birthdate=date(1985, 8, 15),
    driver_license_date=date(2003, 9, 20),
    car_model="Model S",
    car_brand="Tesla",  # Luxury brand
    postal_code="8901CE"
)
print(result['price'])  # Higher price due to luxury brand
```

## Repository Structure

```
.
├── LICENSE
├── README.md
├── .gitignore
└── packages/
    ├── model-a/
    │   ├── pyproject.toml
    │   ├── model_a/
    │   │   ├── __init__.py
    │   │   └── model.py
    │   └── tests/
    │       └── test_model.py
    ├── model-b/
    │   ├── pyproject.toml
    │   ├── model_b/
    │   │   ├── __init__.py
    │   │   └── model.py
    │   └── tests/
    │       └── test_model.py
    └── model-c/
        ├── pyproject.toml
        ├── model_c/
        │   ├── __init__.py
        │   └── model.py
        └── tests/
            └── test_model.py
```

## Development

### Running Tests

```bash
# Test Model A
cd packages/model_a
pytest

# Test all models
cd packages
for model in model-{a,b,c}; do
  cd $model
  pytest
  cd ..
done
```

### Making Changes

1. Clone the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests to ensure nothing breaks
5. Commit: `git commit -am 'Add your feature'`
6. Push: `git push origin feature/your-feature`
7. Create a Pull Request

## Versioning

We use semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

Current version: **0.1.0**

## Using in the API Gateway Project

These models are designed to be used with the Pricing Engine API Gateway.

See the [API Gateway Repository](https://github.com/yourusername/api-gateway-repo) for integration examples.

## Requirements

- Python 3.8+
- No external dependencies (models use only Python standard library)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- Mladen Nikolic - [GitHub Profile](https://github.com/Mladja99)