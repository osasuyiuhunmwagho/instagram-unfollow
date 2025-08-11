from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import logging
from dotenv import load_dotenv


# Load environment variables from .env if present
load_dotenv()

# Configuration from environment variables
USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")
HEADLESS = os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes", "on"}
DISABLE_IMAGES = os.getenv("DISABLE_IMAGES", "true").lower() in {"1", "true", "yes", "on"}
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "")
PAGE_LOAD_STRATEGY = os.getenv("PAGE_LOAD_STRATEGY", "eager")  # eager | normal | none
EXPLICIT_WAIT_SECONDS = int(os.getenv("EXPLICIT_WAIT_SECONDS", "20"))


logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def build_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()

    # Performance-focused options
    if HEADLESS:
        # Use the new headless mode for Chrome >= 109 for better compatibility and speed
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--lang=en-US")

    # Disable images to speed up page loads, if enabled
    if DISABLE_IMAGES:
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.notifications": 2,
        }
        options.add_experimental_option("prefs", prefs)

    # Faster page readiness; we will rely on explicit waits for specific elements
    options.page_load_strategy = PAGE_LOAD_STRATEGY

    service: Service
    if CHROMEDRIVER_PATH and os.path.exists(CHROMEDRIVER_PATH):
        logger.info("Using ChromeDriver from CHROMEDRIVER_PATH")
        service = Service(CHROMEDRIVER_PATH)
    else:
        logger.info("Using webdriver-manager to provision ChromeDriver (cached)")
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_position(0, 0)
    return driver


def login(driver: webdriver.Chrome) -> None:
    wait = WebDriverWait(driver, EXPLICIT_WAIT_SECONDS)

    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    username_input.clear()
    username_input.send_keys(USERNAME)

    password_input.clear()
    password_input.send_keys(PASSWORD)

    # The login button selector can change; using a more stable approach with role or type
    try:
        # Try common button selector variants
        login_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "button[type='submit'], div[role='button'] button[type='submit']",
                )
            )
        )
        login_button.click()
    except TimeoutException:
        # Fallback to the original class-based selector if necessary
        logger.info("Primary login button selector failed; trying fallback selector")
        fallback_selector = "._acan._acap._acas._aj1-._ap30"
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, fallback_selector)))
        login_button.click()


def click_button_css(driver: webdriver.Chrome, css_selector: str) -> None:
    wait = WebDriverWait(driver, EXPLICIT_WAIT_SECONDS)
    try:
        logger.info(f"Clicking element: {css_selector}")
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        element.click()
    except (StaleElementReferenceException, TimeoutException):
        logger.info("Retrying click due to stale or timeout...")
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        element.click()


def navigate_to_inbox(driver: webdriver.Chrome) -> None:
    wait = WebDriverWait(driver, EXPLICIT_WAIT_SECONDS)

    # Open profile dropdown via avatar (alt attribute contains username)
    dropdown_css = f"[alt*='{USERNAME}']"
    click_button_css(driver, dropdown_css)

    # Navigate to inbox via href
    inbox_css = "a[href*='/direct/inbox']"
    click_button_css(driver, inbox_css)

    # Wait for inbox to be visible to ensure navigation completed
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[role='dialog'], [href*='/direct/t/']")))


def main() -> None:
    if not USERNAME or not PASSWORD:
        raise SystemExit("Please set USERNAME and PASSWORD in environment variables or .env file")

    driver = build_driver()
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        login(driver)
        navigate_to_inbox(driver)
        logger.info("Successfully navigated to inbox")
    finally:
        # Ensure we free resources
        driver.quit()


if __name__ == "__main__":
    main()
