class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        initial=len(students)
        c=0
        count=0
        while(len(students)!=0):
            print(sandwiches)
            print()
            if c==len(students):
                break
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count+=1
                c=0
            else:
                a=students.pop(0)
                students.append(a)
                c+=1    
        return len(students)      
             