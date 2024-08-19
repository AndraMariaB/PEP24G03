angajat1 = {
    'nume': 'Ana-Maria Popescu',
    'departament': 'IT',
    'ID': 3409,
    'Salar': 4560,
}
angajat2 = {
    'nume': 'Marian Muntean',
    'departament': 'IT',
    'ID': 2235,
    'Salar': 4556,
}
angajat3 = {
    'nume': 'Maria Manea',
    'departament': 'HR',
    'ID': 1908,
    'Salar': 6755,
}
angajat4 = {
    'nume': 'Oana Popa',
    'departament': 'HR',
    'ID': 1977,
    'Salar': 5400,
}
angajat5 = {
    'nume': 'David Codru',
    'departament': 'Management',
    'ID': 1988,
    'Salar': 12900,
}
lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]


def list_well_payed_employees(lista):
    for angajat in lista:
        if angajat.get("Salar") > 5000:
            print(f"{angajat.get('nume')}-->{angajat.get('departament')}{angajat.get('ID')}")


list_well_payed_employees(lista_dict)


def list_employees(lista):
    lista_employees = []
    for angajat in lista:
        if not angajat.get('departament') == 'Management':
            lista_employees.append(angajat)
    return lista_employees


print(list_employees(lista_dict))


def hr_average(lista):
    sum = 0
    number = 0
    for angajat in lista:
        if angajat.get('departament') == 'HR':
            sum += angajat.get('Salar')
            number += 1
    return sum / number


print(hr_average(lista_dict))
