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

#This function is used to retrieve and display all records from the students
def getAllStudents():
	new.execute("SELECT * FROM students ORDER BY student_id; ")
	x = new.fetchall()
	for x in x:
		print(x)

#this function inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
	new.execute(
		"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
		(first_name, last_name,email, enrollment_date)
	)
	connectit.commit()
	print(f"Student {first_name} {last_name} was just added")

#This function is used to update the emails of a student with a specified student id
def updateStudentEmail(student_id, freshmail):
	new.execute(
		"UPDATE students SET email=%s WHERE student_id=%s",
		(freshmail,student_id)
	)
	connectit.commit()
	print(f"Email for {student_id} has been changed to {freshmail}")

#This function is used to delete the record of the student with the specified student_id
def deleteStudent(student_id):
	new.execute(
		"DELETE FROM students WHERE student_id=%s",(student_id,)
	)
	connectit.commit()
	print(f"Student with student id: {student_id} has been deleted")


#getAllStudents()
#To test the add student function
#addStudent("Peter", "h", "Peterh@gmail.com", "2022-02-14")
#addStudent("Kelvin", "Curry", "kelvincurry5@gmail.com", "2024-09-10" )
#getAllStudents()

#To test the update student function
#updateStudentEmail(12,"jackbrown@gmail.com")
#updateStudentEmail(6,"jaydensixers6@gmail.com")
#getAllStudents()

#To test the delete student function
deleteStudent(12)
#deleteStudent(6)
getAllStudents()

new.close()
connectit.close()