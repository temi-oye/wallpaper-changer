# wallpaper-changer
A script that change your desktop wallpaper to a random one that's inside the specified path. The VBS file can be used in conjunction with windows task scheduler to excute the file 
at a specified time/event. 

For example if you wanted the Script to excute every day at 12:00 you would do as follows:

### Open Windows Task Scheduler 
<hr>
Search for "Task Scheduler" in the windows search bar.

### Click "Create Task"
<hr>
It should be in a column on the right-hand side of the page.

### Creating the task
<hr>

##### General
Add a name eg wallpaper change.
##### Triggers
Go to triggers and make sure it begins a task "On a schedule". 
Hit daily (left-hand side).
Start the task at whatever time and date you want and set it to recur every X days. Once you're happy click OK
##### Actions
Click new and set the action to "Start a program"
Under the Program/script section add this to the text box: ```wscript.exe```
In the "Add arguements" text box put in the path to your VBS file.
In the "Start in" text box add this: ```C:\Windows\System32``` and then hit OK

With that done your script should be up and running. Enjoy!
