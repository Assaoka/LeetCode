class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        COR = image[sr][sc]
        LIN = len(image)
        COL = len(image[0])
        
        def aplicar_filtro(i, j):
            if i < 0 or i >= LIN: return
            if j < 0 or j >= COL: return
            if image[i][j] != COR: return
            
            image[i][j] = color         
            aplicar_filtro(i - 1, j)
            aplicar_filtro(i + 1, j)
            aplicar_filtro(i, j + 1)
            aplicar_filtro(i, j - 1)
        
        if COR != color: aplicar_filtro(sr, sc)
        return image        
