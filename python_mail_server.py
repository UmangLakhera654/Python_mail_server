import smtplib

sender_email = input("Enter the sender's email: ")
password = input("Enter the app generated email password: ")
receiver_email = input("Enter the receiver's email address: ")
message = input("Enter the message: ")

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email, password)
s.sendmail(sender_email, receiver_email, message)
s.quit()

print("Email sent successfully!")


