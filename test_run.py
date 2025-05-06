import re
from playwright.sync_api import Page, expect
import random
import string


def generate_random_user():
    name = 'user_' + ''.join(random.choices(string.ascii_letters, k=6))
    email = name + "@example.com"
    password = "Test1234"
    return name, email, password


def register_user(page: Page, username: str, email: str, password: str):
        page.goto("https://automationexercise.com/")
        page.get_by_role('link', name='Signup / Login').click()
        page.locator('[data-qa="signup-name"]').fill(username)
        page.locator('[data-qa="signup-email"]').fill(email)
        page.get_by_role('button', name='Signup').click()
        expect(page.get_by_text("Enter Account Information")).to_be_visible()

        page.locator('#id_gender1').check()
        page.locator('#password').fill(password)
        page.locator('select[data-qa="days"]').select_option("6")
        page.locator('select[data-qa="months"]').select_option("2")
        page.locator('select[data-qa="years"]').select_option("1994")

        page.locator('#newsletter').check()
        page.locator('#optin').check()

        page.locator('#first_name').fill("Test")
        page.locator('#last_name').fill("User")
        page.locator('#company').fill("Test Company")
        page.locator('#address1').fill("123 Test St")
        page.locator('#address2').fill("Apt 456")
        page.locator('select[data-qa="country"]').select_option("Israel")
        page.locator('#state').fill("State")
        page.locator('#city').fill("City")
        page.locator('#zipcode').fill("123456")
        page.locator('#mobile_number').fill("123456789")

        page.get_by_role('button', name='Create Account').click()
        expect(page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
        page.locator('[data-qa="continue-button"]').click()
        page.get_by_text("Logout").click()

def test_ts_1(page):
        username, email, password = generate_random_user()

        #Step 2
        page.goto("https://automationexercise.com/")

        #Step 3
        expect(page).to_have_title("Automation Exercise")

        #Step 4
        page.get_by_role('link', name='Signup / Login').click()

        #Step 5
        expect(page.get_by_text("New User Signup!")).to_be_visible()

        #Step 6
        page.locator('[data-qa="signup-name"]').fill(username)
        page.locator('[data-qa="signup-email"]').fill(email)

        #Step 7
        page.get_by_role('button', name='Signup').click()

        #Step 8
        expect(page.get_by_text("Enter Account Information")).to_be_visible()

        #Step 9
        page.locator('#id_gender1').check()
        page.locator('#password').fill(password)
        page.locator('select[data-qa="days"]').select_option("6")
        page.locator('select[data-qa="months"]').select_option("2")
        page.locator('select[data-qa="years"]').select_option("1994")

        #Step 10
        page.locator('#newsletter').check()

        #Step 11
        page.locator('#optin').check()

        #Step 12
        page.locator('#first_name').fill("Test1")
        page.locator('#last_name').fill("Test2")
        page.locator('#company').fill("Test3")
        page.locator('#address1').fill("Test4")
        page.locator('#address2').fill("Test5")
        page.locator('select[data-qa="country"]').select_option("Israel")
        page.locator('#state').fill("Test6")
        page.locator('#city').fill("Test7")
        page.locator('#zipcode').fill("Test8")
        page.locator('#mobile_number').fill("Test9")

        #Step 13
        page.get_by_role('button', name='Create Account').click()

        #Step 14
        expect(page.get_by_text("ACCOUNT CREATED!")).to_be_visible()

        #Step 15
        page.locator('[data-qa="continue-button"]').click()

        #Step 16
        expect(page.get_by_text(f"Logged in as {username}")).to_be_visible()

        #Step 17
        page.get_by_text("Delete Account").click()

        #Step 18
        expect(page.get_by_text("Account Deleted!")).to_be_visible()
        page.get_by_text("Continue").click()

#Login User with correct email and password
def test_ts_2(page):
        username, email, password = generate_random_user()
        register_user(page, username, email, password)

        #Step 2
        page.goto("https://automationexercise.com/")

        #Step 3
        expect(page).to_have_title("Automation Exercise")

        #Step 4
        page.get_by_role('link', name='Signup / Login').click()

        #Step 5
        expect(page.get_by_text("Login to your account")).to_be_visible()

        #Step 6
        page.locator('[data-qa="login-email"]').fill(email)
        page.locator('[data-qa="login-password"]').fill(password)

        #Step 7
        page.locator('[data-qa="login-button"]').click()

        #Step 8
        expect(page.get_by_text(f"Logged in as {username}")).to_be_visible()

        #Step 9
        page.get_by_text("Delete Account").click()

        #Step 10
        expect(page.get_by_text("Account Deleted!")).to_be_visible()
        page.get_by_text("Continue").click()