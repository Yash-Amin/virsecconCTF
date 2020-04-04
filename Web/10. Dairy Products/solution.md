# Dairy Products

On the main page, there was huge label
> ## git milk?

So before trying to do anything, I opened `http://142.93.3.19:50008/.git`

It was a git directory, So we can download it and get all history!

I've used `wget -r --no-parent http://142.93.3.19:50008/.git/` command to download the directory.

After downloading the directory, I have used this commad to retrive the flag.

> `git log | grep commit | cut -d ' ' -f2 | while read line; do echo zzzz; git show $line; done | grep -i "{.*}"`

* git log is used to get commit history.
* then the output of `git log` will be passed to `grep commit` to get commit ID.
* we only need the commit ID, so we can use cut command to get 2nd column. 
* for all commits, we can use `git show <commit_id>` to get changes of that commit.
* And we know that the flag is in the format of `[A-Z]*{.*}` we can use grep to get the flag!


> ### LLS{you_gitm_gotm_good_partner}