import pandas as pd
import twilio
import sqlalchemy
from Alerts import Alerts
from Manage_Employees import Employee_Management


if __name__ == '__main__':

    # -- Get phones of Employees opted in
    emp_manage = Employee_Management('mpo', 'temp', 'company.server', 3052)
    empdf = emp_manage.get_alert_employees()
    alertlist = emp_manage.get_alert_phonenums(empdf)

    # -- Set thresholds for current Product SPECs
    thresh = {'pH': [7.0, 8], 'DO': [40, 45]}

    # -- Check Alerts to send (compare current trends with thresholds)
    alertsender = Alerts('mp', '123', '423', 'manuf')
    alertstosend = alertsender.check_alert_threshold(thresh)

    # ---- Send Alert Messages
    alertsender.set_alert_msg(alertstosend, 2402851931, 12345)

