# -*- coding: UTF-8 -*-

#Arquivo Py
nomes = []
    
def cadastrar():
    #print 'Digite um nome'
    #nome = raw_input()
    #nomes.append(nome)
    nomes.append('Luan')
    nomes.append('Matheus')
    nomes.append('Felipe')

def remover():
    print 'Informe um nome que para removido'
    nome_remover = raw_input()
    nomes.remove(nome_remover)
    
def alterar():
    erro = 1    
    while(erro != 0): 
        try:   
            print 'Qual nome deseja alterar?'
            print nomes
            
            nome_atual = raw_input()
            index_nome = nomes.index(nome_atual)

        except ValueError:   
            print 'Nome nao existe na lista!'
            erro = 1
            
        else:
            erro = 0
            
    print 'Qual o novo nome?'
    nome_novo = raw_input()
    
    nomes[index_nome] = nome_novo
    
def procurar():
    print 'Digite o nome para procurar'
    
    nome_procura = raw_input()
    
    if(nome_procura in nomes):
        print 'Nome encontrado'
    else:
        print 'Nome nao encontrado!'
    
def menu_cadastro_remover():

    escolha = ""
    
    while(escolha != "0"):
        print '1 - Cadastrar'
        print '2 - Lista de cadastrados'
        print '3 - Remover Cadastro'
        print '4 - Alterar Cadastro'
        print '5 - Localizar nomes'
        print '0 - Sair'
        
        escolha = raw_input()    
    
        if(escolha == "1"):
            cadastrar()
        if(escolha == "2"):
            print nomes
        if(escolha == "3"):
            remover()
        if(escolha == "4"):
            alterar()
        if(escolha == "5"):
            procurar()
            
def Questao_5():
    frase = 'Python'
    contador = 0
    while(contador < len(frase)):
        print frase[contador]
        contador+=1
    print 'FIM'
            
def menu():
    opcao = ""
    
    while(opcao != "0"):
        print 'Menus de Teste'
        print '1 - Chamar menu de cadastro de cliente'
        print '2 - Questao 5 dos exercicios'
        print '0 - Sair'
        print 'Escolha uma opcao'
        opcao = raw_input()
        
        if(opcao == "1"):
            menu_cadastro_remover()
        
        if(opcao == "2"):
            Questao_5()

menu()