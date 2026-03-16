
# API Testing – Postman Collection

## API Information

Base URL: https://reqres.in/api

Authentication: API Key required in header

Header Key: x-api-key  
Header Value: reqres-free-v1

---

## Collection Details

Collection Name: Second_Lecture_Demo  
Tool Used: Postman  
Testing Type: API Testing / Automated Response Validation

---

## Endpoints Tested

### 1. GET – Retrieve User by ID
Endpoint:
https://reqres.in/api/users/50

Purpose:
Verify system behavior when requesting a user that does not exist.

Test Script Used:

pm.test("Status code is 404", function () {
    pm.response.to.have.status(404);
});

Expected Result:
The API should return HTTP Status Code **404 (Not Found)**.

---

### 2. GET – Valid User Request

Purpose:
Verify that the API successfully returns user information when a valid ID is provided.

Expected Result:
Status Code 200 and correct user data in the response body.

---

### 3. POST – Create User

Purpose:
Verify that a new user can be created using a POST request.

Expected Result:
Status Code 201 and newly created user object in response.

---

### 4. PUT – Update User

Purpose:
Verify that existing user information can be updated.

Expected Result:
Status Code 200 and updated user information returned.

---

### 5. GET – Invalid URL Request

Purpose:
Verify system behavior when an incorrect endpoint is used.

Expected Result:
Appropriate error response from the API.

---

## Test Validation

The following validations are implemented in Postman scripts:

- Response status code validation
- API error handling verification
- Endpoint functionality verification

---

## Testing Outcome

This Postman collection demonstrates:

- Basic API request testing
- Response validation using automated scripts
- Handling valid and invalid API requests
- Verification of HTTP status codes

---

## Tools Used

Postman – API testing tool  
ReqRes API – Public API for testing
