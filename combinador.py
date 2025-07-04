resultadoFinal = []
A = int(input())
i = 0 
def combinar_strings(str1, str2):
    resultado = ""
    p = 0
    j = 0
    while p < len(str1) or j < len(str2):
        if p < len(str1):
            resultado += str1[p]
            p += 1
        if j < len(str2):
            resultado += str2[j]
            j += 1
    return resultado

while i < A:
    B, C = map(str, input().split())
    resultadoFinal.append(combinar_strings(B,C))
    i = i + 1

for i, r in enumerate(resultadoFinal, 1):
    print(r)