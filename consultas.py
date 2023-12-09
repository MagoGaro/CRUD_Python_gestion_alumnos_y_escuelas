import sqlite3

class consultas_db:
    
    def conectar(self):
    
        conexion = sqlite3.connect("mi_db.db")
        return conexion

    def buscar_escuelas(self):
        
        try:
             cone=self.conectar()
             cur=cone.cursor()
             sql="SELECT nombre FROM escuelas"
             cur.execute(sql)
             resultado =cur.fetchall()
             retorno = []
             for e in resultado:
                esc = e[0]
                retorno.append(esc)
             cone.close()
             return retorno
        finally:
            cone.close()
    
    def buscar_localidades(self):
        
        try:
             cone=self.conectar()
             cur=cone.cursor()
             sql="SELECT nombre FROM localidad"
             cur.execute(sql)
             resultado =cur.fetchall()
             retorno = []
             for e in resultado:
                esc = e[0]
                retorno.append(esc)
             cone.close()
             return retorno
        finally:
            cone.close()
    
    def buscar_provincias(self):
        
        try:
             cone=self.conectar()
             cur=cone.cursor()
             sql="SELECT nombre FROM provincia"
             cur.execute(sql)
             resultado =cur.fetchall()
             retorno = []
             for e in resultado:
                esc = e[0]
                retorno.append(esc)
             cone.close()
             return retorno
        finally:
            cone.close()
            
    def buscar_alumno(self,datos):
            
            try:
                cone=self.conectar()
                cur=cone.cursor()
                query_leer = f'''SELECT a.legajo, a.nombre,a.apellido, a.promedio, a.email, a.grado, 
                e.nombre, p.nombre, a.genero FROM alumnos AS a
                INNER JOIN escuelas AS e ON a.id_escuela = e._id
                INNER JOIN provincia AS p ON a.id_provincia = p.id_provincia
                WHERE a.legajo={int(datos)}'''
                cur.execute(query_leer)
                return cur.fetchall()
                
            finally:
                cone.close()
    
    def alta_alumno(self,datos):
    
        cone = self.conectar()
        cur = cone.cursor()
        cur.execute(f'SELECT _id FROM escuelas WHERE nombre = "{datos[0]}"')
        id_escuela = cur.fetchall()
        cur.execute(f'SELECT id_provincia FROM provincia WHERE nombre = "{datos[8]}"')
        id_provincia = cur.fetchall()
        
        sql = f'INSERT INTO alumnos (id_escuela, legajo, nombre, apellido, promedio,grado, email, genero,id_provincia) VALUES ({id_escuela[0][0]}, {datos[1]}, "{datos[2]}", "{datos[3]}", {datos[4]}, {datos[5]},"{datos[6]}","{datos[7]}",{id_provincia[0][0]})'
        
        cur.execute(sql)
        cone.commit()
        cone.close()
        
    def actualizar_alumno(self,datos):
    
        cone = self.conectar()
        cur = cone.cursor()
        cur.execute(f'SELECT _id FROM escuelas WHERE nombre = "{datos[0]}"')
        id_escuela = cur.fetchall()
        cur.execute(f'SELECT id_provincia FROM provincia WHERE nombre = "{datos[8]}"')
        id_provincia = cur.fetchall()
        print("hasta aca llego")
        sql = f'UPDATE alumnos SET id_escuela = {id_escuela[0][0]}, nombre = "{datos[2]}", apellido = "{datos[3]}", promedio = {datos[4]},grado = {datos[5]}, email = "{datos[6]}", genero = "{datos[7]}",id_provincia = {id_provincia[0][0]} WHERE legajo = {datos[1]}'
        print(sql)
        cur.execute(sql)
        cone.commit()
        cone.close()
        
    def baja_alumno(self,datos):
        try:
            cone=self.conectar()
            cursor=cone.cursor()
            sql=f"DELETE from alumnos where legajo={datos}"
            cursor.execute(sql)
            cone.commit()
            cone.close()
        except:
            cone.close()