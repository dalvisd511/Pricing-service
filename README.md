# Backend Pricing & Availability Service

## Overview
This project is a backend service that simulates dynamic pricing logic similar to
travel and marketplace pricing systems. It calculates optimized prices based on
demand and availability inputs.

## Tech Stack
- Python
- Flask
- REST APIs
- Pytest
- Git

## Features
- REST API to calculate dynamic prices
- Modular, maintainable code structure
- Input validation and error handling
- Unit tests for pricing logic

## API Example

POST /price

Request:
{
  "base_price": 120,
  "demand": "high",
  "availability": "low"
}

Response:
{
  "final_price": 187.2
}

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   python app/main.py

3. Run tests:
   pytest

## Learning Outcomes
- Backend API development
- Object-oriented programming
- Writing testable and maintainable code
- Debugging and validation
