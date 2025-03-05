class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Reverse iterate and multiply digit by digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1

                # Add to result and carry over if needed
                total = product + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        # Convert result array to string, skipping leading zeros
        result_str = "".join(map(str, result)).lstrip("0")
        
        return result_str if result_str else "0"
