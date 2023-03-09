#
#                               --->  Fuel Pump
#       Ignition -->  Battery --
#                               --->  Engine
#
class Component:
    # Αρχικοποίηση ονόματος, κατάστασης και δομής αποθήκευσης συνδεδεμένων εξαρτημάτων
    def __init__(self, name):
        self.name = name
        self.power = False
        self.connected = []

    # Προσθήκη εξαρτήματος στη δομή αποθήκευσης συνδεδεμένων εξαρτημάτων
    def connect(self, other):
        self.connected.append(other)

    # Αλλαγή κατάστασης, εκκίνηση συνδεδεμένων εξαρτημάτων και εκτύπωση μηνύματος έναρξης του κάθε εξαρτήματος
    def start(self):
        if not self.power:
            self.power = True
            print(f"Εξάρτημα {self.name}: έναρξη λειτουργίας")
            for comp in self.connected:
                comp.start()

    # Αναστολή λειτουργίας συνδεδεμένων εξαρτημάτων, αλλαγή κατάστασης και εκτύπωση μηνύματος αναστολής του εξαρτήματος
    def stop(self):
        if self.power:
            for comp in self.connected:
                comp.stop()
            self.power = False
            print(f"Εξάρτημα {self.name}: παύση λειτουργίας")

    # Εκτύπωση συνδεδεμένων εξαρτημάτων και κατάστασης εξαρτήματος
    def status(self):
        if (self.power):
            print(f"Κατάσταση: {self.name} σε λειτουργία")
        else:
            print(f"Κατάσταση: {self.name} εκτός λειτουργίας")

        for component in self.connected:
            component.status()


class Ignition(Component):
    def __init__(self, name):
        super().__init__(name)


class Battery(Component):
    def __init__(self, name):
        super().__init__(name)


class FuelPump(Component):
    def __init__(self, name):
        super().__init__(name)


class Engine(Component):
    def __init__(self, name):
        super().__init__(name)


class Car:
    def __init__(self):
        # Δημιουργία των εξαρτημάτων του αυτοκινήτου
        self.ignition = Ignition('Μίζα')
        self.battery = Battery('Μπαταρία')
        self.fuelPump = FuelPump('Αντλία Καυσίμου')
        self.engine = Engine('Κινητήρας')

        # Σύνδεση των εξαρτημάτων μεταξύ τους
        self.ignition.connect(self.battery)
        self.battery.connect(self.fuelPump)
        self.battery.connect(self.engine)

    def status(self):
        print('=========================')
        self.ignition.status()
        print('=========================')


if __name__ == "__main__":
    car = Car()
    car.status()
    car.ignition.start()
    car.status()
    car.ignition.stop()
    car.status()
