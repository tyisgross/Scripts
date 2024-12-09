# update this for each user
$userlogin = "testingg"
$firstname = "testing"
$lastname = "gross"


#constants
$password = "Sample Text!"
$ppassword = $password | ConvertTo-SecureString -AsPlainText -Force
$useremail = $userlogin + "@cleanfleet.org"
$o365 = "###########-75af-4f8e-b61f-###########"
$mde = "###########-a2b7-4360-8d07-###########"
$atp = "###########-f096-40de-a3e9-###########"

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

Start-ADSyncSyncCycle -PolicyType Initial

# Run this stuff to sync with the online office365 portal
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$credential = Get-Credential
Connect-MgGraph -Scopes User.ReadWrite.All, Organization.Read.All
Connect-ExchangeOnline -Credential $credential
Connect-MicrosoftTeams -Credential $credential
Import-Module -UseWindowsPowerShell -Name ADSync;
Start-Sleep -Seconds 60


# These things actually do the work; Setting licenses, distribution lists, teams groups.
Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $o365} -RemoveLicenses @()
Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $mde} -RemoveLicenses @()
Set-MgUserLicense -UserId $useremail -AddLicenses @{SkuID = $atp} -RemoveLicenses @()
Add-DistributionGroupMember -Identity "All Cleanfleet" -Member $useremail
Add-DistributionGroupMember -Identity "All Hands" -Member $useremail
Add-UnifiedGroupLinks -Identity "Driver Services Team" -LinkType Members -Links $useremail -Confirm:$false
Add-UnifiedGroupLinks -Identity "All Hands Team" -LinkType Members -Links $useremail -Confirm:$false
Add-TeamUser -user $useremail -GroupId ###########-5760-481e-b2bc-########### -Role Member
Add-TeamUser -user $useremail -GroupId ###########-623c-4817-9bd5-########### -Role Member
