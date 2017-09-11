import math
def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    str = bin(num)[2:]
    return ~num + int(math.pow(2,len(str)))
