
from dbconnect import DBConnect


def main():
    db = DBConnect()
    while True:
        print("PRESS 1 TO INSERT RECORD IN EMPLOYEE TABLE")
        print("PRESS 2 TO VIEW RECORD FROM EMPLOYEE TABLE")
        print("PRESS 3 TO DELETE RECORD FROM EMPLOYEE TABLE")
        print("PRESS 4 TO UPDATE RECORD IN EMPLOYEE TABLE")
        print("PRESS 5 TO EXIT THE PROGRAM")
        print()
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                eid = int(input("Enter empid: "))
                ename = input("Enter emp_name: ")
                esal = int(input("Enter emp_salary: "))
                edept = input("Enter emp_dept: ")
                db.insert_emp(eid, ename, esal, edept)

            elif choice == 2:
                db.fetch_data()

            elif choice == 3:
                eid = int(input("Enter empid which you want to delete: "))
                db.delete_data(eid)

            elif choice == 4:
                eid = int(input("Enter empid: "))
                ename = input("Enter emp_name: ")
                esal = int(input("Enter emp_salary: "))
                db.update_data(eid, ename, esal)

            elif choice == 5:
                break

            else:
                print("Invalid choice!!! Please try again")

        except Exception as e:
            print(e)
            print("Invalid entry!!!  Try again")


if __name__ == "__main__":
    main()
