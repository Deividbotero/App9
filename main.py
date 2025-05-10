from flask import Flask, jsonify
import sqlite3
from models import init_db

app = Flask(__name__)

init_db()


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return '✅ Bienvenido al sistema de notas de estudiantes'


@app.route('/notas')
def notas_colectivas():
    conn = get_db_connection()
    notas = conn.execute('''
        SELECT e.nombre, n.nota
        FROM estudiantes e
        JOIN notas n ON e.id = n.estudiante_id
        ORDER BY e.nombre
    ''').fetchall()
    conn.close()

    return jsonify([dict(nota) for nota in notas])


@app.route('/notas/<nombre>')
def nota_estudiante(nombre):
    conn = get_db_connection()
    notas = conn.execute(
        '''
        SELECT e.nombre, n.nota
        FROM estudiantes e
        JOIN notas n ON e.id = n.estudiante_id
        WHERE e.nombre = ?
    ''', (nombre, )).fetchall()
    conn.close()

    if notas:
        return jsonify([dict(nota) for nota in notas])
    else:
        return jsonify({'error': f'Estudiante "{nombre}" no encontrado'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
