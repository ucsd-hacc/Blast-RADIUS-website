---
html-id: how-mitigate
question: How can we mitigate this attack in our system?
---

We recommend reading the [detailed guide for implementors](https://www.inkbridgenetworks.com/blastradius) published by Alan DeKok, the maintainer of FreeRADIUS.

Patches including the short-term mitigation described in the [mitigation section](#mitigation) will be available from major RADIUS implementations in coordinated release with this work; downstream vendors and network operators should check for and apply these patches.  Where an option exists to require a `Message-Authenticator` attribute on all packets, this option should be enabled.

Implementers, vendors, and admins should follow the guidance in this [IETF draft to deprecate insecure practices in RADIUS](https://datatracker.ietf.org/doc/draft-ietf-radext-deprecating-radius/) to mitigate numerous other attacks; we expect future versions to mandate `Message-Authenticator` attributes in more settings.

The long-term mitigation for our attack is to use RADIUS inside of a modern cryptographically protected transport like TLS 1.3.  The IETF RADEXT working group has existing [drafts in progress outlining RADIUS/(D)TLS](https://datatracker.ietf.org/doc/draft-ietf-radext-radiusdtls-bis/00/).
