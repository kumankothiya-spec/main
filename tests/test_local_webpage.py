import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.mark.smoke
def test_local_webpage():
    # Launch browser (Chrome in this example)
    driver = webdriver.Chrome()  # or webdriver.Firefox()

    try:
        # Step 1: Open home page
        driver.get("http://127.0.0.1:5000/")
        assert "Welcome" in driver.page_source

        # Step 2: Navigate to Feedback Form
        form_link = driver.find_element(By.LINK_TEXT, "Feedback Form")
        form_link.click()
        time.sleep(1)

        # Step 3: Fill out the form
        name_input = driver.find_element(By.ID, "name")
        feedback_input = driver.find_element(By.ID, "feedback")

        name_input.send_keys("Kuman")
        feedback_input.send_keys("This is a test feedback.")

        # Step 4: Submit the form
        feedback_input.send_keys(Keys.CONTROL, Keys.RETURN)  # or click submit button
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()
        time.sleep(1)

        # Step 5: Verify response
        assert "Thank you, Kuman!" in driver.page_source
        assert "This is a test feedback." in driver.page_source

        print("✅ Test passed: Local webpage works as expected.")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_local_webpage()