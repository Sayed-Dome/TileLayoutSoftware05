class CuttingOptimization:
    def __init__(self):
        self.cutting_optimization = []

    def add_cut(self, cut):
        self.cutting_optimization.append(cut)

    def remove_cut(self, cut):
        self.cutting_optimization.remove(cut)

    def get_cutting_optimization(self):
        return self.cutting_optimization

class MinimizeWaste(CuttingOptimization):
    def __init__(self):
        super().__init__()

    def add_cut(self, cut):
        if len(self.cutting_optimization) % 2 == 0:
            self.cutting_optimization.append(cut)
        else:
            self.cutting_optimization.insert(0, cut)

class MaximizeYield(CuttingOptimization):
    def __init__(self):
        super().__init__()

    def add_cut(self, cut):
        if len(self.cutting_optimization) % 2 == 0:
            self.cutting_optimization.append(cut)
        else:
            self.cutting_optimization.insert(0, cut)
