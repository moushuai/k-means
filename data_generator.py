import numpy as np


class DataGenerator:
    def __init__(self, obj_num, obj_dim, cls_num, discrete=False, supervised=False):
        assert obj_dim < cls_num
        self.obj_num = obj_num
        self.obj_dim = obj_dim
        self.cls_num = cls_num
        self.discrete = discrete
        self.supervised = supervised

    def generate_data(self):
        if self.discrete:
            pass
        else:
            X = None
            for i in range(self.cls_num):
                # Generate the random matrix with [0,1] scale
                X_i = np.random.random(size=(int(round(self.obj_num/self.cls_num)), self.obj_dim))
                # Add bias to each element of random matrix
                bias = [2.*(i+1) for _ in range(int(round(self.obj_num/self.cls_num)) * self.obj_dim)]
                bias = np.reshape(bias, (int(round(self.obj_num/self.cls_num)), self.obj_dim))
                X_i = X_i + bias
                # whether supervised data or not
                if self.supervised:
                    Y_i = [[i] for _ in range(int(round(self.obj_num/self.cls_num)))]
                    X_i = np.column_stack((X_i, Y_i))
                if X is None:
                    X = X_i
                else:
                    X = np.row_stack((X, X_i))
            np.random.shuffle(X)
            return X

