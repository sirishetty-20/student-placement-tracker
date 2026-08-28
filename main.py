class StudentProfile:
    platform = "KodNest"
    total_students = 0

    # Constructor
    def __init__(self, student_id, name, branch, score):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.__score = score

        StudentProfile.total_students += 1

    # Property - Getter
    @property
    def score(self):
        return self.__score

    # Property - Setter
    @score.setter
    def score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
        else:
            print("Invalid score. Score must be between 0 and 100.")

    # Static method - Validate score
    @staticmethod
    def is_valid_score(score):
        if 0 <= score <= 100:
            return True
        else:
            return False

    # Static method - Normalize name
    @staticmethod
    def normalize_name(name):
        return name.strip().title()

    # Instance method - Placement status
    def get_placement_status(self):
        if 80 <= self.__score <= 100:
            return "Placement Ready"
        elif 60 <= self.__score <= 79:
            return "Needs More Practice"
        else:
            return "Not Ready"

    # Instance method - Display profile
    def display_profile(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Mock Score: {self.__score}")
        print(f"Placement Status: {self.get_placement_status()}")
        print(f"Platform: {StudentProfile.platform}")
        print()

    # Alternative constructor
    @classmethod
    def from_string(cls, data):
        student_id, name, branch, score = data.split(",")

        name = cls.normalize_name(name)
        score = int(score)

        return cls(student_id, name, branch, score)

    # Class method - Change platform
    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform

    # Class method - Show total students
    @classmethod
    def show_total_students(cls):
        print(f"Total Students: {cls.total_students}")


# Main program

students = []

while True:

    print("===== Student Placement Tracker =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Score")
    print("4. Change Platform")
    print("5. Show Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Option 1 - Add Student
    if choice == "1":

        student_data = input("Enter student details: ")

        student_id = student_data.split(",")[0]

        duplicate = False

        for student in students:
            if student.student_id == student_id:
                duplicate = True
                break

        if duplicate:
            print("Student ID already exists.")
        else:
            student = StudentProfile.from_string(student_data)
            students.append(student)
            print("Student added successfully.")

    # Option 2 - Display All Students
    elif choice == "2":

        if not students:
            print("No students found.")
        else:
            for student in students:
                student.display_profile()

    # Option 3 - Update Student Score
    elif choice == "3":

        student_id = input("Enter Student ID: ")
        new_score = int(input("Enter New Score: "))

        found = False

        for student in students:

            if student.student_id == student_id:

                found = True

                if StudentProfile.is_valid_score(new_score):
                    student.score = new_score

                    print("Score updated successfully.")
                    print(f"Updated Score: {student.score}")
                    print(f"Updated Status: {student.get_placement_status()}")

                else:
                    print("Invalid score. Score must be between 0 and 100.")

                break

        if not found:
            print("Student not found.")

    # Option 4 - Change Platform
    elif choice == "4":

        new_platform = input("Enter the new platform name: ")

        StudentProfile.change_platform(new_platform)

        print("Platform changed successfully.")

    # Option 5 - Show Total Students
    elif choice == "5":

        StudentProfile.show_total_students()

    # Option 6 - Exit
    elif choice == "6":

        print("Thank you for using the Student Placement Tracker.")
        break

    # Invalid choice
    else:

        print("Invalid choice. Please select an option from 1 to 6.")