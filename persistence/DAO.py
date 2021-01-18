from persistence.DTO import *


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, vaccine):
        cursor = self._conn.cursor()
        self._cursor.execute("""
            INSERT INTO vaccines (date, supplier, quantity) VALUES (?, ?, ?)
        """, [vaccine.date, vaccine.supplier, vaccine.quantity])

    def get(self, **kwargs):
        col = list(kwargs.keys())[0]  # first argument-key
        val = list(kwargs.values())[0]  # first argument-val
        self._cursor.execute("""
            SELECT * FROM vaccines WHERE {} = ?
        """.format(col), [val])
        return Vaccine(*self._cursor.fetchone())

    def all(self, *kwargs):
        self._cursor.execute("""
            SELECT * FROM vaccines ORDER BY vaccines.id
        """)
        if(kwargs):
            col = list(kwargs.keys())[0]  # first argument-key
            val = list(kwargs.values())[0]  # first argument-val
            self._cursor.execute("""
            SELECT * FROM vaccines WHERE {} = ? ORDER BY vaccines.id
                """.format(col), [val])

        _all = self._cursor.fetchall()
        return [Logistic(*logistic) for logistic in _all]

    def first(self):
        self._cursor.execute("""
            SELECT * FROM vaccines ORDER BY(date) ASC
        """)
        return Vaccine(*self._cursor.fetchone())

    def decrease(self, vaccine, **kwargs):
        col = list(kwargs.keys())[0]   # first argument-key
        val = list(kwargs.values())[0]  # first argument-val

        self._cursor.execute("""
        UPDATE vaccines SET {col} = ({col} - ?) WHERE vaccines.id = (?)
        """.format(col=col), [val, vaccine.id])

    def delete(self, vaccine):
        self._conn.execute("""
                DELETE FROM vaccines WHERE id = ? 
        """, [vaccine.id])

    def sum(self, col):
        self._cursor.execute("""
                SELECT SUM({col}) FROM vaccines
        """.format(col))
        return self._cursor.fetchone()


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, supplier):
        self._cursor.execute("""
            INSERT INTO suppliers (id, name, logistic) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.logistic])

    def get(self, **kwargs):
        col = list(kwargs.keys())[0]  # first argument-key
        val = list(kwargs.values())[0]  # first argument-val
        self._cursor.execute("""
            SELECT * FROM suppliers WHERE {} = ?
        """.format(col), [val])
        return Supplier(*self._cursor.fetchone())

    def all(self, *kwargs):
        self._cursor.execute("""
            SELECT * FROM suppliers ORDER BY suppliers.id
        """)
        if(kwargs):
            col = list(kwargs.keys())[0]  # first argument-key
            val = list(kwargs.values())[0]  # first argument-val
            self._cursor.execute("""
            SELECT * FROM suppliers WHERE {} = ? ORDER BY suppliers.id
                """.format(col), [val])

        _all = self._cursor.fetchall()
        return [Logistic(*logistic) for logistic in _all]


class _Clinics:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, clinic):
        self._conn.execute("""
        INSERT INTO clinics (id, location, demand, logistic) VALUES (?, ?, ?, ?)
                """, [clinic.id, clinic.location, clinic.demand, clinic.logistic]
        )

    def get(self, **kwargs):
        col = list(kwargs.keys())[0]  # first argument-key
        val = list(kwargs.values())[0]  # first argument-val
        self._cursor.execute("""
            SELECT * FROM clinics WHERE {} = ?
        """.format(col), [val])
        return Clinic(*self._cursor.fetchone())

    def update(self, logistic, **kwargs):  # ?
        _id = logistic.id
        col = list(kwargs.keys())[0]   # first argument-key
        val = list(kwargs.values())[0]  # first argument-val

        self._cursor.execute("""
        UPDATE logistics SET {col} = (?) WHERE logistics.id = (?)
        """.format(col=col), [val, _id])

    def increment(self, logistic, **kwargs):  # ?
        _id = logistic.id
        col = list(kwargs.keys())[0]   # first argument-key
        val = list(kwargs.values())[0]  # first argument-val

        self._cursor.execute("""
        UPDATE logistics SET {col} = ({col} + ?) WHERE logistics.id = (?)
        """.format(col=col), [val, _id])

    def decrease(self, logistic, **kwargs):  # ?
        _id = logistic.id
        col = list(kwargs.keys())[0]   # first argument-key
        val = list(kwargs.values())[0]  # first argument-val

        self._cursor.execute("""
        UPDATE logistics SET {col} = ({col} - ?) WHERE logistics.id = (?)
        """.format(col=col), [val, _id])


class _Logistics:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, logistic):
        self._conn.execute("""
        INSERT INTO logistics (id, name, count_sent, count_received) VALUES (?, ?, ?, ?)
        """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_received]
        )

    def get(self, **kwargs):
        col = list(kwargs.keys())[0]  # first argument-key
        val = list(kwargs.values())[0]  # first argument-val
        self._cursor.execute("""
            SELECT * FROM logistics WHERE {} = ?
        """.format(col), [val])
        return Logistic(*self._cursor.fetchone())

    def all(self, **kwargs):
        self._cursor.execute("""
            SELECT * FROM logistics
        """)
        if(kwargs):
            col = list(kwargs.keys())[0]  # first argument-key
            val = list(kwargs.values())[0]  # first argument-val
            self._cursor.execute("""
            SELECT * FROM logistics WHERE {} = ?
                """.format(col), [val])

        _all = self._cursor.fetchall()
        return [Logistic(*logistic) for logistic in _all]

    def update(self, logistic, **kwargs):  # ?
        _id = logistic.id
        col = list(kwargs.keys())[0]   # first argument-key
        val = list(kwargs.values())[0]  # first argument-val

        self._cursor.execute("""
        UPDATE logistics SET {col} = (?) WHERE logistics.id = (?)
        """.format(col=col), [val, _id])

    def increment(self, logistic, **kwargs):  # ?
        _id = logistic.id
        col = list(kwargs.keys())[0]   # first argument-key
        val = list(kwargs.values())[0]  # first argument-val

        self._cursor.execute("""
        UPDATE logistics SET {col} = ({col} + ?) WHERE logistics.id = (?)
        """.format(col=col), [val, _id])

    def decrease(self, logistic, **kwargs):  # ?
        col = list(kwargs.keys())[0]   # first argument-key
        val = list(kwargs.values())[0]  # first argument-val

        self._cursor.execute("""
        UPDATE logistics SET {col} = ({col} - ?) WHERE logistics.id = (?)
        """.format(col=col), [val, logistic.id])

    def sum(self, col):
        self._cursor.execute("""
                SELECT SUM({col}) FROM vaccines
        """.format(col))
        return self._cursor.fetchone()
