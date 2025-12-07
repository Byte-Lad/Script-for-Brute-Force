# Script-for-Brute-Force

This project began as an exercise based on old python2 code. The rewrite was note simply a matter of changing the syntax dealing
with legacy libraries and different behavior between versions presented several challenges due to the simple fact that the urllib2
library is no longer available for Python3. The module was completely restructured, so i had to figure out how to use it correctly.

Now, talking a little more about the tool, it reads a wordlist, builds possible paths, and performs HTTP requests to identify
which endpoint exist or return valid response.

Finally, it is worth mentioning that most of the code in this repository has been rewritten for Python3. If you want to compare
it with the original version or udenstand the context from which they emerged, i strongly recommend reading the book "Black Hat Python", where these examples appear in their original form.
