import sqlite3


def sqlite3_connection():
    return sqlite3.connect("sales.db")


def create_tables():
    conn = sqlite3_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
create table if not exists customers (
    customer_id integer primary key,
    name text,
    city text,
    signup_date text
)""")

    cursor.execute(
    """create table if not exists products (
        product_id integer primary key,
        name TEXT,
        category text,
        price real
    )
    """
    )
    cursor.execute(
    """create table if not exists orders (
        order_id integer primary key,
        customer_id integer,
        order_date text,
        foreign key(customer_id) REFERENCES CUSTOMERS (CUSTOMER_ID)
    )
    """
    )
    cursor.execute(
    """create table if not exists orderItems(
        order_item_id integer primary key,
        order_id integer,
        product_id integer,
        quantity integer,
        foreign key(order_id) references orders (order_id),
        foreign key (product_id) references product (product_id)
    )
    """
    )
    conn.commit()
    conn.close()
    