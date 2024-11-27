import pandas as pd
from sqlalchemy import create_engine
class EmployeeDBManager:

    def __init__(self, conn):
        self.conn = conn

    # Gather Employees Dataframe for Alerts
    def get_alert_employees_table(self):
        # print(self.server)
        conn = self.conn
        query = 'SELECT * FROM  CMPNY.PRD.TABLE WHERE CMPNY.PRD.TABLE.ALERT_SUBSCRIPTIONS = True'
        emp_alert_df = pd.read_sql_query(query, conn)
        return emp_alert_df

    ## Gather Phone Numbers of Employees Signed Up for Alerts
    def get_alert_phonenums(self, alert_employees):
        alerts_active_nums = []
        self.alert_employees = alert_employees
        for i in range(1, len(self.alert_employees)):
            if self.alert_employees['alert_toggle'][i] == True:
                alerts_active_nums.append(self.alert_employees['phone'][i])
        return alerts_active_nums

    ## Set individual employee alert toggle
    @classmethod
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


