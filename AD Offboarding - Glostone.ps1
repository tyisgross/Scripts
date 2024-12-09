# update this for each user
$userlogin = "carolynk"


# constant variables
$useremail = $userlogin + "@glostone.com"
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

# Run this stuff first
Remove-ADGroupMember -Group "Glostone Usr" -Member $userlogin -Confirm:$false
Remove-DistributionGroupMember -Identity "Vehicle Services" -Member $useremail -Confirm:$false
Remove-DistributionGroupMember -Identity "All Hands" -Member $useremail -Confirm:$false
Remove-UnifiedGroupLinks -Identity "Vehicle Services Team" -LinkType Members -Links $useremail -Confirm:$false
Disable-ADAccount -Identity $userlogin
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($o365) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($mde) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($atp) -AddLicenses @{}
Remove-TeamUser -user $useremail -GroupId ############-307c-4ae6-8e29-############ -Role Member
Remove-TeamUser -user $useremail -GroupId ############-623c-4817-9bd5-############ -Role Member
