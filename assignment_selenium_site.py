from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 15)

# Navigate to site
driver.get("https://www.saucedemo.com/")

##############################
# 1. Login
##############################
wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print("✅ Logged in successfully.")

##############################
# 2. Add all items to cart
##############################
add_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
for btn in add_buttons:
    btn.click()
print(f"✅ Added {len(add_buttons)} items to the cart.")

##############################
# 3. Remove a few items
##############################
remove_buttons = driver.find_elements(By.XPATH, "//button[text()='Remove']")
for i in range(2):
    remove_buttons[i].click()
print("✅ Removed 2 items from the cart.")

##############################
# 4. Go to cart
##############################
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
print(f"🛒 {len(cart_items)} items in the cart after removal.")

##############################
# 5. Checkout
##############################
driver.find_element(By.ID, "checkout").click()
wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
print("✅ Checkout form submitted.")

##############################
# 6. Finish
##############################
wait.until(EC.presence_of_element_located((By.ID, "finish"))).click()
confirmation = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
print(f"✅ Order completed: {confirmation.text}")

##############################
# 7. Logout (100% fixed)
##############################
# Click menu
menu_button = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
menu_button.click()
time.sleep(1.5)  # Allow menu animation to complete

# Wait for logout link to be visible
logout_link = wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))

# JavaScript click for reliability
driver.execute_script("arguments[0].click();", logout_link)

print("✅ Logged out successfully.")

# Cleanup
driver.quit()
print("🎉 Selenium script completed successfully.")
