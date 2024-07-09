---
html-id: practicality
question: Is your attack practical?
---

Yes and no.  In the proof-of-concept attacks described in our paper,
it took us 3 to 6 minutes to compute the MD5 chosen-prefix hash collision
required for the attack.  This is longer than the 30- to 60-second
timeouts that are commonly used in practice for RADIUS.

However, every step of the collision algorithm parallelizes well and
is amenable to hardware optimization, so we expect a well-resourced
attacker could obtain running times that are tens or hundreds of times faster
by implementing the attack on GPUs, FPGAs, or hardware.

Our reported running times are from optimizing some 15 year old code
and running it on a bunch of 7 to 10 year old CPUs, because this is
what we have access to.  We did not think that spending further
engineering effort to make MD5 collisions faster was a good use of
time when MD5 should have been abolished 20 years ago.
