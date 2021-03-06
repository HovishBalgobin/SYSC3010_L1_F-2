import smtplib, ssl

def email_alert(reason_str, r_email):

    server = smtplib.SMTP_SSL("smtp.gmail.com", port = 465)
    server.login("babymonitor3010@gmail.com","termproject")

    recipient = r_email
    msg = "From: babymonitor3010@gmail.com\nTo:" + recipient +"\nSubject: Smart Crib Alert"
    msg = msg + "\n\nThe baby monitering system has read data out of set bounds. \n"
    msg = msg + "This notification was caused by:\n\n" + reason_str
    msg = msg + "\n\nPlease check on the baby. \n"

    try:
        server.sendmail('babymonitor3010@gmail.com',recipient,msg)
    except:
        return server

    server.quit
