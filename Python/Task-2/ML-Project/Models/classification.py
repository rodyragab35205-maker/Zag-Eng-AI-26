class KNNModel:
    def train(self, X, y):
        self.X = X
        self.y = y
    def predict(self, X):
        return X