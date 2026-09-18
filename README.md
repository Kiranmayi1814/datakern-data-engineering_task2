# Retail Order Management System

**Name:** PAVANI DURGA KIRANMAYI SANGOJU

## Problem Statement

A Python application to manage customers, products and orders, calculate totals, apply discounts and update stock.

## Project Structure

```text
retail_order_management/
├── docs/
│   └── solution_design.md
├── src/
│   ├── Milestone1.py
│   ├── Milestone2.py
│   ├── Milestone3.py
│   ├── Milestone4.py
│   ├── Milestone5.py
│   ├── Milestone6.py
│   ├── Milestone7.py
│   ├── Milestone8.py
│   └── Milestone9.py
├── tests/
│   ├── test_data.md
│   └── test_results.md
├── .gitignore
├── README.md
└── requirements.txt
```

## Technologies

Python 3.12.1, VS Code, Git, GitHub and Python Standard Library.

## Setup & Run

Create a virtual environment and run:

```bash
python -m venv .venv
.venv\Scripts\activate
python src/Milestone9.py
```

## Class Design

Customer stores customer details.
Product stores product details, price and stock.
OrderItem stores product quantity and calculates item amount.
Order manages the order and calculates the total.

## Inheritance

Customer types are created using RegularCustomer, PremiumCustomer and CorporateCustomer classes in Milestone 3 and discount behaviour is added in Milestone 4.

## Polymorphism

The `get_discount()` method returns different discount values for different customer types.

## Encapsulation

Validation is used for product price, stock and order quantity to prevent invalid values.

## Business Rules

Regular: 6%, Premium: 7% and Corporate: 5% discount.
Order total = price × quantity × (1 − discount / 100).
Quantity must be positive and within available stock.

## Testing

Tests cover customer types, discounts, valid orders, invalid quantities and stock updates.

## Assumptions

The application uses sample customer and product data and processes one product order at a time.

## Problems & Solutions

Invalid quantities are handled using validation.
Stock is reduced after a successful order.
