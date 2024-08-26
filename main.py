from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.dialects import mysql

import db
from models import Tarea
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    todas_las_tareas= db.session.query(Tarea).all()
    #for i in todas_las_tareas:
        #print(i)
    return render_template("index.html",lista_de_tareas = todas_las_tareas)

@app.route("/p",methods= ["POST"])
def homes():
    todas_las_tareas= db.session.query(Tarea).all()
    #for i in todas_las_tareas:
        #print(i)
    return render_template("index.html",lista_de_tareas = todas_las_tareas)

@app.route("/crear-tarea", methods= ["POST"])
def crear():
    tarea = Tarea(contenido=request.form['contenido_tarea'], categoria=request.form['categoria_tarea'],
                  fecha= request.form['fecha_tarea'],hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect (url_for('home')) #Esto nos redirecciona a la funcion home()

@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id))
    tarea.delete()
    db.session.commit()
    return redirect (url_for('home'))

@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.hecha= not(tarea.hecha)
    db.session.commit()
    return redirect (url_for('home'))

@app.route('/editar-tarea/<id>')
def get_editar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    return render_template("editar.html", tarea=tarea)

@app.route('/modificar/<id>', methods =["POST"]) # aquí vale con poner POST solo, lo otro se me había colado
def modificar(id):
    tarea = db.session.query(Tarea).filter_by(id=id).first()
    #Modificación de la tarea en la base de datos
    tarea.contenido = request.form["editar-contenido"]
    tarea.categoria = request.form["editar-categoria"]
    tarea.fecha = request.form["editar-fecha"]
    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))

if __name__ == '__main__':
    #db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
