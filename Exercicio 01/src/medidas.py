
class Medida():
    def __init__(self,volume,lado):
        self.__lado = lado
        self.__volume = volume
    def get_volume(self) -> int:  
        return self.__volume 
    
    def get_lado(self) -> int:
        return self.__lado
    

        
        