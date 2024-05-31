import pytest
from pages.eco_contribution_page import EcoContributionPage


@pytest.mark.parametrize("link", ["https://www.avito.ru/avito-care/eco-impact"])
class TestGuestEcoContributionPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        self.eco_contribution_page = EcoContributionPage(browser, link)
        self.eco_contribution_page.open()

    def test_guest_can_see_all_counters_blocks(self):
        self.eco_contribution_page.find_all_counters_blocks()

    def test_guest_can_see_default_content_in_water_counter_block(self):
        self.eco_contribution_page.find_water_counter_block()

    def test_guest_can_see_default_content_in_co2_counter_block(self):
        self.eco_contribution_page.find_co2_counter_block()

    def test_guest_can_see_default_content_in_energy_counter_block(self):
        self.eco_contribution_page.find_energy_counter_block()

    def test_guest_cant_see_photo_in_avatar_block(self):
        self.eco_contribution_page.find_avatar_block()

    def test_guest_can_see_semitransparent_font_in_all_blocks(self):
        self.eco_contribution_page.find_all_counters_blocks(name="6")
