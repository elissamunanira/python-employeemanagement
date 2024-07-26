import mysql.connector

def get_connection():
    
    return mysql.connector.connect(
        host='localhost', 
        user='root',   
        password='', 
        database='emsdb'  
    )

def create_table():
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255),
            role VARCHAR(255),
            gender VARCHAR(255),
            status VARCHAR(255)
        )
    ''')
    conn.commit()
    conn.close()

def fetch_employees():
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    
    return employees

def insert_employee(id, name, role, gender, status):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (id, name, role, gender, status) VALUES (%s, %s, %s, %s, %s)', 
                   (id, name, role, gender, status))
    conn.commit()
    conn.close()

def delete_employee(id):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = %s', (id,))
    conn.commit()
    conn.close()

def update_employee(new_name, new_role, new_gender, new_status, id):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET name = %s, role = %s, gender = %s, status = %s WHERE id = %s", (new_name, new_role, new_gender, new_status, id))
    conn.commit()
    conn.close()

def id_exists(id):
    
    conn = get_connection() 
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM employees WHERE id = %s", (id,))
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    return result[0] > 0


create_table()
