class Solution(object):
    def average_salary(self):
        salary = list(map(int, input("Enter the salaries: ").strip().split()))
        salary.sort()

        counter = 0
        sum = 0.00

        #finding the sum
        for i in range(len(salary)):
            if i == 0 or i == len(salary) - 1:
                pass
            else:
                sum += salary[i]
                counter += 1
        
        averageSalary = sum / counter
        
        print(f"The average salary excluding the maximum and minimum salary is {averageSalary}")


solution1 = Solution()
solution1.average_salary()
