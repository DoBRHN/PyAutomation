# PyAutomation

--

CONTEXT :

Au sein d'une infrastructure de +60 switchs. Ci-présent un petit script avec une UI permettant d'automatiser le processus de sauvegarde (configurations) avec des équipements de manufacture différentes (Cisco et HP).

Le script reste très simple dans l'utilisation du module Netmiko, il s'agit d'une base. Je le module pour m'adapter aux différents projets en cours :

  - Pour l'exemple, le fichier recensant mes hôtes sont un dictionnaire. Dans la réalité, j'utilise plutôt une connexion avec une base de données afin d'avoir toujours       la liste des hôtes à jour
  
  - Si j'ai besoin d'appliquer de la configuration, j'ajoute des boutons programmables, j'utilise d'autres options de Netmiko
  
  - Si j'ai des équipements de manufacture non pris en charge par Netmiko, j'exploite également le module Paramiko
