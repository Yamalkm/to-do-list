from sqlalchemy import Column, Integer, String, Boolean
import db

class Tarea(db.Base):
    __tablename__='tarea'
    __table_args__={'sqlite_autoincrement':True}
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    categoria = Column(String(200), nullable=False)
    fecha = Column(String(200), nullable=False)
    hecha = Column(Boolean)

    def __init__(self,contenido, categoria, fecha, hecha):
        self.contenido = contenido
        self.categoria = categoria
        self.fecha = fecha
        self.hecha = hecha
        print('Tarea creada con éxito')

    def __str__(self):
        return 'Tarea {}: {} :{} :{} ({})'.format(self.id, self.contenido,self.categoria, self.fecha, self.hecha)



