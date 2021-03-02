# Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if
# IP is not a correct IP of any type.
#
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros.
#
# For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and
#     "192.168@1.1" are invalid IPv4 addresses.
#
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
#
# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English
# letters ('A' to 'F').
#
# Leading zeros are allowed in xi.
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses,
# while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

class Solution:
    def validIPAddress(self, ip):

        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        valid_hex = 'abcdefABCDEF0123456789'

        if ip.count('.') == 3:

            ip_list = ip.split('.')

            if len(ip_list) != 4:
                return 'Neither'

            for i in ip_list:

                if len(i) == 0:
                    return 'Neither'

                for j in i:
                    if j in alpha:
                        return 'Neither'

                if int(i) == 0 and len(i) > 1:
                    return 'Neither'

                if int(i) < 0 or int(i) > 255:
                    return 'Neither'

                if int(i) > 0:
                    if i[0] == '0':
                        return 'Neither'

            return 'IPv4'


        elif ip.count(':') == 7:

            ip_list = ip.split(':')

            if len(ip_list) != 8:
                return 'Neither'

            for value in ip_list:

                if len(value) > 4 or len(value) == 0:
                    return 'Neither'

                for char in value:

                    if char not in valid_hex:
                        return 'Neither'

            return 'IPv6'


        else:
            return 'Neither'
