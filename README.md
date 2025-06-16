# is_valid_ipv4()
## Conditions
Given a string, return true if IP is a valid IPv4 address, or false if IP is not a correct IPv4.
A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros.
## Examples
| IP | Is Valid? |
| -------- | ---------- |
| 1.1.1.1.1 | False|
| 1.2 |  False |
| 1.234 | False |
| x.y.z.1 | False |
| 666.123.2.3 |  False |
| 1.01.2.0 |  False |
| -1.4.2.3 |  False |
| "" | False |
| 0 |  False |
| 192.168.0.1 |  True |
| 0.0.0.0|  True |
| 1.2.3.4 |  True |