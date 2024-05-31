from .base_page import BasePage
from .locators import EcoContributionLocators


class EcoContributionPage(BasePage):
    def find_all_counters_blocks(self, name="1"):
        self.take_a_screenshot(*EcoContributionLocators.COUNTERS_MAIN_BLOCK, name)

    def find_water_counter_block(self):
        self.take_a_screenshot(*EcoContributionLocators.WATER_COUNTER_BLOCK, name="2")

    def find_co2_counter_block(self):
        self.take_a_screenshot(*EcoContributionLocators.CO2_COUNTER_BLOCK, name="3")

    def find_energy_counter_block(self):
        self.take_a_screenshot(*EcoContributionLocators.ENERGY_COUNTER_BLOCK, name="4")

    def find_avatar_block(self):
        self.take_a_screenshot(*EcoContributionLocators.AVATAR_BLOCK, name="5")
