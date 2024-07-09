---
html-id: whos-affected
question: Who is affected by these vulnerabilities?
---

Nearly all RADIUS/UDP implementations are vulnerable to our protocol attack when using non-EAP authentication methods.  RADIUS is used by many organizations to control access to a wide variety of network devices and services.  Our attack requires man-in-the-middle network access; organizations should evaluate their own network security threat model.

RADIUS implementers, vendors, and system administrators should follow [best practices](https://datatracker.ietf.org/doc/draft-ietf-radext-deprecating-radius/) and [the guidance in this document](https://www.inkbridgenetworks.com/blastradius).  Our attack does not compromise end user credentials, and there is nothing that end users can do to protect against this attack.  

EAP authentication methods are protected against our attack because [RFC 2869](https://datatracker.ietf.org/doc/html/rfc2869) mandates that a `Message-Authenticator` attribute must be present, and this attribute is an HMAC-MD5 over the entire packet that we cannot forge. A theoretical protocol vulnerability appears to exist, but may not be practically exploitable.  RADIUS Accounting also appears to be affected by a theoretical protocol vulnerability that seems to be difficult to exploit in practice.


