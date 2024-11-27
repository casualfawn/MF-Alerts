
<a id="readme-top"></a>



<!-- PROJECT SHIELDS -->


[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">


<h3 align="center">Alert and Monitoring System</h3>

  <p align="center">
    Monitoring system for tracking streaming trends of process measurements and sending SMS Alerts.
    <br />
    <a href="https://github.com/casualfawn/MF-Alerts"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  
</div>







<!-- ABOUT THE PROJECT -->
## About The Project

<p align="right">(<a href="#readme-top">back to top</a>)</p>
 The Alert and Monitoring system is a pythonic approach to developing a program that will periodically check a processes' measurements and determine whether the current values are above or below a set threshold range. Upon setting the monitoring schedule and toggling alert statuses for defined measures, this program will send alert SMS messages to those subscribed for alerts when process parameters are out of spec. This program has been tailored to fit a manufacturing processes and a machine learning algorithm (CNN, Tensorflow). In this specific use-case, model predictions of parameter values are continuously stored in a data table. This alert program queries for the most recent values based on a user-defined schedule and checks if the predictions are above or below predefined thresholds. If above or below the set points, SMS messages are sent to team members who are sigend up for alerts with warnings of the current trends so adjustments can be made as-needed.  



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Set up your database connection to a table that stores process data.
Set your Twilio authentication token and Twilio phone number.
Set employee/team member message toggles for those who are subscribed.
set measures to be monitored and thresholds that will trigger an alert message.
Schedule the frequency at which the program checks current trneds.

### Prerequisites


* Twilio Acct Token / Auth in main.py:
  ```sh
		db_conn = engine.connect()
  ```
  
 
* Twilio Set Account Phone Number
  ```sh
  TwilioMessageManager().set_twilio_phone(9991234567)
  ```

### main.py

1. Update Metric Alerts Trigger States 
   ```sh
     alert_sys.set_alert_trigger_states()
   ```
2. Get the SMS Alerts Toggle Status
   ```sh
    alerts_to_send = alert_sys.get_alert_toggle_status()
   ```
3. Get phone numbers of users opted in for alerts
   ```
    emp_manage = EmployeeDBManager(db_conn)
    emp_alerts_df = emp_manage.get_alert_employees_table()
    alert_phone_list = emp_manage.get_alert_phonenums(emp_alerts_df)
   ```
4. Send sms to subscribed users for toggled alerts
   ```js
    for key, items in alerts_to_send:
        if items == 'On':
            sms_sender.send_message(f"Alerts for the {key} measure is {items} and this trend is out of specification as of {Sys.Date()}. Please diagnose the issue or contact your manager.")
            print(f"Alert Messages sent for the current {key} value.", alert_phone_list)
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] EmployeeDBManagement
- [ ] Alerts
- [ ] TwilioMessageManager


See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make projects even better. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/casualfawn/MF-Alerts/">
  <img src="https://contrib.rocks/image?repo=casualfawn/MF-Alerts" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact



Project Link: [https://github.com/casualfawn/MF-Alerts](https://github.com/casualfawn/MF-Alerts)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mark-oelkuct-b4371723a/?
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
