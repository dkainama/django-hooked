## What is Hooked?

Receive signed and secure webhooks in Django




### Setup Hooked for contributing / development / testing

Now choose dev environment, with __virtualenvwrapper__ installed:

      make setup2 NAME=hook # for python 2.X
     
      make setup3 NAME=hook # for python 3.X
      
Now init dev environment

      make init
      
Run tests

      make test


#### HMAC & payload

The hash consists of the following parts:

     B64(HMAC(SHA256,SHA1(PAYLOAD),SHARED_SECRET));


* __PAYLOAD__ is a SHA1 of the JSON (stringified).
* __SHARED_SECRET__ is generated when creating a new HookedApp


#### Clients

> Write more about HMAC tokens {Ruby, ~~PHP~~, JS}

##### PHP

__Function:__

    string base64_encode(hash_hmac(“sha256” , sha1(“{}”), false));

__Example:__
    
    $ php -a
    php > $payload = “{ … }”
    php > $data = json_encode(json_decode($payload), JSON_UNESCAPED_SLASHES);
    php > $match = sha1($data);
    php > echo base64_encode(hash_hmac("sha256", $match, "example1234", true));

### Is it any good?

[Yes.](http://news.ycombinator.com/item?id=3067434)


#### Credits

Inspired by article on webhook receivers in Django:
https://medium.com/@raiderrobert


