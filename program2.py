class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass

        def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    length = len(s)
    for i in range(length):
        current_val = roman_values[s[i]]
        if i + 1 < length and current_val < roman_values[s[i + 1]]:
            total -= current_val
        else:
            total += current_val
    return total
