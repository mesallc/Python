#Работа клиента с сервером

class Server:

     server_username = 'NaN'
     server_password = 'NaN'

     def register_account(client_username, client_password):
          global server_username
          global server_password

          server_username = client_username
          server_password = client_password

     def login_account(client_username, client_password):
          global server_username
          global server_password

          if client_username == server_username and client_password == server_password:
               Menu.start_menu()
          else: print('Wrong username or password!')

class Client:

     def register():
          client_username = input('create username: ')
          client_password = input('create password: ')
          Server.register_account(client_username, client_password)
     
     def login():
          client_username = input('enter your username: ')
          client_password = input('enter your password: ')
          Server.login_account(client_username, client_password)
     
     def confirm_password():
          check_pass = input('confirm your password: ')
          if check_pass == Server.server_password:
               return True
          else:
               login()
     
class Menu:
     def start_menu():
          user_choose = int(input('[menu]\n[1] get my log/pass\n[2] change pass'))

          if user_choose == 1:
               if Client.confirm_password() == True:
                    print('username:' + Server.server_username + '\npassword:' + server_password)
                    start_menu()

          elif user_choose == 2:
               if Client.confirm_password() == True:
                    server_password = input('create new password: ')
                    Client.login()

Client.register()
Client.login()

