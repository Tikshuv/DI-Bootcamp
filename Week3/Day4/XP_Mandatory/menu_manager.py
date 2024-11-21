import psycopg2
import password
from menu_item import MenuItem


class MenuManager:
    your_p = password.password
    db = "Public"
    user_n = "postgres"
    port = 5433
    host = "localhost"

    @classmethod
    def get_by_name(cls, name):
        """Get one item from db by name"""
        q = '''
                SELECT item_name, item_price
                FROM Menu_Items
                WHERE item_name = %s;
                '''
        try:
            with psycopg2.connect(
                    host=cls.host, password=cls.your_p, dbname=cls.db,
                    port=cls.port, user=cls.user_n
            ) as db:
                with db.cursor() as cursor:
                    cursor.execute(q, (name,))
                    result = cursor.fetchone()
                    if result:
                        print(result)
                        return MenuItem(result[0], result[1])
                    else:
                        return None
        except Exception as e:
            print(f"Error fetching item by name: {e}")
            return None

    @classmethod
    def all_items(cls):
        """Get all items from the db."""
        q = '''
            SELECT item_name, item_price
            FROM Menu_Items;
            '''
        try:
            with psycopg2.connect(
                    host=cls.host, password=cls.your_p, dbname=cls.db,
                    port=cls.port, user=cls.user_n
            ) as db:
                with db.cursor() as cursor:
                    cursor.execute(q)
                    results = cursor.fetchall()
                    print(results)
                    return [MenuItem(row[0], row[1]) for row in results]
        except Exception as e:
            print(f"Error fetching all items: {e}")
            return []
import dotenv

#
# a = MenuItem('Beer', 33)
# a.save()
# a.update('Vodka', 50)
# b = MenuItem('Sausage', 10)
# b.delete()
# b.save()
# MenuManager.get_by_name('Vodka')
# print(MenuManager.all_items())
MenuManager.all_items()
