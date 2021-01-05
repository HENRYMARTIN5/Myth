def deep_index(lst, w):
    return [[i, sub.index(w)] for (i, sub) in enumerate(lst) if w in sub]
class variable():
    def __init__(self, name, val):
        self.name = name
        self.val = val
class variableHandler():
    def __init__(self):
        self.varList = []
    def create(self, varName, varVal):
        inList = False
        for var in self.varList:
            if var.name == varName:
                inList = True
        if not inList:
            var = variable(varName, varVal)
            self.varList.append(var)
            return var
        else:
            for var in self.varList:
                if var.name == varName:
                    var.val = varVal
            return variable(varName, varVal)
    def get(self, varName):
        for var in self.varList:
            if var.name == varName:
                return var.val
        return None
varHandler = variableHandler()