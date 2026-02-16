Construction Resource Optimizer API (Senior Python Suite)
📌 Project Overview
A production-ready microservice designed to calculate high-efficiency resource allocation for large-scale engineering projects. This project demonstrates Senior-level engineering practices including Clean Architecture, Test-Driven Development (TDD), and automated CI/CD pipelines.

Key Features
Asynchronous Processing: Built with FastAPI for high-concurrency performance.

TDD Methodology: Developed using a strict Red-Green-Refactor cycle with Pytest.

Strict Typing: Full implementation of Python 3.11 type hinting and Pydantic V2 for data validation.

Containerization: Fully Dockerized for seamless deployment across Linux environments (AWS Fargate/EC2).

🏗 Architecture & Design Patterns
This project adheres to SOLID principles and utilizes the following patterns:

Service Layer Pattern: Logic is decoupled from the API routes to ensure maintainability.

Strategy Pattern: (Planned) To handle different machinery efficiency profiles.

Centralized Error Handling: Custom middleware to translate domain exceptions into standardized HTTP responses.
