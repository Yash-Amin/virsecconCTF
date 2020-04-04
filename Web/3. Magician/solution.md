# Magician

* In this challenge, We have to find the value so that its md5 hash is equal to `0e953532678923638053842468642408`
* We can use magic hash, because the given hash is in the form of `/^0e\d*$/`

* PHP's == comparison, these types of string will be treated as float;

    ```php
    if ('0e111' == '0e222') {
        echo "True";  // Prints True!
    } else {
        echo "False";
    }
    ```
* So if we submit any magic hash, it will be accepted if the website uses `==` operator.
    
* I have used `QLTHNDT`, its hash is `0e405967825401955372549139051580`
    > https://github.com/spaze/hashes/blob/master/md5.md 

* After submitting it, I got the flag!
    > ### LLS{magic_hashes_make_for_a_good_show}