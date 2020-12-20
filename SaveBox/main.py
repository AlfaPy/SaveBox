import subprocess, datetime, time, log
needBackup = True
while True:
	sap = False
	iap = False
	dap = False
	retry = False
	needBackup = True
	while needBackup:
		r = subprocess.run(["idevice_id","--list"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		if sap == False:
			print("Recherche d'iPhone en cours")
			log.logged("Going into research mod",1)
			sap = True
		if r.stdout:
			print("iPhone detecte, tentative de backup")
			log.logged("iPhone detected",1)
			a = subprocess.run(["idevicepair","pair"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			ret = a.stdout[:5]
			while ret == b"ERROR":
				if iap == False:
					iap = True
					print("Veuillez rentrer votre code")
					log.logged("Waiting for the iPhone code",1)
				a = subprocess.run(["idevicepair","pair"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				ret = a.stdout[:5]
				time.sleep(3)
			print("lancement de la backup")
			log.logged("Launching the backup",1)
			a = subprocess.run(["sudo","idevicebackup2","backup","ios_backup"],stdout=subprocess.PIPE)
			if "Backup Successful" in a.stdout.decode():
				print("backup réussi")
				log.logged("Backup succeeded",1)
			else:
				print("echec de la backup")
				log.logged("Backup failure",3)
				retry = True
			a = subprocess.run(["idevice_id","--list"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			while a.stdout and not retry:
				if dap == False:
					print("Attente de deconnexion de l'iPhone")
					log.logged("Waiting for the iPhone to deconect",1)
					dap = True
				a = subprocess.run(["idevice_id","--list"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				time.sleep(5)
			needBackup = False
			log.logged("iPhone deconnected",1)
