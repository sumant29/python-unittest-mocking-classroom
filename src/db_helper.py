import pandas as pd

info = [['Aman',10000],['Raman',20000],['Chaman',30000]]
df = pd.DataFrame(info,columns = ['Empl_Name','Salary'])
class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        return df['Salary'].max()

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        return df['Salary'].min()

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
