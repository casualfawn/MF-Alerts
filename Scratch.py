id_query = 'SELECT EMPID from CMPNY.PRD.TABLE'
new_emps_query = 'SELECT * FROM  CMPNY.PRD.HR where CMPNY.PRD.HR.EMPID not in CMPNY.PRD.TABLE.EMPID'

def get_ids(query):
    #id_list = getquery id_query
    #return id_list


def add_new_employee(new_emps_query):
    # new_employees = sqlquery(new_emps_query)
    # sql.insert new_employees


def get_dept_emps(department):
    dept_query = 'SELECT * FROM  CMPNY.PRD.TABLE WHERE CMPNY.PRD.TABLE.DEPARTMENT = {}'.format(department)
    print(dept_query)

get_dept_emps('"manuf"')


class MF_Team_Manager(Employee):
    def __init__(self, first,last,phone,email,alerts_active, employees = None):
        super().__init__(first, last, phone, email, alerts_active)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def send_alerts(self):
        for emp in self.employees:
            print(emp)
    def toggle_alerts(self):
        for emp in self.employees:
            # set_alert_msg(alerttext, alert_metrics, alert_thresh, 240275, 2304921)

            # a = Employee('cally', '1234567891', 'temp@temp.com')
            # b = Employee('ben', '12343241', 'temp2@temp2.com')
            a.printemp()

            employee.printemp()




def get_all_employees(sqlquery):
    all_emp = pd.read_csv('data/emp.csv', names = ['empid', 'name', 'phone', 'email', 'department'])
    return all_emp

def add_new_employee(newemployeedf):
    employees = get_all_employees('emp.csv')
    if list(newemployeedf['empid']) not in list(employees['empid']):
        df = pd.concat([employees, newemployeedf])
    else:
        df = employees
    return df
