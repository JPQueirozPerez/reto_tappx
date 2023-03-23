RETO TAPPEX
24/03/2023

@ggispert
@jqueiroz
@clballes

El primer paso que hemos realizado ha sido el de data cleaning. Hemos planteado el proyecto fiándonos y limpiando las keywords dadas en vez de extraerlas del texto. 
Las hemos limpiado aplicando una longitud de 2 caracteres por keyword mínimo, así como que estén todas en minúscula y sin signos de puntuación ni espacios de por medio.
Hemos hecho este proceso con las keywords de los videos, artículos y todas las categorías de los videos y artículos conjuntamente guardadas. Seguidamente hemos usado la API de Google trans ya que hemos traducido todas las palabras al inglés ya que pensamos que sería óptimo por las “ñ” y los acentos de las palabras clave.

Hemos usado el método wordtovec para poder relacionar dos palabras a través de la similitud del coseno. Este algoritmo lo usamos para relacionar cada keyword con todas las categorías posibles. Así que para cada artículo le pasamos las keywords y el wordtovec nos da un score entre keywords y las distintas categorías. Después hacemos la media de todas las keywords del artículo, y nos da un score de la categoría más relevante para el artículo y en nuestro caso también hemos contemplado las otras 6 categorías más relevantes para compararlas con los videos. 
En los videos hacemos el mismo proceso y así tenemos distintos scores de las categorías más relevantes de artículos y videos. 

Cuando tenemos los scores filtramos las seis categorías más relevantes de cada vídeo y artículo y comparamos si coinciden. Para asegurarnos que haya dos videos por artículo, si no acaban de encajar los videos y los artículos, somos más permisivos y contempla más categorías en busca del score. Así que el score es cuantas categorías de estas 6 que estamos comparando coinciden así que siempre es un numero en fracción de seis.