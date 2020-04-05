# Chasm

* Looks like we can inject any command and get output!
* After running `a & ls` command, I found that there is `flag.txt` file in that directory.
    ![RCE](1.png)

* Then I tried reading `flag.txt` but it gave error. Because the `server.py` contains one condition, if command contains `flag` then don't execute it.  
    ![Flag](2.png)

* But we know the flag's format. So we can use grep on this directory to get the flag!
    > `a & grep -r "LS{" .`
    
    ![Flag](3.png)
<!-- 
    * Output  
    ```
    ECHO: a  
    ./flag.txt:LLS{dangerous_echos_in_this_chasm}
    ``` -->
    
> ### LLS{dangerous_echos_in_this_chasm}