from persistence import DAO, DTO
import sqlite3
import atexit


class _Repository:
    def __init__(self):
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

    def receive_shipment(self, arrOfCurrOrder):
        supplier = self.suppliers.get(name=arrOfCurrOrder[0])
        vaccToAdd = DTO.Vaccine(
            0, arrOfCurrOrder[2], supplier[0], arrOfCurrOrder[1])
        self.vaccines.insert(vaccToAdd)
        logistic = self.logistics.get(id=supplier[2])
        self.logistics.update(logistic, received_count=arrOfCurrOrder[1])
        self._conn.commit()

    def send_shipment(self, arrOfCurrOrder):
        amount = int(arrOfCurrOrder[1])
        while amount > 0:
            vaccine = self.vaccines.getVaccineToSend()
            if vaccine is None:
                break
            tempAmount = amount - vaccine.quantity
            if (tempAmount > 0):
                self.vaccines.deleteVacc(vaccine.id)
                amount = tempAmount
            else:
                self.vaccines.update(vaccine, quantity=amount)
                amount = 0
        supplied = int(arrOfCurrOrder[1]) - amount
        clinic = self.clinics.get(location=arrOfCurrOrder[0])
        self.clinics.updateDemand(clinic[0], supplied)
        logistic = self.logistics.get(id=clinic[3])
        self.logistics.update(logistic, count_sent=supplied)
        self._conn.commit()


repo = _Repository()
atexit.register(repo._close)
