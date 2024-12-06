$useremail = "barryl@glostone.com"
$licenses = Get-MgSubscribedSku

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Import-Module ExchangeOnlineManagement
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes User.ReadWrite.All, Organization.Read.All -NoWelcome

Connect-ExchangeOnline -UserPrincipalName tyg@glostone.com

# Run this stuff first

Remove-DistributionGroupMember -Identity AllGlostone -Member $useremail
Remove-DistributionGroupMember -Identity AllUsers -Member $useremail
Remove-DistributionGroupMember -Identity AllHands -Member $useremail