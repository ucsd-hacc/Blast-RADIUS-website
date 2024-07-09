---
html-id: pocs
question: Is attack code available?
---

We are not publishing end-to-end attack code.  Our improvements to the
MD5 chosen-prefix collision attack are available in the [hashclash
GitHub
repository](https://github.com/cr-marcstevens/hashclash/pull/37).


If you are a vendor or system administrator who wishes to test for this vulnerability, a
RADIUS server implementation is vulnerable if it does not require a
Message-Authenticator attribute in every client request.  A RADIUS
client is vulnerable if it does not require a Message-Authenticator
attribute from every server response.  See [Alan DeKok's white
paper](https://www.inkbridgenetworks.com/blastradius)
for more information.