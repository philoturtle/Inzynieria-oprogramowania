
# Project Documentation: Intelligent Finance Manager

## Table of contents:
1. [Overview](#1-overview)
2. [Copyright and required licenses](#2-copyright-information)
3. [Requirements specification](#3-requirements-specification)
4. [System architecture](#4-system-architecture)
5. [Testing](#5-testing)


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
| REQ-5 | Analytics Dashboard         | Display visualizations of expenses grouped by time periods.                 | 4        | Functional        |
| REQ-6 | User Authentication         | Provide login functionality for secure access.                              | 1        | Functional        |
| REQ-7 | User Registration           | User can create an account by providing email address and password          | 1        | Functional        |
| REQ-8 | Notifiactions               | User gets notifications if they are approaching a spending limit of the budget.| 4       | Functional        |
| REQ-9 | Safety                      | User passwords must be stored securely and should be encrypted              | 1        | Non-functional    |
| REQ-10 | Performance Optimization    | Ensure quick receipt uploads and processing (<3 seconds for OCR).           | 2        | Non-functional    |
| REQ-11 | Responsive Design           | Ensure compatibility with mobile and desktop browsers.                      | 4        | Non-functional    |
| REQ-12 | Efficiency                 | The application should support up to 1000 active users simultaneously without noticeable lag.| 4        | Non-functional    |


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
| Pytesseract   | OCR for Receipt Processing    | Latest    |
| Chart.js      | Frontend Visualizations       | 3.9.1     |
| Docker        | Containerization              | 20.10.8   |
| Ubuntu        | Hosting Environment           | 20.04 LTS |
| Mongoengine   | Database engine               |           |
| VScode        | Code editor                   |           |


---

## 5. Testing

### **Test Scenarios**
| ID    | Test Case Name          | Description                                        | Expected Outcome                    |
|-------|-------------------------|----------------------------------------------------|-------------------------------------|
| TC-1  | Receipt Upload Test     | Upload a valid receipt image.                      | Receipt details extracted properly. |
| TC-2  | Invalid File Format     | Upload an invalid file format (e.g., PDF).         | Receive an error message.           |
| TC-3  | Manual Expense Entry    | Add a manual expense with valid details.           | Expense saved successfully.         |
| TC-4  | Dashboard Visualization | View the analytics dashboard after filtering.      | Charts display correct data.        |

