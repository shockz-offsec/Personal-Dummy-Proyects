# TVTime
Esta aplicaci贸n te muestra cuanto tiempo te ha llevado ver una serie o todas tus series favoritas

## Requisitos

* [Python3](https://www.python.org/downloads/).

* Librerias : ```python -m pip install -r requirements.txt``` (En el directorio del codigo)
  
* API IMDB: puedes obtenerla mediante: https://rapidapi.com/apidojo/api/imdb8 , te registras y te suscribes a la api, luego copias la ```x-rapidapi-key``` en la secci贸n ```__headers``` al comienzo del c贸digo.


## Configuraci贸n 馃敡

Se requiere un archivo ```series.txt``` en el directorio raiz de la aplicaci贸n con la lista de series a procesar.
Estas volcar谩n los resultados en un archivo xlsx, ademas los errores de incompatibilidad a la hora de buscar la serie se volcar谩n en el archivo ```errores.txt```.

#Dise帽o

* Se utilizo *Pandas* para la exportaci贸n del dataframe con los datos.

* *Requests* para las peticiones.

* *openpyxl* para la entrada/salida de archivos xlsx.


## Ejecuci贸n

 * Puede usar el comando y ```py -u" Ruta del archivo py "```, Es necesario tener la ruta de Python definida en las variables de entorno del sistema.

* Si est谩 utilizando un IDE o un editor de c贸digo configurado, simplemente compile y ejecute el c贸digo.

##Vistas a futuro

* Utilizar otra API que permita m谩s peticiones para asi poder procesar una cantidad superior de series, sin agotar peticiones.

* No depender de una API y utilizar *Selenium* con *BeautifulSoap*
