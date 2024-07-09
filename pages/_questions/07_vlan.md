---
html-id: vlan
question: Our RADIUS traffic is in a separate VLAN; are we secure against this attack?
---

A current best practice for RADIUS/UDP traffic is to expose it only to a restricted-access management VLAN within an organization.  While this reduces the attack surface and is certainly preferable to exposing UDP traffic to a broader network or the open internet, there may still be vulnerabilities in case of a network misconfiguration or attacker compromise of this portion of the network.

This approach is also at odds with the US Executive Branch Office of Management and Budget's [2022 memo](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf), which envisions moving to systems that do not rely on network separation for security: "A key tenet of a zero trust architecture is that no network is implicitly considered trusted".
