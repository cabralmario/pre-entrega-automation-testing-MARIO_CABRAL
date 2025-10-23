from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_saucedemo(setup_driver):
    driver = setup_driver
    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products", "❌ El login no fue exitoso"

    print("✅ Login exitoso en SauceDemo")
    time.sleep(2)


def test_agregar_producto_al_carrito(setup_driver):
    driver = setup_driver
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # Agregar un producto al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    assert carrito == "1", "❌ No se agregó el producto correctamente"
    print("✅ Producto agregado al carrito con éxito")
    time.sleep(2)
