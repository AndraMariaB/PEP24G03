def calcul_medie(nume, note: list):
    for index, nota in enumerate(note.copy()):
        note.append(float(note.pop(0)))
    media = sum(note) / len(note)
    print(f"media este :", media)
    print(f"{nume} a {'picat' if media < 5 else 'trecut'} clasa,")


while True:
    nume = input("Introduceti numele elevului: ")
    note = input("Introduceti notele elevului: ").split(',')
    calcul_medie(nume, note)
