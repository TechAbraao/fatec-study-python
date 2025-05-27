# Atividades da Py Aula 02

A, B, C = 10, 15, 4
print(A < B and A < C or C != 0) # $ True

A, B, C = 10, 15, 4
print(A < B and (A < C or C != 0)) # $ True

A, B, C = 1, 9, 0
print(not (A >= 0 and B == C)) # $ True

A, B, C = 1, 9, 9
print(not (A >= 0) and not (B == C)) # $ False

A, B, C = 1, 9, 0
print((A >= 0 or B == C) and B > A) # $ True

A, B, C = -2, 0, 2
print(not (A <= B) or C > B) # $ True

A, B, C = -2, 0, 2
print(not (A <= B) or C > B) # $ True

A, B, C = 5, 0, 0
print(A == 0 and B != 0 and C == 0) # $ False

A, B, C = 5, 0, 0
print(A == 0 and B != 0 or C == 0) # $ True

