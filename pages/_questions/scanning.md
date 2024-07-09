---
html-id: scanning
question: How many RADIUS deployments are vulnerable to this attack?
---

Unfortunately, we are not able to use network scanning to provide a representative picture of RADIUS deployments.  Many RADIUS servers will be on internal networks.  Even for external-facing servers, RADIUS hosts are identified by IP address and servers only accept packets from allowed addresses.  The RADIUS RFC specifies that servers should drop requests for hosts that they have not been pre-configured to have a shared secret with.  Our scanning host  would not be whitelisted by properly configured servers, so an internet-wide scan would thus only turn up misconfigured servers. Additionally, since it is a UDP-based protocol with no handshake before a login request, we cannot do TCP SYN scanning and would need to scan using a well-formed UDP `Access-Request`, which would appear as an attack to network administrators.

This does not affect the adversary in our attack model, who intercepts traffic between a legitimate client and server.

However, since this vulnerability is in the protocol, nearly all RADIUS/UDP implementations are vulnerable to our attack **when using non-EAP authentication methods**.
