class Angajat:

    def __init__(self, salariu, departament):
        self.salariu = salariu
        self.departament = departament

    def get_details(self):
        return f"salariu:{self.salariu},\ndepartament:{self.departament}"


class Firma:
    angajati: list[Angajat] = []

    def adaugare_angajati(self, *args: Angajat):
        for ang in args:
            self.angajati.append(ang)

    def detalii_angajati(self):
        for ang in self.angajati:
            print(ang.get_details())


if __name__ == "__main__":
    firma1 = Firma()
    angajat1 = Angajat(3000, 'HR')
    angajat2 = Angajat(2500, 'HR')
    firma1.adaugare_angajati(angajat1, angajat2)
    firma1.detalii_angajati()
