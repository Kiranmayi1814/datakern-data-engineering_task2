# Solution Design – Retail Order Management System
## 1. Problem Statement
This project is a command-line Python application for managing
customers, products and retail orders.

## 2. Users and Requirements
The application is used by retail staff to create orders,
calculate totals, apply discounts and update product stock.

## 3. Main Classes
Customer stores customer ID, name and discount information.
Product stores product ID, name, price and available stock.
OrderItem connects a product with its quantity and amount.
Order manages order items, totals and order placement.

## 4. Inheritance
RegularCustomer, PremiumCustomer and CorporateCustomer
inherit from Customer to represent different customer types.

## 5. Polymorphism
Customer types can provide different discount behaviours.
The Order class can use customer discount information
to calculate the final payable amount.

## 6. Encapsulation and Validation
Product validates price and stock during object creation.
Product.reduce_stock() controls stock changes.
OrderItem validates positive quantity and stock availability.
Order validates that an order contains items before placing.

## 7. Business Rules
Item amount = Product Price × Quantity.
Discount = Order Total × Customer Discount / 100.
Final Total = Order Total − Discount.
Stock decreases when an order is placed.

## 8. Assumptions
The application uses the Python standard library.
The final command-line flow handles one product order.