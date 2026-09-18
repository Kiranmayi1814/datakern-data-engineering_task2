
# Retail Order Management System
**Name:** PAVANI DURGA KIRANMAYI SANGOJU

## Problem Statement
A Python application to manage customers, products and orders, calculate totals, apply discounts and update stock.

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
Customer stores common customer details.
RegularCustomer, PremiumCustomer and CorporateCustomer provide customer-specific behaviour.
Product manages product price and stock.
OrderItem stores product quantity and item amount.
Order manages order items and total calculation.

## Inheritance
Customer subclasses share common details and implement different discount rules.

## Polymorphism
The `get_discount()` method provides customer-specific discount behaviour.

## Encapsulation
Validation controls product price, stock and order quantity to prevent invalid values.

## Business Rules
Regular: 6%, Premium: 7% and Corporate: 5% discount.
Order total = price × quantity × (1 − discount / 100).
Quantity must be positive and within available stock.

## Testing
Tests cover customer types, discounts, valid orders, invalid quantities and stock updates.

## Assumptions
The application processes one order item at a time and uses sample product data.

## Problems & Solutions
Invalid quantities are handled through validation.
Stock is reduced only after a successful order.