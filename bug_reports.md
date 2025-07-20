# Bug Reports - E-Commerce Website

**Project:** TechStore Online Shopping Platform  
**Tester:** Metehan Kutlu  
**Reporting Date:** December 2024  

---

## Bug Report #001

**Title:** Shopping Cart Total Price Not Updated After Item Removal  
**Bug ID:** BUG-001  
**Date Reported:** 15.12.2024  
**Reporter:** Metehan Kutlu  
**Severity:** High  
**Priority:** High  
**Status:** Open  

### Environment
- **Browser:** Chrome 120.0.6099.62
- **OS:** Windows 11
- **Device:** Desktop (Intel i5 12th Gen, 32GB RAM)
- **Resolution:** 1920x1080

### Description
When removing an item from the shopping cart, the total price is not recalculated correctly. The subtotal remains the same as before removal.

### Steps to Reproduce
1. Add iPhone 14 Pro ($999) to cart
2. Add iPad Air ($599) to cart  
3. Verify total shows $1,598
4. Remove iPad Air from cart
5. Check total price

### Expected Result
Total price should update to $999 (iPhone 14 Pro only)

### Actual Result
Total price remains $1,598 despite iPad Air being removed

### Test Data
- iPhone 14 Pro: $999
- iPad Air: $599
- Expected total after removal: $999
- Actual total after removal: $1,598

### Impact
Users may be charged incorrect amounts during checkout

### Attachments
- Screenshot: cart-total-bug-001.png
- Browser console log: console-error-001.txt

---

## Bug Report #002

**Title:** Mobile Navigation Menu Overlaps with Page Content  
**Bug ID:** BUG-002  
**Date Reported:** 16.12.2024  
**Reporter:** Metehan Kutlu  
**Severity:** Medium  
**Priority:** Medium  
**Status:** Open  

### Environment
- **Browser:** Safari Mobile
- **OS:** iOS 17.2
- **Device:** iPhone 14
- **Resolution:** 390x844

### Description
On iPhone 14, when opening the hamburger menu, it overlaps with the main page content instead of pushing it aside or covering it properly with a background overlay.

### Steps to Reproduce
1. Open website on iPhone 14
2. Tap hamburger menu icon (☰)
3. Observe menu behavior

### Expected Result
Menu should either:
- Push page content to the right, OR
- Cover content with proper background overlay

### Actual Result
Menu appears over content without proper background, making both menu and content partially visible and confusing

### Test Data
- Device: iPhone 14 (390x844 resolution)
- Browser: Safari iOS 17.2
- Menu items: Home, Products, Cart, Account, Contact

### Impact
Poor user experience on mobile devices, navigation becomes difficult

### Attachments
- Screenshot: mobile-menu-overlap-002.png
- Screen recording: menu-behavior-002.mp4

---

## Bug Report #003

**Title:** Password Field Shows Plain Text in Firefox  
**Bug ID:** BUG-003  
**Date Reported:** 16.12.2024  
**Reporter:** Metehan Kutlu  
**Severity:** Critical  
**Priority:** Critical  
**Status:** Open  

### Environment
- **Browser:** Firefox 121.0
- **OS:** Windows 11
- **Device:** Desktop (Intel i5 12th Gen, 32GB RAM)

### Description
In the login form, password input field displays entered text as plain text instead of masking it with dots/asterisks in Firefox browser.

### Steps to Reproduce
1. Open Firefox browser
2. Navigate to login page
3. Click on password field
4. Type any password (e.g., "TestPass123!")
5. Observe password visibility

### Expected Result
Password should be masked with dots (•••••••••••)

### Actual Result  
Password appears as plain text: "TestPass123!"

### Test Data
- Test password: TestPass123!
- Browser: Firefox 121.0
- Working correctly in: Chrome, Safari

### Impact
**SECURITY RISK:** Password visible to anyone looking at the screen

### Attachments
- Screenshot: password-plaintext-firefox-003.png
- Browser info: firefox-version-003.txt

### Additional Notes
- Bug only occurs in Firefox
- Tested in Chrome and Safari - working correctly
- Affects both login and registration forms

