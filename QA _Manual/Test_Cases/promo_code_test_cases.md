# Promo Code Test Cases

## Test Case 313: Create New Promo Code
- **Description:** Verify that the admin panel allows creating a new promo code  
- **Preconditions:** User is authorized in admin panel  
- **Postconditions:** New promo code is created  
- **Priority:** High  
- **Severity:** Critical  
- **Type:** Functional  
- **Behavior:** Positive  
- **Automation:** Not automated  
- **Status:** Actual  
- **Layer:** Unknown  
- **Steps:**
  1. Go to "Promo codes and rules" in CompanyX
  2. Click "Create new promo code"
  3. Fill in basic information with valid data
  4. Set discount settings appropriately
  5. Configure conditions as needed
  6. Click "Create" or "Create and create more"
- **Expected Results:**
  1. Promo code is successfully created
  2. Cart rule is created successfully
  3. All required fields are correctly populated
  4. Discount settings applied correctly
  5. Conditions saved successfully
  6. Additional promo codes can be created if needed

---

## Test Case 402: Prevent Duplicate Promo Code
- **Description:** Verify that the system does not allow creating a duplicate promo code  
- **Preconditions:** 
  - Admin is authorized in admin panel  
  - A promo code with the code "satesto001" already exists in CompanyX system  
- **Postconditions:** Only one promo code with this code exists  
- **Priority:** High  
- **Severity:** Major  
- **Type:** Functional  
- **Behavior:** Negative  
- **Automation:** Not automated  
- **Status:** Actual  
- **Layer:** E2E  
- **Steps:**
  1. Go to "Promo codes and coupons" in CompanyX
  2. Click "Create new promo code"
  3. Enter the existing coupon code "satesto001"
  4. Observe system behavior
  5. Click "Create" or "Create and create more"
- **Expected Results:**
  1. System prevents duplicate promo code creation
  2. Error messages are displayed
  3. Coupon is not created
  4. Fields remain populated for correction
  5. No duplicate is saved

---

## Test Case 414: Invalid Coupon Parameters
- **Description:** Verify system behavior when entering invalid promo code data  
- **Preconditions:** Admin is authorized in admin panel  
- **Postconditions:** Coupon is not created in the system  
- **Priority:** High  
- **Severity:** Major  
- **Type:** Functional  
- **Behavior:** Negative  
- **Automation:** Not automated  
- **Status:** Actual  
- **Layer:** E2E  
- **Steps:**
  1. Click "Create new promo code" in CompanyX
  2. Enter coupon code: "sate011"
  3. Fill in discount settings
  4. Enter percentage discount: -30%
  5. Click "Create" or "Create and create more"
- **Expected Results:**
  1. System displays an error
  2. Coupon is not created
  3. Invalid fields are highlighted
  4. No invalid data is saved
  5. User can correct inputs

---

## Test Case 419: Coupon Validity Dates
- **Description:** Verify that the "valid from" and "valid to" fields save correctly  
- **Preconditions:** Admin is authorized in admin panel  
- **Postconditions:** Dates are correctly stored in CompanyX  
- **Priority:** High  
- **Severity:** Critical  
- **Type:** Functional  
- **Behavior:** Positive  
- **Automation:** Not automated  
- **Status:** Actual  
- **Layer:** E2E  
- **Steps:**
  1. Go to "Promo codes and coupons"
  2. Click "Create new promo code"
  3. Fill in basic information
  4. Set discount settings
  5. Enter "valid from" and "valid to" dates
- **Expected Results:**
  1. Dates are saved correctly
  2. Fields display correct values
  3. Admin panel reflects changes
  4. Promo code is usable within specified dates
  5. System accepts valid date range

---

## Test Case 429: Edit Existing Promo Code for Additional Settings
- **Description:** Verify additional parameters can be added to an existing promo code  
- **Preconditions:** 
  - Admin is authorized in admin panel  
  - Promo code exists in CompanyX system  
- **Postconditions:** Additional parameter is successfully activated  
- **Priority:** Medium  
- **Severity:** Normal  
- **Type:** Functional  
- **Behavior:** Positive  
- **Automation:** Not automated  
- **Status:** Actual  
- **Layer:** E2E  
- **Steps:**
  1. Edit promo code "satesto011"
  2. Modify discount target
  3. Enable "Free shipping" option
- **Expected Results:**
  1. Additional parameter is activated
  2. Changes are saved successfully
  3. Promo code functions as expected

---

## Test Case 432: Create Fixed Discount Amount Promo Code
- **Description:** Verify that a promo code can be created with only a fixed discount amount  
- **Preconditions:** Admin is authorized in admin panel  
- **Postconditions:** Promo code is created successfully  
- **Priority:** High  
- **Severity:** Major  
- **Type:** Functional  
- **Behavior:** Positive  
- **Automation:** Not automated  
- **Status:** Actual  
- **Layer:** E2E  
- **Steps:**
  1. Go to "Promo codes and coupons"
  2. Click "Create new promo code"
  3. Fill in basic information
  4. Fill in discount settings
  5. Set Fixed Discount Amount: 50 USD
  6. Set Condition: Minimum Cart Amount 150 USD
  7. Click "Create" or "Create and create more"
- **Expected Results:**
  1. Promo code is created successfully
  2. Discount amount is correctly applied
  3. Minimum cart condition works
  4. Promo code functions as intended
