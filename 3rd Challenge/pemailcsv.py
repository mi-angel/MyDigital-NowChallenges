import csv, smtplib, ssl

# Setting message components

sender="bugsbony007@gmail.com"
# password = input("Type your password and press enter: ")
# My password is saved on the .txt file
with open("BugsBonyMultiPase.txt") as multipase:
    for pas in multipase:
        password = pas

subject = "I have a dream"

# Creating SSL context to connect
mysslcontext = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=mysslcontext) as server:
    server.login(sender, password)
    with open("Book1.csv") as emails: # Working with CSV file
        reader = csv.reader(emails)
        next(emails) # to skip headers row
        for name, email, message in reader:
            mymessage = f"""Subject: {subject}

    Hi {name},

    This is great.
    {message} 

    Best regards.
    
    Get SMTP.Gmail for Pyhton =P"""
            
            # SMTP object (called server) sends emails
            server.sendmail(sender,email,mymessage)

print("********************\n* Successfuly sent *\n********************")










# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------Iterationi through .CSV-------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------


# import csv
# import smtplib
# import time


# with open("Book1.csv") as emails:
#     reader = csv.reader(emails)
#     next(reader) # Skip header row
#     for name, email, message in reader:
#         print(f'Sending email to {name} with the message {message} to the email {email}')




# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------
# -------------------------------To send one email by local host---------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------
# The following code works properly jus to send one email because the next error appears trying to sent more than 1
# ValueError("There may be at most {} {} headers "
# ValueError: There may be at most 1 Subject headers in a message

# import csv
# import smtplib


# from email.message import EmailMessage
# msg = EmailMessage()

# me = 'bugsbony007@gmail.com'

##The next line allows to work in the local host, paste and excecute it directly on CMD
##python -m smtpd -c DebuggingServer -n localhost:1025

# with open('Book1.csv', mode="r") as emails:
#      csv_reader = csv.reader(emails,delimiter=",")
#      row = 0
#      for col in csv_reader:
#         #print(f'\t{col[0]} , {col[1]} , {col[2]}')
#         if row != 0:
#             msg.set_content(f'{col[2]}')
#             you = f'\{col[1]}'

#             msg['Subject'] =f'Friendly Reminder'
#             msg['From'] = me
#             msg['To'] = you
#             s = smtplib.SMTP("localhost",port=1025)
#             s.send_message(msg)
#             s.quit()

#             # print(f'{col[0]}')
#             # print(f'{col[1]}')
#             # print(f'{col[2]}')
#         row += 1
    
# print('emails sent')

# #    print(f'{emails.read()}')

# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------







# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------To Work with CSV FILES--------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------

#import csv

# with open('Book1.csv', mode="r") as emails:
#     csv_reader = csv.reader(emails,delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {",".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} has this email {row[1]} and got this message {row[2]}')
#             line_count += 1
#     print(f'{line_count} lines have been processed')






##THIS IS TO WORK WITH A DICTIONARY "csv.DictReader"
# with open('Book1.csv', mode="r") as emails:
#     csv_reader = csv.DictReader(emails)
#     line_count = 0
#     for row in csv_reader:
        
#         # if line_count == 0:
#         #     print(f'Column names are {",".join(row)}')
#         #     line_count += 1
#         # print(F'this person {row["name"]} has an {row["email"]} with the message {row["message"]}.')
        
#         print(f'{row["name"]} and  {row["email"]}   and   {row["message"]}')

#         print(f'{row["email"]}')
#         line_count += 1
        
#     print(f'Successfully Processed {line_count}')

# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------