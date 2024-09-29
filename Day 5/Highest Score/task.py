student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#finds the top score in a list, prints that top score
# highest_score = max(student_scores)
# print(highest_score)

#manual 'for loop' of the function max()
top_score = 0
for score in student_scores:
    if score > top_score:
        top_score = score

print(top_score)