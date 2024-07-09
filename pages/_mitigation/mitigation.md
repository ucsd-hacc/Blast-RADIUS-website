---
title: Mitigation 
html-id: mitigation
---

Network administrators and vendors should follow the guidance given in this [white paper](https://www.inkbridgenetworks.com/blastradius) authored by Alan DeKok of FreeRADIUS.

Our recommended short-term mitigation for implementers and vendors is to mandate that clients and servers always send and require `Message-Authenticator` attributes for _all_ requests and responses. For `Access-Accept` or `Access-Reject` responses, the `Message-Authenticator` should be included as the _first_ attribute. Patches implementing this mitigation have been implemented by all RADIUS implementations that we are aware of.  This guidance is being put into an upcoming [RADIUS RFC](https://datatracker.ietf.org/doc/draft-ietf-radext-deprecating-radius/).

The long-term mitigation is to use RADIUS inside of an encrypted and authenticated channel that offers modern cryptographic security guarantees. The IETF has begun work to standardize [RADIUS over (D)TLS](https://datatracker.ietf.org/doc/draft-ietf-radext-radiusdtls-bis/).