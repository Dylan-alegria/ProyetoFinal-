import mysql.connector 

conn=mysql.connector.connect(user="root", password='', host='localhost', port='3306',db='verduleros')



cursor = conn.cursor()



def seeP():# se imprimen los productos 
            sentencia= 'SELECT * FROM productos '
            cursor.execute(sentencia)
            registro= cursor.fetchall()
            print(registro)
     
    
def addP(a,b,c):# se agregan producto 
        sentecia= 'INSERT INTO productos(nomProducto,idGrupo,precio)VALUES(%s,%s,%s)'
        valores=(a,b,c)
        cursor.execute(sentecia, valores)
        conn.commit()
        
    


def updateP(name,idG, precio,idP): # se actualizan productos 
        sentecia= 'UPDATE productos SET nomProducto=%s, idGrupo=%s ,precio=%s Where idProducto =%s'
        valores=(name,idG, precio,idP)
        cursor.execute(sentecia, valores)
        conn.commit()
       
              
def deleteP(a):#  se borra un dato  de la tabla productos 
        sentecia= 'DELETE FROM productos WHERE idProducto = %s '
        valores=(a,)
        cursor.execute(sentecia, valores)
        conn.commit()

#-------------------------------------------Comienza el CRUD de los vendedores 
def seeV():
            sentencia= 'SELECT * FROM vendedores '
            cursor.execute(sentencia)
            registro= cursor.fetchall()
            print(registro)
     
    
def addV(a,b,c,d):# se agregan 
        sentecia= 'INSERT INTO vendedores(nombreVendedor,fechaAlta,fechaNac,direccion)VALUES(%s,%s,%s,%s)'
        valores=(a,b,c,d)
        cursor.execute(sentecia, valores)
        conn.commit()
        
    


def updateV(name,fecA,fecN,dirr, idV): # se actualizan 
        sentecia= 'UPDATE vendedores SET nombreVendedor=%s,fechaAlta=%s ,fechaNac=%s ,direccion=%s Where idVendedor=%s'
        valores=(name,fecA, fecN,dirr,idV )
        cursor.execute(sentecia, valores)
        conn.commit()
       
      

        
        
def deleteV(a):#  se borra un dato  
        sentecia= 'DELETE FROM vendedores  WHERE idVendedor = %s '
        valores=(a,)
        cursor.execute(sentecia, valores)
        conn.commit()        
           
#----------------------------------Comienza el CRUD de Ventas ---------------------------------------
def seeS():
            sentencia= 'SELECT * FROM ventas '
            cursor.execute(sentencia)
            registro= cursor.fetchall()
            print(registro)
     
    
def addS(a,b,c,d):# se agregan producto 
        sentecia= 'INSERT INTO ventas(idVendedor,idProducto,fecha,kilos)VALUES(%s,%s,%s,%s)'
        valores=(a,b,c,d)
        cursor.execute(sentecia, valores)
        conn.commit()
        





