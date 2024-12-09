# update this for each user
$userlogin = "testingg"

# constant variables
$useremail = $userlogin + "@cleanfleet.org"
$o365 = "############-75af-4f8e-b61f-############"
$mde = "############-a2b7-4360-8d07-############"
$atp = "############-f096-40de-a3e9-############"

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$credential = Get-Credential
#Import-Module ExchangeOnlineManagement
#Import-Module Microsoft.Graph
Connect-MgGraph -Scopes User.ReadWrite.All, Organization.Read.All
Connect-ExchangeOnline -Credential $credential
Connect-MicrosoftTeams -Credential $credential

# These things actually do the work; Removing licenses, distribution lists, teams groups, 
Remove-ADGroupMember -Identity "CleanFleet Usr" -Member $userlogin -Confirm:$false
Remove-DistributionGroupMember -Identity "All Cleanfleet" -Member $useremail -Confirm:$false
Remove-DistributionGroupMember -Identity "All Hands" -Member $useremail -Confirm:$false
Remove-UnifiedGroupLinks -Identity "All Hands Team" -LinkType Members -Links $useremail -Confirm:$false
Disable-ADAccount -Identity $userlogin
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($o365) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($mde) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($atp) -AddLicenses @{}
Remove-TeamUser -user $useremail -GroupId ############-5760-481e-b2bc-############ -Role Member
Remove-TeamUser -user $useremail -GroupId ############-623c-4817-9bd5-############ -Role Member

#remember to check work :)

