import pandas as pd
from sqlalchemy import create_engine
class Employee_Management:

    def __init__(self, userid, pwd, server, port):
        self.userid = userid
        self.pwd = pwd
        self.server = server
        self.port = port


    # Gather Employees Dataframe for Alerts
    def get_alert_employees(self):
       # print(self.server)
       # engine = create_engine(self.server)
       #conn = engine.connect()
       # query = 'SELECT * FROM  CMPNY.PRD.TABLE WHERE CMPNY.PRD.TABLE.DEPARTMENT = "manuf" AND CMPNY.PRD.TABLE.ALERT_TOGGLE = True'
       # emp_alert_df = pd.read_sql_query(query, conn)
        emp_alert_df = pd.read_csv('data/emp.csv')
        return emp_alert_df

    ## Gather Phone Numbers of Employees Signed Up for Alerts
    def get_alert_phonenums(self, employees):
        alerts_active_nums = []
        self.employees = employees
        for i in range(1, len(self.employees)):
            if self.employees['department'][i] == 'manuf' and self.employees['alert_toggle'][i] == True:
                alerts_active_nums.append(self.employees['phone'][i])
        return alerts_active_nums

    ## Set individual employee alert toggle
    def set_emp_alert_toggle(self, employee_id, toggle_status):
        update_toggle_query = '''
        UPDATE COMPANY.PRD.EMP A 
        SET alert_toggle = {0}
        FROM COMPANY.PRD.EMP B
        WHERE B.empid = A.{1}
        '''.format(toggle_status, employee_id)

    ## Get all Active Employees
    def get_active_employees(self):
            emp_list = list()
            #rs = con.execute('SELECT FULL_NAME, ALERTS_TOGGLE FROM COMPANY.PRD.EMP where ACTIVE == True and department == "manuf"')
            empdf = pd.read_csv('data/emp.csv', names=['empid', 'name', 'phone', 'email', 'department', 'alerts_toggle'])
            empdf = empdf[["name", "department", "phone"]]
            for row in empdf.items():
                emp_list.append(row)
            return emp_list


