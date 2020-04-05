# Ssh, quite!


* When we use `ssh user@jh2i.com -p 50035` to connect and enter the password to log in, we immediately disconnect from SSH.

* I dont know if this is the correct way to do it or not! This is what I did...

* I have used `scp` to download file, tried downloading `flag.txt` and it worked!  
    `scp -P 50035 user@jh2i.com:flag.txt flag.txt`
    

    > ### LLS{automate_ssh_like_a_boss}
