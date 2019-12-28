# CTF-416
The notebook

## RSA
**RsaCtfTool**: https://github.com/Ganapati/RsaCtfTool

## Web
`.` transforms to `_` in php, can bypass `preg_match("/_| /i", $var)`.

**dnsrecon** can be used to find flag hidden in DNS records.

**webshell**: `"$_=" + make_letters("echoFlag") + ";$_();"` where `echoFlag` is the function to execute in server.
