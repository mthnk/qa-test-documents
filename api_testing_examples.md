# API Testing Examples - E-Commerce Platform

**Project:** TechStore API Testing  
**Tester:** Metehan Kutlu  
**Date:** December 2024  
**Tools:** Postman, Python requests  

---

## API Test Scenarios

### Authentication API Tests

#### Test Case: POST /api/auth/login
**Description:** Test user authentication endpoint  
**Method:** POST  
**Endpoint:** `https://api.techstore.com/v1/auth/login`  

**Request Headers:**
```json
{
    "Content-Type": "application/json",
    "Accept": "application/json"
}
```

**Test Data - Valid Login:**
```json
{
    "email": "testuser@example.com",
    "password": "TestPass123!"
}
```

**Expected Response (200 OK):**
```json
{
    "status": "success",
    "message": "Login successful",
    "data": {
        "user_id": 12345,
        "email": "testuser@example.com",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "expires_in": 3600
    }
}
```

**Test Results:**
- ✅ Status Code: 200 OK
- ✅ Response Time: 245ms
- ✅ Token format valid (JWT)
- ✅ Expires_in field present

---

#### Test Case: POST /api/auth/login - Invalid Credentials
**Test Data - Invalid Login:**
```json
{
    "email": "testuser@example.com", 
    "password": "wrongpassword"
}
```

**Expected Response (401 Unauthorized):**
```json
{
    "status": "error",
    "message": "Invalid credentials",
    "error_code": "AUTH_001"
}
```

**Test Results:**
- ✅ Status Code: 401 Unauthorized
- ✅ Response Time: 180ms
- ✅ Error message clear and appropriate
- ✅ No sensitive data leaked in response

---

### Product API Tests

#### Test Case: GET /api/products
**Description:** Retrieve product list with pagination  
**Method:** GET  
**Endpoint:** `https://api.techstore.com/v1/products?page=1&limit=10`  

**Request Headers:**
```json
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "Accept": "application/json"
}
```

**Expected Response (200 OK):**
```json
{
    "status": "success",
    "data": {
        "products": [
            {
                "id": 1001,
                "name": "iPhone 14 Pro",
                "price": 999.99,
                "currency": "USD",
                "stock": 25,
                "category": "smartphones"
            }
        ],
        "pagination": {
            "current_page": 1,
            "total_pages": 50,
            "total_items": 500,
            "items_per_page": 10
        }
    }
}
```

**Test Results:**
- ✅ Status Code: 200 OK
- ✅ Response Time: 320ms
- ✅ Pagination data correct
- ✅ Product fields complete
- ⚠️ Price format consistent (2 decimal places)

---

#### Test Case: GET /api/products/{id}
**Description:** Get single product details  
**Method:** GET  
**Endpoint:** `https://api.techstore.com/v1/products/1001`  

**Expected Response (200 OK):**
```json
{
    "status": "success", 
    "data": {
        "id": 1001,
        "name": "iPhone 14 Pro",
        "description": "Latest iPhone with A16 Bionic chip...",
        "price": 999.99,
        "currency": "USD",
        "stock": 25,
        "category": "smartphones",
        "images": [
            "https://cdn.techstore.com/products/iphone14pro_1.jpg"
        ],
        "specifications": {
            "storage": "128GB",
            "color": "Space Black",
            "warranty": "1 year"
        }
    }
}
```

**Test Results:**
- ✅ Status Code: 200 OK
- ✅ Response Time: 280ms
- ✅ All product fields present
- ✅ Image URLs accessible

---

#### Test Case: GET /api/products/{id} - Product Not Found
**Method:** GET  
**Endpoint:** `https://api.techstore.com/v1/products/99999`  

**Expected Response (404 Not Found):**
```json
{
    "status": "error",
    "message": "Product not found",
    "error_code": "PRODUCT_001"
}
```

**Test Results:**
- ✅ Status Code: 404 Not Found
- ✅ Response Time: 150ms
- ✅ Appropriate error message
- ✅ Error code for debugging

---

### Shopping Cart API Tests

#### Test Case: POST /api/cart/add
**Description:** Add product to shopping cart  
**Method:** POST  
**Endpoint:** `https://api.techstore.com/v1/cart/add`  

**Request Headers:**
```json
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
    "product_id": 1001,
    "quantity": 2,
    "specifications": {
        "color": "Space Black",
        "storage": "128GB"
    }
}
```

**Expected Response (201 Created):**
```json
{
    "status": "success",
    "message": "Product added to cart",
    "data": {
        "cart_item_id": 5001,
        "product_id": 1001,
        "quantity": 2,
        "unit_price": 999.99,
        "total_price": 1999.98,
        "added_at": "2024-12-19T10:30:00Z"
    }
}
```

