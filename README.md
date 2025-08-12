# E-store Template

## Table of Contents
- [Installation]
- [Description of Functionality]
- [Testing]


## Installation:

```
git clone https://github.com/olex108/Homework10_1.git
```

## Description of Functionality:

### Classes:

#### Category

The class describes the name, short description and list of products of the category

```commandline
name: Name of the category
description: Description of the category
products: List of products of the category
```

#### Product

Class Product descriptions name, short description, price and quantity of product

```commandline
name: Name of the product
description: Description of the product
price: Price of the product
quantity: Quantity of the product
```

### Module utils

#### load_data_from_json

Function to load data from json file

#### create_category_objects_from_data

Function to create category objects from data, which include list of Products objects

### Testing

#### Classes:

Test for initialization classes Product, Category

#### Module utils

Test for function load_data_from_json include: Test with json data and Test with FileError

Test for function create_category_objects_from_data include: Test categories objects, Test products objects, # Test Category counters
