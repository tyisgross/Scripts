# update this for each user
$userlogin = "diannad"
$useremail = $userlogin + "@cleanfleet.org"

#license constants
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

Add-DistributionGroupMember -Identity AllCleanFleet -Member $useremail
Add-DistributionGroupMember -Identity AllUsers -Member $useremail
Add-DistributionGroupMember -Identity AllHands -Member $useremail

Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $o365} -RemoveLicenses @()
Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $mde} -RemoveLicenses @()
Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $atp} -RemoveLicenses @()
