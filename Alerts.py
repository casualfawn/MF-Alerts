import pandas as pd
class Alerts:
    
    def __init__(self, usr, pwd, server, mf_emps):
        self.usr = usr
        self.pwd = pwd
        self.server = server
        self.mf_emps = mf_emps


    def query_current_trends(self):
        current_trends = pd.read_csv('data/biordf.csv', names=["pH", "DO", "Temperature", "RPM", "Timestamp"])
        return current_trends

    ## Check if current trends are above/below threshold
    def check_alert_threshold(self, thresholds):
        thresholds = thresholds
        current_trends = self.query_current_trends()
        alert_trends = []
        for measures,values in current_trends.items():
            if measures and measures in thresholds:
                if float(values[1]) < thresholds[measures][0]:
                    alert_trends.append([measures, 'below'])
                if float(values[1]) > thresholds[measures][1]:
                    alert_trends.append([measures, 'above'])
        return alert_trends

    ## Create body of alert message
    def set_alert_msg(self, alertstosend, phone_from, phone_to):
        self.alerttext = 'The {0} is {1} threshold you need to check it'
        msglist = list()
        for i in range(len(alertstosend)):
            print(self.alerttext.format(alertstosend[i][0], alertstosend[i][1]))
        return print('Alert Message Sent')