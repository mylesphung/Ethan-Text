# Ethan Text
 Program I made for my friend to help him with his landscaping business. ethantext.py takes inputs from another script, scheduleReader (read Note), and formats them into a premade text message. It then emails the message to an SMS gateway, which forwards the email as a text message to the provided number.

 **Note:**
  This is only the script for actually sending the emails. The other script, scheduleReader, is not attached because it contains his email and password. It also has a set path to read his schedule, which I also can't attach, because it has people's names and numbers. Without a copy of the schedule, the scheduleReader program wouldn't make a lot of sense, so I just didn't include it. The names, numbers, dates, his email, and his password are all imported from that script.

Modules needed:
- emails
- smtplib
- ssl
- scheduleReader script
