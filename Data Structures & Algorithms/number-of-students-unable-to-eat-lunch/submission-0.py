class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)

        count = Counter(students) # Count each occurence of students in the array and put into hashmap

        # Go through each sandwich in order
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                result -= 1
                count[sandwich] -= 1
            else:
                return result

        return result
        