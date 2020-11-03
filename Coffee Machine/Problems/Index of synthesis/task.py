index_of_synthesis = float(input())

if index_of_synthesis > 3.0:
    type_of_language = "Polysynthetic"
elif index_of_synthesis < 2.0:
    type_of_language = "Analytic"
else:
    type_of_language = "Synthetic"

print(type_of_language)
