---
html-id: further-improvements
question: How can your attack time be further reduced?
---

We reduced the online running time for our MD5 chosen-prefix attack from hours down to minutes. However, this should be interpreted as a generous upper bound for the true cost of such collisions, because of the limits on our computational resources. Newer CPUs than the seven to ten year old machines we have access to would likely provide minutes of improvement, as would optimizing cache locality.

Access to more and faster GPUs for the chosen-prefix attack would reduce the time for the birthday stage and/or reduce the number of near-collision blocks, reducing time for the near-collision stage.

Reimplementing hashclash in hardware, for example on FPGAs (Field Programmable Gate Arrays) or ASICs (Application-Specific Integrated Circuits) would likely improve the running time by a factor of ten to a hundred.

It would be eminently feasible to run this attack on cloud resources.  Amazon EC2 lists the on-demand price of a `c7a.48xlarge` instance with 192 vCPUs at $9.85/hour, and the price of a `g6.48xlarge` instance with 192 vCPUs and 8 NVIDIA L4 GPUs at $13.35/hour.  It would cost around $50/hour to exceed our computing capacity, and in principle one could scale to many more machines.
