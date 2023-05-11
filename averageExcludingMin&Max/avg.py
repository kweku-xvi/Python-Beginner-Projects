class Solution(object):
    def average_salary(self):
        salaries = list(map(int, input("Enter the salaries: ").strip().split()))
        salaries.sort()

        sum = 0

        for salary in salaries:
            sum += salary
        n = len(salaries)
        average = (sum - (salaries[0] + salaries[n - 1])) / (n - 2)
        print(f"The average salary excluding the maximum and minimum salary is {average}")
        


solution1 = Solution()
solution1.average_salary()
