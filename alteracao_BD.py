import pymysql

def inserindo_BancoDados(nome: str, email: str, senha: str, pref: str) -> bool:
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cadastro'
    )
    
    try:
        cursor = conexao.cursor()
       
        sql = 'INSERT INTO cliente (id, nome, email, senha, preferencia) VALUES (DEFAULT, %s, %s, %s, %s)'
        valores = (nome, email, senha, pref)
        
        cursor.execute(sql, valores)
        conexao.commit()
    except Exception as e:
        print("Erro ao inserir dados:", e)
        cursor.close()  
        conexao.close() 
        return False
    finally:
       
        cursor.close()
        conexao.close()
    return True

def conectar_banco():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cadastro'
    )

def procurar_BancoDados(email: str) -> list:
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM cliente WHERE email = %s', (email,))
        lista = list(cursor.fetchone())  
    except Exception as e:
        print(f"Erro ao buscar o cliente: {e}")
        lista = []
    finally:
        cursor.close()
        conexao.close()
    return lista

def verifica_cliente(lista: list, email: str, senha: str) -> bool:
    return str(lista[2]) == email and str(lista[3]) == senha

def removendo_BancoDados(email: str, senha: str) -> bool:
    lista = procurar_BancoDados(email)
    if not lista or not verifica_cliente(lista, email, senha):
        return False

    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        cursor.execute('DELETE FROM cliente WHERE id = %s', (lista[0],))
        conexao.commit()
        sucesso = True
    except Exception as e:
        print(f"Erro ao remover o cliente: {e}")
        sucesso = False
    finally:
        cursor.close()
        conexao.close()
    return sucesso

    
def alterar_senha_BancoDados(email: str, senha_antiga: str, senha_nova: str) -> bool:
    try:
        lista = procurar_BancoDados(email)
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cadastro'
        )
        cursor = conexao.cursor()

        
        if verifica_cliente(lista, email, senha_antiga):
            cursor.execute("UPDATE cliente SET senha = %s WHERE email = %s", (senha_nova, email))
            conexao.commit()  
            return True

    except Exception as e:
        print("Erro ao alterar dados:", e)
    
    finally:
        cursor.close()  
        conexao.close()  

    return False


def alterar_nome_BancoDados(email: str, senha: str, novo_nome: str) -> bool:
    conexao = None
    cursor = None
    lista = procurar_BancoDados(email)

    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cadastro'
        )
        cursor = conexao.cursor()

        if lista and verifica_cliente(lista, email, senha):
            cursor.execute("UPDATE cliente SET nome = %s WHERE email = %s", (novo_nome, email))
            conexao.commit()  
            return True 

    except Exception as e:
        print("Erro ao alterar nome:", e)

    finally:
        if cursor:  
            cursor.close()  
        if conexao:  
            conexao.close()  

    return False

def alterar_pref_BancoDados(email: str,senha: str, pref_nova: str) -> bool:
    lista = procurar_BancoDados(email)
    
    conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cadastro'
    )

    cursor = conexao.cursor()

    if lista and verifica_cliente(lista, email, senha):
        cursor.execute("UPDATE cliente SET preferencia = %s WHERE email = %s", (pref_nova, email))
        conexao.commit()  
        return True 

    cursor.close()
    conexao.close() 


def imprimir_BD():
    conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cadastro'
    )

    cursor = conexao.cursor()
    cursor.execute("select * from cliente")
    lista = list(cursor.fetchall())

    print("===========================================================================================")
    for i in lista:
        print("(ID:",i[0],") (NOME:",i[1],") (EMAIL:",i[2], ") (SENHA:",i[3],") (PREF:",i[4],")")
    print("===========================================================================================")

    cursor.close()
    conexao.close()
