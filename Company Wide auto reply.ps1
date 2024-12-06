$Users = "alexb@glostone.com","BrianG@cleanfleet.org","Carolynk@glostone.com","Cheyo@cleanfleet.org","cyndik@glostone.com","DiannaD@cleanfleet.org","@cleanfleet.org","Ericn@glostone.com","HeatherB@cleanfleet.org","HeatherG@glostone.com","JeffD@glostone.com","JennaK@glostone.com","JenniferG@glostone.com","JenniferK@cleanfleet.org","JesseN@cleanfleet.org","JesseZ@cleanfleet.org","JohnM@glostone.com","justink@cleanfleet.org","kimberlyg@cleanfleet.org","Kristinat@glostone.com","RaquelT@cleanfleet.org","LilliA@glostone.com","LindseyH@glostone.com","Lourdess@cleanfleet.org","mariet@cleanfleet.org","Micahp@glostone.com","RebeccaW@cleanfleet.org","robinm@glostone.com","SarahM@cleanfleet.org","Sarahybr@cleanfleet.org","SuzanneS@cleanfleet.org","tyg@glostone.com","TylerK@cleanfleet.org","Aleksandrab@cleanfleet.org"

$(foreach ($User in $Users){

Set-MailboxAutoReplyConfiguration -Identity $User -AutoReplyState Disabled 

})