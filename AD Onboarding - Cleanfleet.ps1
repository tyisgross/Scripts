# update this for each user
$userlogin = "testingt"
$firstname = "testing"
$lastname = "ty"


#constants
$password = "Gradient2025!"
$ppassword = $password | ConvertTo-SecureString -AsPlainText -Force
$useremail = $userlogin + "@cleanfleet.org"
$o365 = "f245ecc8-75af-4f8e-b61f-27d8114de5f3"
$mde = "5e1e7702-a2b7-4360-8d07-2f515792896f"
$atp = "4ef96642-f096-40de-a3e9-d83fb2f90211"

#creates user locally
$splat = @{
    Name = $firstname + ' ' + $lastname
    GivenName = $firstname
    Surname = $lastname
    AccountPassword = $ppassword
    Enabled = $true
    UserPrincipalName = $useremail
    SamAccountName = $userlogin
    Path = "OU=Users,OU=CleanFleet,DC=GlostoneTrucking,DC=local"
}
New-ADUser @splat

Add-ADGroupMember -Identity "CleanFleet Usr" -Members $userlogin -Confirm:$false

Start-Sleep -Seconds 10

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

# These things actually do the work; Setting licenses, distribution lists, teams groups.
Set-EntraUser -UserId $useremail -UsageLocation "US"
Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $o365} -RemoveLicenses @()
Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $mde} -RemoveLicenses @()
Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $atp} -RemoveLicenses @()
Add-DistributionGroupMember -Identity "All Cleanfleet" -Member $useremail
Add-DistributionGroupMember -Identity "All Hands" -Member $useremail
Add-UnifiedGroupLinks -Identity "Driver Services Team" -LinkType Members -Links $useremail -Confirm:$false
Add-UnifiedGroupLinks -Identity "All Hands Team" -LinkType Members -Links $useremail -Confirm:$false
Add-TeamUser -user $useremail -GroupId b5e025d7-5760-481e-b2bc-d3467db9353d -Role Member
Add-TeamUser -user $useremail -GroupId 25de6371-623c-4817-9bd5-337184768dfe -Role Member
