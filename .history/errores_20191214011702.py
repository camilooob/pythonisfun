paises = {
	"colombia": 49,
	"mexico": 244,
 	"argentina": 20
}
while True:
	country = str(input("Ingrese el pais:")).lower()

	try:
		print("El pais {} tiene {}".format(country, paises[country]))
	except KeyError:
		print("No tenemos ese dato")
