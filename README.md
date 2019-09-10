# SLR (Sign Language Recognition)

Proyecto final - Ironhack Data Analytics Bootcamp.

#### SLR es un interpretador del lenguaje de signos a través de la cámara web

## PROCESO:

#### El proyecto se estructura en cuatro fases:

####  1. Obtención de la base de datos (videoToImages.py):

Las imágenes empleadas en el proyecto fueron obtenidas al dividir vídeos realizados con la cámara web en imágenes. De una grabación aproximada de 35 segundos se obtenían alrededor de 3000 imágenes. En un primer momento, el procedimiento se realizó con todas las letras, pero debido a limitaciones computacionales, se buscó un punto óptimo entra la cantidad de las letras y la funcionalidad de la demo. Por este motivo, el proyecto cuenta por ahora con 5 letras (R,O,S,T,Y) y la palabra amigo.

####  2. Convertir todas las imágenes a NumPy array y guardarlas como pickle (imagesToPickle.py):

Al contar ya con suficientes imágenes el siguiente paso es redimensionarlas 500x350x1 y convertirlas en numpy array. Después se obtiene la etiqueta de cada imagen y se guardan las imágenes como final_x.pickle, las etiquetas se guardan como final_y.pickle

####  3. Creación del modelo de red neuronal (machineLearningModel.ipynb):

Una vez creada la base de datos, se entrena una red neuronal convolucional para que sea capaz de detectar y clasificar las formas de las manos.

La red neuronal elegida es la siguiente:

####  4. Realización del programa (my_main.py): 

Se crea un archivo my_main.py, el cual al ejecutarse activa la cámara web y se conecta con el modelo creado, reconociendo en tiempo real los signos captados.

<center><img width="350" alt="Captura de pantalla 2019-09-10 a las 8 50 06" src="https://user-images.githubusercontent.com/51289289/64590751-8de3e500-d3a8-11e9-8141-f75d03da482b.png"></center>

## Librerías usadas:

- OpenCV
- NumPy
- Keras
- TensorFlow
- Pickle


