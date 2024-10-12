class Angajat:
    def __init__(self, salariu, departament):
        self.salariu = salariu
        self.departament = departament

    def get_details(self):
        return f"salariu:{self.salariu},\ndepartament:{self.departament}"

    def change_salary(self, procent):
        self.salariu = (int(procent) + 100) / 100 * self.salariu


class Firma:
    angajati: list[Angajat] = []

    def get_department(self, departament):
        return list(filter(lambda x: x.departament == departament, self.angajati))

    def adaugare_angajati(self, *args: Angajat):
        for ang in args:
            self.angajati.append(ang)

    def detalii_angajati(self):
        for ang in self.angajati:
            print(ang.get_details())

    def grow_salary_department(self, departament, procent):
        angajati = self.get_department(departament)
        for angajat in angajati:
            angajat.change_salary(procent)


if __name__ == "__main__":
    firma1 = Firma()
    angajat1 = Angajat(3000, 'HR')
    angajat2 = Angajat(2500, 'HR')
    angajat3 = Angajat(3100, 'IT')
    firma1.adaugare_angajati(angajat1, angajat2, angajat3)
    firma1.detalii_angajati()
    amgajati_hr = firma1.get_department("HR")
    print(80 * '*')
    print(*map(lambda x: x.get_details(), amgajati_hr), sep='\n')
    print(80 * '*')
    print(firma1.get_department("HR"))
    firma1.grow_salary_department(departament='HR', procent=10)
    print(*map(lambda x: x.get_details(), amgajati_hr), sep='\n')
