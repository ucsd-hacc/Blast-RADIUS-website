---
html-id: bad-mitigations
question: I have a different idea for a mitigation that I think works better.
---

A number of tempting, commonly suggested countermeasures do not sufficiently mitigate the vulnerability.

### Decreasing Timeouts

It is tempting to hope that simply setting a shorter client timeout would mitigate our attack.  We believe this should not be done: it decreases usability and does not protect against our attack.

Our MD5 collisions were computed after applying some optimizations to a 15-year-old proof-of-concept codebase, which we are running on CPUs mostly dating from seven to ten years ago, because these are the resources we have access to.  An adversary with a budget for professional engineering would be able to decrease the computational cost of the collision by a factor of tens to hundreds.

The most common timeout in practice is 30 seconds, and 60 seconds is commonly recommended when multifactor authentication is involved, since shorter timeouts could be problematic for real users.

### Using TACACS+ or Diameter

RADIUS is not the only protocol to suffer from the types of security issues that we outline.  TACACS+ is a popular (TCP-based) administrator login protocol for switches that also does not meet modern cryptographic security standards.  [RFC 8907](https://www.rfc-editor.org/info/rfc8907) was published in September 2020, and explicitly mandates that TACACS+ be used with a secure transport.
However, much like RADIUS, however, TACACS+ is still most commonly used over insecure transports.

Diameter ([RFC 6733](https://www.rfc-editor.org/info/rfc6733)) was initially designed as a successor to RADIUS, although it never replaced RADIUS for many common use cases.  It is used in 3G+ networks, and is generally only supported in large NAS equipment used by bigger ISPs and telecommunications providers; consumer or enterprise-grade equipment typically only supports RADIUS.  
Although Diameter was intended to replace RADIUS, the protocol itself offers no security when used over TCP.  As a result, RFC 6733 suggests that Diameter messages should be secured using TLS or DTLS; 5G has replaced Diameter with signaling over HTTP/2. The US government [has described exploits](https://www.404media.co/cyber-official-speaks-out-reveals-mobile-network-attacks-in-u-s/) against Diameter targeting mobile users.

### Random shared secrets

Organizations can protect against dictionary attacks on the shared secret by picking random shared secrets of sufficient length, as the runtime of such an attack grows exponentially with the entropy of the secret. For example, [this work-in-progress IETF draft](https://datatracker.ietf.org/doc/draft-ietf-radext-deprecating-radius/00/) recommends shared secrets with at least 96 bits of entropy, so an offline dictionary attack would involve on the order of $$2^{96}$$ MD5 compressions. However, as our attack does not try to brute force the shared secret, choosing a strong shared secret does not affect the runtime of our attack.

### Using Multi-Factor Authentication (MFA)

Using MFA or 2FA is not a mitigation either. Our attack largely bypasses the user authentication mechanism, and forges the accept response from the server's reject.  MFA may be supported through multiple mechanisms within the RADIUS protocol, including authentication protocols like PAP that are vulnerable by default to our attack.

### Rejecting Proxy-States

Our forged Access-Accept packets contain `Proxy-State` attributes that the client is not expecting. However, having the client discard packets with unexpected `Proxy-States` does not mitigate the vulnerability.  First, such a mitigation would only apply to a NAS; the `Proxy-State` attribute is actually used by RADIUS server proxies and thus difficult to remove without breaking functionality.

Even if NAS clients rejected unexpected `Proxy-State` attributes, it would be possible to craft colliding packets where the `Access-Accept` has the collision gibberish in a different attribute such as `Vendor-Specific` or `Reply-Message` that is likely to be accepted; the client does not need to support or attempt to interpret the garbage attribute to be vulnerable.

The colliding `Access-Reject` packet would still use `Proxy-State` attributes, as the server is guaranteed to include `Proxy-State` attributes unchanged in an `Access-Reject`.
For simplicity our implementation uses `Proxy-States` in both colliding packets, as no RADIUS client we tested complained about the unexpected `Proxy-State`.

### Replacing MD5

It is tempting to think that simply replacing MD5 in the `Response Authenticator` with a secure hash function like SHA-2 or SHA-3 might be a short-term mitigation against our attacks.  However, since the RADIUS protocol does not provide for any cryptographic agility, such a change would be incompatible with all existing implementations, and thus be equivalent to requiring a new protocol.  Given the other security and privacy concerns with the rest of RADIUS, it would be better at that point to redesign the entire protocol or transport.
