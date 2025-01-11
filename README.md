
# Project Documentation: Intelligent Finance Manager

## Table of contents:
1. [Overview](#1-overview)
2. [Copyright and required licenses](#2-copyright-information)
3. [Requirements specification](#3-requirements-specification)
4. [System architecture](#4-system-architecture)
5. [Testing](#5-testing)
6. [Run](#6-run)


## 1. Overview

**Short Name**: SMARTcash  
**Full Name**: SMARTcash - Intelligent Financial Management System with Receipt Analysis  

**Description**:  
The Intelligent Finance Manager is a web application designed to help users manage their finances efficiently. The application allows users to scan and upload receipts, automatically extracting and categorizing expenses. Additionally, users can manually add expenses, filter receipts by date, and view detailed analytics with visualizations. The project aims to simplify personal financial management through automation and user-friendly features.

---

## 2. Copyright Information

**Author**:  
Maria Krakowiak

**License**:  
The project is licensed under the MIT License, allowing open use, modification and distribution..

---

## 3. Requirements Specification

### **A: Structured List**  

| ID    | Name                        | Description                                                                 | Priority | Category          |
|-------|-----------------------------|-----------------------------------------------------------------------------|----------|-------------------|
| REQ-1 | Receipt Upload              | Allow users to upload scanned receipts in format img. png.                  | 1        | Functional        |
| REQ-2 | Expense Extraction          | Automatically extract expense details from receipts using OCR.              | 1        | Functional        |
| REQ-3 | Manual Expense Entry        | Enable users to manually add expenses.                                      | 3        | Functional        |
| REQ-4 | Receipt Filtering           | Filter receipts by year, month, or day.                                     | 2        | Functional        |
| REQ-5 | Analytics Dashboard         | Display visualizations of expenses grouped by time periods.                 | 3        | Functional        |
| REQ-6 | User Authentication         | Provide login functionality for secure access.                              | 1        | Functional        |
| REQ-7 | User Registration           | User can create an account by providing email address and password          | 1        | Functional        |
| REQ-8 | Notifiactions               | User gets notifications if they are approaching a spending limit of the budget.| 3       | Functional        |
| REQ-9 | Safety                      | User passwords must be stored securely and should be encrypted              | 1        | Non-functional    |
| REQ-10 | Performance Optimization    | Ensure quick receipt uploads and processing (<3 seconds for OCR).           | 2        | Non-functional    |
| REQ-11 | Responsive Design           | Ensure compatibility with mobile and desktop browsers.                      | 3        | Non-functional    |
| REQ-12 | Efficiency                 | The application should support up to 1000 active users simultaneously without noticeable lag.| 3        | Non-functional    |


### **B: User Stories**
I. User registration

The user wants to create a new account.

Scenario:

1. The user clicks the "Register" button.
2. The system asks for an email address and password.
3. The user provides data.
4. The system saves the data in the database and displays a confirmation message.

Effect: The user account has been created.

II. User login

The user wants to log in to the system.

Scenario:

1. The user clicks the "Log in" button.
2. The system asks for an email address and password.
3. The user provides data.
4. The system verifies the data.
5. The user is logged into the system.

Required: The user is registered
Effect: The user is logged into the system.

III. Scanning the receipt

The user wants to add a new receipt to the system.

Scenario:

1. The user clicks the "Add receipt" button.
2. The system asks to attach a file with the receipt (photo/scan).
3. The user sends the file.
4. The system analyzes the receipt, extracting products and their prices.
5. The system assigns expenses to appropriate categories.
6. The system saves the data in the database and displays information to the user about adding the receipt.

Required: The user is logged in
Effect: The expense data from the receipt has been saved.

IV. Expense forecasting

The user wants to see the expense forecasts for the next month. 

Scenario:

1. The user selects the "Forecasts" option.
2. The system analyzes the user's previous expenses.
3. The system generates expense forecasts for the next month.
4. The user sees the forecasts in the form of graphs and tables.

Requirement: The user has at least one month of expense history.

Effect: The forecast is displayed to the user.

V. Budget management

The user wants to set a budget for the next month.

Scenario:

1. The user selects the "Set budget" option.
2. The system asks for an amount for each expense category.
3. The user sets the budget amounts.
4. The system saves the data and displays a confirmation message.
Requirement: The user is logged in.
Effect: The budget settings have been saved.

---

## 4. System Architecture

### **Development Stack and deployment stack**
| Name          | Purpose                       | Version   |
|---------------|-------------------------------|-----------|
| FastAPI       | Backend API Framework         | 0.88.0    |
| MongoDB       | NoSQL Database                | 6.0.19    |
| Pytesseract   | OCR for Receipt Processing    | 0.3.13    |
| Docker        | Containerization              | 20.10.8   |
| Ubuntu        | Hosting Environment           | 20.04 LTS |
| Mongoengine   | Database engine               | 0.29.1    |
| Python        | Interpreter                   |      3.11 |



---

## 5. Testing

### **Test Scenarios**

#### **User Registration Tests**
1. **Successful Registration** passed :heavy_check_mark:
   - Test if a new user can register with a unique email address and password.
   - Expected Outcome: User account is created successfully.
2. **Duplicate Email Registration**  passed :heavy_check_mark:
   - Test if the system rejects a registration attempt with an already existing email.
   - Expected Outcome: Error message is displayed, and registration is blocked.
3. **Password Validation**  passed :heavy_check_mark:
   - Test if the system blocks registration when the password does not meet the requirements (e.g., length, digits, special characters).
   - Expected Outcome: Registration fails with appropriate validation error.

---

#### **User Login Tests**
4. **Successful Login**  passed :heavy_check_mark:
   - Test if a user can log in with correct email and password.
   - Expected Outcome: User is successfully authenticated.
5. **Failed Login**  not done 🔲
   - Test if the system rejects incorrect login credentials (e.g., wrong email or password).
   - Expected Outcome: Error message is displayed.

---

#### **Receipt Scanning Tests**
6. **Valid Receipt Processing**  partially done 🔲
   - Test if the system correctly extracts products, prices, and categories from a clear receipt.
   - Expected Outcome: Data is accurately extracted and categorized.
7. **Partially Legible Receipt**  not done 🔲
   - Test if the system handles a partially unreadable receipt (e.g., blurred text).
   - Expected Outcome: The system processes as much data as possible and highlights errors.

---

#### **Manual Expense Entry Tests**
8. **Adding a Valid Expense**  passed :heavy_check_mark:
   - Test if the user can manually add an expense with a valid amount and category.
   - Expected Outcome: Expense is saved successfully.
9. **Invalid Data Validation**  not done 🔲
   - Test if the system blocks adding expenses with invalid data (e.g., negative amount or missing category).
   - Expected Outcome: Error message is displayed, and the expense is not saved.

---

#### **Budget Management Tests**
10. **Budget Setup**  not done 🔲
    - Test if the user can set up budgets for specific categories.
    - Expected Outcome: Budgets are saved successfully.
11. **Budget Limit Warning**  not done 🔲
    - Test if the system sends notifications when a user approaches or exceeds the budget limit.
    - Expected Outcome: Warning notification is triggered.

---

#### **Data Consistency Tests**
12. **Receipt Data Consistency**   passed :heavy_check_mark:
    - Test if the data extracted from a receipt is stored accurately in the database.
    - Expected Outcome: Data is consistent and correct.
13. **Category Correction**  not done 🔲
    - Test if the user can manually correct a product's category after an incorrect assignment by the system.
    - Expected Outcome: Category is updated successfully.

---

#### **Expense Forecasting Tests**
14. **Accurate Forecasting**  not done 🔲
    - Test if the system generates accurate spending forecasts based on the user's expense history.
    - Expected Outcome: Forecast aligns with historical data and trends.
15. **Forecast Updates**  not done 🔲
    - Test if forecasts update correctly when a new expense is added or a budget is modified.
    - Expected Outcome: Forecasts are recalculated and displayed accurately.

---

#### **Report Generation Tests**
16. **Financial Report Creation**  not done 🔲
    - Test if the system generates financial reports for a specific time period with correct data.
    - Expected Outcome: Reports are generated with all expenses categorized correctly.
17. **Chart Accuracy**  passed :heavy_check_mark:
    - Test if visualizations (charts) correctly represent expense data.
    - Expected Outcome: Charts align with the data in the reports.

---

#### **System Performance Tests**
18. **Receipt Processing Speed**  not done 🔲
    - Test if the system processes and analyzes receipts within 5 seconds, even with a large dataset.
    - Expected Outcome: Processing time does not exceed 5 seconds.
19. **High User Load**  not done 🔲
    - Test if the system handles simultaneous logins from many users (e.g., 1,000 users).
    - Expected Outcome: No performance degradation or crashes.

---

#### **Authentication Security Tests**
20. **Password Encryption**  passed :heavy_check_mark:
    - Test if passwords are securely encrypted and stored in the database.
    - Expected Outcome: Passwords are hashed and not stored in plain text.
21. **Brute-force Attack Prevention**  not done 🔲
    - Test if the system blocks multiple failed login attempts to prevent brute-force attacks.
    - Expected Outcome: Account is temporarily locked, and the user is notified.

---

## 6. Run
```bash
git clone git@github.com:philoturtle/Inzynieria-oprogramowania.git
cd Inzynieria-oprogramowania
docker compose up -d
```

APP api is exposed at localhost:8080
Mongo express (mongodb web gui) is accessible with http://localhost:8081



