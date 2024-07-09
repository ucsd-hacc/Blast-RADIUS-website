---
html-id: detect-compromise
question: Can I detect whether this attack was run on my network?
---

Yes, but you need log files of `Access-Rejects` on the RADIUS server and `Access-Accepts` on the RADIUS client.

If you have detailed log files on the RADIUS client that log the values of all attributes, you could look for suspicious `Proxy-State` attributes. If there are `Access-Accept` packets with `Proxy-State` attributes consisting of random bytes, then this might be a sign of an attack.  End clients should not receive packets with `Proxy-State` attributes.

To confirm an attack, you need would need to find the corresponding `Access-Reject` (or any other type) response packet in the RADIUS server logs, and verify that the server's response differs from the response received by the client, and that both contain valid `Response Authenticator` values for the request ID and `Request Authenticator`.

<!-- should we publish code to check this? -->

If both of these packets produce the same MD5 hash in the `Response Authenticator`, this issue was exploited in your system.
