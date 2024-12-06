Import-Module ExchangeOnlineManagement

Connect-ExchangeOnline -UserPrincipalName tyg@glostone.com

# Run this stuff first

Remove-DistributionGroupMember -Identity AllGlostone -Member jenniferg@glostone.com
Remove-DistributionGroupMember -Identity AllUsers -Member jenniferg@glostone.com
Add-DistributionGroupMember -Identity FirstTeam -Member kieshas@glostone.com

