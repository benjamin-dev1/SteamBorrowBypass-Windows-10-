from tkinter import *
import subprocess

# Command to check if the rule exists
check_rule_command = 'powershell.exe -Command "Get-NetFirewallRule -DisplayName \'steaminternetblocker\'"'

# Command to create the rule
create_rule_command = 'powershell.exe -Command "New-NetFirewallRule -Program \'C:\\Program Files (x86)\\Steam\\Steam.exe\' -Action Block -Profile Domain,Private,Public -DisplayName \'steaminternetblocker\' -Description \'Block Steam internet access\' -Direction Outbound"'

# Command to enable/disable the existing firewall rule
enable_command = 'powershell.exe -Command "Set-NetFirewallRule -DisplayName \'steaminternetblocker\' -Enabled True"'
disable_command = 'powershell.exe -Command "Set-NetFirewallRule -DisplayName \'steaminternetblocker\' -Enabled False"'

def rule_exists():
    # Check if the rule exists
    result = subprocess.run(check_rule_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def create_rule():
    # Create the rule if it doesn't exist
    subprocess.run(create_rule_command, shell=True)

def Simpletoggle():
    if rule_exists():
        if toggle_button.config('text')[-1] == 'Turn ON':
            toggle_button.config(text='Turn OFF')
            subprocess.Popen(enable_command, shell=True)
        else:
            toggle_button.config(text='Turn ON')
            subprocess.Popen(disable_command, shell=True)
    else:
        create_rule()  # Create the rule
        Simpletoggle()  # Toggle the rule after creation


ws = Tk()
ws.title("Steam Internet Blocker")
ws.geometry("300x100")

toggle_button = Button(text="Click Me", width=20, command=Simpletoggle, compound='top')
toggle_button.pack(pady=10)

label_on_top = Label(text="Steam Internet Blocker", fg="black")  # Add a label on top of the button
label_on_top.pack()

ws.mainloop()
