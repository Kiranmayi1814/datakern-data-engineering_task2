# Test Data

| Test ID | Scenario | Input | Expected Result | Status |
|---|---|---|---|---|
| T001 | Regular customer buys one product | Valid customer/product, Qty 1 | Order succeeds | |
| T002 | Premium customer places order | Valid inputs | Premium rule applied | |
| T003 | Corporate customer places order | Valid inputs | Corporate rule applied | |
| T004 | Quantity exceeds stock | Qty > stock | Order rejected | |
| T005 | Invalid quantity | Qty 0 or negative | Validation error | |
