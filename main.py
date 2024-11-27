import pandas as pd
import twilio
import sqlalchemy
from Alerts import AlertSys
from EmployeeDBManagemenet import EmployeeDBManager
from TwilioMessageManager import TwilioMessageManager, TwilioMessageSender

if __name__ == '__main__':

    # DB Connection
    db_conn = engine.connect()

    # -- Get phones of Employees opted in
    emp_manage = EmployeeDBManager(db_conn)
    emp_alerts_df = emp_manage.get_alert_employees_table()
    alert_phone_list = emp_manage.get_alert_phonenums(emp_alerts_df)

    # -- Message Manager
    sms_manager = TwilioMessageManager()
    # -- Message Sender
    sms_sender = TwilioMessageSender(sms_manager)
    # -- Check thresholds for current Product SPECs


    # -- Update Alerts Trigger Status with Most Recent Data Capture
    alert_sys = AlertSys()
    alert_sys.set_alert_trigger_states()
    # -- Get Updated Alerts Trigger Status
    alerts_to_send = alert_sys.get_alert_toggle_status()


    # ---- Send Alert Messages
    for key, items in alerts_to_send:
        if items == 'On':
            sms_sender.send_message(f"The Bioreactor {key} is reading {value} and is out of specification as of {Sys.Date()}. Please diagnose the issue or contact your manager.")
            print(f"Alert Messages sent for the current {key} value.")

