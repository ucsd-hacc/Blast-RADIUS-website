---
html-id: eap-tls
question: Is using RADIUS with EAP-TLS the same as RADIUS/TLS?  Is EAP-TLS vulnerable?
---

EAP-TLS is not the same as RADIUS/TLS. EAP-TLS uses a TLS handshake to carry out certificate-based authentication, but does not use TLS to encrypt the RADIUS access request and response packets, which are still transmitted over UDP in the clear. This is different from RADIUS/TLS, which transmits all RADIUS packets inside of an encrypted TLS session.  

In more detail, when EAP (Extensible Authentication Protocol) is used for authentication within RADIUS, the client NAS sends a RADIUS `Access-Request` packet to the RADIUS server that contains a RADIUS attribute called `EAP-Message`.  For RADIUS/UDP, this `Access-Request` is sent in the clear via UDP.  The authenticating peer and server then authenticate using the requested EAP method: for EAP-TLS, they use certificates to complete a TLS handshake.  After the end of the EAP authentication process, the server completes the RADIUS conversation by sending a RADIUS `Access-Accept` or `Access-Reject` packet; for RADIUS/UDP this packet is again sent in the clear over UDP.

Our attack targets RADIUS access requests and responses.  However, EAP-TLS does not appear to be practically exploitable by our attack because all packets containing `EAP-Message` attributes must contain a MD5-HMAC `Message-Authenticator` attribute that we cannot forge.  However, a theoretical protocol attack may still be possible against RADIUS even when clients make an EAP-TLS (or other EAP) authentication request.  The details and the impact of such an attack would be implementation-dependent and we have not found a practically exploitable implementation.

A more detailed explanation is in Section 5.6 of [our paper](/pdf/radius.pdf).
