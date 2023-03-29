n = int(input())
arr = map(int, input().split())
score = []
for i in arr:
    score.append(i)
    score.sort(reverse = 1)
#to check if the count of max score in score list not more than 1
if score.count(max(score)) == 1:
    print(score[1])
#to check if the count of max score in score list more than 1
elif score.count(max(score)) > 1:
    set1 = set(score)
    set1.remove(max(set1))
    print(max(set1))