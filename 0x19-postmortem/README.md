Issue Summary 
Our wordpress website was returning a 500 Internal Server Error. This started on May 7th , 6:00 AM EAT and ended on May on May 7th , 6:00 AM EAT. This caused our website to be down. This was due to a configuration error.
Timeline 
The issue was detected on on May 7th , 6:00 AM EAT
An ALX SE student noticed the site was down
The system server was investigated from the error message given
The incident was escalated to peers
The incident was resolved by debugging the server using strace

Root cause and resolution
The issue was cause by a typo in /var/www/html/wp-settings.php with a filename ending with phpp instead of php
This was fixed by correcting the typo by running the command: sed -i s/phpp/php/g /var/www/html/wp-settings.php
Corrective and preventative measures must contain:


This issues can be fixed by automating certain tasks, automating tasks like configuring servers can make them less prone to errors than doing it manually. Always monitor your system to ensure everything is working well.

