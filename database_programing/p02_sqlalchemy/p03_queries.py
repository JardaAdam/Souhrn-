from sqlalchemy import or_, and_, desc

from connect_db import session, db  # pripojeni do databaze
from models_students import Student
from sqlalchemy.sql import text

# session =

# kombinace cisteho SQL s SQLAlchemy
with db.connect() as conn:
    sql_statement = text("SELECT * FROM students")
    rows = conn.execute(sql_statement)
    for row in rows:
        print(row)

print("Všichni studenti v databázi:")
# SELECT * FROM students;
students = session.query(Student).all()  # vrací seznam objektů
print(f"students: {students}")
for student in students:
    print(student)

print('-' * 80)
print("Počet studentů v databázi:")
total = session.query(Student).count()  # vraci pocet zaznamu
print(f"Počet: {total}")

print('-' * 80)
print("Studenti s id >=2")
""" eqivalent pro:
SELECT * FROM students
WHERE students.id >= 2
"""
rows = session.query(Student).filter(Student.id >= 2)
# print(rows)   # tento radek vypise SQL kod ktery se pouzije pro vypsani
# naseho Py prikazu
for row in rows:
    print(row)

print('-' * 80)
print("Studenti, jejichz prijmeni zacina na 'Svob'")
rows = session.query(Student).filter(Student.last_name.like("Svob%"))
for row in rows:
    print(row)

print('-' * 80)
print("Studenti s id > 2 a prijmeni zacinajici na 'Cer'")
# rows = session.query(Student).filter(Student.id > 4, Student.last_name.like("Cer%"))
rows = session.query(Student).filter(and_(Student.id > 4, Student.last_name.like("Cer%")))
for row in rows:
    print(row)

print('-' * 80)
print("")
rows = session.query(Student).filter(or_(Student.first_name.like('B%'),
                                         Student.last_name.like('B%')))
# session.add(Student(first_name="Gusta", last_name="Benes"))
# session.commit()
for row in rows:  # kdyz po radku 55 pridam dalsiho studenta tak se mi
    # vypise protoze tento radek je az po tomto pridani a pracuje s aktualnimi daty
    print(row)
print('-' * 40)
# session.add(Student(first_name="Helena", last_name="Budinska"))
# session.commit()
for row in rows:  # pokazde bude vystup aktualni i kdyby data pridal nekdo od jinud
    print(row)

print('-' * 80)
print("Vsichni studenti usporadani podle prijmeni")
rows = session.query(Student).order_by(Student.last_name, Student.first_name)
for row in rows:
    print(row)

print('-' * 80)
print("Vsichni studenti usporadani podle prijmeni sestupne")
rows = session.query(Student).order_by(desc(Student.last_name), desc(Student.first_name))
for row in rows:
    print(row)

print('-' * 80)
print("Studenti s id >= 5 usporadani abecedne podle prijmeni")
rows = session.query(Student).filter(Student.id >= 5).order_by(Student.last_name)
for row in rows:
    print(row)

print('-' * 80)
print("offset = 3 (preskocim prvni 3 zaznam)")
rows = session.query(Student).offset(3)
for row in rows:
    print(row)

print('-' * 80)
print("Studenty s id >=5, vynechat prvni 2 radky")
rows = session.query(Student).filter(Student.id >= 5).offset(2)
for row in rows:
    print(row)

print('-' * 80)
print("Prvni 3 studenti prijmeni dle abecedy")
rows = session.query(Student).order_by(Student.last_name).limit(3)
for row in rows:
    print(row)

print('-' * 80)
print("Prvni student")
rows = session.query(Student).limit(1)
for row in rows:
    print(row)

print('-' * 40)
result = session.query(Student).first()
# for row in rows:
#   print(row)
# TypeError: 'Student' object is not iterable
print(result)

print('-' * 80)
print("Student s id == 6")
rows = session.query(Student).filter(Student.id == 6)  # seznam obsahujici jednoho studenta
for row in rows:
    print(row)
print('-' * 40)
# LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of
# SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as
# Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
#   result = session.query(Student).get(6)  # jeden objekt
result = session.query(Student).get(6)  # jeden objekt
print(result)
