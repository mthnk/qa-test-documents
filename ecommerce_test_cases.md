# Test Cases - E-Commerce Website

**Project:** TechStore Online Shopping Platform  
**Tester:** Metehan Kutlu  
**Date:** December 2024  

## User Registration & Authentication

### TC001 - User Registration with Valid Data
**Priority:** High  
**Severity:** Critical  
**Prerequisites:** Browser is open, website is accessible  

**Test Steps:**
1. Navigate to registration page
2. Enter valid email: testuser@example.com
3. Enter password: TestPass123!
4. Confirm password: TestPass123!
5. Enter first name: Metehan
6. Enter last name: Test
7. Click "Register" button

**Expected Result:** User successfully registered, redirected to dashboard  
**Test Data:** Valid email format, strong password  
**Status:** Not Executed  

---

### TC002 - Login with Valid Credentials
**Priority:** High  
**Severity:** Critical  
**Prerequisites:** User account exists  

**Test Steps:**
1. Navigate to login page
2. Enter email: testuser@example.com
3. Enter password: TestPass123!
4. Click "Login" button

**Expected Result:** User successfully logged in, redirected to homepage  
**Test Data:** Existing user credentials  
**Status:** Not Executed  

---

### TC003 - Login with Invalid Password
**Priority:** Medium  
**Severity:** High  
**Prerequisites:** User account exists  

**Test Steps:**
1. Navigate to login page
2. Enter valid email: testuser@example.com
3. Enter invalid password: wrongpass
4. Click "Login" button

**Expected Result:** Error message displayed: "Invalid email or password"  
**Test Data:** Valid email, invalid password  
**Status:** Not Executed  

---

## Product Search & Catalog

### TC004 - Search Product by Name
**Priority:** High  
**Severity:** Medium  
**Prerequisites:** User is on homepage  

**Test Steps:**
1. Click on search bar
2. Type "iPhone" in search field
3. Press Enter or click search button
4. Review search results

**Expected Result:** Relevant iPhone products displayed in results  
**Test Data:** "iPhone" keyword  
**Status:** Not Executed  

---

### TC005 - Filter Products by Price Range
**Priority:** Medium  
**Severity:** Low  
**Prerequisites:** User is on product listing page  

**Test Steps:**
1. Navigate to Electronics category
2. Use price filter: Set min price to 500, max price to 1000
3. Click "Apply Filter"
4. Review filtered results

**Expected Result:** Only products within 500-1000 price range displayed  
**Test Data:** Price range: 500-1000  
**Status:** Not Executed  

---

## Shopping Cart Functionality

### TC006 - Add Product to Cart
**Priority:** High  
**Severity:** Critical  
**Prerequisites:** User is logged in, product page is open  

**Test Steps:**
1. Select product: "iPhone 14 Pro"
2. Choose quantity: 1
3. Select color: Space Gray
4. Click "Add to Cart" button
5. Verify cart icon updates with item count

**Expected Result:** Product added to cart, cart counter increases  
**Test Data:** iPhone 14 Pro, Qty: 1, Color: Space Gray  
**Status:** Not Executed  

---

### TC007 - Update Cart Quantity
**Priority:** Medium  
**Severity:** Medium  
**Prerequisites:** Cart has at least one item  

**Test Steps:**
1. Navigate to shopping cart
2. Locate product in cart
3. Change quantity from 1 to 3
4. Click "Update" button
5. Verify total price calculation

**Expected Result:** Quantity updated, total price recalculated correctly  
**Test Data:** Original qty: 1, New qty: 3  
**Status:** Not Executed  

---

### TC008 - Remove Item from Cart
**Priority:** Medium  
**Severity:** Medium  
**Prerequisites:** Cart has at least one item  

**Test Steps:**
1. Navigate to shopping cart
2. Locate product to remove
3. Click "Remove" or trash icon
4. Confirm removal if prompted
5. Verify item is removed from cart

