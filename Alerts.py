#import pandas as pd
class AlertSys:

    def __init__(self):
        self.active_status = 'On'  # alert_trigger_states  dictionary
        self.metric_alert_trigger_states = {'Measure1': 'On', 'Measure2': 'On', 'Measure3': 'On', 'Measure4': 'On',
                                            'Measure5': 'On'}
        self.metric_thresholds = {'Measure1': [30, 50], 'Measure2': [7.5, 7.15], 'Measure3': [20, 30],
                                  'Measure4': [.03, .1], 'Measure5': [60, 70]}  # alert_trigger thresholds

    def get_alert_toggle_status(self): #returns toggle status of measures being monitored
        print('Current Monitored Measures and Alert Toggle Status:')
        print(self.metric_alert_trigger_states)
        return self.metric_alert_trigger_states

    def get_threshold_ranges(self): #returns threshold ranges for monitoring
        print('Current Monitored Measures and Threshold Ranges:')
        print(self.metric_thresholds)

    def get_alerts_to_send(self, alertstosend):

        for i in range(len(alertstosend)):
            print(self.alerttext.format(alertstosend[i][0], alertstosend[i][1]))


    @classmethod
    def add_new_metric_monitoring(cls, metric_name, threshold_low, threshold_high):
        #AlertSys.metric_categories += metric_name

        AlertSys().metric_thresholds[metric_name] = [threshold_low, threshold_high]

    @ classmethod
    def set_alert_trigger_states(self, most_recent_captured_output):
        for key, item in zip(AlertSys.metric_thresholds, most_recent_captured_output):
            if most_recent_captured_output < item:
                AlertSys.alert_trigger_states[key] = 'On'
            elif most_recent_captured_output > item:
                AlertSys.alert_trigger_states[key] = 'On'
            else:
                AlertSys.alert_trigger_states[key] = 'Off'

