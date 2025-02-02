class Solution(object):
    def isValid(self, s):
        self.pilha = ['A']
        self.casos = {'}': '{',
                      ']': '[',
                      ')': '('}
        
        for c in s:
            if c in '([{':
                self.pilha.append(c)
            elif self.casos[c] == self.pilha[-1]:
                self.pilha.pop()
            else:
                return False
            
        if self.pilha == ['A']:
            return True
        return False
        