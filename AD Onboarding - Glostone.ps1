# update this for each user
$userlogin = "diannad"
$firstname = "dianna"
$lastname = "dilling"



#constants we do not need to change
$password = "Sample Text"
$ppassword = $password | ConvertTo-SecureString -AsPlainText -Force
$useremail = $userlogin + "@glostone.com"
$o365 = "########-75af-4f8e-b61f-########"
$mde = "########-a2b7-4360-8d07-########"
$atp = "########-f096-40de-a3e9-########"

#creates user locally
$splat = @{
    Name = $firstname + ' ' + $lastname
    GivenName = $firstname
    Surname = $lastname
    AccountPassword = $ppassword
    Enabled = $true
    UserPrincipalName = $useremail
    SamAccountName = $userlogin
    Path = "OU=Users,OU=Glostone,DC=GlostoneTrucking,DC=local"
}
New-ADUser @splat

Add-ADGroupMember -Identity "Glostone Usr" -Members $userlogin -Confirm:$false

Start-Sleep -Seconds 10

Import-Module -UseWindowsPowerShell -Name ADSync;
Start-ADSyncSyncCycle -PolicyType Initial

# Run this stuff to sync with the online office365 portal
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$credential = Get-Credential
Connect-MgGraph -Scopes User.ReadWrite.All, Organization.Read.All
Connect-ExchangeOnline -Credential $credential
Connect-MicrosoftTeams -Credential $credential

Start-Sleep -Seconds 60

# These things actually do the work; Setting licenses, distribution lists, teams groups, 
Add-DistributionGroupMember -Identity "Vehicle Services" -Member $useremail
Add-DistributionGroupMember -Identity "All Hands" -Member $useremail
Add-UnifiedGroupLinks -Identity "Vehicle Services Team" -LinkType Members -Links $useremail -Confirm:$false
Add-UnifiedGroupLinks -Identity "All Hands Team" -LinkType Members -Links $useremail -Confirm:$false
Add-TeamUser -user $useremail -GroupId ########-307c-4ae6-8e29-######## -Role Member
Add-TeamUser -user $useremail -GroupId ########-623c-4817-9bd5-######## -Role Member
