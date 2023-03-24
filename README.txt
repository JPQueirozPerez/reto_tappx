RETO TAPPEX
24/03/2023

@ggispert
@jqueiroz
@clballes

El primer paso que hemos realizado ha sido el de data cleaning. Hemos planteado el proyecto en base a las keywords originales en vez de extraerlas del texto, aunque con más tiempo habríamos acabado aplicando este método.

Las hemos limpiado aplicando una longitud de 2 caracteres por keyword mínimo, así como que estén todas en minúscula y sin signos de puntuación ni espacios de por medio. Hemos hecho este proceso con las keywords de los videos, artículos y todas las categorías de videos y artículos conjuntamente guardadas en diccionarios en el caso de las keywords y una lista en el caso de las categorías.

Seguidamente hemos usado la API de Google trans para traducir todas las palabras al inglés ya optimiza el uso de PLN por las “ñ” del español que se codifican como "n" y la falta de acentos de las palabras clave.

Hemos usado el módulo Word2vec de la librería Gensim, para poder relacionar dos palabras a través de la similitud del coseno. Para cada artículo le pasamos las keywords y Word2vec nos da un score entre keywords y las distintas categorías. Después hacemos la media de todas las keywords del artículo, y nos da un score de la categoría más relevante para el artículo y en nuestro caso también hemos contemplado las otras 6 categorías más relevantes para compararlas con los videos. En los videos llevamos a cabo el mismo proceso, y así tenemos distintos scores de las categorías más relevantes de artículos y videos. 

El corpus que hemos utilizado es el de Google News que se puede encontrar en alguno de los siguientes enlaces:

Drive de descarga: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g
Github de descarga: https://github.com/mmihaltz/word2vec-GoogleNews-vectors

Este corpus que cuenta con 3 millardos de palabras de uso actual, tiene 3 millones de vectores de palabras en inglés de 300 dimensiones.

Finalmente, cuando tenemos los scores filtramos las 6 categorías más relevantes de cada vídeo y artículo y comparamos si coinciden. Para asegurarnos que haya 2 videos por artículo mínimo, si no acaban de encajar los videos y los artículos, somos más permisivos y contemplamos más categorías en busca del score. Así que el score final corresponde a cuantas de estas 6 categorías que estamos comparando coinciden así que siempre es un numero en fracción de 6.
