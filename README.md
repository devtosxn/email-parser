# email-parser
## SCOPE
Terminal program to parse and split  email into username and domain given certain constraints

## CONSTRAINTS
- Username will be made up of alphabets or alphanumerics. Ex. `john`, `johndoe`, `john123`. 
- Username however cannot start with a number
- Username can also support only the + character in between, not at the end or beginning, for example: `jane+doe`, `j+doe`, etc.
- Domains will always end in .com, Ex. `gmail.com`, `yahoo.com`, `bz2.com`, etc.
- The part before .com in domains will be made up of alphabets or alphanumerics, Ex. `gmail`, `bz2`, `dom555`, etc. 
- Domain cannot also start with a number

`None` will be returned if constraints above are not satisfied

## OUTPUT
For ==> jane+doe@gmail.com, the format below is returned:
``` 
{
  'username' : 'jane+doe',
  'domain' : 'gmail.com'
}

```

For ==> johndoe123@gmail.com, the format below is returned:
``` 
{
  'username' : 'johndoe123',
  'domain' : 'gmail.com'
}

```

For ==> 3janedoe@gmail.com, +jdoe@bz2.com, james2@gmail.yahoo.com the format below is returned
```
None
```


