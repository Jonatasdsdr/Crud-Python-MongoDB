from mailbox import NotEmptyError
import pymongo
import json

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/") #Endereço mongo.
    mydb = myclient ["TESTEMONGO3"]
    mycol = mydb ["Teste"]

    print("\nOk\n")

except:
    print("\nErro!\n")


#funções:

def inserir():

    print("Inserir dados de um novo colaborador.\n\n")

    idd = input ("ID do profissional: ")
    nome = input ("Nome do profissional: ")
    idade = input ("Idade do profissional: ")
    ocupacao = input ("Ocupação do profissional: ")

    avulso = {"id": idd, "nome": nome, "idade": idade, "ocupacao": ocupacao} #insere uma linha ta tabela JSON.
    x = mycol.insert_one(avulso)




def ler():

    print("Mostrar dados do funcionário.")

    nome = input ("Nome do profissional: ")
    myquery = {"nome": nome}
    mydoc = mycol.find(myquery)

    print("\nDados do colaborador:\n")

    for x in mydoc: #Para mostrar a tabela de dados dos colaboradores.
        print(x)
        print("\n")




def modificar():

    print("Modificar dados de um funcionário.")

    nome = input ("Digite o nome: ")
    mudar = input ("Digite o novo nome: ")

    myquery = {"nome": nome}
    newvalue = {"$set": {"nome": mudar}}
    mycol.update_many(myquery, newvalue) #Atualiza os dados de um funcionário conforme input do usuário.




def deletar():

    print("Deletar dados de um funcionário.")

    nome = input ("Digite o nome do colaborador que deseja excluir: ")
    myquery = {"nome": nome}
    mycol.delete_many(myquery) #Apaga dados de um funcionário conforme input.

print ("MENU:\n\n") #Menu para escolher as opções desejadas.
print ("Digite 1 para: inserir;")
print ("Digite 2 para: ler;")
print ("Digite 3 para: atualizar;")
print ("Digite 4 para: deletar.")

menu = input ("\n>>> ")
print("\n\n")

if (menu == "1"):

    inserir()

elif (menu == "2"):

    ler()

elif (menu == "3"):

    modificar()

elif (menu == "4"):

    deletar()

