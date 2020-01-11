import os
import pandas as pd


def get_products():
    products_directory = os.path.abspath("csv/products.csv")
    return pd.read_csv(products_directory)


def get_orders():
    orders_directory = os.path.abspath("csv/orders.csv")
    return pd.read_csv(orders_directory)


def get_customers():
    customers_directory = os.path.abspath("csv/customers.csv")
    return pd.read_csv(customers_directory)


def save_csv(dataframe, file_name):
    csv_directory = os.path.abspath(f"tasks/{file_name}.csv")
    dataframe.to_csv(csv_directory, index=False)


def get_price_per_product(product_id):
    return PRODUCTS[product_id]["cost"]


def get_list_of_products(products):
    return [int(product) for product in products.split(" ")]


def get_price_from_products(products):
    return sum([get_price_per_product(product) for product in products])


def update_customer_products(customer_products, customer, products):
    new_customer = not bool(customer_products.get(customer))
    if new_customer:
        customer_products[customer] = products
        return customer_products
    customer_products[customer] = f"{customer_products[customer]} {products}"
    return customer_products


def get_products_per_customer(orders):
    customer_products = {}
    for order in orders:
        customer_products = \
            update_customer_products(customer_products,
                                     order["customer"], order["products"])
    return customer_products


def get_euros_per_customer(customer_products):
    euros_per_customer = []
    for key, value in customer_products.items():
        products = get_list_of_products(value)
        euros = get_price_from_products(products)
        euros_per_customer.append([key, euros])
    return euros_per_customer


def get_order_prices(orders):
    order_prices = []
    for order in orders:
        products = get_list_of_products(order["products"])
        euros = get_price_from_products(products)
        order_prices.append([order["id"], euros])
    return order_prices


def get_product_customers(products, orders):
    product_customers = []
    for product in products:
        customers = []
        for order in orders:
            products = get_list_of_products(order["products"])
            product_in_order = product["id"] in products
            new_customer = str(order["customer"]) not in customers
            if product_in_order and new_customer:
                customers.append(str(order["customer"]))
        product_customers.append([product["id"], " ".join(customers)])
    return product_customers


def get_customer_ranking_dataframe(euros_per_customer, customers):
    euros_per_customer_df = pd.DataFrame(
        euros_per_customer, columns=["id", "total_euros"])
    customers_with_euros = \
        pd.merge(customers, euros_per_customer_df, on="id").sort_values(
            by=["total_euros"], ascending=False)
    return customers_with_euros


PRODUCTS = get_products().to_dict('records')
ORDERS = get_orders().to_dict('records')
CUSTOMERS = get_customers()


# Task 1
ORDER_PRICES = get_order_prices(ORDERS)
ORDER_PRICES_DF = pd.DataFrame(ORDER_PRICES, columns=["id", "euros"])
save_csv(ORDER_PRICES_DF, "order_prices")


# Task 2
PRODUCT_CUSTOMERS = get_product_customers(PRODUCTS, ORDERS)
PRODUCT_CUSTOMERS_DF = pd.DataFrame(PRODUCT_CUSTOMERS,
                                    columns=["id", "customer_ids"])
save_csv(PRODUCT_CUSTOMERS_DF, "product_customers")


# Task 3
CUSTOMER_RANKING = get_euros_per_customer(get_products_per_customer(ORDERS))
CUSTOMER_RANKING_DF = get_customer_ranking_dataframe(
    CUSTOMER_RANKING, CUSTOMERS)
save_csv(CUSTOMER_RANKING_DF, "customer_ranking")
