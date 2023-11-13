# Visualization Project - Boat Sales
Este repositorio incluye el trabajo llevado a cabo con el fin de mostrar las conclusiones que se pueden extraer de la base de datos de una página web de venta de barcos de primera y segunda mano.

![ValenciaBoatShow](./images/BoatShow.jpg)

## ETL - Extracción, transformación y carga de la BBDD

La base de datos ha sido descargda del siguiente [link](https://www.kaggle.com/datasets/karthikbhandary2/boat-sales/data).

En esta base de datos se incluyen las siguientes columnas:
* Price: precio de la embarcación en distintas monedas.
* Boat Type: Estilo de embarcación
* Manufacturer: Fabricante/astillero
* Type: Condición y tipo de propulsión
* Year Built: Año de fabricación
* Length: Eslora - largo del barco
* Width: Manga - ancho del barco
* Material: Material principal de fabricación
* Location: Lugar donde se encuentra el barco
* Number of Views: Valor entero con la cantidad de visitas del anuncio.

El primer paso tras descargar la información de tipo CSV es limpiar y preparar la información de cara a la visualización.

1) Limpieza

En la carpeta [notebooks](https://github.com/Jacobomb/VisualizationProject-Boat_Sales/tree/main/notebooks) se puede encontrar el [fichero](https://github.com/Jacobomb/VisualizationProject-Boat_Sales/blob/main/notebooks/1.CleaningData.ipynb) en Python donde se realiza la limpieza de la tabla. 

Los pasos han sido los siguientes:

* Columna `Price`: Dado que en esta columna venían juntos el precio de la embarcación y la moneda del país donde se encontraba el mismo, se ha procedido a separar la información en dos y después a calcular el precio en Euro por ser esta la moneda más común de la base de datos. Se anima a ver la carpeta [src](https://github.com/Jacobomb/VisualizationProject-Boat_Sales/tree/main/src) en la que se incluyen las funciones utilizadas para este paso.

* Para las columnas `Material` y `Manufacturer`, aquellas filas que no tuvieran un valor asignado han sido rellenadas con `unknown`. 

* La columna `Location` ha sido limpiada para separar en País y Ciudad. Se puede apreciar un patrón de separación y se explica en mayor detalle en el mencionado [fichero](https://github.com/Jacobomb/VisualizationProject-Boat_Sales/blob/main/notebooks/1).

Una vez la BBDD está lista, se guarda en [data](https://github.com/Jacobomb/VisualizationProject-Boat_Sales/tree/main/data) distinguióndola de la BBDD original. 

Llegados a este punto se puede proceder con la visualización.

## Visualización

Para visualizar los insights extraidos del estudio se ha utilizado la herramienta Power BI. 

Para aquellos usuarios que dispongan de acceso, [aquí](https://app.powerbi.com/groups/me/reports/a79565ec-3dd7-4219-9099-cd4a31be35eb/ReportSectionb37d356e0c97e07a0a98?experience=power-bi) se encuentra la visualización llevada a cabo en la plataforma de *Microsoft*.

En caso de no contar con acceso, en la carpeta [visuals_captures](https://github.com/Jacobomb/VisualizationProject-Boat_Sales/tree/main/visuals_captures) se han incluido capturas de cada una de las pestañas del documento original. No son interactivas pero dan una idea el lector del contenido.

En primer lugar se muestra un *Overview* con infromación de la BBDD. Se incluye un mapa para mostrar la catnidad de países de los que se tienen anuncios de barcos.

![Overview](./visuals_captures/Overview.png)

En el resto de páginas del proyecto se puede dividir en dos partes. 

1) En primer lugar se estudia el gusto de los consumidores vía la variable `Visitas en los últimos 7 días`. Se utiliza esta variable como un indicador de gusto del potencial comprador. Para ello, se han .....(SEGUIR AQUÍ CONTANDO UN POCO POR ENCIMA QUE HAY EN CADA PESTAÑA Y CONCLUISONES POR ENCIMA QUE SE PUEDAN OBTENER, LO DE LOS PRECIOS DE LOS MATERIALES Y TAL...)

## Trabajos futuros

COMENTAR AQUÍ COMO PUEDE MEJORAR EL ESTUDIO!!!

## Herramientas y fuentes utilizadas

* [Pandas](https://pandas.pydata.org/docs/)
* [Kaggle](https://www.kaggle.com/datasets/karthikbhandary2/boat-sales/data)
* [PowerBI](https://powerbi.microsoft.com/es-es/)





