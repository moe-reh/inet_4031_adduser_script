# inet_4031_adduser_script

## Program Description
This program automates the manual process of creating users & group assignments. Rather than the manuel process of using the "adduser" command, for setting passwords and user info per each user, this script allows you to generate multiple users simutaneouly. The process is streamlined by inputing a file with the list of all users (with respective user passwords & info) upon exection of the program. The program reads each line from the input file to process the user details which then the program then constructs the appropriate commands to create the user, set password, and assign to groups. By automating these steps the program saves time and ensures consistency for managing multiple users. 
## Program User Operation
The program works by reading the input file line by line ensuring that each entry (checks all fields) is valid. After the data processing, each field in the entry gets assigned to the proper command that'll create the user, set password and assign to group(s). The user must provide a input file that is formatted properly so the program can read & process the data automatically without user interference.  
### Input File Format
Each line in the input file represents one user and it must contain five entries or fields which are seperated by colons. 
Each entry must contain the following fields (in order):
1. Username<br>
    a. Placing a '#' in the front will skip the creation of that user.
3. Password
4. First Name
5. Last Name
6. Group(s)<br>
    a. Use a comma to separate if user belongs in more than one group.<br>
    b. Use a '-' if user does not have a group.
### Command Execution
User may need to set the Python file to be executable by using: chmod +x create-user.py
Execute the file by using: ./create-users.py < createusers.input
Or alternatively: sudo python3 create-users.py < create-users.input 
### "Dry Run"
If the user decides to do a Dry Run, the program will run as normal but no changes will be made to the system meaning that no users will be generated. In a dry run the commands used to create the user will be printed. User can do a dry run by commenting out all lines saying "os.system(cmd)".
