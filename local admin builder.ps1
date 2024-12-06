##This script should be run with a GPO to build a local admin account on computer startup so that the IT team always has a backdoor.

$username = "gstadmin"
$password = ConvertTo-SecureString "GSTL0c@!adm12" -AsPlainText -Force
New-LocalUSer -Name "$username" -Password $password -FullName "$username" -Description "Local Admin"
Add-LocalGroupMember -Group "Administrators" -Member "$username"