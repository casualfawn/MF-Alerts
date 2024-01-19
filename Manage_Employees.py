class Employee_Management:

    def __init__(self, all_emp):
        self.all_emp = all_emp

    def alert_phones(self, employees):
        alerts_active_nums = []
        self.employees = employees
        for i in range(1, len(self.employees)):
            if self.employees['department'][i] == 'manuf':
                alerts_active_nums.append(self.employees['phone'][i])
        return alerts_active_nums
