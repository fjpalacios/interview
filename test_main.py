import main


def test_get_price_per_product():
    price = main.get_price_per_product(0)
    assert price == 2.981163654411736


def test_get_list_of_products():
    products = "1 2 3 4"
    list_of_products = main.get_list_of_products(products)
    assert list_of_products == [1, 2, 3, 4]


def test_get_price_from_products():
    products = [1, 2]
    price_from_products = main.get_price_from_products(products)
    assert price_from_products == 9.394128558256284


def test_update_customer_products_new_customer():
    previous_customer_products = {}
    customer = 1
    products = "1 4 5"
    customer_products = \
        main.update_customer_products(
            previous_customer_products, customer, products)
    assert customer_products == {1: "1 4 5"}


def test_update_customer_products_previous_customer():
    previous_customer_products = {1: "1 4 5"}
    customer = 1
    products = "0 3"
    customer_products = \
        main.update_customer_products(
            previous_customer_products, customer, products)
    assert customer_products == {1: "1 4 5 0 3"}


def test_get_products_per_customer():
    orders = [{"id": 0, "customer": 0, "products": "1 0 1 0"}]
    products_per_customer = main.get_products_per_customer(orders)
    assert products_per_customer == {0: "1 0 1 0"}
