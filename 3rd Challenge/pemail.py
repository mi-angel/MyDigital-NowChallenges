import csv, datetime, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class People:
    
    def __init__(self) -> None:
        pass

    def __init__(self, name, email, message, birthday):
        self.name = name
        self.email = email
        self.message = message
        self.birthday = birthday

class Html_Tmplt:
    def happy_birthday(name):
        return f"""
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>

    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
</head>

<body>
    <div class="es-wrapper-color">
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        

                        <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p25t es-p25b es-p40r es-p40l es-m-p20r es-m-p20l" align="center">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="520" align="left" class="esd-container-frame">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="border-radius: 25px; border-collapse: separate; background-color: #e0ecfe;" bgcolor="#e0ecfe">
                                                                            <tbody> 
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-m-txt-c es-p10t es-p20b es-p25r es-p25l">
                                                                                    <!-- <td align="center" class="esd-block-image es-p20t" style="font-size: 0px;"> -->
                                                                                        <i><h2 style="color:#e40c0c"> {name}: We whish you </h2></i>
                                                                                        <!-- <a target="_blank" href="https://viewstripo.email">
                                                                                            <img src="https://tlr.stripocdn.email/content/guids/CABINET_c9caacaf71bd41e65369951f9007184063f0b585518ef1531165f4ac2deaa9a1/images/untitled1.png" alt style="display: block;" width="60">
                                                                                        </a> -->
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-image es-p20t">
                                                                                        <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0">
                                                                                            <tbody align="center">
                                                                                                <tr align="center">
                                                                                                    <img src="https://gifocard.com/en/b/10/g/happy-birthday.gif"  align="center" class="esd-block-image es-p20t" alt style="display:block; border-radius:10%; border-collapse:separate;" width="300"/>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center"><p style="background: #e0ecfe; border-color: #e0ecfe; padding: 0px 20px; color: #9f1717; border-radius:40%; font-weight:normal">Click on the boxes below to see your gifts</p></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>


                        <table cellpadding="0" cellspacing="0" class="esd-header-popover es-header" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table bgcolor="#ffffff" class="es-header-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p10b es-p20r es-p20l" align="left">
                                                        
                                                        <table cellpadding="0" cellspacing="0" align="left" class="es-left">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="100" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-image es-m-txt-c" style="font-size: 0px;">
                                                                                        <a target="_blank" href="https://pyecon.org/lecture/"><img src="https://cliply.co/wp-content/uploads/2019/09/371907580_SPECIAL_GIFT_400px.gif" alt="Python" style="display: block;" title="Econometrics with Python" height="100"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td width="100" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-image es-m-txt-c" style="font-size: 0px;">
                                                                                        <a target="_blank" href="https://www.econometrics-with-r.org/"><img src="https://cliply.co/wp-content/uploads/2019/09/371907580_SPECIAL_GIFT_400px.gif" alt="R" style="display: block;" title="Econometrics with R" height="100"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td width="100" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-image es-m-txt-c" style="font-size: 0px;">
                                                                                        <a target="_blank" href="https://docs.python.org/3.9/tutorial/"><img src="https://cliply.co/wp-content/uploads/2019/09/371907580_SPECIAL_GIFT_400px.gif" alt="Python Tutorial" style="display: block;" title="Python Tutorial" height="100"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td width="100" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-image es-m-txt-c" style="font-size: 0px;">
                                                                                        <a target="_blank" href="https://www.ldoceonline.com/exercise/" ><img src="https://cliply.co/wp-content/uploads/2019/09/371907580_SPECIAL_GIFT_400px.gif" alt="Logo" style="display: block;" title="Longman English" height="100"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td width="100" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-image es-m-txt-c" style="font-size: 0px;">
                                                                                        <a target="_blank" href="https://forvo.com/"><img src="https://cliply.co/wp-content/uploads/2019/09/371907580_SPECIAL_GIFT_400px.gif" alt="Forvo (Many Languages)" style="display: block;" title="Forvo (Many Languages)" height="100"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td width="100" align="left" class="esd-container-frame es-m-p20b">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-image es-m-txt-c" style="font-size: 0px;">
                                                                                        <a target="_blank" href="https://librivox.org/"><img src="https://cliply.co/wp-content/uploads/2019/09/371907580_SPECIAL_GIFT_400px.gif" alt="LibriVox (Free Audiobooks)" style="display: block;" title="LibriVox (Free Audiobooks)" height="100"></a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td style="border-bottom: 1px solid #8d99ae; background: unset; height: 1px; width: 100%; margin: 0px;" class="esd-structure es-p20r es-p20l" align="left">
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20r es-p20l" align="left">
                                                        <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="326" valign="top"><![endif]-->
                                                        <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="600" class="es-m-p20b esd-container-frame" align="left">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-menu" esd-tmp-menu-padding="8|6" esd-tmp-menu-font-size="12px" esd-tmp-menu-font-weight="normal">
                                                                                        <table cellpadding="0" cellspacing="0" width="100%" height="18px" class="es-menu">
                                                                                            <tbody>
                                                                                                <!-- I change my mind and let the links inside the boxes  <tr class="links">
                                                                                                    <td align="center" valign="top" width="17%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-top: 8px; padding-bottom: 6px;"><a target="_blank" href="https://pyecon.org/lecture/" style="font-size: 12px; font-weight: normal;">Python</a></td>
                                                                                                    <td align="center" valign="top" width="15%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-top: 8px; padding-bottom: 6px;"><a target="_blank" href="https://www.econometrics-with-r.org/" style="font-size: 12px; font-weight: normal;"> R </a></td>
                                                                                                    <td align="center" valign="top" width="18%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-top: 8px; padding-bottom: 6px;"><a target="_blank" href="https://docs.python.org/3.9/tutorial/" style="font-size: 12px; font-weight: normal;"> Python tutorial </a></td>
                                                                                                    <td align="center" valign="top" width="17%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-top: 8px; padding-bottom: 6px;"><a target="_blank" href="https://www.ldoceonline.com/exercise/"  style="font-size: 12px; font-weight: normal;">Longman</a></td>
                                                                                                    <td align="center" valign="top" width="16%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-top: 8px; padding-bottom: 6px;"><a target="_blank" href="https://forvo.com/" style="font-size: 12px; font-weight: normal;"> Forvo </a></td>
                                                                                                    <td align="center" valign="top" width="17%" class="es-p10t es-p10b es-p5r es-p5l" style="padding-top: 8px; padding-bottom: 6px;"><a target="_blank" href="https://librivox.org/" style="font-size: 12px; font-weight: normal;"> LibriVox </a></td>
                                                                                                </tr> -->
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>


        <table cellpadding="0" cellspacing="0" class="es-footer esd-footer-popover" align="center">
            <tbody>
                <tr>
                    <td class="esd-stripe" align="center" esd-custom-block-id="882773">
                        <table class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600" bgcolor="rgba(0, 0, 0, 0)">
                            <tbody>
                                <tr>
                                    <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left" esd-custom-block-id="682351">
                                        <table cellpadding="0" cellspacing="0" width="100%">
                                            <tbody>
                                                <tr>
                                                    <td width="560" class="esd-container-frame" align="left">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr></tr>
                                                                <tr></tr>
                                                                <tr>
                                                                    <td align="center" class="esd-block-text es-p10t es-p10b" esd-links-color="#ffffff" esd-links-underline="none">
                                                                        <p style="color:ghostwhite; font-size:25px"  ><b>All the best for you.</b></p>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>

        """
        


