﻿$csvpath = "C:\Users\Administrator.GLOSTONETRUCKIN\Downloads\usersemail.csv"
$teamID = "25de6371-623c-4817-9bd5-337184768dfe"
$users = Import-Csv -Path $csvpath
foreach($user in $users){
    Add-TeamUser -GroupId $teamID -User $user.UserEmail
}


Start-SPOTenantRename -DomainName "gradientway" -ScheduledDateTime "2024-11-5T20:30:00"