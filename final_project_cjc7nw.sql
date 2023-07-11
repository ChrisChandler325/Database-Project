CREATE view EmployeesPerRegion AS
SELECT r.region_name, COUNT(e.employee_id) AS "NumberofEmployees"
FROM regions r,employees e, departments d, locations l, countries c
WHERE e.department_id = d.department_id AND d.location_id = l.location_id AND l.country_id = c.country_id AND c.region_id = r.region_id
GROUP BY region_name;

SELECT * FROM EmployeesPerRegion WHERE region_name = "Americas";

CREATE view managers AS
SELECT e.first_name,e.last_Name,e.phone_number,e.email,j.job_title,d.department_name
FROM employees e, jobs j, departments d
WHERE e.department_id = d.department_id AND e.job_id = j.job_id AND e.employee_id IN (SELECT manager_id FROM employees);

SELECT department_name, COUNT(email) FROM managers GROUP BY department_name;

CREATE view DependentsByDepartment AS
SELECT b.department_name,COUNT(a.dependent_id) as "NumOfDependents"
FROM dependents a, employees e, departments b
WHERE e.employee_id=a.employee_id AND e.department_id = b.department_id
GROUP BY e.department_id;

SELECT department_name,NumOfDependents FROM DependentsByDepartment WHERE NumOfDependents = (SELECT MAX(NumOfDependents)FROM DependentsByDepartment); 

CREATE view HiresByYear AS
SELECT YEAR(hire_date) AS "Year", COUNT(employee_id)
FROM employees
GROUP BY YEAR(hire_date);

SELECT * FROM HiresByYear WHERE year = '1997';

CREATE view SalaryByDepartment AS
SELECT d.department_name, SUM(e.salary) AS "Total_Salary"
FROM employees e, departments d
WHERE e.department_id = d.department_id
GROUP BY d.department_name; 

SELECT * FROM SalaryByDepartment WHERE department_name = "Finance";

CREATE view SalaryByJobTitle AS
SELECT j.job_title, SUM(e.salary) AS "Total_Salary"
FROM employees e, jobs j
WHERE e.job_id = j.job_id
GROUP BY job_title;

SELECT * FROM SalaryByJobTitle WHERE Total_Salary = (SELECT MAX(Total_Salary) FROM SalaryByJobTitle);

CREATE view EmployeeDependents AS
SELECT e.first_name,e.last_Name,e.email,e.phone_number,COUNT(d.dependent_id) AS "NumOfDependents"
FROM employees e
LEFT JOIN dependents d
ON e.employee_id = d.employee_id
GROUP BY e.employee_id;

SELECT * FROM EmployeeDependents WHERE NumOfDependents = 0;

CREATE view CountryLocation AS
SELECT c.country_name, COUNT(d.department_id) AS "NumOfLocations"
FROM countries c
LEFT JOIN locations l
ON l.country_id = c.country_id
LEFT JOIN departments d
ON d.location_id = l.location_id
GROUP BY c.country_id;

SELECT * FROM CountryLocation WHERE NumOfLocations = 0;