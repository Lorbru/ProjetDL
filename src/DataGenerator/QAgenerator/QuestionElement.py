import numpy as np
import json

class QuestionElement():
    
    def __init__(self, count:int, shape:str, color:str):

        with open('src/DataGenerator/QAgenerator/grammar.json', 'r') as f:
            self.grammar = json.load(f)
        
        self.count = count                       
        self.shape = shape    
        self.color = color  

    def printObject(self, indet=False):

        genre = self.grammar["shape"][self.shape]["genre"]
        if indet : 
            shape = self.grammar["shape"][self.shape]["indet"]
            clr = self.grammar["color"][self.color][genre + "P"]
            return shape + " " + clr
        else : 
            num = self.grammar["cardinal"][genre][self.count]
            if self.count != 1 : 
                shape = self.grammar["shape"][self.shape]["plural"]
                clr = self.grammar["color"][self.color][genre + "P"]
            else :
                shape = self.grammar["shape"][self.shape]["singul"]
                clr = self.grammar["color"][self.color][genre]
            return num + " " + shape + " " + clr

    @staticmethod
    def randomElement() :

        rd_count = np.random.randint(0, 10)
        rd_shape = np.random.choice(["etoile", "ellipse", "rectangle", "triangle"])
        rd_clr = np.random.choice(["red", "green", "blue", "white"])
        
        return QuestionElement(rd_count, rd_shape, rd_clr)