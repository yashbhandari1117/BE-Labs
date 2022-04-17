def Union(X,Y):
    C={}
    for k in X.keys():
      if k in Y:
        C[k]=max(X[k],Y[k])
        Y[k]=-1
      else:
        C[k]=X[k]
    for k in Y.keys():
      if Y[k]!=-1:
        C[k]=Y[k]
    return C
def Intersection(X,Y):
    C={}
    for k in X.keys():
      if k in Y:
        C[k]=min(X[k],Y[k])
        Y[k]=-1
      else:
        C[k]=X[k]
    for k in Y.keys():
      if Y[k]!=-1:
        C[k]=Y[k]
    return C
def Difference(X,Y):
    C={}
    for k in X.keys():
      if k in Y:
        C[k]=min(X[k],1-Y[k])
        Y[k]=-1
      else:
        C[k]=X[k]
    for k in Y.keys():
      if Y[k]!=-1:
        C[k]=Y[k]
    return C
def Complement(X):
    C={}
    for k in X.keys():
        C[k]=1-X[k]
    return C
def Cartesian_Product(X,Y):
    C=list()
    for i in range(len(X)):
        for j in range(len(Y)):
            C.append([X[i],Y[j]])
    return C

A={"a":0.2, "b":0.45, "c":0.32, "d":0.12, "e":0.3}
B={"a":0.52, "b":0.5, "c":0.23, "d":0.6, "f":0.8}

print("Fuzzy set A ", A)
print("\nFuzzy set B ", B)

print("\nFuzzy Set Operations:-")
D=Union(A,B)
print("1]Union of Fuzzy set A and B: ", D)

A={"a":0.2, "b":0.45, "c":0.32, "d":0.12, "e":0.3}
B={"a":0.52, "b":0.5, "c":0.23, "d":0.6, "f":0.8}
D=Intersection(A,B)
print("\n2]Intersection of Fuzzy set A and B: ", D)

A={"a":0.2, "b":0.45, "c":0.32, "d":0.12, "e":0.3}
B={"a":0.52, "b":0.5, "c":0.23, "d":0.6, "f":0.8}
D=Difference(A,B)
print("\n3]Difference of Fuzzy set A and B: ", D)

A={"a":0.2, "b":0.45, "c":0.32, "d":0.12, "e":0.3}
B={"a":0.52, "b":0.5, "c":0.23, "d":0.6, "f":0.8}
D=Complement(A)
E=Complement(B)
print("\n4a]Complement of A: ",D)
print("4b]Complement of B: ",E)

# Cartesian Product of two fuzzy sets
A=[0.2,0.4,0.34,0.23,0.87]
B=[0.45,0.38,0.67]
D=Cartesian_Product(A,B)
print("\n5]Cartesian products: ",D)
