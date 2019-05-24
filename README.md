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


* __PAYLOAD:__ is a SHA1 of the JSON (stringified).
* __SHARED_SECRET:__ is generated when creating a new HookedApp


#### Clients

> Write more about HMAC tokens {Ruby, ~~PHP~~, JS}

##### PHP

__Function:__

    string base64_encode(hash_hmac(“sha256” , sha1(“{}”), false), "SECRET");

__Example:__
    
    $ php -a
    php > $payload = “{ … }”
    php > $data = json_encode(json_decode($payload), JSON_UNESCAPED_SLASHES);
    php > $match = sha1($data);
    php > echo base64_encode(hash_hmac("sha256", $match, "white-stripes muse M89 killers prides", true));


Usage
=====

### Curl request for webhook <span style="text-decoration:underline;">with</span> authentication

    curl \
        -X POST \
        -d '{ data: { id: 1 }, hooked: { event: 'ADDED' }}' \
        -H "Content-Type: application/json" \
        -H "X-HOOKED-APP-ID: APP_UUID" \
        -H "X-HOOKED-TOKEN:  HMAC_TOKEN" \
        -H "X-HOOKED-EVENT:  EVENT" \ 
        "https://example.com/myapp/webhooks/"

> If authentication is required: we expect the following headers in the POST request for validation:


<table>
  <tr>
   <td colspan="3" >
   </td>
  </tr>
  <tr>
   <td>X-HOOKED-APP-ID
   </td>
   <td>required
   </td>
   <td>unique identifier for client / app
   </td>
  </tr>
  <tr>
   <td>X-HOOKED-TOKEN
   </td>
   <td>required<em> (if endpoint is secured)</em>
   </td>
   <td>HMAC token derived HMAC(256) => request body + shared_secret
   </td>
  </tr>
  <tr>
   <td>X-HOOKED-EVENT
   </td>
   <td>required
   </td>
   <td>to identify a request, ex: delete, create, test, enz .
   </td>
  </tr>
</table>


### Is it any good?

[Yes.](http://news.ycombinator.com/item?id=3067434)


#### Credits

Inspired by article on webhook receivers in Django:
https://medium.com/@raiderrobert


