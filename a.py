import smtplib


username = "heritagedev63@gmail.com"
password = "ouyp wqlm zxpn pyyy"


def send_mail(Subject = "Hello World", Body= "Welcome", from_email = " Heritage <heritagedev63@gmail.com>", to_email = None):
    if to_email is None:
        raise ValueError("Enter Recipient email")

    
    msg = (f"Subject: {Subject}\n\n From: {from_email}\n To: {to_email}\n {Body}\n Are you happy to be with us ")
    server = smtplib.SMTP(host='smtp.gmail.com', port= 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg)
    server.quit
    print("Successful")

print(send_mail(to_email="ademokunwadaniel@gmail.com"))