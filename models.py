import sqlite3


def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER,
            nota REAL,
            FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id)
        )
    ''')

    c.execute("SELECT COUNT(*) FROM estudiantes")
    if c.fetchone()[0] == 0:
        nombres = [
            'Ana', 'Luis', 'Carlos', 'María', 'Pedro', 'Laura', 'Andrés',
            'Sofía', 'Mateo', 'Valentina', 'Daniel', 'Camila', 'Julián',
            'Isabella', 'Sebastián', 'Martina', 'Diego', 'Lucía', 'Tomás',
            'Paula', 'Juan', 'Sara', 'David', 'Nicole', 'Felipe', 'Antonia',
            'Emilio', 'Renata', 'Esteban', 'Emma', 'Gabriel', 'Alejandra',
            'Simón', 'Mía', 'Ricardo', 'Victoria', 'Rodrigo', 'Josefa',
            'Cristóbal', 'Florencia', 'Ignacio', 'Elena', 'Benjamín',
            'Catalina', 'Maximiliano', 'Fernanda', 'Joaquín', 'Manuela',
            'Agustín', 'Julieta'
        ]
        notas = [
            85.5, 78.0, 92.3, 88.4, 73.0, 95.6, 81.2, 67.4, 90.0, 76.5, 82.1,
            89.7, 91.2, 77.3, 80.0, 85.0, 79.5, 84.3, 69.2, 93.1, 87.5, 74.6,
            66.0, 82.9, 88.0, 91.5, 83.7, 72.5, 76.3, 94.2, 89.0, 86.8, 75.4,
            92.0, 70.5, 78.6, 81.9, 80.5, 85.8, 69.9, 73.4, 90.5, 88.2, 67.9,
            86.4, 77.7, 84.1, 79.0, 68.8, 91.9
        ]

        for i in range(50):
            c.execute("INSERT INTO estudiantes (nombre) VALUES (?)",
                      (nombres[i], ))
            estudiante_id = c.lastrowid
            c.execute("INSERT INTO notas (estudiante_id, nota) VALUES (?, ?)",
                      (estudiante_id, notas[i]))

    conn.commit()
    conn.close()
