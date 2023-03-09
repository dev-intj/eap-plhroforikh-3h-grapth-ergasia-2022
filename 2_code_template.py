class Camera:  # Κλάση Camera
    # Ζητείται να αρχικοποιήσετε τη συνάρτηση του αντικειμένου Camera
    def __init__(self, location, operation, zoom, night_vision):
        self.location = location
        self.operation = operation
        self.zoom = zoom
        self.night_vision = night_vision

    # Ζητείται να δημιουργήσετε τη μέθοδο που ενεργοποιεί ή απενεργοποιεί την Camera
    def power(self):
        self.operation = not self.operation

    # Ζητείται να δημιουργήσετε τη μέθοδο που αυξάνει το zoom της Camera
    def zoomUp(self):
        if (self.zoom + 1 != 11):
            self.zoom += 1

    # Ζητείται να δημιουργήσετε τη μέθοδο που μειώνει το zoom της Camera
    def zoomDown(self):
        if (self.zoom - 1 != - 1):
            self.zoom -= 1

    # Ζητείται να δημιουργήσετε τη μέθοδο που ενεργοποιεί ή απενεργοποιεί τη λειτουργία νυχτερινής όρασης της Camera
    def nightVision(self):
        self.night_vision = not self.night_vision

    # Μέθοδος αποτύπωσης των συγκεντρωτικών πληροφοριών για όλες τις λειτουργίες της Camera
    def __str__(self):
        out = f'Στοιχεία Κάμερας:\nΤοποθεσία: {self.location}\n'
        out += f"Κατάσταση κάμερας: {'σε λειτουργία' if self.operation else 'απενεργοποιημένη'}\n"
        if self.operation:
            out += f"zoom: {self.zoom}\n"
            out += f"{'(νυχτερινή όραση)' if self.night_vision else ''}\n"
        return out

    def __repr__(self):
        return repr(self.location)


class Panel():  # Κλάση πίνακα ελέγχου
    def __init__(self):  # Ζητείται να δημιουργήσετε μια λίστα με αντικείμενα τύπου Camera
        tameio = Camera("Ταµείο", True, 5, False)
        eisodos = Camera("Είσοδος", True, 5, False)
        apothiki = Camera("Αποθήκη", True, 5, False)
        self.items = []
        self.items.append(tameio)
        self.items.append(eisodos)
        self.items.append(apothiki)
        self.camera = None

    # Ζητείται να δημιουργήσετε τη μέθοδο που επιτρέπει στον χρήστη να επιλέξει τη Camera την οποία θα ελέγξει
    def select_camera(self, index):
        self.camera = self.items[index]

    # Mέθοδος για έλεγχο της επιλεγμένης Camera (power, zoom, night_vision)
    def control_panel(self):
        while True:
            print(f"\nΠανελ ελέγχου κάμερας {self.camera.location}")
            print(self.camera)
            sel = input(
                'o(on/off), (z)oom (+/-), (n)(yes/no), <enter>: exit:').strip()
            if not sel:
                break
            if sel[0].lower() == "z":
                if sel[-1] == "+":
                    self.camera.zoomUp()
                if sel[-1] == "-":
                    self.camera.zoomDown()
            elif sel[0].lower() == "n":
                self.camera.nightVision()
            elif sel[0].lower() == "o":
                self.camera.power()

    # Μέθοδος αποτύπωσης των συγκεντρωτικών πληροφοριών για όλες τις λειτουργίες της Camera
    def __str__(self):
        out = "Οι κάµερες ασφαλείας είναι: \n"
        for idx, i in enumerate(self.items):
            out += f'{idx}.{i.location} \n'
        return out


panel = Panel()

print(panel)

userInput = None
while userInput != "":
    userInput = input("\nΕπιλέξτε κάµερα, <return> για έξοδο: ")

    try:
        int(userInput)
        panel.select_camera(int(userInput))
        panel.control_panel()
    except:
        print('Έξοδος εφαρμογής')
