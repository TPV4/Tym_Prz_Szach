class Partia:
    def __init__(self, pozycja):
        self.pozycja=[[pozycja[j][i] for i in range(8)] for j in range(8)]
    
    def __eq__(self, poprzednia):
        for i in range(8):
            for j in range(8):
                if self.pozycja[i][j]!=poprzednia.pozycja[i][j]:
                    return False
        return True
        