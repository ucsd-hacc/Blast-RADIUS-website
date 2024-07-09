---
html-id: threat-model
question: What is the threat model for this attack? Who can run it?
---

Our attack requires the adversary to have network access to act as a man-in-the-middle attacker on the connection between the victim device's RADIUS client and RADIUS server.  When there are proxies, the attack can occur between any hop.
Our attacker will need to be able to act as a full network man-in-the-middle who can read, intercept, block, and modify inbound and outbound network packets.

Such access to RADIUS traffic may happen through different mechanisms. Although sending RADIUS/UDP over the open internet is discouraged, this is still known to [happen](https://www.ietf.org/archive/id/draft-ietf-radext-deprecating-radius-01.html) [in practice](https://www.rfc-editor.org/rfc/rfc6614). For internal network traffic, the attacker might initially compromise part of an enterprise network; such compromises appear frequently in [news reports](https://www.404media.co/cyber-official-speaks-out-reveals-mobile-network-attacks-in-u-s/) and [security advisories](https://www.cisa.gov/sites/default/files/2023-01/ar-16-20173.pdf).  Even if RADIUS traffic is confined to a protected part of an internal network, configuration or routing mistakes might unintentionally expose this traffic. An attacker with partial network access may be able to [exploit DHCP or other mechanisms to cause victim devices to send traffic outside of a dedicated VPN](https://www.leviathansecurity.com/blog/tunnelvision).

Our adversary does not know the shared secret between the RADIUS client and server.

