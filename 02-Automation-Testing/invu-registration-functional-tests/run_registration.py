from __future__ import annotations

from pages.registration_page import RegistrationPage
from utils.config import Settings
from utils.driver_factory import create_chrome_driver


def main() -> None:
    settings = Settings()
    driver = create_chrome_driver(settings.headless)

    try:
        page = RegistrationPage(driver, settings.wait_timeout)
        email = settings.build_email()

        page.open_registration_form(settings.base_url)
        page.fill_registration_form(
            first_name=settings.first_name,
            last_name=settings.last_name,
            email=email,
            password=settings.password,
        )

        if not settings.submit_form:
            print("Registration form opened and filled successfully.")
            print(f"Generated email: {email}")
            print("Form submission is disabled. Set INVU_SUBMIT_FORM=true to submit it.")
            return

        page.submit_registration()
        result = page.verify_submission_result(settings.base_url, email)

        print("=" * 60)
        print("INVU Registration Automation Result")
        print("=" * 60)
        print(f"Success: {result.success}")
        print(f"Email used: {result.email}")
        print(f"Message: {result.message}")
        print("=" * 60)

        if not result.success:
            raise AssertionError(result.message)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
