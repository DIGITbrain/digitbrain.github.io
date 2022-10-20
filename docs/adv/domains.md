# Dynamic Domain Names

Cloud instances deployed as part of a DIGITbrain application
can have FQDNs (fully qualified domain names) allocated to
them at provision time. All FQDNs will be a subdomain of:

> <big>cbp-routing.ch</big>

To take advantage of this feature, simply provide your desired
subdomain as a string in the deployment metadata when describing
your cloud instances. If you then, for example,
[expose a microservice](../expose) **externally** on that instance
on port 80, you can reach the service at:

> <big>http://<subdomain\>.cbp-routing.ch</big>

See the relevant field
[here](/attributes/deployment/#domain_name).