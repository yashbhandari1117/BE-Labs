import numpy as np

class Perceptron:
    def __init__(self,W,lr=0.5,epochs=100):
        self.W=W
        self.lr=lr
        self.epochs=epochs
    def activation_fn(self,a):
        if(a>=0):return 1
        else:return 0
    def predict(self,W,x):
        y=np.dot(self.W,x)
        z=self.activation_fn(y)
        return z
    def fit(self,W,x,o):
        for j in range(self.epochs):
            for i in range(o.shape[0]):
                x1=np.insert(x[i],0,1)
                y=self.predict(self.W,x1)
                loss=o[i]-y
                self.W=self.W+(self.lr*loss*x1)
        return self.W
input_size=int(input("Enter input size:"))
w=np.zeros(np.array(input_size+1))

# For AND
X=np.array([[0,0],[0,1],[1,0],[1,1]])
Y=np.array([0,0,0,1])
p=Perceptron(w)
w1=p.fit(w,X,Y)
print("\nFor AND:-")
print("\nTrained Weights-",w1)
for i in range(4):
    x1=np.insert(X[i],0,1)
    O=p.predict(w1,x1)
    print("For input as: ",X[i],"Output: ",O)

#For OR
X=np.array([[0,0],[0,1],[1,0],[1,1]])
Y=np.array([0,1,1,1])
p1=Perceptron(w)
w1=p1.fit(w,X,Y)
print("\nFor OR:-")
print("\nTrained Weights-",w1)
for i in range(4):
    x1=np.insert(X[i],0,1)
    O=p1.predict(w1,x1)
    print("For input as: ",X[i],"Output: ",O)



            
    
    
