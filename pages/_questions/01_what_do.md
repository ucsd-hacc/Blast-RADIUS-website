---
html-id: what-do
question: What should I do about this issue?
---

If you are an end user, there is nothing that you can or should do.

If you are a system administrator, then consider the following questions:

1. Is all RADIUS traffic accounting, and only accounting?  Our attack does not seem to be practical in that setting.  You should still upgrade everything, but you can take your time.

2. Are all Access-Request packets sent over RADIUS/TLS (RadSec)?  The TLS should protect against our attack.  You should still upgrade everything, but you can take your time.

3. Are your RADIUS servers only doing EAP authentication, and no other kinds of authentication?  Our attack does not seem to be practical in that setting.  You should still upgrade everything, but you can take your time.

4. Are the RADIUS servers only handling local requests?  That is, no RADIUS servers in your network are doing proxying?  Upgrade your RADIUS servers first.  All server vendors have deployed a mitigation that includes a Message-Authenticator attribute as the first attribute of every response, which we believe mitigates our attack. You should still upgrade your NAS equipment/RADIUS clients, but this is less critical than updating servers immediately.

5. For everyone else, you should upgrade your RADIUS servers immediately, then upgrade clients/NAS equipment where possible, and set the configuration flags on both sides to require Message-Authenticator attributes.  The specific configuration is vendor-specific and you will need to consult your RADIUS vendor.

You can find other FAQs on the upgrade process [here](https://www.inkbridgenetworks.com/blastradius/faq).