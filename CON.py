import mysql.connector

conn = mysql.connector.connect(
    host="localhost",        
    user="root",             
    password="SIDHU@2006", 
    port=3306,
    database="giet2"  
)

cursor = conn.cursor()


def run_query(query, description):
    print(f"\n{description}")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

# 1. 
run_query("SELECT * FROM giet2;", "1. All data from giet2")

# 2. 
run_query("SELECT name FROM giet2;", "2. Only name column")

# 3. 
run_query("SELECT name, address FROM giet2;", "3. Name and address")

# 4. 
run_query("SELECT roll, salary FROM giet2;", "4. Roll and salary")

# 5. 
run_query("SELECT * FROM giet2 WHERE name='aman';", "5. Name = aman")

# 6. 
run_query("SELECT * FROM giet2 WHERE address='delhi';", "6. Address = delhi")

# 7.
run_query("SELECT * FROM giet2 WHERE gender='M';", "7. Gender = M")

# 8.
run_query("SELECT * FROM giet2 WHERE desig='doctor';", "8. Designation = doctor")

# 9. 
run_query("SELECT * FROM giet2 WHERE salary=15000;", "9. Salary = 15000")

# 10.
run_query("SELECT * FROM giet2 WHERE salary>20000;", "10. Salary > 20000")

# 11. 
run_query("SELECT * FROM giet2 WHERE salary<30000;", "11. Salary < 30000")

# 12.
run_query("SELECT * FROM giet2 WHERE gender='M' AND salary>20000;", "12. Male AND salary > 20000")

# 13. 
run_query("SELECT * FROM giet2 WHERE gender='F' OR address='raipur';", "13. Female OR address = raipur")

# 14. 
run_query("SELECT * FROM giet2 WHERE name LIKE 'a%';", "14. Name starts with 'a'")

# 15. 
run_query("SELECT * FROM giet2 WHERE name LIKE '%h';", "15. Name ends with 'h'")

# 16. 
run_query("SELECT * FROM giet2 WHERE address LIKE '%pur%';", "16. Address contains 'pur'")

# 17.
run_query("SELECT * FROM giet2 ORDER BY name ASC;", "17. Sorted by name ASC")

# 18. 
run_query("SELECT * FROM giet2 ORDER BY salary DESC;", "18. Sorted by salary DESC")

# 19. 
run_query("SELECT COUNT(*) FROM giet2;", "19. Total employees")

# 20. 
run_query("SELECT COUNT(*) FROM giet2 WHERE gender='M';", "20. Count male employees")


cursor.close()
conn.close()
