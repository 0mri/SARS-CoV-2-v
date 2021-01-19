from persistence import DAO, DTO
import sqlite3
import atexit
import os


class _Repository:
    def __init__(self):
        if os.path.isfile("database.db"):
            os.remove("database.db")
        self._conn = sqlite3.connect('database.db')
        self.vaccines = DAO._Vaccines(self._conn)
        self.suppliers = DAO._Suppliers(self._conn)
        self.clinics = DAO._Clinics(self._conn)
        self.logistics = DAO._Logistics(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""        
        CREATE TABLE IF NOT EXISTS vaccines (
            id INTEGER PRIMARY KEY,
            date DATE NOT NULL,
            supplier INTEGER REFERENCES suppliers(id),
            quantity INTEGER NOT NULL
        );
    
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name STRING NOT NULL,
            logistic INTEGER REFERENCES logistics(id)
        );
    
        CREATE TABLE IF NOT EXISTS clinics (
            id INTEGER PRIMARY KEY,
            location STRING NOT NULL,
            demand INTEGER NOT NULL,
            logistic INTEGER REFERENCES logistics(id)
        );
        CREATE TABLE IF NOT EXISTS logistics (
            id INTEGER PRIMARY KEY,
            name STRING NOT NULL,
            count_sent INTEGER NOT NULL,
            count_received INTEGER NOT NULL
        );
        """)

    def receive(self, order_data_arr):
        supplier = self.suppliers.get(name=order_data_arr[0])
        vaccine = DTO.Vaccine(
            0, order_data_arr[2], supplier.id, order_data_arr[1])
        self.vaccines.insert(vaccine)
        logistic = self.logistics.get(id=supplier.logistic)
        self.logistics.increment(logistic, count_received=order_data_arr[1])
        self._conn.commit()

    def send(self, order_data_arr):
        amount = int(order_data_arr[1])
        vaccine = self.vaccines.first()
        while vaccine:
            if (amount - vaccine.quantity > 0):
                self.vaccines.delete(vaccine)
                amount = amount - vaccine.quantity
            else:
                self.vaccines.decrease(vaccine, quantity=amount)
                amount = 0
                break
            vaccine = self.vaccines.first()

        supplied = int(order_data_arr[1]) - amount
        clinic = self.clinics.get(location=order_data_arr[0])
        self.clinics.decrease(clinic, demand=supplied)
        logistic = self.logistics.get(id=clinic.logistic)
        self.logistics.increment(logistic, count_sent=supplied)
        self._conn.commit()


repo = _Repository()
atexit.register(repo._close)
