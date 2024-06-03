"""
i'm createing a bank application ...
 withdraw , deposit , trasfer, create account , close account , balance , check balance, movments

"""
from enum import Enum, auto
import json
import os

DEBUG =True


class Bank_Actions(Enum):
    CREATE_ACCOUNT =auto()
    CLOSE_ACCOUNT=auto()
    EXIT =auto()
    COUNT_CLIENTS =auto()
    SHOW_ALL_CLIENTS=auto()
    CLIENT_ACTIONS =auto()

class Clien_Actions(Enum):
    WITHDRAW = auto()
    DEPOSIT =auto() 
    TRANSFER =auto()
    CHECK_BALANCE=auto()
    SHOW_MOVMENTS =auto()

class Client:
    def __init__(self,id,first_name,occupation) -> None:
        self.id = id
        self.first_name =first_name
        self.occupation =occupation
        self.__balance =0
        self.__password="123"

    def __str__(self) -> str:
        return json.dumps({
            'id': self.id,
            'first_name': self.first_name,
            'occupation': self.occupation,
            'balance':self.__balance
        })
    
    def reset_password(self,new_pas):
        self.__password =new_pas

    def check_password(self,password):
        if password == self.__password: return True
        return False

    def withdraw(self,password):
        if self.check_password(password):
            self.__balance -= 100

    def deposit(self):
        self.__balance +=200

    def __repr__(self):
        return f"Client(id={self.id}, first_name='{self.first_name}', occupation='{self.occupation}')"
    
    def get_balance(self):
        return self.balance
    

class Bank:
    clients =list()
    def check_duplicate(self,id):
        for client in self.clients:
            if id == client.id: return True
        return False

    #To create account data must include :id ,first name
    def create_account(self,id,first_name,occupation="self employee"):
        if self.check_duplicate(id): return

        #else - client data was checked
        client =Client(id,first_name,occupation)
        self.clients.append(client)
        print(f"account created - first name {client.first_name} , id: {client.id}")
        return client

    def close_account(self):
        print("close account - under construction")

    def show_menu(self):
        for action in Bank_Actions:
            print(f'{action.value} - {action.name}')
        return Bank_Actions( int( input ("your selection?")))

    def show_client_menu(self):
        for action in Clien_Actions:
            print(f'{action.value} - {action.name}')
        return Clien_Actions( int( input ("your selection?")))

    def show_all_clients(self):
        for client in self.clients:
            print( client)

    def get_client_by_id(self,id):
        for client in self.clients:
            if str(client.id) == str( id) :return client
        

def client_gather_data():
    client_id=input("clien id?")
    first_name= input("first name?")
    occupation= input("occupation? (optional)")

    return client_id,first_name,occupation


def test_add_clients(bank):
    if DEBUG :
        c= bank.create_account(111,"Waga","killer") # Done
        c.deposit()
        c1=bank.create_account(222,"baga","teller") # Done
        c1.deposit()
        c1.deposit()


if __name__ =='__main__':
    bank = Bank()
    test_add_clients(bank)
    while True:
        
        user_selection= bank.show_menu()
        if user_selection == Bank_Actions.EXIT:  exit() 
        elif user_selection == Bank_Actions.CREATE_ACCOUNT: 
            client_id, first_name, occupation = client_gather_data()
            bank.create_account(client_id,first_name,occupation) # Done
        elif user_selection == Bank_Actions.CLOSE_ACCOUNT: bank.close_account()
        elif user_selection == Bank_Actions.SHOW_ALL_CLIENTS: bank.show_all_clients() #DONE
        elif user_selection == Bank_Actions.CLIENT_ACTIONS:
            os.system('cls')
            user_selection= bank.show_client_menu()
            if user_selection ==Clien_Actions.DEPOSIT:
                    bank.show_all_clients()
                    c=bank.get_client_by_id( input("please select client (by id)"))
                    print( c)
                    c.deposit()
                    print("after deposit...")
                    print( c)
        
        
# WITHDRAW = auto()
#     DEPOSIT =auto() 
#     TRANSFER =auto()
#     CHECK_BALANCE=auto()
#     SHOW_MOVMENTS =auto()

# https://github.com/Deepali-Srivastava/object-oriented-programming-in-python/tree/main/exercise-code

# procedure oriented