**Test Results:**
- ✅ Status Code: 201 Created
- ✅ Response Time: 290ms
- ✅ Cart item ID generated
- ✅ Price calculation correct
- ✅ Timestamp in ISO format

---

#### Test Case: GET /api/cart
**Description:** Retrieve user's shopping cart  
**Method:** GET  
**Endpoint:** `https://api.techstore.com/v1/cart`  

**Expected Response (200 OK):**
```json
{
    "status": "success",
    "data": {
        "cart_id": "cart_user_12345",
        "items": [
            {
                "cart_item_id": 5001,
                "product": {
                    "id": 1001,
                    "name": "iPhone 14 Pro",
                    "price": 999.99
                },
                "quantity": 2,
                "subtotal": 1999.98
            }
        ],
        "summary": {
            "total_items": 2,
            "subtotal": 1999.98,
            "tax": 159.99,
            "shipping": 0.00,
            "total": 2159.97
        }
    }
}
```

**Test Results:**
- ✅ Status Code: 200 OK
- ✅ Response Time: 210ms
- ✅ Cart calculations accurate
- ✅ Tax calculation applied
- ❌ **BUG FOUND:** Total calculation incorrect (should be 2159.97)

---

## API Testing with Python Requests

### Automated API Test Script

```python
import requests
import json
import time

class APITestSuite:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None
        
    def login_and_get_token(self):
        """Authenticate and store token for subsequent requests"""
        login_data = {
            "email": "testuser@example.com",
            "password": "TestPass123!"
        }
        
        response = self.session.post(
            f"{self.base_url}/auth/login",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            self.token = response.json()["data"]["token"]
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}"
            })
            return True
        return False
        
    def test_get_products(self):
        """Test products endpoint"""
        response = self.session.get(f"{self.base_url}/products")
        
        # Assertions
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 1.0  # Response time < 1sec
        
        data = response.json()
        assert "products" in data["data"]
        assert "pagination" in data["data"]
        
        print("✅ Products API test passed")
        
    def test_add_to_cart(self):
        """Test add to cart functionality"""
        cart_data = {
            "product_id": 1001,
            "quantity": 1
        }
        
        response = self.session.post(
            f"{self.base_url}/cart/add",
            json=cart_data
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["status"] == "success"
        assert "cart_item_id" in data["data"]
        
        print("✅ Add to cart API test passed")

# Test execution
if __name__ == "__main__":
    api_test = APITestSuite("https://api.techstore.com/v1")
    
    if api_test.login_and_get_token():
        api_test.test_get_products()
        api_test.test_add_to_cart()
        print("All API tests completed successfully!")
```

---

## Performance Testing Results

### Response Time Analysis
| Endpoint | Method | Avg Response Time | Max Response Time | Status |
|----------|---------|------------------|-------------------|---------|
| /auth/login | POST | 245ms | 380ms | ✅ Good |
| /products | GET | 320ms | 450ms | ⚠️ Acceptable |
| /products/{id} | GET | 280ms | 350ms | ✅ Good |
| /cart/add | POST | 290ms | 420ms | ✅ Good |
| /cart | GET | 210ms | 300ms | ✅ Excellent |

### Load Testing (100 concurrent users)
- **Success Rate:** 99.2%
- **Average Response Time:** 315ms
- **95th Percentile:** 650ms
- **Failed Requests:** 8/1000 (timeout errors)

---

## Security Testing Observations

### Authentication Security
- ✅ JWT tokens properly formatted
- ✅ Token expiration implemented (3600 seconds)
- ✅ Invalid credentials handled securely
- ⚠️ **Recommendation:** Implement rate limiting for login attempts

### Data Validation
- ✅ Input validation on required fields
- ✅ Proper HTTP status codes returned
- ✅ Error messages don't reveal sensitive information
- ⚠️ **Recommendation:** Add input sanitization for special characters

---

## Bug Summary - API Testing

### Found Issues
1. **Cart Total Calculation Bug** - High Priority
   - Endpoint: GET /api/cart
   - Issue: Total calculation incorrect in some scenarios
   - Expected: 2159.97, Actual: 2149.97

2. **Response Time Degradation** - Medium Priority
   - Endpoint: GET /api/products
   - Issue: Response time occasionally exceeds 400ms
   - Recommendation: Database query optimization

### Recommendations
1. Implement comprehensive API monitoring
2. Add automated API regression testing
3. Enhance error logging for debugging
4. Consider API rate limiting implementation

---

**Testing Environment:**
- **Hardware:** Intel i5 12th Gen, RTX 3060, 32GB RAM
- **Network:** Stable broadband connection
- **Tools:** Postman v10.x, Python requests library
- **Test Duration:** 3 days
- **Total API Calls:** 1,247 requests

**Tester:** Metehan Kutlu  
**LinkedIn:** [linkedin.com/in/metehank](https://linkedin.com/in/metehank)