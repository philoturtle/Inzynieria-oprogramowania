
# Project Documentation: Intelligent Finance Manager

## Table of contents:
1. [Overview](#1-overview)
2. [Copyright and required licenses](#2-copyright-information)
3. [Requirements specification](#3-requirements-specification)
4. [System architecture](#4-system-architecture)
5. [Testing](#5-testing)


## 1. Overview

**Short Name**: Intelligent Finance Manager  
**Full Name**: Intelligent Financial Management System with Receipt Analysis  

**Description**:  
The Intelligent Finance Manager is a web application designed to help users manage their finances efficiently. The application allows users to scan and upload receipts, automatically extracting and categorizing expenses. Additionally, users can manually add expenses, filter receipts by date, and view detailed analytics with visualizations. The project aims to simplify personal financial management through automation and user-friendly features.

---

## 2. Copyright Information

**Author**:  
Maria Krakowiak

**License**:  
The project is licensed under the MIT License, allowing open use, modification, and distribution while ensuring proper credit to the authors.

---

## 3. Requirements Specification

### **A: Structured List**  

| ID    | Name                        | Description                                                                 | Priority | Category          |
|-------|-----------------------------|-----------------------------------------------------------------------------|----------|-------------------|
| REQ-1 | Receipt Upload              | Allow users to upload scanned receipts in format img. png.                  | 1        | Functional        |
| REQ-2 | Expense Extraction          | Automatically extract expense details from receipts using OCR.              | 1        | Functional        |
| REQ-3 | Manual Expense Entry        | Enable users to manually add expenses.                                      | 1        | Functional        |
| REQ-4 | Receipt Filtering           | Filter receipts by year, month, or day.                                     | 1        | Functional        |
| REQ-5 | Analytics Dashboard         | Display visualizations of expenses grouped by time periods.                 | 2        | Functional        |
| REQ-6 | User Authentication         | Provide login functionality for secure access.                              | 1        | Functional        |
| REQ-7 | Performance Optimization    | Ensure quick receipt uploads and processing (<2 seconds for OCR).           | 2        | Non-functional    |
| REQ-8 | Responsive Design           | Ensure compatibility with mobile and desktop browsers.                      | 3        | Non-functional    |

### **B: User Stories**

1. As a user, I want to upload receipts so that I can keep track of my expenses effortlessly.  
2. As a user, I want to manually add expenses to ensure accuracy for unscanned receipts.  
3. As a user, I want to filter my receipts by date to find specific expenses quickly.  
4. As a user, I want to see expense analytics so that I can understand my spending patterns.

---

## 4. System Architecture

### **Development Stack**
| Name          | Purpose                       | Version   |
|---------------|-------------------------------|-----------|
| FastAPI       | Backend API Framework         | 0.88.0    |
| MongoDB       | NoSQL Database                | 5.0       |
| Pytesseract   | OCR for Receipt Processing    | Latest    |
| Jinja2        | Templating Engine             | Latest    |
| Seaborn       | Data Visualization            | Latest    |
| Chart.js      | Frontend Visualizations       | 3.9.1     |

### **Deployment Stack**
| Name          | Purpose                       | Version   |
|---------------|-------------------------------|-----------|
| Docker        | Containerization              | 20.10.8   |
| Ubuntu        | Hosting Environment           | 20.04 LTS |

---

## 5. Testing

### **Test Scenarios**
| ID    | Test Case Name          | Description                                        | Expected Outcome                    |
|-------|-------------------------|----------------------------------------------------|-------------------------------------|
| TC-1  | Receipt Upload Test     | Upload a valid receipt image.                     | Receipt details extracted properly. |
| TC-2  | Invalid File Format     | Upload an invalid file format (e.g., PDF).        | Receive an error message.           |
| TC-3  | Manual Expense Entry    | Add a manual expense with valid details.          | Expense saved successfully.         |
| TC-4  | Dashboard Visualization | View the analytics dashboard after filtering.     | Charts display correct data.        |

