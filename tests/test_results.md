# Test Results
| Test ID | Test Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| T001 | Regular customer, quantity 1 | Order succeeds | Order completed; total = 47000.0 | PASS |
| T002 | Premium customer, quantity 1 | Premium rule applied | Order completed; total = 46500.0 | PASS |
| T003 | Corporate customer, quantity 1 | Corporate rule applied | Order completed; total = 47500.0 | PASS |
| T004 | Regular customer, quantity 11 | Order rejected due to stock | Error: Invalid quantity or stock | PASS |
| T005 | Regular customer, quantity 0 | Validation error | Error: Invalid quantity or stock | PASS |


