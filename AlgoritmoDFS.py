
#Importar libreria Queue para generar colas / listas en el programa
from queue import Queue

#Se crea la clase Grafo, dentro de la cual instanciaremos un objeto y a su vez se generaran nodos.
class Grafo:
    """
    Nuestra clase Grafo se encargará de representar el grafo con los atributos
    y funcionalidades de estos. 
    Definimos los atributos
    m_numero_nodos : int
            Nodos que forman parte del grafo
        m_nodos : int
            Especificación de rango de nodos del grafo
        m_dirigido : boolean
            Tipo de grafo: dirigido o no dirigido.
        m_lista_adyacencia : diccionario
            Diccionario que almacena el valor de los nodos mediante una lista de adyacencia
    """
    def __init__(self, num_de_nodos, dirigido=True):
        """
        Definición del constructor con parametros, que recibirá el numero de nodos que tendrá la clase Grafo 
        Este método se encarga de recibir el (M_num_de_nodos), para a partir de eso crear un rango de nodos (m_nodos) e
        indicar el tipo de grafo con el que se está trabajando (m_dirigido) y po último se crea el diccionario de datos mediante 
        la figuración del grafo con una lista de adyacencia
        """

        #Definición de número de nodos del Grafo
        self.m_num_de_nodos = num_de_nodos
        #Especificación de rango de nodos del Grafo
        self.m_nodos = range(self.m_num_de_nodos)

        #Establecer tipo de grafo (Dirigido o No Dirigido)
        self.m_dirigido = dirigido

        #Figurar el grafo mediante una lista de adyacencia 
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}#Implementación de lista de adyacencia mediante un diccionario