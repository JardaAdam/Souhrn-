from connect_db import session
from models_students import *

print("Všechny známky - výpis ve formátu: jméno a příjmení studenta: známka")

rows = session.query(Student, Grade).join(Grade)
for student, grade in rows:
    print(f"{student.first_name} {student.last_name}: {grade.grade}")

print('-' * 80)
print("Výpis všech známek pro každého studenta")
# TODO odcházím na večeři v 19:30

print("Výpis počtu známek pro každého studenta")

print("Výpis průměrné známky pro každého studenta")

print("Student s nejlepším průměrným hodnocením")

print("Smazání nejstarší známky")
