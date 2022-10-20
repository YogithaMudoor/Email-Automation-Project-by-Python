
    
   You need to create a email reminder program for the students of a course series which sends reminder email to the students just before the class day. But if the class happens on Monday, the reminder should go on Friday. (the class will happen only on weekdays)
      The schedule of the class is given in schedule.txt in the below format 

2021 8 Nov 10:00 AM - Class 1 Mod 1

2021 11 Nov 11:00 AM - Class 1 Mod 2

2021 15 Nov 9:00 PM - Class 2 Mod 1

2021 17 Nov 11:00 AM - Class 2 Mod 2

Important Notes:

Please create a reminder_mail.py file which executes the above email reminder program.

The email reminder program reminder_mail.py should be run everyday at 12:00 PM by automatic scheduling so that the student gets the mail one day before the class on 12:00 PM. For eg. if the class is on Friday, the student should get the mail on Thursday 12:00 PM.

The emails should be sent from your email id to the students email id.

The email's subject and body should be written in the below manner
Subject - OneLearn course series reminder

body - This is a reminder mail for your class on <Topic name of the day taken from schedule.txt> at <given date and time from schedule.txt>. Please join the class on time.

For eg. for the class on 8 nov 2021, the mail will go out on 12:00PM on 5 Nov (as 8 nov is monday). The mail's subject and body will be
Subject - OneLearn course series reminder

Body - This is a reminder mail for your class on Class 1 Mod 1 at 2021 8 Nov 10:00 AM. Please join the class on time.

Once you are finished with the script, you need to put the script for automatic scheduling for 8 days. The script will be sending mails to the student according to the above schedule.txt file requirement.(we will monitor if we are getting the appropriate mails or not). Remember that when there is no class the next day, don't send any email. (Specifically if the class is on Monday, don't send any reminder mail on Sunday for it, it should be sent on prior Friday)

Additional Notes:

Automatic scheduling of email can be done using the 'Task Scheduler' Program in windows. After 8 days you may need to delete the daily automatic schedule of email reminder program.

Automatic scheduling will be running from your computer so remember that you may need to open your computer around 12:00 PM everyday when your program is running. You need to have the reminder_mail.py on your computer in order to run this script everyday from your computer.

You can use this tutorial to learn how to send emails and run automatic scheduling program - https://onelearn.notion.site/Email-Reminder-Program-Tutorials-8b9e612a7a7046588c4c2e26661a7a94

You need to work with smptlib library in order to send emails and login to your email id using the script file. When you are logging in you will need to provide your email id and password to the program. Please provide these two parameters as command line arguments to the script, don't put them in the script file reminder_mail.py as it might lead to privacy voilation of your details.

Important Note:Here file is created in Visual Studio.You can use colab for file creation.
You can use sys.arg for username and password.

Here two files are present one is extract.py and another one is reminder.py
extract file is used to extract schedule from schedule.txt file 
reminder file imports extract file from extract module
