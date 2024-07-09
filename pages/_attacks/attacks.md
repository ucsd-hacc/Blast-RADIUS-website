---
title: Blast-RADIUS Attack in More Detail
menu-title: Attack Details
html-id: attacks
---

The RADIUS (Remote Authentication Dial-In User Service) protocol is at the core of today's network infrastructure.
Although the protocol was first designed in 1991 &mdash; during the era of dial-up
internet &mdash; it remains the de facto standard lightweight authentication protocol used for remote access for users and administrators to networked devices.  RADIUS is supported by "essentially every switch, router, access point, and VPN concentrator product sold in the last twenty years" ([source](https://www.inkbridgenetworks.com/blastradius)).

In RADIUS, a NAS (Network Access Server) acts as a client that verifies an end user's credentials via RADIUS requests to a central server.
The RADIUS client and server share a fixed secret.
The server responds with an accept or reject message (called `Access-Accept` and `Access-Reject`, respectively).  Requests and responses may contain labeled fields called "attributes" that specify various parameters such as username and password in a request, or network access in a response.
Request packets include a value called a `Request Authenticator` that is essentially a random nonce.  Response packets include a value called a `Response Authenticator` value that is intended to integrity-protect server responses.

The `Response Authenticator` is computed as
\\[ \mathtt{MD5} ( \mathtt{Code} || \mathtt{ID} || \mathtt{Length} || \mathtt{Request\ Authenticator} || \mathtt{Packet\ Attributes} || \mathtt{Shared\ Secret}), \\]
where, as the figure below shows, $$\mathtt{ID}$$ and $$\mathtt{Request\ Authenticator}$$ are random values that are in the request; $$\mathtt{Code}$$, $$\mathtt{Length}$$, and $$\mathtt{Packet\ Attributes}$$ are values in the server response, and $$\mathtt{Shared\ Secret}$$ is the fixed shared secret that client and server know, but which is unknown to the attacker.

<img alt="Response Authenticator preimage" src="/img/preimage.png" style="width: 100%;">

In our paper, we give an attack against this ad hoc RADIUS `Response Authenticator` "MAC" construction.
Our attack allows a man in the middle between the RADIUS client and server to forge a valid `Access-Accept` response to a failed authentication request.  The attacker does this by injecting a malicious `Proxy-State` attribute into a valid client request.  This `Proxy-State` attribute is guaranteed to be echoed back by the server in its response.  The attacker constructs the `Proxy-State` so that the `Response Authenticator` values between the valid response and the response the attacker wishes to forge will be identical.
This forgery will cause the NAS to grant the adversary access to network devices and services without the adversary guessing or brute forcing passwords or shared secrets.

The MD5 collision attack that we exploit is a version of the chosen-prefix collision from [Stevens et al.](https://eprint.iacr.org/2009/111).
A chosen-prefix collision allows us, given distinct prefixes $$P_1$$ and $$P_2$$, to efficiently compute gibberish blocks $$G_1$$ and $$G_2$$ such that $$\mathtt{MD5}(P_1 || G_1 ) = \mathtt{MD5}(P_2 || G_2)$$.
Having done so, the structure of MD5 means that we can then append any fixed suffix $$S$$ and the resulting messages still have colliding MD5 hashes: $$\mathtt{MD5}(P_1 || G_1 || S) = \mathtt{MD5}(P_2 || G_2 || S)$$.

In summary, the following figure illustrates our attack when RADIUS is used with PAP, the Password Authentication Protocol.

<img alt="attack flow" src="/img/radius_overview.png" style="width: 100%;">

1. The adversary enters the username of a privileged user and an arbitrary incorrect password.
2. This causes the RADIUS client of a victim's network device to generate a RADIUS `Access-Request`, which includes a 16-byte random value called `Request Authenticator`.
3. The man-in-the-middle adversary intercepts this request and uses the `Access-Request` (including the random `Request Authenticator`) to predict the format of the server response (which will be an `Access-Reject` as the entered password is incorrect). Then the adversary computes an MD5 collision between the predicted `Access-Reject` and an `Access-Accept` response that it would like to forge. This results in binary gibberish strings 
$$\mathtt{RejectGibberish}$$ and $$\mathtt{AcceptGibberish}$$ such that
$$\mathtt{MD5}(\mathtt{Access\text{-}Reject || RejectGibberish})$$
equals $$\mathtt{MD5}(\mathtt{Access\text{-}Accept || AcceptGibberish})$$.
4. After computing the collision, the man-in-the-middle attacker adds $$\mathtt{RejectGibberish}$$ to the `Access-Request` packet, disguised as a `Proxy-State` attribute.
5. The server receiving this modified `Access-Request` checks the user password, decides to reject the request, and responds with an `Access-Reject` packet. As the RADIUS protocol mandates that the `Proxy-State` attributes are included in responses, $$\mathtt{RejectGibberish}$$ is attached to the response. In addition, the server computes and sends a `Response Authenticator`, which is essentially 
$$\mathtt{MD5}(\mathtt{Access\text{-}Reject || RejectGibberish || SharedSecret})$$,
for its `Access-Reject` response, to prevent tampering.  The attacker does not know the value of $$\mathtt{SharedSecret}$$ and cannot predict or verify the MD5 hash.
6. The adversary intercepts this response and checks that the packet format matches the predicted
$$\mathtt{Access\text{-}Reject || RejectGibberish}$$
pattern. If it does, the adversary replaces the response by
$$\mathtt{Access\text{-}Accept || AcceptGibberish}$$
and sends it with the unmodified `Response Authenticator` to the client.
7. Due to the MD5 collision, the `Access-Accept` sent by the adversary verifies with the `Response Authenticator`, without the adversary knowing the shared secret. Hence, the RADIUS client believes the server approved this login request and grants the adversary access.
{: .text-left }

This description is simplified. In particular, we had to do cryptographic work to split the MD5 collision gibberish across multiple properly formatted `Proxy-State` attributes, and to optimize and parallelize the MD5 collision attack to run in minutes instead of hours.  Please read [our paper](/pdf/radius.pdf) for a comprehensive description.
