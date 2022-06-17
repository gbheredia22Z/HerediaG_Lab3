
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

            
    def agregar_borde(self, nodo1, nodo2, peso=1):
        """
        Se agrega nodos a la lista de adyacencia recibiendo como parámetros : nodo1, nodo2 y el peso
        Posteriormente los nodos son agregados a la lista de adyacencia, evaluando los parámetros:

        nodo1: int
        nodo2: int
        peso: int

        Retorno: Ningun valor de retorno
        """
        #Agregar nodo 2 a lista de adyacencia en nodo 1
        self.m_lista_adyacencia[nodo1].add((nodo2, peso)) 
        
        #Si el nodo no es dirigido
        if not self.m_dirigido:
            # Agregar nodo 1 a lista de adyacencia en nodo2
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
            
    def imprimir_lista_adyacente(self):
        """
        Se realiza la impresión del grafo de la lista de adyacencia sin recibir parámetros 

        Parametros : Ningun parámetro
        Retorno :  Ningun valor de retorno
        """
        #Lista de adyacencia recorrida
        for llave in self.m_lista_adyacencia.keys():
             # Impresión del nodo
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])
  
    def dfs(self, inicio, objetivo, ruta = [], visitado = set()):
        """
        Este método imprime el recorrido dfs generado a través de un nodo inicial y un nodo objetivo.
        Genera una lista de los nodos visitados y muestra el recorrido realizado hasta llegar al objetivo. 

        Parametros
        ----------
        ruta : lista
        visitado : diccionario

        Retorno
        -------
        ruta / resultado / None 
        """

        ruta.append(inicio) #se agrega a la ruta el nodo inicial
        visitado.add(inicio) #se agrega a la la lista de nodos visitados el nodo inicial

        if inicio == objetivo:  #Si inicio es igual a objetivo
            return ruta #Retorna la ruta
            
        for(vecino, peso) in self.m_lista_adyacencia[inicio]: #Bucle que recorrera la lista de adyacencia
            if vecino not in visitado:  #Si el vecino no se encuentra en el diccionario de nodos visitados
                resultado = self.dfs(vecino, objetivo, ruta, visitado) #se asigna a la variable resultado el nodo vecino, el objetivo, la ruta y la lista de nodos visitados
                
                if resultado is not None: #Si la lista resultado no esta vacio
                    return resultado #Retorna resultado
                    
        
        ruta.pop() # elimina y retorna el elemento de la ruta
        return None           