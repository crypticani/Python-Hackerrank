# Python program to get average of a list 
def Average(num): 
    return sum(num) / len(num) 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    average = Average(query_scores)
    print(format(average,'.2f'))
