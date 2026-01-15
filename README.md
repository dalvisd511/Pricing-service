# Pricing Service – Backend API (Flask)

## Overview

This project is a **backend Pricing Service API** built using **Python and Flask**, designed to simulate how large-scale travel platforms (like Expedia Group) calculate and return dynamic prices based on user input. The service demonstrates clean backend architecture, API design, input validation, and business-logic separation — aligned with real-world backend engineering practices.

The project was built as a **portfolio-grade backend system** to showcase backend development fundamentals, system structure, and readiness for Software Development Engineer (Backend) roles.

---

## Key Objectives

* Build a clean, modular backend service using Flask
* Design a RESTful API endpoint for price calculation
* Apply object-oriented programming and data validation
* Follow industry-standard project and folder structure
* Demonstrate Git/GitHub workflow and professional documentation

---

## Tech Stack

* **Language:** Python 3
* **Framework:** Flask
* **API Style:** REST
* **Version Control:** Git & GitHub
* **Environment:** Local development (VS Code)

---

## Project Structure

```
pricing-service/
│
├── app/
│   ├── __init__.py        # Flask app initialization
│   ├── main.py            # Application entry point
│   ├── models.py          # Request data models and validation
│   ├── services.py        # Pricing business logic
│   └── routes.py          # API route definitions
│
├── tests/                 # Placeholder for unit tests
│   └── test_pricing.py
│
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignored files
```

---

## API Functionality

### Endpoint: Calculate Price

**URL**

```
POST /price
```

**Description**
Accepts a pricing request and returns a calculated price based on quantity and base rate logic.

---

### Request Body (JSON)

```json
{
  "base_price": 100,
  "quantity": 2
}
```

| Field      | Type | Description                    |
| ---------- | ---- | ------------------------------ |
| base_price | int  | Base price of the item/service |
| quantity   | int  | Number of units requested      |

---

### Response (JSON)

```json
{
  "final_price": 200
}
```

---

## Business Logic

The pricing calculation is intentionally simple and transparent:

```
final_price = base_price * quantity
```

This structure allows easy extension for:

* Discounts
* Dynamic pricing rules
* Taxes and fees
* Localization logic

---

## How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/pricing-service.git
cd pricing-service
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python -m app.main
```

### Step 4: Access the API

Open browser or API client:

```
http://127.0.0.1:5000/price
```

---

## What This Project Demonstrates

* Backend API development using Flask
* Clean separation of concerns (routes, services, models)
* Object-oriented design for request handling
* Error-free local server execution
* GitHub-based version control and documentation
* Readiness for scalable backend system design

---

## Future Improvements

* Add unit tests using pytest
* Introduce database integration
* Add logging and monitoring
* Implement advanced pricing rules
* Convert to microservice-ready architecture

---

## Why This Project Matters

This project reflects how **real backend teams** build and structure services:

* Clear API contracts
* Modular and maintainable code
* Strong foundation for distributed systems

It is intentionally aligned with **entry-level backend engineering roles** in high-scale tech environments.

---

## Author

**Shubham Dalvi**
Backend Developer | Python | Flask

---

## License

This project is for educational and portfolio purposes.

