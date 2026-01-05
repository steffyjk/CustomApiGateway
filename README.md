📌 Task: Build an API Gateway Service
Objective

Design and implement an API Gateway that acts as an intermediary layer between external clients and backend services.
The gateway must expose selected APIs, enforce security policies, apply rate limiting, and forward validated requests to a downstream service.

Functional Requirements
1. API Exposure

Expose the following REST APIs through the gateway:

/users

/posts

/comments

/albums

/photos

/todos

All APIs must be accessible via the gateway and routed to a backend service.

2. Backend Integration

The gateway must forward incoming requests to the backend service:

https://jsonplaceholder.typicode.com


The gateway must act purely as a proxy layer and should not implement business logic.

3. Authentication & Authorization

Secure all APIs using API Key–based authentication.

Clients must provide a valid API key via request headers.

Unauthorized or invalid requests must be rejected with appropriate HTTP status codes.

4. Rate Limiting

Implement rate limiting to prevent abuse.

Rate limits must be enforced per client (API key).

Requests exceeding the allowed limit must be rejected with 429 Too Many Requests.

5. Request Validation

Only allow predefined routes and supported HTTP methods.

Reject unknown or unsupported endpoints.

Validate required headers before forwarding requests.

6. Security

Prevent forwarding sensitive client headers (e.g., API keys, authorization headers) to the backend service.

Ensure safe and controlled communication between the gateway and backend.

7. Logging & Monitoring

Log incoming requests with:

Client identifier

Endpoint

HTTP method

Response status code

Request processing time

Logs should assist in debugging and auditing.

8. Performance & Scalability

The gateway must be implemented using an asynchronous, non-blocking framework.

The design should support horizontal scalability.

Shared rate limiting should work across multiple instances.

Non-Functional Requirements

The system should be modular and maintainable.

The codebase should follow clean architecture principles.

The gateway should be easily extendable for future features such as JWT authentication, caching, or additional backend services.

Deliverables

Fully functional API Gateway service

Well-structured source code

README with setup and usage instructions

Example API requests for testing

Summary

This task demonstrates the implementation of a real-world API Gateway that handles authentication, rate limiting, request validation, secure proxying, and logging—reflecting production-level backend engineering practices.