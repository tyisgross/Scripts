# update this for each user
$userlogin = "testingb"


# constant variables
$useremail = $userlogin + "@glostone.com"
$o365 = "f245ecc8-75af-4f8e-b61f-27d8114de5f3"
$mde = "5e1e7702-a2b7-4360-8d07-2f515792896f"
$atp = "4ef96642-f096-40de-a3e9-d83fb2f90211"

$credential = Get-Credential
Import-Module -UseWindowsPowerShell -Name ADSync;
Start-ADSyncSyncCycle -PolicyType Initial
Import-Module Microsoft.Graph.Entra

# Run this stuff to sync with the online office365 portal
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Connect-MgGraph -Scopes "User.Read.All","Group.ReadWrite.All"
Connect-ExchangeOnline -Credential $credential
Connect-MicrosoftTeams -Credential $credential
Start-Sleep -Seconds 45

# These things actually do the work; Setting licenses, distribution lists, teams groups, 
Remove-ADGroupMember -Identity "Glostone Usr" -Member $userlogin -Confirm:$false
Remove-DistributionGroupMember -Identity "Vehicle Services" -Member $useremail -Confirm:$false
Remove-DistributionGroupMember -Identity "All Hands" -Member $useremail -Confirm:$false
Remove-UnifiedGroupLinks -Identity "Vehicle Services Team" -LinkType Members -Links $useremail -Confirm:$false
Remove-UnifiedGroupLinks -Identity "All Hands Team" -LinkType Members -Links $useremail -Confirm:$false
Disable-ADAccount -Identity $userlogin
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($o365) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($mde) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($atp) -AddLicenses @{}
Remove-TeamUser -user $useremail -GroupId 84b08969-307c-4ae6-8e29-7818839e1a9d -Role Member
Remove-TeamUser -user $useremail -GroupId 25de6371-623c-4817-9bd5-337184768dfe -Role Member
