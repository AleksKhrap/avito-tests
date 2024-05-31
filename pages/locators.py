from selenium.webdriver.common.by import By


class EcoContributionLocators:
    COUNTERS_MAIN_BLOCK = (By.CSS_SELECTOR, ".desktop-impact-items-F7T6E")
    WATER_COUNTER_BLOCK = (By.CSS_SELECTOR, ".desktop-impact-items-F7T6E :nth-child(4)")
    CO2_COUNTER_BLOCK = (By.CSS_SELECTOR, ".desktop-impact-items-F7T6E :nth-child(2)")
    ENERGY_COUNTER_BLOCK = (By.CSS_SELECTOR, ".desktop-impact-items-F7T6E :nth-child(6)")
    AVATAR_BLOCK = (By.CSS_SELECTOR, ".desktop-impact-items-F7T6E :nth-child(5)")
