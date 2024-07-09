---                                                                                                                                                                                                                                          
title: Blast-RADIUS
menu-title: overview
html-id: abstract
---

Blast-RADIUS is a vulnerability that affects the RADIUS protocol. 
RADIUS is a very common protocol used for authentication,
authorization, and accounting (AAA) for networked devices on
enterprise and telecommunication networks.

### What can the attacker do?

The Blast-RADIUS attack allows a man-in-the-middle attacker between
the RADIUS client and server to forge a valid protocol accept message
in response to a failed authentication request.  This forgery could
give the attacker access to network devices and services without the
attacker guessing or brute forcing passwords or shared secrets.  The
attacker does not learn user credentials.

### Who is affected?

Blast-RADIUS is a protocol vulnerability, and thus affects all
RADIUS implementations using non-EAP authentication methods over UDP.

System administrators of networks using RADIUS should check with
vendors for a patch against this vulnerability, and follow best
practices for RADIUS configuration as discussed below.  There is
nothing that end users can do on their own to protect against this
attack.

RADIUS is used in a wide variety of applications, including in
enterprise networks to authenticate access to switches and other
routing infrastructure, for VPN access, by ISPs for DSL and FTTH
(Fiber to the Home), in 802.1X and Wi-Fi authentication, 2G and 3G
cellular roaming and 5G DNN (Data Network Name) authentication, mobile
Wi-Fi offload with SIM card-based authentication, private APN
authentication, to authenticate access to critical infrastructure, and
in the Eduroam and OpenRoaming wifi consortia.

### What is the vulnerability?

The RADIUS protocol predates modern cryptographic guarantees and is
typically unencrypted and unauthenticated.  However, the protocol does
attempt to authenticate server responses using an ad hoc construction
based on the MD5 hash function and a fixed shared secret between a
client and server.

Our attack combines a novel protocol vulnerability with an MD5
chosen-prefix collision attack and several new speed and space
improvements.  The attacker injects a malicious attribute into a
request that causes a collision between the authentication information
in the valid server response and the attacker's desired forgery.
This allows the attacker to turn a reject into an accept, and
add arbitrary protocol attributes.
