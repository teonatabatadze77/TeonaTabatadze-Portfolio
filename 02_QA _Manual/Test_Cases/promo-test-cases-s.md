
**ID:** 313

**Title:** Create Promo Code

**Description:** Verify that a new promo code can be created successfully

**Preconditions:** User is logged into the SampleApp admin panel

**Postconditions:** Promo code is created in the system

**Priority:** High

**Severity:** Major

**Type:** Functional

**Steps:**

1. Navigate to Promo Codes and Coupons
2. Click Create New Promo Code
3. Enter promo code TESTCODE001
4. Fill in the required fields
5. Click Create

**Expected Result:**

Promo code is created successfully and appears in the promo codes list

---

**ID:** 402

**Title:** Create Duplicate Promo Code

**Description:** Verify that the system does not allow duplicate promo codes

**Preconditions:** Promo code TESTCODE001 already exists

**Postconditions:** Duplicate promo code is not created

**Priority:** High

**Severity:** Major

**Type:** Functional

**Steps:**

1. Navigate to Promo Codes and Coupons
2. Click Create New Promo Code
3. Enter promo code TESTCODE001
4. Fill in the required fields
5. Click Create

**Expected Result:**

System displays an error message that the promo code already exists

---

**ID:** 414

**Title:** Invalid Coupon Parameter

**Description:** Verify validation when invalid coupon parameters are entered

**Preconditions:** User is logged into the SampleApp admin panel

**Postconditions:** Invalid coupon is not created

**Priority:** High

**Severity:** Major

**Type:** Functional

**Steps:**

1. Navigate to Promo Codes and Coupons
2. Click Create New Promo Code
3. Enter coupon code
4. Enter invalid discount value
5. Click Create

**Expected Result:**

System shows validation error and does not allow invalid parameters

---

**ID:** 419

**Title:** Coupon Date Validation

**Description:** Verify validation of coupon start and end dates

**Preconditions:** User is logged into the SampleApp admin panel

**Postconditions:** Coupon dates are validated

**Priority:** Medium

**Severity:** Major

**Type:** Functional

**Steps:**

1. Navigate to Promo Codes and Coupons
2. Click Create New Promo Code
3. Enter coupon information
4. Set start date and end date
5. Click Create

**Expected Result:**

System validates coupon date range correctly
