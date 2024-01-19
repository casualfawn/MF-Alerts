import pandas as pd
import twilio
import sqlalchemy
from Alerts import Alerts
from Manage_Employees import Employee_Management


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # -- Get phones of Employees opted in
    empdf = pd.read_csv('data/emp.csv', names=['empid', 'name', 'phone', 'email', 'department'])
    emp_manage = Employee_Management(empdf)
    alertlist = emp_manage.alert_phones(empdf)

    # -- Set thresholds
    thresh = {'pH': [7.0, 8], 'DO': [40, 45]}

    # -- Check Alerts to send (compare dataset with thresholds)
    alertsender = Alerts('mp', '123', '423', 'manuf')
    alertstosend = alertsender.check_alert_threshold(thresh, 'data/biordf.csv')

    # ---- Send Alert Messages

    alertsender.set_alert_msg(alertstosend, 2402851931, 12345)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
