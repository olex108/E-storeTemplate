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

#### Abstract Classes

1. BaseProduct - Abstract class for class Product

2. BaseOrder - Abstract class for classes Order and Category


#### Mixin Classes

1. ProductMixin - Mixin class for product classes


#### Category

The class describes the name, short description and list of products of the category

```commandline
name: Name of the category
description: Description of the category
products: List of products of the category
```

The class describe methods: 

 - add_product: Method to add new product to the category, include check if user add product object


#### Order 

The class describes product, quantity and price in order

```commandline
product: Product instance
quantity: Quantity
total_price: Total price
```

#### Product

Class Product descriptions name, short description, price and quantity of product. 
Class describe methods for add new products, addition products, change price and others

```commandline
name: Name of the product
description: Description of the product
price: Price of the product
quantity: Quantity of the product
```

The class describe methods: 

 - __add__: Dander method to add products include check if products are in one class
 - new_product: Create new product from given dictionary if product_in_dict describe as class create new product


##### Smartphone(Product)

Class Smartphone descriptions name, short description, price and quantity of product, efficiency, model, memory, color

##### LawnGrass(Product)

Class Smartphone descriptions name, short description, price and quantity of product, country, germination_period, color

#### ProductInCategoryIterator

Class of Iterator for list od products in category

### Module utils

#### load_data_from_json

Function to load data from json file

#### create_category_objects_from_data

Function to create category objects from data, which include list of Products objects

### Testing

#### Classes:

Test for initialization classes Product, Category, ProductInCategoryIterator

#### Module utils

Test for function load_data_from_json include: Test with json data and Test with FileError

Test for function create_category_objects_from_data include: Test categories objects, Test products objects, # Test Category counters