**Expected Result:** Item removed, cart total updated, cart counter decreases  
**Test Data:** Any item in cart  
**Status:** Not Executed  

---

## Checkout Process

### TC009 - Complete Checkout with Valid Data
**Priority:** High  
**Severity:** Critical  
**Prerequisites:** User logged in, items in cart  

**Test Steps:**
1. Navigate to shopping cart
2. Click "Proceed to Checkout"
3. Verify shipping address
4. Select shipping method: Standard (5-7 days)
5. Enter payment details (Test Card)
6. Review order summary
7. Click "Place Order"

**Expected Result:** Order completed successfully, confirmation page displayed  
**Test Data:** Valid shipping address, test payment details  
**Status:** Not Executed  

---

### TC010 - Checkout with Empty Cart
**Priority:** Low  
**Severity:** Low  
**Prerequisites:** User logged in, empty cart  

**Test Steps:**
1. Navigate to shopping cart (empty)
2. Try to click "Proceed to Checkout"

**Expected Result:** Error message or disabled checkout button  
**Test Data:** Empty cart  
**Status:** Not Executed  

---

## Mobile Responsive Testing

### TC011 - Mobile Navigation Menu
**Priority:** High  
**Severity:** Medium  
**Prerequisites:** Mobile device (iPhone 14), website loaded  
**Device:** iPhone 14 (iOS 17.x)  

**Test Steps:**
1. Open website on iPhone 14
2. Verify hamburger menu appears
3. Tap hamburger menu
4. Verify menu items are accessible
5. Test menu item navigation

**Expected Result:** Mobile menu works correctly, all items accessible  
**Test Data:** iPhone 14 screen size  
**Status:** Not Executed  

---

### TC012 - Mobile Cart Functionality
**Priority:** High  
**Severity:** High  
**Prerequisites:** Mobile device (iPhone XR), user logged in  
**Device:** iPhone XR (iOS 16.x)  

**Test Steps:**
1. Add product to cart on iPhone XR
2. Navigate to cart page
3. Verify cart items display correctly
4. Test quantity update on mobile
5. Test remove item functionality

**Expected Result:** Cart functions properly on mobile, touch interactions work  
**Test Data:** iPhone XR screen size  
**Status:** Not Executed  

---

## Cross-Browser Testing

### TC013 - Login Function - Chrome
**Priority:** High  
**Severity:** High  
**Browser:** Chrome (Latest)  
**OS:** Windows 11  

**Test Steps:**
1. Open Chrome browser
2. Navigate to login page
3. Enter valid credentials
4. Verify login success

**Expected Result:** Login works correctly in Chrome  
**Status:** Not Executed  

---

### TC014 - Login Function - Firefox
**Priority:** High  
**Severity:** High  
**Browser:** Firefox (Latest)  
**OS:** Windows 11  

**Test Steps:**
1. Open Firefox browser
2. Navigate to login page
3. Enter valid credentials
4. Verify login success

**Expected Result:** Login works correctly in Firefox  
**Status:** Not Executed  

---

### TC015 - Login Function - Safari
**Priority:** High  
**Severity:** High  
**Browser:** Safari (Latest)  
**Device:** iPhone 14  

**Test Steps:**
1. Open Safari on iPhone 14
2. Navigate to login page
3. Enter valid credentials
4. Verify login success

**Expected Result:** Login works correctly in Safari mobile  
**Status:** Not Executed  

---

## Test Summary
**Total Test Cases:** 15  
**Critical Priority:** 8  
**High Priority:** 6  
**Medium Priority:** 1  
**Coverage Areas:** Authentication, Product Management, Cart, Checkout, Mobile, Cross-browser  

**Testing Environment:**
- Desktop: Intel i5 12th Gen, 32GB RAM, RTX 3060
- Mobile: iPhone 14, iPhone XR
- Browsers: Chrome, Firefox, Safari