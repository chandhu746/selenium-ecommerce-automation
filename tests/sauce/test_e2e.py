from utils.read_config import load_test_data
from pages.sauce.login import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)

def pytest_generate_tests(metafunc):
    site = metafunc.config.getoption("site")
    test_data = load_test_data(site)
    metafunc.parametrize("test_list_item", test_data)

def test_e2e(browserInstance,test_list_item):
    driver, config = browserInstance
    logger.info(f"Running test {test_list_item['base_url']}")

    # Login
    login = LoginPage(driver)
    products = login.login(config["username"],config["password"])

    # add products with condition
    products.add_products_with_conditions(max_price=30,exclude = "t-shirt")

    # navigate to cart
    cart_page = products.go_to_cart()

    # get cart details
    item_names = cart_page.get_item_names()
    item_prices = cart_page.get_item_prices()

    logger.info(f"Cart contains: {item_names}")
    logger.info(f"Cart price: {item_prices}")

    assert  all(price <=30 for price in item_prices),"found item with price > $30"
    assert  all("t-shirt".lower() not in name.lower() for name in item_names),"Excluded item found in cart"

    # checkout page
    checkout_page = cart_page.proceed_to_checkout()
    checkout_page.checkout(first_name="chandhu",last_name="M",post_code="517591")
    order_summary_page = checkout_page.proceed_to_finish()

    # order summary page
    summary_items = order_summary_page.get_item()
    summary_prices = order_summary_page.get_item_prices()
    summary_details = order_summary_page.get_summary_details()

    # logging
    logger.info(f"Order summary items: {summary_items}")
    logger.info(f"Order summary prices: {summary_prices}")
    logger.info(f"Summary totals: {summary_details}")

    # validating
    assert set(item_names) == set(summary_items), "Cart items and summary items mismatch!"
    assert set(item_prices) == set(summary_prices), "Cart prices and summary prices mismatch!"

    # finish page
    finish_page = order_summary_page.finish_order()
    success_message = finish_page.get_success_message()

    assert "THANK YOU" in success_message.upper(), "Order was not completed successfully!"

#     checkout pa
#     ge test code:





