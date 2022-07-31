from datetime import datetime
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException

from var import  SAVE_DIR, README_FILE, CISCO_CONF, COMWARE_CONF, TODAY, START_TIME
from hosts import HOSTS

def pysave(sw_login, sw_password):
    count = 0
    print('[INFO]', file=open(README_FILE, 'w'))
    print(f"Export du : {TODAY}\n", file=open(README_FILE, "a"))

    for key, value in HOSTS.items():
        try:
            FILE = SAVE_DIR / f'{key}.txt'
            switch = {
                'device_type' : value,
                'ip' : key,
                'username' : sw_login,
                'password' : sw_password,
            }
            net_connect = ConnectHandler(**switch)
            if value == 'hp_comware':
                output = net_connect.send_config_set(COMWARE_CONF)

            else:
                output = net_connect.send_command(CISCO_CONF)


            with open(FILE, 'w', encoding='utf-8') as f:
                f.writelines(output)

            count += 1

        except NetMikoAuthenticationException:
            print('[Erreur] - Login / Mot de passe incorrect')
            break

        except NetMikoTimeoutException:
            print(f"L'hôte {key} est injoignable")

    END_TIME = datetime.now()
    print("\nSauvegarde terminée, voir le fichier readme.txt pour plus d'informations")
    print('\n[RESUME]', file=open(README_FILE, 'a'))
    print(f"{count} switch sauvegardés\n", file=open(README_FILE, 'a'))
    print(f"Temps d'execution du script: {END_TIME - START_TIME}", file=open(README_FILE, 'a'))