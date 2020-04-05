# GET Encoded

We have this website that says `Machine hunts for more than humand do`, Nothing else. But the challenge's name is GET Encode, there must be something to do with the query parameters. 
![Index](1.png)

So I sent request to `/?aaa=bbb` and in the response I got error message that function `aaa` was undefined.
![Command execution](2.png)

So then I tried printf function to check does it takes function arguments? So I sent the request `/?printf=test123` and it worked.
![printf](3.png)

Then I tried using the `shellexec` function to execute code but it gave this error. After spending about 20 minutes on REQUEST_URI header, I could not find anything. I have also tried other functions like exec, passthru... file nothing workked. 
![shellexec](4.png)


Then after URL encoding the parameter's name, I sent the request. So,
*  >  `/?passthru=cat+index.php`   

![passthru](5.png)

After URL ecoding

* > `/?%70%61%73%73%74%68%72%75=cat+index.php`

![url encoding](6.png)

And it worked. I can execute any command like this so after executing `ls` command I found these files. There was robots.txt file too that I did not notice before! 

After opening the robots.txt file I foudn that we can use `/?debug` query to get PHP source code!
![Robots](8.png)
![Code](9.png)

Anyway, I used `cat` command to read the flag.php file. But it did not allow dots, so I had to URL encode the value as well.

![Flag](10.png)

> ### LLS{i_gotcha_url_encoding}


