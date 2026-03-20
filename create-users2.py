#!/usr/bin/python3

# INET4031
# Moe Reh
# Date Created: 3-20-2026
# Date Last Modified: 3-20-2026

# os is used to run system commands
# re is used to check for patterns in text
# sys is used to read input from the file 
import os
import re
import sys

def main():
    # Asks user if they want to run in dry run mode.
    choice = input("Would you like to run in dry run mode? Y/N: ").strip().lower()
    
    # dry_run will be True if user enters 'y'.
    dry_run = (choice == 'y')

    # Lets user know what mode they are in.
    if dry_run:
        print("\n*** Running in DRY-RUN mode (no changes will be made) ***\n")
    else:
        print("\n*** Running in NORMAL mode (changes WILL be made) ***\n")

    with open(sys.argv[1], 'r') as f:
        for line in f:

            # Checks if the line starts with '#', assigns match with true or false which will later be used to skip the line.
            match = re.match("^#",line)

            # Splits up the line into fields, the colon seperates each field. 
            fields = line.strip().split(':')

            #REPLACE THESE COMMENTS with a single comment describing the logic of the IF 
            # Checks if match is true or fields is not 5
            # If either are meets the condition, the line is skipped.
            # It gets skipped because the '#' in front of the line indicates user wants it to be skipped, or an entry is invalid because it has more or less than 5 fields filled out.
            if match or len(fields) != 5:
                # In dry-run, show why the line is skipped
                if dry_run:
                    if match:
                        print("Skipping comment line:", line.strip())
                    elif len(fields) != 5:
                        print("Invalid line (does not have 5 fields):", line.strip())
                continue

            # Gets user info from each field in the line (username, password, first name, last name)
            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3],fields[2])

            # Gets groups which are split into a list separated by commas.
            groups = fields[4].split(',')

            # Shows that the following account is being created.
            print("==> Creating account for %s..." % (username))
            # Builds the command that will create a new user with no password and sets user info.
            cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

            # Prints the command (dry run purposes) and then runs it to create the user
            # If dry-run, only print command, otherwise run it
            if dry_run:
                print(cmd)
            else:
                os.system(cmd)

            # Shows thta the password is being set for the user.
            print("==> Setting the password for %s..." % (username))
            # Builds the command to set the password by sending it into the password command.
            cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

            # Prints the command and then runs it to set the user password
            # If dry-run, only print command, otherwise run it
            if dry_run:
                print(cmd)
            else:
                os.system(cmd)

            for group in groups:
                # If the group is not '-', add the user to that group (otherwise skip).
                if group != '-':
                    print("==> Assigning %s to the %s group..." % (username,group))
                
                    #Builds the command to add the user to the group.
                    cmd = "/usr/sbin/adduser %s %s" % (username,group)
                
                    # Prints the command and then run it to assign the group.
                    # If dry-run, only print command, otherwise run it
                    if dry_run:
                        print(cmd)
                    else:
                        os.system(cmd)

if __name__ == '__main__':
    main()
