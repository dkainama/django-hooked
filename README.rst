What is Hooked?
---------------

Receive signed and secure webhooks in Django

Setup Hooked for contributing / development / testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now choose dev environment, with **virtualenvwrapper** installed:

::

     make setup2 NAME=hook # for python 2.X
    
     make setup3 NAME=hook # for python 3.X
     

Now init dev environment

::

     make init
     

Run tests

::

     make test

HMAC & payload
^^^^^^^^^^^^^^

The hash consists of the following parts:

::

    B64(HMAC(SHA256,SHA1(PAYLOAD),SHARED_SECRET));

-  **PAYLOAD:** is a SHA1 of the JSON (stringified).
-  **SHARED_SECRET:** is generated when creating a new HookedApp

Clients
^^^^^^^

   Write more about HMAC tokens {Ruby, [STRIKEOUT:PHP], JS}

PHP
'''

**Function:**

::

   string base64_encode(hash_hmac(“sha256” , sha1(“{}”), false), "SECRET");

**Example:**

::

   $ php -a
   php > $payload = “{ … }”
   php > $data = json_encode(json_decode($payload), JSON_UNESCAPED_SLASHES);
   php > $match = sha1($data);
   php > echo base64_encode(hash_hmac("sha256", $match, "white-stripes muse M89 killers prides", true));

Usage
=====

Curl request for webhook with authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   curl \
       -X POST \
       -d '{ data: { id: 1 }, hooked: { event: 'ADDED' }}' \
       -H "Content-Type: application/json" \
       -H "X-HOOKED-APP-ID: APP_UUID" \
       -H "X-HOOKED-TOKEN:  HMAC_TOKEN" \
       -H "X-HOOKED-EVENT:  EVENT" \ 
       "https://example.com/myapp/webhooks/"

..

   If authentication is required: we expect the following headers in the
   POST request for validation:

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td colspan="3">

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

X-HOOKED-APP-ID

.. raw:: html

   </td>

.. raw:: html

   <td>

required

.. raw:: html

   </td>

.. raw:: html

   <td>

unique identifier for client / app

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

X-HOOKED-TOKEN

.. raw:: html

   </td>

.. raw:: html

   <td>

required (if endpoint is secured)

.. raw:: html

   </td>

.. raw:: html

   <td>

HMAC token derived HMAC(256) => request body + shared_secret

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

X-HOOKED-EVENT

.. raw:: html

   </td>

.. raw:: html

   <td>

required

.. raw:: html

   </td>

.. raw:: html

   <td>

to identify a request, ex: delete, create, test, enz .

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

Is it any good?
~~~~~~~~~~~~~~~

`Yes. <http://news.ycombinator.com/item?id=3067434>`__

Credits
^^^^^^^

Inspired by article on webhook receivers in Django:
https://medium.com/@raiderrobert
