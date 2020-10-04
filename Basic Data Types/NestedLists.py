if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name,score))
        
    second_lowest=sorted(list(set([x[1] for x in students])))[1]
    second_students=sorted([s for s,g in students if g==second_lowest])
   
    for s in second_students:
        print(s)
