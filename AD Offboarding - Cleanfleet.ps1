# update this for each user
$userlogin = "diannad"
$useremail = $userlogin + "@cleanfleet.org"

# constant variables
$o365 = "f245ecc8-75af-4f8e-b61f-27d8114de5f3"
$mde = "5e1e7702-a2b7-4360-8d07-2f515792896f"
$atp = "4ef96642-f096-40de-a3e9-d83fb2f90211"

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#Import-Module ExchangeOnlineManagement
#Import-Module Microsoft.Graph
Connect-MgGraph -Scopes User.ReadWrite.All, Organization.Read.All
Connect-ExchangeOnline -UserPrincipalName tyg@glostone.com
Connect-MicrosoftTeams -UserPrincipalName tyg@glostone.com

# Run this stuff first

Remove-DistributionGroupMember -Identity AllCleanFleet -Member $useremail -Confirm:$false
Remove-DistributionGroupMember -Identity AllUsers -Member $useremail -Confirm:$false
Remove-DistributionGroupMember -Identity AllHands -Member $useremail -Confirm:$false
Disable-ADAccount -Identity $userlogin
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($o365) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($mde) -AddLicenses @{}
Set-MgUserLicense -UserId $useremail -RemoveLicenses @($atp) -AddLicenses @{}
Remove-TeamUser -user $useremail -GroupId b5e025d7-5760-481e-b2bc-d3467db9353d -Role Member
Remove-TeamUser -user $useremail -GroupId 25de6371-623c-4817-9bd5-337184768dfe -Role Member
