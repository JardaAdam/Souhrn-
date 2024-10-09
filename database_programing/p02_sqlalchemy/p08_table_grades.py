"""Create a table called grades
● It should include the following fields:
○ id int, primary key, autoincrement
○ student int, foreign key
○ grade int or string - whichever you prefer
○ date_created datetime
● Add some grades for each student
● Print out all grades per each student using filter"""
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from connect_db import session, db
from models_students import *

Base.metadata.create_all(db)

try:
    session.add_all(
        [
            Grade(student=1, grade=2, date_created=datetime(2024, 10, 21, 14, 20, 21)),
            Grade(student=2, grade=3, date_created=datetime(2024, 5, 21, 13, 20, 21)),
            Grade(student=3, grade=4, date_created=datetime(2024, 4, 21, 14, 20, 21)),
            Grade(student=4, grade=1, date_created=datetime(2024, 7, 21, 14, 20, 21)),
            Grade(student=5, grade=3, date_created=datetime(2024, 8, 21, 14, 20, 21)),
            Grade(student=6, grade=2, date_created=datetime(2024, 3, 21, 14, 20, 21)),
            Grade(student=8, grade=4, date_created=datetime(2024, 2, 21, 14, 20, 21)),
            Grade(student=7, grade=2, date_created=datetime(2024, 9, 21, 14, 20, 21)),
            Grade(student=3, grade=5, date_created=datetime(2024, 7, 21, 14, 20, 21)),
            Grade(student=4, grade=1, date_created=datetime(2024, 4, 21, 14, 20, 21)),
            Grade(student=5, grade=2, date_created=datetime(2024, 1, 21, 14, 20, 21))

        ]
    )

    session.commit()

except IntegrityError as e:
    session.rollback()
    print(f"ERROR: {e}")
