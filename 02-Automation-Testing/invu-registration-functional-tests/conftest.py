from __future__ import annotations

import pytest

from utils.config import Settings
from utils.driver_factory import create_chrome_driver


@pytest.fixture
def settings() -> Settings:
    return Settings()


@pytest.fixture
def driver(settings: Settings):
    driver = create_chrome_driver(settings.headless)
    yield driver
    driver.quit()
