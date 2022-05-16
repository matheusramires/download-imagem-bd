import psycopg2
import pandas as pd
import PIL.Image as Image
import io

db_name = '********'
db_host = '***********'
db_port = '5432'
db_user = 'postgres'
db_password = '**********'

connect = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
cursor = connect.cursor()


def mostraFoto(lote):
    sql_imagem = f"""select imagem, nome_foto from schema.tabela where coluna ={str(variavel)}"""
    cursor.execute(sql_imagem)
    fotos = cursor.fetchall()
    
    autoSize = 400
    largSize = 300
    
    for foto in fotos:
        print(foto[0])
        image_pil = Image.open(io.BytesIO(foto[0]))
        image_pil.save(f'imagem/{foto[1]}.jpg')
 
 
 
 
mostraFoto(1220244)