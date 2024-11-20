import psycopg2
import password


class MenuItem:
    your_p = password.password
    db = "Public"
    user_n = "postgres"
    port = 5433
    host = "localhost"
    items = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        MenuItem.items.append(self)

    def save(self):
        save_q = '''
        INSERT INTO Menu_Items(item_name, item_price)
        VALUES(%s, %s);
        '''
        try:
            with psycopg2.connect(
                    host=MenuItem.host, password=MenuItem.your_p, dbname=MenuItem.db,
                    port=MenuItem.port, user=MenuItem.user_n) as db:
                with db.cursor() as cursor:
                    cursor.execute(save_q, (self.name, self.price))
            print(f"Deleted {self.name}, {self.price}")
        except Exception as e:
            print("Error saving item", e)

    def delete(self):
        delete_q = '''
        DELETE FROM Menu_Items
        WHERE item_name = %s
'''
        try:
            with psycopg2.connect(
                    host=MenuItem.host, password=MenuItem.your_p, dbname=MenuItem.db,
                    port=MenuItem.port, user=MenuItem.user_n) as db:
                with db.cursor() as cursor:
                    cursor.execute(delete_q, (self.name,))
            print(f"deleted {self.name}, {self.price}")
        except Exception as e:
            print("Error deleting item", e)

    def update(self, name=None, price=None):

        if name is not None:
            u_name = name
        else:
            u_name = self.name
        if price is not None:
            u_price = price
        else:
            u_price = self.price
        update_q = '''
        UPDATE Menu_Items
        SET item_name = %s, item_price = %s
        WHERE item_name = %s
'''
        try:
            with psycopg2.connect(
                    host=MenuItem.host, password=MenuItem.your_p, dbname=MenuItem.db,
                    port=MenuItem.port, user=MenuItem.user_n) as db:
                with db.cursor() as cursor:
                    cursor.execute(update_q, (u_name, u_price, self.name))
            print(f"Updated with {u_name}, {u_price}")
        except Exception as e:
            print("Error updating item", e)

        self.name = u_name
        self.price = u_price

    def __repr__(self):
        return f"MenuItem(name='{self.name}', price={self.price})"

