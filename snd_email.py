import smtplib


class SndEmail:
    def __init__(self, email):
        self.user_email = email

    def send_email(self):
        MY_EMAIL = "qfazah@gmail.com"
        MY_PASSWORD = "xennnacwogzwdbhy"  # ❗ removed extra space

        if not self.user_email:
            print("No email provided")
            return

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=self.user_email,
                msg="Subject: Expense Tracker\n\nyou are doing too much kharcha!"
            )

        print("Email sent successfully")