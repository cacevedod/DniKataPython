class Dni:

    tabla = {
        "0": "T",
        "1": "R",
        "2": "W",
        "3": "A",
        "4": "G",
        "5": "M",
        "6": "Y",
        "7": "F",
        "8": "P",
        "9": "D",
        "10": "X",
        "11": "B",
        "12": "N",
        "13": "J",
        "14": "Z",
        "15": "S",
        "16": "Q",
        "17": "V",
        "18": "H",
        "19": "L",
        "20": "C",
        "21": "K",
        "22": "E",
    }

    def construir(self, dniEntrada):
        if (len(dniEntrada)!=9):
            return False
        
        dniList = list(dniEntrada.strip())
        sumDni = 0
        for i in range(len(dniList)-1):
            sumDni = sumDni + int(dniList[i])
        
        modulo = sumDni % 23
        
        tmp = dniList[len(dniList)-1]
        
        if (tmp!= self.tabla[str(modulo)]):
            return False

        return True