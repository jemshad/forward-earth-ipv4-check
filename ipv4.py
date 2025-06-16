# Given a string, return true if IP is a valid IPv4 address, or false if IP is not a correct IPv4.
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain
# leading zeros.
# For example, "192.168.1.1" and "192.168.10" are valid IPv4 addresses.

def is_valid_ipv4(ip:str) -> bool:
    if not isinstance(ip, str):
        return False

    # do we have 4 parts?
    parts = ip.split(".")
    if len(parts) != 4:
       return False

    for p in parts:
        # are all digits?
        if not p.isdecimal():
            return False

        # more than 1 character and starts with 0?
        if len(p) > 1 and p.startswith("0"):
            return False

        # are they in the range 0 - 255?
        if int(p) < 0 or int(p) > 255:
            return False

    return True

## tests
def test_is_valid_ipv4():
    testdata = [
        ["1.1.1.1.1", False],
        ["1.2", False],
        ["1.2.3.4", True],
        [1.234, False ],
        ["x.y.z.1", False],
        ["666.123.2.3", False],
        ["0.0.0.0", True],
        ["1.01.2.0", False],
        ["-1.4.2.3", False],
        ["", False],
        [0, False],
        ["192.168.0.1", True]
    ]

    for t in testdata:
        assert is_valid_ipv4(t[0]) == t[1]
