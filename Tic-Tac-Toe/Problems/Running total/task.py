print(list('15325'))
sequence = list('15325')
print([sequence[i-1] + sequence[i] for i in range(1, len(sequence))])
[sequence[i] for i in range(len(sequence))]
