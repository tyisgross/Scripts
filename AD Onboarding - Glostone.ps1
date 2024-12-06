$useremail = "shellya@glostone.com"

Import-Module ExchangeOnlineManagement

Connect-ExchangeOnline -UserPrincipalName tyg@glostone.com

# Run this stuff first

Add-DistributionGroupMember -Identity AllGlostone -Member $useremail
Add-DistributionGroupMember -Identity AllUsers -Member $useremail