import PySimpleGUI as sg
import os

from netmiko import ConnectHandler

from var import DATA, today

class AppGui():
    def __init__(self):
        sg.theme('Material2')
        self.layout = [
            [sg.Text('Selection du système cible')],
            [sg.Radio('IOS', 'GROUPE_1', size=(12, 1), key='cisco_ios'), 
            sg.Radio('NXOS', 'GROUPE_1', size=(12, 1), key='cisco_nxos'), 
            sg.Radio('Alcatel AOS', 'GROUPE_1', size=(12, 1), key='alcatel_aos')],
            [sg.Text('Hôtes', border_width=20), sg.Multiline(key='-HOST-', size=(35,5), expand_x=True)],
            [sg.Text('Commandes'), sg.Multiline(key='-COMMAND-', size=(35,5), expand_x=True)],
            [sg.Text('-'*130)],
            [sg.Text('Login', border_width=13), sg.Input(size=(15,1), key='-LOGIN-')], 
            [sg.Text('Password'), sg.Input(size=(15,1), password_char="*", key='-PASSWORD-')],
            [sg.Text('-'*130)],
            [sg.Button('DEPLOIEMENT')],
            [sg.Text('Output', key='-OUTPUT-')],
            [sg.Output(size=(80,15), expand_x=True)],
        ]

    def main(self):
        if Path(DATA).is_dir() == False:
            os.makedirs(DATA)

        window = sg.Window("PyAutomation").Layout(self.layout)
        while True:
            event, values = window.read()  # type: ignore
            self.sw_login = values['-LOGIN-']
            self.sw_password = values['-PASSWORD-']
            ip_host = values['-HOST-']
            self.final_host = ip_host.split(',')
            cli_command = values['-COMMAND-']
            self.final_command = cli_command.split(',')

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == 'DEPLOIEMENT':
                for key, value in values.items(): 
                    if value == True:
                        self.device_type = key
                a.functions()
                
    def functions(self):
        for f in self.final_host:
            FILE = os.path.join(DATA, f'{f}_{today}.txt')
            try:
                switch = {
                    'device_type' : self.device_type,
                    'ip' : f,
                    'username' : self.sw_login,
                    'password' : self.sw_password,
                }
                net_connect = ConnectHandler(**switch)
                output = net_connect.send_config_set(self.final_command)
                with open(FILE, 'a', encoding='utf-8') as f:
                    f.writelines(output)
                print(output)
                print("\nVous pouvez retrouver l'output complet dans le dossier DATA à la racine du programme.")
                
            except:
                print(f"[Erreur] - Connexion impossible à l'hôte {f}. Vérifier le login / password")
 
if __name__ == "__main__":
    a = AppGui()
    a.main()
