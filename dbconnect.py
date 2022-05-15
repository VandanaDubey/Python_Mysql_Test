import mysql.connector as connector


class DBConnect:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='',
                                     database='pythontest')
        query = """create table if not exists employee
                    (empId integer primary key,
                    empName varchar(15) not null,
                    empSalary integer,
                    empDept varchar(15))
                    """
        cur = self.con.cursor()
        cur.execute(query)
        print("Table succesfully created")

    # inserting records
    def insert_emp(self, empid, ename, esal, edept):
        q = """insert into employee(empId,empName,empSalary,empDept)
                values ({},'{}',{},'{}')""".format(empid, ename, esal, edept)

        cur = self.con.cursor()
        cur.execute(q)
        self.con.commit()
        print("Record inserted successfully")

    def fetch_data(self):
        q = "Select * from employee"
        cur = self.con.cursor()
        cur.execute(q)
        for row in cur:
            print("ID: ", row[0])
            print("Name: ", row[1])
            print("Salary: ", row[2])
            print("Department: ", row[3])
            print()

    def delete_data(self, empid):
        q = "delete from employee where empId = {}".format(empid)
        cur = self.con.cursor()
        cur.execute(q)
        self.con.commit()
        print("Record deleted successfully")

    def update_data(self, empid, newname, newsal):
        q = "update employee set empName = '{}', empSalary = {} where empId = {}".format(
            newname, newsal, empid)
        cur = self.con.cursor()
        cur.execute(q)
        self.con.commit()
        print("Record updated successfully")


# db = DBConnect()
# db.insert_emp(2, 'shivay', 40000, 'Gaming')
# db.insert_emp(3, 'arun', 60000, 'Testing')
# db.insert_emp(4, 'geeta', 25000, 'Admin')
# db.delete_data(4)
# db.update_data(2, 'shiv', 65000)
# db.fetch_data()
