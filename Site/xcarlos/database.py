import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("Banco.db")
    return conexao

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""CREATE table if not exists usuarios (id integer primary key, email text,
                    nome text, senha text,imagem text default 'none',publicacoes text default 'none')""")
    
    cursor.execute("""CREATE table if not exists publicacoes (id integer primary key, email text,
                    nome text, imagem text default 'none')""")

    conexao.commit()
    conexao.close()

def cadastro(informacoes):
    conexao = conectar_banco()
    cursor = conexao.cursor()   

    cursor.execute("SELECT COUNT(email) FROM usuarios WHERE email=?", (informacoes['email'],))
    conexao.commit()
    
    quantidade_de_emails = cursor.fetchone()
    if (quantidade_de_emails[0] > 0):
        print ("email já cadastrado, tente novamente")
        return False
    

    cursor.execute("INSERT INTO usuarios (email,nome,senha) VALUES (?,?,?)", (informacoes['email'], informacoes['nome'], informacoes['senha']))

    
    conexao.commit()

    return True

def login(informacoes):
    conexao = conectar_banco()
    cursor = conexao.cursor()   

    cursor.execute("SELECT COUNT(email) FROM usuarios WHERE email=? AND senha=?", (informacoes['email'], informacoes['password']))
    conexao.commit()
    
    quantidade_de_emails = cursor.fetchone()
    if (quantidade_de_emails[0] > 0):
        print ("login bem sucedido")
        return True
    
    print ("email ou senha incorretos, tente novamente")
    return False
    
    

if __name__ == '__main__':
    criar_tabela()