---
html-id: pocs
question: Is attack code available?
---

A script with an example collision is available [here](/example.py).
The `--verbose` option allows the printing of unshortened values.
The script goes through the attack step by step:
1. The Access-Request sent by the RADIUS client, from which the adversary learns the Request Authenticator and IDs.
2. The MITM uses these values from the Access-Request to predict Accept and Reject prefixes and then computes the collision gibberish that it computes for these prefixes.
3. The MITM assembles the Access-Request with that Reject gibberish appended, that is sent to the RADIUS server.
4. The Access-Reject sent back by the server contains the Response Authenticator.
5. The MITM puts this value to assemble the Access-Accept.
6. We show both the Access-Accept and Access-Reject both produce the same Response Authenticator.

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
