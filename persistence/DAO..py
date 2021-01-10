class _Vaccines:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, vaccine):
        cursor = self._conn.cursor()
        self._cursor.execute("""
            INSERT INTO Vaccines (id, date, supplier, quantity) VALUES (?, ?, ?, ?)
        """, [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])

    def fetch_table(self):
        self._cursor.execute("SELECT * FROM Vaccines ORDER BY Vaccines.id")
        all_data = self._cursor.fetchall()
        return all_data


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, supplier):
        self._cursor.execute("""
            INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def fetch_table(self):
        self._cursor.execute("SELECT * FROM Suppliers ORDER BY Suppliers.id")
        all_data = self._cursor.fetchall()
        return all_data


class _Clinics:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, product):
        self._cursor.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)
        """, [product.product_id, product.description, product.price, product.quantity])

    def fetch_table(self):
        self._cursor.execute("SELECT * FROM Products ORDER BY Products.id")
        all_data = self._cursor.fetchall()
        return all_data

    def update(self, product_id, quantity):
        self._cursor.execute("""UPDATE Products SET quantity = quantity + ?
        WHERE id = ?""", [quantity, product_id])

    def get_quantity(self, product_id):
        self._cursor.execute("""SELECT quantity FROM Products
                    WHERE id = ?
                    """, [product_id])
        return int(self._cursor.fetchone()[0])


class _Logistics:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, coffee_stand):
        self._cursor.execute("""
            INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
        """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def fetch_table(self):
        self._cursor.execute(
            "SELECT * FROM Coffee_stands ORDER BY Coffee_stands.id")
        all_data = self._cursor.fetchall()
        return all_data


class _Activities:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, activity):
        self._cursor.execute("""
            INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
        """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def fetch_table(self):
        self._cursor.execute(
            "SELECT * FROM Activities ORDER BY Activities.date")
        all_data = self._cursor.fetchall()
        return all_data
