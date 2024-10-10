import pandas as pd
from Database_Config import BF_Con

con = BF_Con('user1', 'pass1')

class Employee_Management:

    def __init__(self):
        self.conn =  con

    # Gather Employees Dataframe for Alerts
    def get_alert_team(self):
        query = 'SELECT * FROM  CMPNY.PRD.TABLE WHERE CMPNY.PRD.TABLE.DEPARTMENT = "manuf" AND CMPNY.PRD.TABLE.ALERT_TOGGLE = True'
        emp_alert_df = pd.read_sql_query(query, conn)
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
            emp = con.execute('SELECT FULL_NAME, ALERTS_TOGGLE FROM COMPANY.PRD.EMP where ACTIVE == True and department == "manuf"')
            emp_alert_df = pd.read_sql_query(query, conn)
            return emp_alert_df


a = Employee_Management
a.