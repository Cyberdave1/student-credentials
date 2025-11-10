import psycopg2
DB_NAME ="Studentdatabase"
DB_USER = "postgres"
DB_PASSWORD = "1.Tycoone"
DB_HOST = "localhost"
DB_PORT = "5432"

connectit = psycopg2.connect(
	dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD, host = DB_HOST, port = DB_PORT
)
new = connectit.cursor()

def getAllStudents():
	new.execute("SELECT * FROM students by student_id: ")
	for x in new.fetchall():
		print(x)

def addStudent(first_name, last_name, email, enrollment_date):
	new.execute(
		"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
		(first_name, last_name,email, enrollment_date)
	)
	student_id = new.fetchone()[0]
	connectit.commit()
	print(f"New student added with student id : {student_id}")

def updateStudentEmail(student_id, freshmail):
	new.execute(
		"UPDATE students SET email=%s WHERE student_id=%s",(freshmail,student_id)
	)
	connectit.commit()
	print(f"Email for {student_id} has been changed to {freshmail}")

def deleteStudent(student_id):
	new.execute(
		"DELETE FROM students WHERE student_id=%s",(student_id)
	)
	connectit.commit()
	print(f"Student with student id: {student_id} has been deleted")


new.close()
connectit.close()