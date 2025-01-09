# update this for each user
$fname = Read-Host 'Enter the users first name'
$lname = Read-Host 'Enter the users last name'
$userlogin = $fname + $lname.Substring(0,1)
$useremail = $userlogin + "@cleanfleet.org"

# constant variables
$o365 = "f245ecc8-75af-4f8e-b61f-27d8114de5f3"
$mde = "5e1e7702-a2b7-4360-8d07-2f515792896f"
$atp = "4ef96642-f096-40de-a3e9-d83fb2f90211"
$DSteam = "b5e025d7-5760-481e-b2bc-d3467db9353d"
$Allhandsteam = "25de6371-623c-4817-9bd5-337184768dfe"

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

Remove-DistributionGroupMember -Identity "All CleanFleet" -Member $useremail -Confirm:$false
Remove-DistributionGroupMember -Identity "All Hands" -Member $useremail -Confirm:$false
Remove-UnifiedGroupLinks -Identity "Driver Services Team" -LinkType Members -Links $useremail -Confirm:$false
Remove-UnifiedGroupLinks -Identity "All Hands Team" -LinkType Members -Links $useremail -Confirm:$false
Disable-ADAccount -Identity $userlogin
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($o365) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($mde) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($atp) -AddLicenses @{}
Remove-TeamUser -user $useremail -GroupId $DSteam -Role Member
Remove-TeamUser -user $useremail -GroupId $Allhandsteam -Role Member

#remember to check work :)
