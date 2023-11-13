# Visualization Project - Boat_Sales
Este repositorio incluye el trabajo llevado a cabo con el fin de mostrar las conclusiones que se pueden extraer de la base de datos de una página web de venta de barcos de primera y segunda mano.

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

Para aquellos usuarios que dispongan de acceso, [aquí](https://app.powerbi.com/groups/me/reports/a79565ec-3dd7-4219-9099-cd4a31be35eb/ReportSectionb37d356e0c97e07a0a98?experience=power-bi) se da acceso a la visualización llevada a cabo en la plataforma de *Microsoft*.

En primer lugar se muestra un *Overview* con infromación de la BBDD. Se incluye un mapa para mostrar la catnidad de países de los que se tienen anuncios de barcos.





## Herramientas y fuentes utilizadas

* [Pandas](https://pandas.pydata.org/docs/)
* [Kaggle](https://www.kaggle.com/datasets/karthikbhandary2/boat-sales/data)
* [PowerBI](https://powerbi.microsoft.com/es-es/)





