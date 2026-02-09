class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        splited = address.split(".")
        return "[.]".join(splited)