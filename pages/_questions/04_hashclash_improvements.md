---
html-id: hashclash-improvements
question: Hasn't MD5 been broken for 20 years?  How is this attack new?
---

Our attack is more complex than simply applying an old MD5 collision attack.

While an MD5 hash collision was first demonstrated in 2004, it was not
thought to be possible to exploit this in the context of the RADIUS
protocol.  Our attack identifies a protocol vulnerability in the way
RADIUS uses MD5 that allows the attacker to inject a malicious
protocol attribute that produces a hash collision between the
server-generated Response Authenticator and the attacker's desired
forged response packet.

In addition, because our attack is online, the attacker needs to be
able to compute a so-called chosen-prefix MD5 collision attack in minutes
or seconds.  The previous best reported chosen-prefix collision attack
times took hours, and produced collisions that were not compatible with the RADIUS
protocol.

We introduce several improvements in speed, space, and scaling for the
existing MD5 attacks to demonstrate that these collisions can be
computed in at most minutes and can fit within RADIUS protocol
attributes.