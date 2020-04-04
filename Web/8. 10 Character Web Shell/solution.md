# 10 Character Web Shell


The main page displayed the code of index page.
```php
<?php

    $c = $_GET[c];

    if(strlen($c) < 10){
            echo shell_exec($c);
    }else{
            echo "too long!";
    }
    highlight_file(__FILE__);
?>
```
If we pass any value of `c`, it will execute it. But its length must me **less than 10.**
So I tried `echo hey` and it worked. Then I tried the command `ls` to list directory. 
There were about 300 files with random looking names.  I scrolled to bottom and saw `flag.txt`.

Then I tried `cat flag.txt` but as length of the string is 12, It didn't execute it. I remembered one article where some unicode characters were used to bypass this length limit, but here there was no case transformation so I thought it wouldn't work.

Then after few minutes, I thought that flag is in the same directory, so instead of passing command, I can simply access it by `http://jh2i.com:50001/flag.txt`

> ### LLS{you_really_can_see_in_the_dark}