# Main process

msg = MIMEMultipart('alternative')

with open('Book1.csv') as emails:
    reader = csv.reader(emails)
    next(emails)
    
    
    pID=[] 
    for name, email, message, birthday in reader:
        pID.append(People(name, email, message, birthday))
        

for i  in pID:
    month, day, year = i.birthday.split("/")

    if datetime.datetime.strftime(datetime.datetime.now(),"%d") == day and str(int(datetime.datetime.strftime(datetime.datetime.now(),"%m"))) == month:
        print(f'Happy birthday {i.name} {i.birthday}')

        # Setting message components
        
        # Sender
        sender="bugsbony007@gmail.com"
        msg['From']= sender

        # Subject
        subject = "Happy Birthday"
        msg['Subject']= subject

        # Recipient
        msg['To'] = i.email

        # Message
        myMessage = Html_Tmplt.happy_birthday(i.name)

        msg.attach(MIMEText(myMessage,'html'))
                   
        # Password (it is saved on the .txt file)
        with open("BugsBonyMultiPase.txt") as multipase:
            for pas in multipase:
                password = pas

        # Creating SSL context to connect
        mysslcontext = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=mysslcontext) as cli:
            cli.login(sender, password)
            print('Successfuly connected and logged in')
            
            # Setting HTML message

            # SMTP object (called cli) sends emails
            cli.sendmail(sender,i.email,msg.as_string())
            cli.quit()

print("********************\n* Successfuly sent *\n********************")
# print(Html_Tmplt.happy_birthday("Julia"))