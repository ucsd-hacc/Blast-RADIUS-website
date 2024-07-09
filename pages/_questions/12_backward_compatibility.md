---
html-id: backward-compatibility
question: Are your recommended mitigations backward compatible?
---

It depends.

Including a `Message-Authenticator` attribute in every packet is backward compatible.  Unfortunately, requiring the presence of a `Message-Authenticator` attribute in requests and responses may not be backward compatible with old client or server implementations that do not have the option to include them.

Our long-term mitigation of moving to RADIUS/TLS requires clients and servers that support TLS, as well as new configuration (like PKI) on the part of network operators.  TLS may not be supported at all on older hardware.