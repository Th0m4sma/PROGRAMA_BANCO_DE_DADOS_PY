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

def procurar_BancoDados(email: str) -> list:
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='cadastro'
    )

    cursor = conexao.cursor()
    cursor.execute(f'select * from cliente where email="{email}"')

    lista = list(cursor.fetchall())
    cursor.close()
    conexao.close()
    return lista

def verifica_cliente(lista:list,email:str,senha:str) -> bool:
    if lista[2]!=email or lista[3] != senha:
        return False
    else:
        return True


def removendo_BancoDados(email: str, senha: str) -> bool:
    conexao = None
    cursor = None
    try:
        # Conecta ao banco de dados
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cadastro'
        )
        
        lista = procurar_BancoDados(email)

        # Verifica se o cliente existe e se a senha está correta
        if not lista or not verifica_cliente(email, senha):
            return False
        
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM cliente WHERE id = %s', (lista[0],))  # Corrige a tupla para (lista[0],)
        
        conexao.commit()  # Confirma a transação
        return True  # Retorna True após a remoção bem-sucedida

    except Exception as e:
        print("Erro ao remover dados:", e)
        return False  # Retorna False em caso de erro

    finally:
        # Fecha o cursor e a conexão se foram criados
        if cursor:
            cursor.close()  
        if conexao:
            conexao.close()  

def alterar_senha_BancoDados(email: str, senha_antiga: str, senha_nova: str) -> bool:
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cadastro'
        )
        cursor = conexao.cursor()

        
        if verifica_cliente(procurar_BancoDados(email, senha_antiga), email, senha_antiga):
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
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cadastro'
        )
        cursor = conexao.cursor()

        lista = procurar_BancoDados(email)

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

    print("========================================")
    for i in lista:
        print("(ID:",i[0],") (NOME:",i[1],") (EMAIL:",i[2], ") (SENHA:",i[3],") (PREF:",i[4],")")
    print("========================================")

    cursor.close()
    conexao.close()
