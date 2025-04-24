# Apuntes de Clase.

### Normalización - Parte 1. 

##### Dependencias Funcionales.

La **Dependencia Funcional** depende exclusivamente de la *semántica* de los atributos, no de las propiedades 
de los atributos. Es decir, por ejemplo, puede existir dependencia funcional entre dos atributos que pertenecen 
a la clave primaria. 

Las **Dependencias Funcionales** son locales a la relación (a la tabla). 
Para *relaciones distintas*, tenemos las *foreght keys*. 

Para confirmar las **Dependencias Funcionales** hay que entender el contexto y los datos. Podemos suponer la 
exisecia de **DF** a partir de las combinaciones de los atributos en las diferentes tuplas, pero no podemos 
*confirmarlas* sin entender el contexto completo de los datos.


##### Formas Normales basadas en Clave Primaria - 1FN.

De las estrategias nombradas, se recomiendo usar siempre la primera.
- Si en el parcial usas otra, te va a costar una muy buena argumentación de por qué usas esa por sobre la recomendada.