---

## Bug Report #004

**Title:** Search Function Returns No Results for Valid Products  
**Bug ID:** BUG-004  
**Date Reported:** 17.12.2024  
**Reporter:** Metehan Kutlu  
**Severity:** Medium  
**Priority:** High  
**Status:** Open  

### Environment
- **Browser:** Chrome 120.0.6099.62
- **OS:** Windows 11
- **Device:** Desktop

### Description
Search function fails to return results for products that exist in the catalog when searching with specific terms.

### Steps to Reproduce
1. Navigate to homepage
2. Click search bar
3. Enter "macbook" (lowercase)
4. Press Enter or click search button
5. Observe results

### Expected Result
Should display MacBook products available in catalog

### Actual Result
"No products found" message displayed

### Test Data
- Search term: "macbook" (lowercase)
- Existing products: MacBook Pro 13", MacBook Air M2
- Working search terms: "MacBook" (exact case), "laptop"

### Impact
Users cannot find products they're looking for, potential sales loss

### Workaround
Search with exact case matching works ("MacBook")

### Attachments
- Screenshot: search-no-results-004.png
- Product catalog: available-products-004.xlsx

---

## Bug Report #005

**Title:** Checkout Button Disabled After Adding iPhone XR  
**Bug ID:** BUG-005  
**Date Reported:** 17.12.2024  
**Reporter:** Metehan Kutlu  
**Severity:** High  
**Priority:** High  
**Status:** Open  

### Environment
- **Browser:** Safari Mobile  
- **OS:** iOS 16.7
- **Device:** iPhone XR
- **Resolution:** 414x896

### Description
When adding iPhone XR to cart and proceeding to checkout on iPhone XR device, the checkout button becomes disabled and unclickable.

### Steps to Reproduce
1. Open website on iPhone XR
2. Navigate to iPhone XR product page
3. Add iPhone XR to cart
4. Go to cart page
5. Click "Proceed to Checkout"
6. Observe checkout button status

### Expected Result
Checkout button should be enabled and clickable

### Actual Result
Checkout button appears grayed out and is unclickable

### Test Data
- Product: iPhone XR 128GB Red
- Price: $499
- Cart total: $499
- Device: iPhone XR (iOS 16.7)

### Impact
Users with iPhone XR cannot complete purchases of iPhone XR products

### Additional Notes
- Bug is specific to iPhone XR product + iPhone XR device combination
- Other products work fine on iPhone XR
- iPhone XR product works fine on other devices

### Attachments
- Screenshot: checkout-disabled-xr-005.png
- Device info: iphone-xr-specs-005.txt

---

## Bug Summary

| Bug ID | Title | Severity | Priority | Status | Browser/Device |
|--------|-------|----------|----------|---------|----------------|
| BUG-001 | Cart Total Not Updated | High | High | Open | Chrome/Desktop |
| BUG-002 | Mobile Menu Overlap | Medium | Medium | Open | Safari/iPhone 14 |
| BUG-003 | Password Plain Text | Critical | Critical | Open | Firefox/Desktop |
| BUG-004 | Search Case Sensitivity | Medium | High | Open | Chrome/Desktop |  
| BUG-005 | Checkout Disabled XR | High | High | Open | Safari/iPhone XR |

### Summary Statistics
- **Total Bugs Reported:** 5
- **Critical:** 1 (Security issue)
- **High:** 3 (Functionality issues)  
- **Medium:** 1 (UI/UX issue)
- **Open:** 5
- **Fixed:** 0

### Affected Areas
- Shopping Cart: 1 bug
- Mobile UI: 2 bugs  
- Security: 1 bug
- Search: 1 bug

### Browser Distribution
- Chrome: 2 bugs
- Firefox: 1 bug  
- Safari (Mobile): 2 bugs

**Test Environment Used:**
- Desktop: Intel i5 12th Gen, RTX 3060, 32GB RAM
- Mobile: iPhone 14 (iOS 17.2), iPhone XR (iOS 16.7)
- Browsers: Chrome 120, Firefox 121, Safari Mobile