Import-Module ExchangeOnlineManagement

Connect-ExchangeOnline -UserPrincipalName tyg@glostone.com

# Run this stuff first

$Users = "tylerk@cleanfleet.org", "jessez@cleanfleet.org"
$(foreach ($User in $Users){

Set-MailboxAutoReplyConfiguration -Identity $User -AutoReplyState Enabled `
-InternalMessage "Hello, I am currently out of the office. My emails are not being monitored. For immediate assistance please contact our team at 503-479-6082. Thanks" `
-ExternalMessage "Hello, I am currently out of the office. My emails are not being monitored. For immediate assistance please contact our team at 503-479-6082. Thanks"

})
