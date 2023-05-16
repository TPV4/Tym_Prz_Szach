class Partia:
    def __init__(self, pozycja):
        self.pozycja=[[pozycja[j][i] for i in range(8)] for j in range(8)]
    
    def __eq__(self, poprzednia):
        for i in range(8):
            for j in range(8):
                if self.pozycja[i][j]!=poprzednia.pozycja[i][j]:
                    return False
        return True
    
class Error(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.litera=args[0]

    def __str__(self) -> str:
        return f'w pliku wystepuje niepoprawny znak {self.litera}'
    
