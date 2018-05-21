##########################use recursive#################################
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits)==0:
            return [1]
        lst = digits[len(digits)-1]
        lst += 1
        if lst == 10:
            lst = 0
            digits = self.plusOne(digits[:len(digits)-1])
            digits.append(lst)
        else:
            digits[len(digits)-1] = lst
            
        return digits
        
        
############################use for loop####################################3
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1 , -1, -1):
            num = digits[i]+carry
            if num == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0
                break
                
        
        if carry ==1:
            digits.insert(0, 1)
        
        return digits
